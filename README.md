# MatchPoint 🎮

### University Tournament Management System

MatchPoint is a full-stack tournament management platform built using **Flask** and **MySQL**, designed to streamline the organization and management of university-level gaming and sports tournaments.

The system supports both **Admin** and **Player** roles, enabling tournament creation, player registration, match scheduling, result tracking, and dynamic leaderboard generation through a responsive web interface.

---

## 🚀 Features

### 👨‍💼 Admin Features

* Secure admin login system
* Create and manage tournaments
* Add and manage players
* Schedule matches
* Record match results
* View admin login activity logs
* Monthly tournament analytics
* Real-time leaderboard tracking

### 🎮 Player Features

* Player registration and login
* View available tournaments
* Join tournaments
* View personal tournament participation
* Access live leaderboard standings

---

## 🧠 Database Concepts Implemented

* Relational Database Design
* Database Normalization (up to 3NF)
* SQL Joins
* Views
* Triggers
* Aggregation Queries
* Role-Based Access Control
* Session Handling

---

## 🛠️ Tech Stack

### Frontend

* HTML
* CSS

### Backend

* Python (Flask)

### Database

* MySQL

---

## 📊 Key Highlights

* Dynamic leaderboard generation using SQL Views
* Trigger-based automated leaderboard updates
* Monthly tournament analytics using SQL aggregation
* Separate admin and player workflows
* Responsive esports-inspired UI design

---

## 📂 Project Structure

```bash
MatchPoint/
│
├── app.py
├── db.py
├── schema.sql
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── admin_dashboard.html
│   ├── leaderboard.html
│   └── ...
│
├── static/
│   ├── style.css
│   └── images/
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <repository-link>
cd MatchPoint
```

---

### 2️⃣ Install Dependencies

```bash
pip install flask mysql-connector-python
```

---

### 3️⃣ Configure MySQL

Create a MySQL database and import the schema:

```sql
SOURCE schema.sql;
```

Update database credentials inside `db.py`.

---

### 4️⃣ Run the Application

```bash
python app.py
```

Open in browser:

```bash
http://127.0.0.1:5000
```

---

## 📸 Demo

The project includes:

* Admin workflow demo
* Player workflow demo
* MySQL database operations
* Dynamic leaderboard updates

---

## 🔮 Future Improvements

* Tournament brackets visualization
* Email notifications
* Match history analytics
* Player statistics dashboard
* Mobile responsiveness
* Password encryption & security improvements

---

## 🤝 Contributors

* Kashyap Ramakrishnan
* Sourav M B

---

## 📌 Conclusion

MatchPoint was developed not just as a CRUD application, but as a system-focused project emphasizing database design, integrity, and practical workflow management.

Because storing data is easy.
Designing it properly is where the real fight starts.
