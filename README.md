# Secure Coding Review Report

## Application Profile
- **Language:** Python
- **Framework:** Flask
- **Objective:** Identify security vulnerabilities in `vulnerable_app.py` and provide remediation.

## Findings

### 1. SQL Injection (SQLi)
- **Vulnerable Code:** `cursor.execute(f"SELECT * FROM users WHERE username = '{query}'")`
- **Impact:** Critical. Attackers can inject malicious SQL payloads (e.g., `' OR 1=1 --`) to bypass authentication, read, modify, or drop database tables.
- **Remediation:** Use parameterized queries instead of string formatting.

### 2. Cross-Site Scripting (XSS)
- **Vulnerable Code:** `html_response = f"<h1>Search Results for: {query}</h1>"`
- **Impact:** High. User input is rendered directly into the HTML without sanitization. Attackers can inject malicious JavaScript to steal cookies or redirect users.
- **Remediation:** Escape user input before rendering.

### 3. Hardcoded Secrets
- **Vulnerable Code:** `SECRET_API_KEY = "12345-SUPER-SECRET-KEY"`
- **Impact:** High. Exposed secrets in source code can lead to unauthorized access.
- **Remediation:** Store secrets in environment variables.
