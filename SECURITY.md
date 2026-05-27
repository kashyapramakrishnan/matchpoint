# Security Policy

## Overview

The security of **MatchPoint** and its users is taken seriously. This document outlines which versions are actively maintained, how to responsibly report a vulnerability, and what contributors can expect during the disclosure process.

---

## Supported Versions

| Version | Status |
|---|---|
| `main` branch | ✅ Actively maintained |
| Older tagged releases | ❌ Not supported |

Only the current `main` branch receives security updates. If you are running an older snapshot, please update to the latest commit.

---

## Known Security Limitations (Acknowledged)

MatchPoint is an academic project developed as a Semester II DBMS coursework submission at **Amrita Vishwa Vidyapeetham, Coimbatore**. The following known limitations exist and are documented transparently:

| Issue | Severity | Status |
|---|---|---|
| Passwords stored in plaintext in MySQL | High | Documented — bcrypt migration listed in roadmap |
| `app.secret_key` is hardcoded | Medium | Not suitable for production deployment |
| No CSRF protection on forms | Medium | Documented — CSRF tokens listed in roadmap |
| No rate limiting on login endpoint | Medium | Documented |
| No HTTPS enforcement | Low | Out of scope for local development setup |

> ⚠️ **MatchPoint is not intended for production deployment in its current form.** It is a controlled academic demonstration. Do not deploy it on a public-facing server without addressing the above.

---

## Reporting a Vulnerability

If you discover a security vulnerability — including issues beyond those listed above — please follow responsible disclosure:

### 🔒 Do NOT open a public GitHub Issue for security vulnerabilities.

Instead, report it privately via email:

| Maintainer | Email |
|---|---|
| Kashyap Ramakrishnan | kashyapramakrishnan04@gmail.com |
| Sourav M B | me@sourav.ru |

### What to include in your report

Please provide as much detail as possible:

1. **Description** — A clear description of the vulnerability.
2. **Location** — The file, function, route, or SQL query where the vulnerability exists.
3. **Impact** — What an attacker could do if this vulnerability were exploited.
4. **Reproduction Steps** — A step-by-step guide to reproduce the issue.
5. **Suggested Fix** (optional but appreciated) — Your recommended remediation.
6. **Your contact information** — So we can follow up with you.

---

## Disclosure Process

Once a report is received:

1. **Acknowledgement** — We will acknowledge receipt of your report within **48 hours**.
2. **Assessment** — We will assess the severity and validity of the vulnerability within **5 business days**.
3. **Fix** — A patch will be developed and tested.
4. **Disclosure** — Once patched, we will publicly document the vulnerability and credit the reporter (unless you prefer to remain anonymous).

We ask that you give us a reasonable time to address the vulnerability before any public disclosure.

---

## Security Best Practices for Contributors

If you are contributing code to MatchPoint, please adhere to the following:

- **Never** commit credentials, API keys, or secrets to the repository.
- **Always** use parameterised SQL queries — never string interpolation.
- **Validate and sanitise** all user inputs on the server side.
- **Use HTTPS** in any deployment environment.
- **Hash passwords** — use `bcrypt` or `werkzeug.security` — never store plaintext.
- Report any security concerns you discover during development using the process above.

---

## Attribution

We deeply appreciate responsible security research and disclosure. Reporters who follow this policy will be acknowledged in the repository (with their permission) upon resolution of the reported issue.

---

*MatchPoint — Amrita Vishwa Vidyapeetham, Coimbatore*  
*MSc Applied Statistics and Data Analytics, Semester II*
