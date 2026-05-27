-- Creating database
CREATE DATABASE tournament_db;
USE tournament_db;

-- Admin Table
CREATE TABLE admins(
    admin_id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100) NOT NULL
);

-- Inserting Sample Admin Details
INSERT INTO admins VALUES('admin@admin.com', 'admin');

-- Player Table
CREATE TABLE players (
    player_id INT PRIMARY KEY AUTO_INCREMENT,
    player_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tournaments Table
CREATE TABLE tournaments (
    tournament_id INT PRIMARY KEY AUTO_INCREMENT,
    tournament_name VARCHAR(150) NOT NULL,
    game_name VARCHAR(100) NOT NULL,
    start_date DATE,
    end_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tournament Participants Table
CREATE TABLE tournament_participants (
    participant_id INT PRIMARY KEY AUTO_INCREMENT,
    tournament_id INT,
    player_id INT,
    FOREIGN KEY (tournament_id) REFERENCES tournaments(tournament_id)
        ON DELETE CASCADE,
    FOREIGN KEY (player_id) REFERENCES players(player_id)
);

-- Matches Table
CREATE TABLE matches (
    match_id INT PRIMARY KEY AUTO_INCREMENT,
    tournament_id INT,
    stage_id INT,
    player1_id INT,
    player2_id INT,
    match_date DATETIME,
    status ENUM('scheduled','completed') DEFAULT 'scheduled',
    FOREIGN KEY (tournament_id) REFERENCES tournaments(tournament_id),
    FOREIGN KEY (player1_id) REFERENCES players(player_id),
    FOREIGN KEY (player2_id) REFERENCES players(player_id)
);

-- Match Results Table
CREATE TABLE match_results (
    result_id INT PRIMARY KEY AUTO_INCREMENT,
    match_id INT UNIQUE,
    player1_score INT,
    player2_score INT,
    winner_id INT,
    loser_id INT,
    FOREIGN KEY (match_id) REFERENCES matches(match_id)
        ON DELETE CASCADE,
    FOREIGN KEY (winner_id) REFERENCES players(player_id),
    FOREIGN KEY (loser_id) REFERENCES players(player_id)
);

-- Leaderboard View
CREATE OR REPLACE VIEW leaderboard_view AS
SELECT 
    p.player_id,
    p.player_name,
    COUNT(CASE WHEN m.winner_id = p.player_id THEN 1 END) AS wins,
    COUNT(CASE WHEN m.loser_id = p.player_id THEN 1 END) AS losses,
    COALESCE(SUM(CASE WHEN m.winner_id = p.player_id THEN 2 ELSE 0 END),0) AS points
FROM players p
LEFT JOIN match_results m 
    ON p.player_id = m.winner_id 
    OR p.player_id = m.loser_id
GROUP BY p.player_id, p.player_name;

-- Admin Login Log Table
CREATE TABLE admin_login_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    admin_username VARCHAR(50),
    login_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Admin Audit Table
CREATE TABLE admin_audit (
    audit_id INT AUTO_INCREMENT PRIMARY KEY,
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Admin Login Trigger
DELIMITER $$

CREATE TRIGGER after_admin_login
AFTER INSERT ON admin_login_log
FOR EACH ROW
BEGIN
    INSERT INTO admin_audit(message)
    VALUES (CONCAT('Admin ', NEW.admin_username, ' logged in at ', NEW.login_time));
END$$

DELIMITER ;