<div align="center">

<img src="https://img.shields.io/badge/MatchPoint-Tournament%20Management-6C63FF?style=for-the-badge&logo=gamepad&logoColor=white" alt="MatchPoint"/>

# MatchPoint

### University Tournament Management System

*Engineered with precision. Designed for competition.*

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0%2B-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0%2B-4479A1?style=flat-square&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](./LICENSE)
[![Institution](https://img.shields.io/badge/Amrita%20Vishwa%20Vidyapeetham-Coimbatore-orange?style=flat-square)](https://www.amrita.edu/)
[![Semester](https://img.shields.io/badge/MSc%20ASDA-Semester%20II%20DBMS-blueviolet?style=flat-square)]()

<br/>

**MatchPoint** is a full-stack tournament management platform built with **Flask** and **MySQL**, designed to streamline the organisation and management of university-level gaming and esports tournaments. The system supports dual role-based workflows — **Admin** and **Player** — covering everything from tournament creation to real-time leaderboard generation, backed by a rigorously designed relational database.

<br/>

[Features](#-features) · [Architecture](#-system-architecture) · [Database Design](#-database-design) · [Setup](#-installation--setup) · [API Routes](#-route-reference) · [Roadmap](#-roadmap) · [Contributing](#-contributing) · [Authors](#-authors)

</div>

---

## Table of Contents

1. [Project Overview](#-project-overview)
2. [Features](#-features)
3. [System Architecture](#-system-architecture)
4. [Database Design](#-database-design)
5. [Tech Stack](#-tech-stack)
6. [Project Structure](#-project-structure)
7. [Installation & Setup](#-installation--setup)
8. [Route Reference](#-route-reference)
9. [Key Technical Highlights](#-key-technical-highlights)
10. [Security Considerations](#-security-considerations)
11. [Roadmap](#-roadmap)
12. [Contributing](#-contributing)
13. [Authors](#-authors)
14. [License](#-license)

---

## Project Overview

MatchPoint was built as a **Semester II DBMS project** for the MSc Applied Statistics and Data Analytics programme at **Amrita Vishwa Vidyapeetham, Coimbatore**. The goal was to go well beyond a basic CRUD application — to architect a system where the database is the backbone, not an afterthought.

The project demonstrates the practical application of:
- Relational schema design normalised to **Third Normal Form (3NF)**
- **SQL Views** for derived, reusable query logic
- **Triggers** for automated, event-driven database operations
- **Role-Based Access Control** enforced at both the application and session layer
- **Aggregation and analytics** queries for operational reporting

---

## Features

### Admin Capabilities

| Feature | Description |
|---|---|
| Secure Login | Admin authentication with session management and audit logging |
| Tournament Management | Create tournaments with game name, start/end dates |
| Player Management | Add players directly from the admin panel |
| Match Scheduling | Schedule matches between players within a tournament |
| Result Recording | Record scores, declare winner and loser per match |
| Admin Audit Logs | View the last 5 admin login events with timestamps |
| Monthly Analytics | Tournament count per month via SQL aggregation |
| Per-Game Analytics | Monthly breakdown of tournaments by game title |
| Dashboard | Overview of total tournaments at a glance |

### Player Capabilities

| Feature | Description |
|---|---|
| Self-Registration | Players register independently via the portal |
| Secure Login | Session-based authentication with role isolation |
| Browse Tournaments | View all available tournaments |
| Join Tournament | Enrol in any listed tournament |
| My Tournaments | View personally joined tournaments |
| Live Leaderboard | Real-time standings generated from a SQL View |
| Match History | View all scheduled matches involving the player |

---

## System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                        Browser                          │
│               HTML / CSS (Jinja2 Templates)             │
└────────────────────────┬────────────────────────────────┘
                         │  HTTP
┌────────────────────────▼────────────────────────────────┐
│                   Flask Application                     │
│                                                         │
│   ┌───────────────┐          ┌───────────────────────┐  │
│   │  Admin Routes │          │     Player Routes     │  │
│   │  /admin/*     │          │     /player/*         │  │
│   └──────┬────────┘          └──────────┬────────────┘  │
│          │                             │                │
│   ┌──────▼─────────────────────────────▼────────────┐   │
│   │           Authentication Decorators             │   │
│   │     @admin_required   |   @player_required      │   │
│   └──────────────────────┬──────────────────────────┘   │
│                          │                              │
│   ┌──────────────────────▼───────────────────────────┐  │
│   │             db.py — get_db_connection()          │  │
│   └──────────────────────┬───────────────────────────┘  │
└──────────────────────────┼──────────────────────────────┘
                           │  mysql-connector-python
┌──────────────────────────▼──────────────────────────────┐
│                     MySQL Database                      │
│                                                         │
│  Tables: players, admins, tournaments, matches,         │
│          match_results, tournament_participants,        │
│          admin_login_log, admin_audit                   │
│                                                         │
│  Views:    leaderboard_view                             │
│  Triggers: after_admin_login                            │
└─────────────────────────────────────────────────────────┘
```

---

## Database Design

### Entity-Relationship Summary

The database consists of **8 tables**, **1 view**, and **1 trigger**, normalised to 3NF.

```
admins ──────────────────────────── admin_login_log
                                          │
                                     admin_audit (via trigger)

players ─────────┬──────────────── tournament_participants
                 │                          │
                 │                     tournaments
                 │                          │
                 └──────── matches ─────────┘
                               │
                          match_results
                               │
                        leaderboard_view (derived)
```

### Schema Overview

| Table | Purpose | Key Columns |
|---|---|---|
| `admins` | Admin credentials | `admin_id`, `email`, `password` |
| `players` | Player profiles | `player_id`, `player_name`, `email`, `password` |
| `tournaments` | Tournament records | `tournament_id`, `tournament_name`, `game_name`, `start_date`, `end_date` |
| `tournament_participants` | Many-to-many: players ↔ tournaments | `participant_id`, `tournament_id`, `player_id` |
| `matches` | Scheduled match instances | `match_id`, `tournament_id`, `player1_id`, `player2_id`, `match_date`, `status` |
| `match_results` | Outcomes per match | `result_id`, `match_id`, `player1_score`, `player2_score`, `winner_id`, `loser_id` |
| `admin_login_log` | Admin login audit trail | `log_id`, `admin_username`, `login_time` |
| `admin_audit` | Trigger-generated audit messages | `audit_id`, `message`, `created_at` |

### View: `leaderboard_view`

Derives wins, losses, and points for every player dynamically:

```sql
SELECT 
    p.player_id,
    p.player_name,
    COUNT(CASE WHEN m.winner_id = p.player_id THEN 1 END) AS wins,
    COUNT(CASE WHEN m.loser_id  = p.player_id THEN 1 END) AS losses,
    COALESCE(SUM(CASE WHEN m.winner_id = p.player_id THEN 2 ELSE 0 END), 0) AS points
FROM players p
LEFT JOIN match_results m ON p.player_id = m.winner_id OR p.player_id = m.loser_id
GROUP BY p.player_id, p.player_name;
```

### Trigger: `after_admin_login`

Automatically writes a formatted audit entry to `admin_audit` after every row inserted into `admin_login_log`:

```sql
CREATE TRIGGER after_admin_login
AFTER INSERT ON admin_login_log
FOR EACH ROW
BEGIN
    INSERT INTO admin_audit(message)
    VALUES (CONCAT('Admin ', NEW.admin_username, ' logged in at ', NEW.login_time));
END;
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | HTML5, CSS3, Jinja2 |
| **Backend** | Python 3.9+, Flask |
| **Database** | MySQL 8.0+ |
| **DB Connector** | mysql-connector-python |
| **Session Management** | Flask server-side sessions |
| **Authentication** | Custom decorator-based RBAC |

---

## Project Structure

```
matchpoint/
│
├── app.py                        # Main Flask application — all routes
├── db.py                         # Database connection factory
├── schema.sql                    # Full database schema, views, triggers
│
├── templates/
│   ├── base.html                 # Base layout template
│   ├── login.html                # Unified login page
│   │
│   ├── admin_home.html           # Admin landing page
│   ├── admin_dashboard.html      # Admin statistics dashboard
│   ├── admin_logs.html           # Admin login audit log
│   ├── add_player.html           # Add player form
│   ├── create_tournament.html    # Create tournament form
│   ├── schedule_match.html       # Schedule match form
│   ├── record_result.html        # Record match result form
│   ├── monthly_stats.html        # Monthly tournament stats
│   ├── monthly_game_stats.html   # Per-game monthly stats
│   │
│   ├── player_home.html          # Player landing page
│   ├── player_register.html      # Player self-registration
│   ├── player_tournaments.html   # Browse all tournaments
│   ├── player_join_tournament.html # Join a tournament
│   ├── my_tournaments.html       # Player's joined tournaments
│   ├── player_matches.html       # Player's match schedule
│   ├── participants.html         # Tournament participants
│   └── leaderboard.html          # Live leaderboard
│
├── static/
│   ├── style.css                 # Global stylesheet
│   └── images/                   # Static assets
│
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE
└── README.md
```

---

## Installation & Setup

### Prerequisites

- Python 3.9 or higher
- MySQL 8.0 or higher
- pip

---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/kashyapramakrishnan/matchpoint.git
cd matchpoint
```

---

### 2️⃣ Install Dependencies

```bash
pip install flask mysql-connector-python
```

---

### 3️⃣ Configure the Database

Launch MySQL and run the schema file to create all tables, views, and triggers:

```bash
mysql -u root -p < schema.sql
```

Or from within the MySQL shell:

```sql
SOURCE schema.sql;
```

---

### 4️⃣ Update Database Credentials

Edit `db.py` with your local MySQL credentials:

```python
conn = mysql.connector.connect(
    host="localhost",
    user="your_mysql_username",
    password="your_mysql_password",
    database="tournament_db"
)
```

> ⚠️ Never commit real credentials to the repository. Use environment variables for any shared deployment.

---

### 5️⃣ Run the Application

```bash
python app.py
```

Open in your browser:

```
http://127.0.0.1:5000
```

---

### Default Admin Credentials (Development Only)

```
Email:    admin@admin.com
Password: admin
```

> ⚠️ For development and demonstration use only.

---

## Route Reference

### Authentication

| Method | Route | Description |
|---|---|---|
| `GET/POST` | `/login` | Unified login for admins and players |
| `GET` | `/admin/logout` | Admin session logout |
| `GET` | `/player/logout` | Player session logout |

### Admin Routes (require `@admin_required`)

| Method | Route | Description |
|---|---|---|
| `GET` | `/admin` | Admin home |
| `GET` | `/admin/dashboard` | Statistics dashboard |
| `GET` | `/admin/admin_logs` | Last 5 admin login events |
| `GET/POST` | `/admin/add_player` | Add a new player |
| `GET/POST` | `/admin/create_tournament` | Create a tournament |
| `GET/POST` | `/admin/schedule_match` | Schedule a match |
| `GET/POST` | `/admin/record_result` | Record a match result |
| `GET` | `/admin/monthly_stats` | Monthly tournament counts |
| `GET` | `/admin/monthly_game_stats` | Monthly per-game breakdown |

### Player Routes (require `@player_required`)

| Method | Route | Description |
|---|---|---|
| `GET` | `/player` | Player home |
| `GET/POST` | `/player/register` | Player self-registration |
| `GET` | `/player/tournaments` | Browse all tournaments |
| `GET/POST` | `/player/join` | Join a tournament |
| `GET` | `/player/my_tournaments` | View joined tournaments |
| `GET` | `/player/leaderboard` | View live leaderboard |
| `GET` | `/player/matches/<player_id>` | View matches for a player |

---

## Key Technical Highlights

**SQL View for Leaderboard**  
The leaderboard is not stored — it is derived on demand from `match_results` using a `LEFT JOIN` and conditional aggregation. This ensures the standings are always consistent with the actual match data, with no risk of stale cached values.

**Trigger-Based Audit Trail**  
The `after_admin_login` trigger fires automatically on every insert into `admin_login_log`, writing a formatted human-readable audit message to `admin_audit`. The application layer does not need to explicitly manage this — it is guaranteed by the database engine.

**Decorator-Based RBAC**  
Both `@admin_required` and `@player_required` are implemented as Python decorators using `functools.wraps`, cleanly separating authentication logic from route logic and allowing role enforcement to be applied declaratively.

**Parameterised Queries Throughout**  
All SQL statements use `%s` placeholders with `mysql-connector-python`'s parameterised execution, preventing SQL injection across all routes.

**Normalised to 3NF**  
The schema eliminates transitive dependencies. Player information, tournament metadata, participation records, and match outcomes are each stored in dedicated, purpose-specific tables with referential integrity enforced through foreign key constraints.

---

## Security Considerations

This project is an academic demonstration and has known limitations that would need to be addressed before any production deployment:

| Issue | Recommended Fix |
|---|---|
| Passwords stored in plaintext | Migrate to `bcrypt` via `werkzeug.security` |
| Hardcoded `secret_key` in `app.py` | Load from environment variable |
| No CSRF protection | Integrate Flask-WTF |
| No login rate limiting | Implement Flask-Limiter |
| No HTTPS enforcement | Configure via reverse proxy (nginx) |

See [`SECURITY.md`](./SECURITY.md) for the full responsible disclosure policy.

---

## Roadmap

- [ ] Tournament bracket visualisation (single elimination, round robin)
- [ ] bcrypt password hashing
- [ ] CSRF token protection
- [ ] Email notifications for match schedules
- [ ] Per-player statistics dashboard with win rate, streak, and match history
- [ ] Tournament-level leaderboards (not just global)
- [ ] Mobile-responsive UI overhaul
- [ ] REST API layer for future frontend decoupling
- [ ] Docker + docker-compose setup for portable deployment
- [ ] Automated database migrations

---

## Contributing

Contributions are welcome. Please read [`CONTRIBUTING.md`](./CONTRIBUTING.md) for branch naming conventions, commit message guidelines, coding standards, and the pull request process.

Please also review the [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md) before participating.

---

## Authors

<table>
<tr>
<td align="center">
<b>Kashyap Ramakrishnan</b><br/>
<a href="mailto:kashyapramakrishnan04@gmail.com">kashyapramakrishnan04@gmail.com</a><br/>
<a href="https://github.com/kashyapramakrishnan">@kashyapramakrishnan</a>
</td>
<td align="center">
<b>Sourav M B</b><br/>
<a href="mailto:me@sourav.ru">me@sourav.ru</a><br/>
<a href="https://github.com/souravmb">@souravmb</a>
</td>
</tr>
</table>

M.Sc Applied Statistics and Data Analytics  
**Amrita Vishwa Vidyapeetham, Coimbatore**

---

## License

This project is licensed under the **MIT License**.  
See [`LICENSE`](./LICENSE) for the full text.

---

<div align="center">

*Because storing data is easy.*  
*Designing it properly is where the real fight starts.*

<br/>

**MatchPoint** · Amrita Vishwa Vidyapeetham · 2026

</div>
