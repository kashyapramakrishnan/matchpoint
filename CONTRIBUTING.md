# Contributing to MatchPoint

Thank you for your interest in contributing to **MatchPoint** — a university tournament management system built with Flask and MySQL. Whether you're fixing a bug, proposing a feature, improving documentation, or refining the database design, every contribution matters.

Please take a few minutes to read these guidelines before contributing. They exist to keep the codebase clean, the review process efficient, and the collaboration enjoyable for everyone.

---

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [How to Contribute](#how-to-contribute)
4. [Development Setup](#development-setup)
5. [Branch Naming Convention](#branch-naming-convention)
6. [Commit Message Guidelines](#commit-message-guidelines)
7. [Pull Request Process](#pull-request-process)
8. [Coding Standards](#coding-standards)
9. [Database Contribution Guidelines](#database-contribution-guidelines)
10. [Reporting Bugs](#reporting-bugs)
11. [Suggesting Features](#suggesting-features)
12. [Contact](#contact)

---

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](./CODE_OF_CONDUCT.md). Please read it before contributing.

---

## Getting Started

1. **Fork** the repository on GitHub.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/<your-username>/matchpoint.git
   cd matchpoint
   ```
3. **Add the upstream remote:**
   ```bash
   git remote add upstream https://github.com/kashyapramakrishnan/matchpoint.git
   ```
4. **Create a new branch** for your work (see [Branch Naming Convention](#branch-naming-convention)).

---

## How to Contribute

There are several ways you can contribute:

| Type | Description |
|---|---|
| 🐛 Bug Fix | Fix an existing issue logged in the tracker |
| ✨ Feature | Implement a new feature from the roadmap or your own proposal |
| 📝 Documentation | Improve README, docstrings, or inline comments |
| 🗄️ Database | Optimise queries, improve schema design, add migrations |
| 🎨 UI/UX | Improve HTML templates or CSS styling |
| 🔒 Security | Identify and resolve security vulnerabilities |
| ✅ Tests | Add or improve test coverage |

---

## Development Setup

### Prerequisites

- Python 3.9+
- MySQL 8.0+
- pip

### Installation

```bash
# Install Python dependencies
pip install flask mysql-connector-python

# Set up the database
mysql -u root -p < schema.sql

# Update credentials in db.py
# host, user, password, database

# Run the application
python app.py
```

The application will be available at `http://127.0.0.1:5000`.

### Default Admin Credentials (Development Only)

```
Email:    admin@admin.com
Password: admin
```

> ⚠️ Never use default credentials in any production or public deployment.

---

## Branch Naming Convention

Use clear, descriptive branch names following this format:

```
<type>/<short-description>
```

| Type | When to use |
|---|---|
| `feat/` | New feature |
| `fix/` | Bug fix |
| `docs/` | Documentation changes only |
| `refactor/` | Code restructuring without behaviour change |
| `db/` | Schema or query changes |
| `style/` | UI/CSS changes |
| `security/` | Security patches |

**Examples:**
```
feat/tournament-brackets
fix/leaderboard-null-scores
docs/update-setup-guide
db/index-match-results
security/hash-passwords
```

---

## Commit Message Guidelines

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification.

### Format

```
<type>(<scope>): <short summary>

[optional body]

[optional footer]
```

### Types

| Type | Description |
|---|---|
| `feat` | A new feature |
| `fix` | A bug fix |
| `docs` | Documentation only |
| `style` | Formatting, no logic change |
| `refactor` | Code change that is neither fix nor feat |
| `db` | Database schema or query change |
| `security` | Security improvement |
| `chore` | Maintenance, dependency updates |

### Examples

```
feat(player): add match history view for individual players

fix(leaderboard): handle NULL scores in leaderboard_view query

db(schema): add index on match_results.winner_id for query optimisation

security(auth): replace plaintext passwords with bcrypt hashing
```

---

## Pull Request Process

1. Ensure your branch is **up to date** with `main`:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. Make sure your code **works locally** and does not break existing functionality.

3. Fill in the **pull request template** completely — incomplete PRs will be asked for more information before review.

4. Reference the relevant **issue number** (e.g., `Closes #12`) in your PR description.

5. PRs must be reviewed and approved by at least **one maintainer** before merging.

6. Maintainers may request changes. Please address all review comments respectfully and promptly.

7. Once approved, a maintainer will merge your PR using **squash and merge** to keep the commit history clean.

---

## Coding Standards

### Python (Flask)

- Follow [PEP 8](https://peps.python.org/pep-0008/) style guidelines.
- Use meaningful variable and function names.
- All routes must use appropriate authentication decorators (`@admin_required` / `@player_required`).
- Always close database cursors and connections, or use context managers.
- Never store credentials or secret keys in source code. Use environment variables.
- Use parameterised queries — never string-formatted SQL (prevents SQL injection).

```python
# ✅ Correct — parameterised query
cursor.execute("SELECT * FROM players WHERE email=%s", (email,))

# ❌ Wrong — vulnerable to SQL injection
cursor.execute(f"SELECT * FROM players WHERE email='{email}'")
```

### HTML Templates

- All templates must extend `base.html`.
- Use semantic HTML5 elements.
- Keep logic minimal in templates — push computation to Python.

---

## Database Contribution Guidelines

MatchPoint's database is a core part of the project. If you are modifying the schema:

- All schema changes must be reflected in `schema.sql`.
- Explain the rationale for structural changes (normalisation, performance, integrity).
- New tables must include appropriate **foreign keys** and **constraints**.
- New queries must be tested with sample data before submitting.
- Views and Triggers must include comments explaining their purpose.
- Do not drop or rename existing columns without a deprecation notice in the PR.

---

## Reporting Bugs

Use the **Bug Report** issue template. Include:

- A clear title and description
- Steps to reproduce the issue
- Expected vs actual behaviour
- Screenshots if applicable
- Environment details (OS, Python version, MySQL version)

---

## Suggesting Features

Use the **Feature Request** issue template. Include:

- The problem your feature solves
- A description of the proposed solution
- Any alternatives you considered
- Whether it involves database changes

---

## Contact

For questions, suggestions, or anything else:

| Maintainer | Email |
|---|---|
| Kashyap Ramakrishnan | kashyapramakrishnan04@gmail.com |
| Sourav M B | me@sourav.ru |

---

*MatchPoint — Amrita Vishwa Vidyapeetham, Coimbatore*  
*MSc Applied Statistics and Data Analytics, Semester II*
