# Playwright + Pytest Automation Framework

A scalable hybrid automation framework built using Python, Playwright, Pytest, and Requests.

This project demonstrates modern QA automation practices including:

- UI Automation using Playwright
- API Automation using Requests
- Page Object Model (POM)
- Pytest Fixtures
- Data-Driven Testing
- End-to-End Testing
- HTML Reporting
- Logging Framework
- GitHub Actions CI/CD
- Environment Variable Management
- Cross-Browser Testing

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Playwright | UI Automation |
| Pytest | Test Framework |
| Requests | API Automation |
| Pytest HTML | HTML Reporting |
| Logging Module | Logging Framework |
| python-dotenv | Environment Variable Management |
| GitHub Actions | CI/CD Pipeline |

---

# Framework Architecture

```text
saucedemo-automation-framework/
│
├── api/
│   ├── clients/
│   │   └── user_client.py
│   │
│   └── tests/
│       └── test_users_api.py
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_e2e_checkout.py
│
├── utils/
│   └── logger.py
│
├── reports/
├── logs/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Features Implemented

## UI Automation

- Login validation
- Product selection
- Cart validation
- Checkout flow
- End-to-end purchase workflow

---

## API Automation

- GET API validation
- POST API validation
- Status code validation
- Response body validation
- Request/response logging

---

## Framework Features

- Page Object Model (POM)
- Reusable BasePage
- Centralized Logging
- Environment Variable Support
- Cross-Browser Testing
- Pytest Fixtures
- Parametrized Tests
- HTML Reports
- GitHub Actions CI/CD

---

# Installation

## Clone Repository

```bash
git clone https://github.com/tomprasad/saucedemo-automation-framework
cd saucedemo-automation-framework
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Playwright Browsers

```bash
playwright install
```

---

# Environment Variables

Create a `.env` file in the project root:

```env
REQRES_API_KEY=your_api_key
```

---

# Running Tests

## Run All Tests

```bash
pytest
```

---

## Run Tests in Firefox

```bash
pytest --browser=firefox
```

---

## Run Smoke Tests

```bash
pytest -m smoke
```

---

## Run Regression Tests

```bash
pytest -m regression
```

---

## Run API Tests

```bash
pytest -m api
```

---

## Run End-to-End Tests

```bash
pytest -m e2e
```

---

# HTML Reporting

Reports are generated automatically using pytest-html.

Generated report location:

```text
reports/report.html
```

---

# Logging

Framework uses Python logging module with centralized logger implementation.

Generated log location:

```text
logs/automation.log
```

Logging includes:

- UI actions
- API requests
- API responses
- Business workflow logs
- Element interactions

---

# Cross-Browser Support

Supported browsers:

- Chromium
- Firefox
- WebKit

Examples:

```bash
pytest --browser=chromium
pytest --browser=firefox
pytest --browser=webkit
```

---

# CI/CD Pipeline

GitHub Actions workflow automatically:

- installs dependencies
- installs Playwright browsers
- executes UI and API tests
- runs scheduled daily regression execution
- uploads screenshots, logs, and reports as artifacts
- validates pull requests

Workflow file:

```text
.github/workflows/ci.yml
```

CI/CD capabilities implemented:

- Scheduled daily execution
- Cross-browser execution support
- Secure GitHub Secrets integration
- Automated artifact upload
- Failure screenshot capture
- HTML report generation
- Log collection

---

# Failure Screenshot Capture

Framework automatically captures screenshots when UI tests fail.

Generated screenshot location:

```text
screenshots/
```

Features:

- Timestamped screenshots
- Automatic failure detection
- Full-page screenshot capture
- CI artifact upload support

---

# Test Artifacts

GitHub Actions uploads the following artifacts automatically:

```text
screenshots/
logs/
reports/
```

Artifacts can be downloaded directly from the GitHub Actions workflow run.

---

# Test Design Patterns Used

- Page Object Model (POM)
- Fixture-Based Architecture
- Reusable Base Classes
- Centralized Logging
- Data-Driven Testing
- API Client Abstraction

---

# Future Improvements

- Docker Integration
- Parallel Execution Optimization
- Allure Reporting
- Database Validation
- Jenkins Integration
- Retry Mechanism
- API Schema Validation

---

# Author

Tom

QA Automation Engineer

