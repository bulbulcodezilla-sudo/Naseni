# Naseni ERP — Simple UI Test Framework (Playwright + Pytest + POM)

A beginner-friendly starter framework for testing the NASENI ERP web app
(`https://erp.naseni.xyz`), covering the **Login** screen and the
**My Desk** dashboard.

## What is POM (Page Object Model)?

Instead of writing raw Playwright clicks inside every test, we create
one Python class per screen (a "Page Object"). The class holds:
- the elements on that screen (buttons, fields)
- the actions you can do (login, search, click a tab)

Tests then read like plain English:
```python
login_page.login("email", "password")
```
instead of a pile of `page.locator(...)` calls repeated everywhere.

## Folder structure

```
Naseni/
├── config/
│   └── config.yaml        # base_url + login credentials
├── pages/
│   ├── base_page.py        # shared helper methods (click, type_text, ...)
│   ├── login_page.py        # Login screen
│   └── dashboard_page.py    # My Desk screen
├── tests/
│   ├── test_login.py
│   └── test_dashboard.py
├── utils/
│   └── config_reader.py     # loads config.yaml
├── conftest.py               # pytest fixtures: browser, page, config
├── pytest.ini
└── requirements.txt
```

## 1. One-time setup

```bat
:: activate your virtual environment
myenv\Scripts\activate

:: install everything needed
pip install -r requirements.txt
playwright install
```

## 2. Set your real password (don't put it in config.yaml)

```bat
set NASENI_PASSWORD=yourrealpassword
```

## 3. Run the tests

```bat
pytest                              :: run everything
pytest tests/test_login.py -v       :: run only login tests
pytest -k "dashboard"               :: run only tests with "dashboard" in the name
```

Since `headless: false` in `config.yaml`, a real Chrome window will pop
up and you can watch the test click through the app — great for learning.
Set it to `true` once you're comfortable and want faster/CI runs.

A report is generated at `reports/report.html` after each run — open it
in your browser to see pass/fail results.

## 4. If a locator doesn't match (very common with real apps!)

The selectors in `login_page.py` / `dashboard_page.py` were written
from your screenshots. Real apps sometimes hide extra attributes that
change what Playwright needs. If a test fails saying it "couldn't find"
an element, the fastest fix is:

```bat
playwright codegen https://erp.naseni.xyz/login
```

This opens a browser + a recorder window. Click the field/button you
care about, and Playwright shows you the exact locator to use — copy
it into the matching page object.

## 5. Adding a new screen

1. Create `pages/your_screen_page.py`, copy the pattern from
   `dashboard_page.py` (list the elements in `__init__`, add action
   methods below).
2. Create `tests/test_your_screen.py` and write tests using it.

That's the whole workflow — every new screen is just one more file.
