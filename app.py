from flask import Flask, render_template, redirect, request, session, flash
from datetime import timedelta
from db import get_db_connection
from functools import wraps

#Admin Authentication Decorator
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function

#Player Authentication Decorators
def player_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not session.get('player_id'):
            return redirect('/login')
        return f(*args, **kwargs)
    return wrapper

app = Flask(__name__)
app.secret_key = 'admin123'
app.permanent_session_lifetime = timedelta(days=5)

#Admin Home Page
@app.route('/')
def home():
    return redirect('/login')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conn = get_db_connection()
        cursor = conn.cursor()

        #Check whether the user is an admin
        cursor.execute(
            "SELECT * FROM admins WHERE email=%s AND password=%s",
            (email,password)
        )
        admin = cursor.fetchone()
        if admin:
            session['admin_logged_in'] = True
            cursor.execute(
                "INSERT INTO admin_login_log (admin_username) VALUES (%s)",
                (admin[1],)
            )
            conn.commit()
            return redirect('/admin')

        #Check whether the user is a player
        cursor.execute(
            "SELECT player_id FROM players WHERE email=%s AND password=%s",
            (email,password)
        )
        player = cursor.fetchone()
        if player:
            session['player_id'] = player[0]
            return redirect('/player')
        else:
            flash('Invalid credentials. Please try again.')
            return redirect('/login')
    return render_template('login.html')
    
@app.route('/admin')
@admin_required
def admin_home():
    if not session.get('admin_logged_in'):
        return redirect('/login')
    return render_template('admin_home.html')

@app.route('/admin/admin_logs')
@admin_required
def admin_logs():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT admin_username, login_time
        FROM admin_login_log
        ORDER BY login_time DESC
        LIMIT 5
    """)
    logs = cursor.fetchall()
    return render_template('admin_logs.html', logs=logs)

#Admin Routes
@app.route('/admin/add_player', methods = ['POST', 'GET'])
@admin_required
def add_player():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        conn = get_db_connection()
        cursor = conn.cursor()
        query = 'INSERT INTO players (player_name, email, password) VALUES (%s, %s, %s)'
        cursor.execute(query, (name, email, password))
        conn.commit()
        cursor.close()
        conn.close()
        flash('Player added successfully!')
        return redirect('/admin')
    return render_template('add_player.html')

@app.route('/admin/create_tournament', methods=['GET','POST'])
@admin_required
def create_tournament():
    if request.method == 'POST':
        name = request.form['name']
        game = request.form['game']
        start = request.form['start_date']
        end = request.form['end_date']
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """INSERT INTO tournaments 
                   (tournament_name,game_name,start_date,end_date)
                   VALUES (%s,%s,%s,%s)"""
        cursor.execute(query,(name,game,start,end))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/admin')
    return render_template('create_tournament.html')


@app.route('/admin/schedule_match', methods=['GET','POST'])
@admin_required
def schedule_match():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM players")
    players = cursor.fetchall()
    cursor.execute("SELECT * FROM tournaments")
    tournaments = cursor.fetchall()
    if request.method == 'POST':
        tournament = request.form['tournament']
        p1 = request.form['player1']
        p2 = request.form['player2']
        date = request.form['date']
        query = """INSERT INTO matches 
                   (tournament_id,player1_id,player2_id,match_date)
                   VALUES (%s,%s,%s,%s)"""
        cursor.execute(query,(tournament,p1,p2,date))
        conn.commit()
        return redirect('/admin')
    return render_template('schedule_match.html', players=players,tournaments=tournaments)


@app.route('/admin/record_result', methods=['GET','POST'])
@admin_required
def record_result():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM matches")
    matches = cursor.fetchall()
    if request.method == 'POST':
        match_id = request.form['match']
        p1_score = request.form['p1_score']
        p2_score = request.form['p2_score']
        winner = request.form['winner']
        loser = request.form['loser']
        query = """INSERT INTO match_results
                   (result_id,match_id,player1_score,player2_score,winner_id, loser_id)
                   VALUES (%s,%s,%s,%s,%s,%s)"""
        cursor.execute(query,(None,match_id,p1_score,p2_score,winner,loser))
        conn.commit()
        return redirect('/admin')
    return render_template('record_result.html',matches=matches)

@app.route('/admin/monthly_stats')
@admin_required
def monthly_stats():

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
        SELECT 
            DATE_FORMAT(start_date, '%Y-%m') AS month,
            COUNT(*) AS total_tournaments
        FROM tournaments
        GROUP BY month
        ORDER BY month;
    """

    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('monthly_stats.html', data=data)

@app.route('/admin/monthly_game_stats')
def monthly_game_stats():

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
        SELECT 
            DATE_FORMAT(start_date, '%Y-%m') AS month,
            game_name,
            COUNT(*) AS total
        FROM tournaments
        GROUP BY month, game_name
        ORDER BY month, game_name;
    """

    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('monthly_game_stats.html', data=data)

@app.route('/admin/dashboard')
def admin_dashboard():

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT COUNT(*) FROM tournaments"
    cursor.execute(query)

    total_tournaments = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return render_template('admin_dashboard.html',
                           total_tournaments=total_tournaments)

@app.route('/admin/logout')
@admin_required
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect('/')


#Player Routes
@app.route('/player')
def player_home():
    return render_template('player_home.html')

@app.route('/player/register', methods=['GET','POST'])
def player_register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO players (player_name,email,password) VALUES (%s,%s,%s)",
            (name,email,password)
        )
        conn.commit()
        cursor.close()
        conn.close()
        flash('Registration successful! Please log in.\n\n')
        return redirect('/')
    return render_template('player_register.html')

@app.route('/player/tournaments')
@player_required
def view_tournaments():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tournaments")
    tournaments = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return render_template('player_tournaments.html', tournaments=tournaments)

@app.route('/player/join', methods=['GET','POST'])
@player_required
def join_tournament():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tournaments")
    tournaments = cursor.fetchall()
    if request.method == 'POST':
        player_id = session['player_id']
        tournament_id = request.form['tournament']
        cursor.execute("""
            INSERT INTO tournament_participants (tournament_id, player_id)
            VALUES (%s,%s)
        """,(tournament_id,player_id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/player')
    return render_template('player_join_tournament.html', tournaments=tournaments)

@app.route('/player/my_tournaments')
@player_required
def my_tournaments():
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        SELECT t.tournament_name, t.game_name, t.start_date, t.end_date
        FROM tournament_participants tp
        JOIN tournaments t ON tp.tournament_id = t.tournament_id
    """
    cursor.execute(query)
    tournaments = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return render_template('my_tournaments.html', tournaments=tournaments)

@app.route('/player/participants/<game_name>')
@player_required
def view_participants(game_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        SELECT p.player_name
        FROM tournament_participants tp
        JOIN players p ON tp.player_id = p.player_id
        WHERE tp.tournament_id = %s
    """
    cursor.execute(query,(game_name,))
    participants = cursor.fetchall()
    conn.commit()
    return render_template('participants.html', participants=participants)

@app.route('/player/leaderboard')
def leaderboard():
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        SELECT player_id, player_name, wins, losses, points
        FROM leaderboard_view
        ORDER BY points DESC
    """
    cursor.execute(query)
    leaderboard = cursor.fetchall()
    print(leaderboard)
    cursor.close()
    conn.close()
    return render_template('leaderboard.html', leaderboard=leaderboard)

@app.route('/player/matches/<int:player_id>')
@player_required
def player_matches(player_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
    SELECT *
    FROM matches
    WHERE player1_id = %s OR player2_id = %s
    """
    cursor.execute(query,(player_id,player_id))
    matches = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return render_template('player_matches.html', matches=matches)

@app.route('/player/logout')
@player_required
def player_logout():
    session.pop('player_id', None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)