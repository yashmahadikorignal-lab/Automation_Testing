# OpenCart Selenium Automation Framework

A Page Object Model (POM) test automation framework for the [OpenCart](https://www.opencart.com/) demo storefront, built with **Selenium WebDriver**, **pytest**, and **Python**. Covers account registration, login, and logout flows, with HTML reporting, screenshots on failure, and data-driven tests via Excel.

## Tech Stack

- **Python 3.13**
- **Selenium WebDriver 4.48** — browser automation
- **pytest 9.1** — test runner, with `pytest-html` for reports and `pytest-xdist` for parallel runs
- **webdriver-manager** — auto-downloads the correct browser driver (Chrome / Firefox / Edge)
- **openpyxl** — reads test data from Excel for data-driven tests
- **allure-pytest** — optional richer reporting

## Project Structure

```
Automation Project/
├── Configuration/
│   └── config.ini          # base URL + test account credentials
├── PageObjects/             # one class per page (locators + actions)
│   ├── HomePage.py
│   ├── LoginPage.py
│   ├── RegisterPage.py
│   └── MyAccountPage.py
├── Test_cases/               # pytest test classes
│   ├── conftest.py           # driver setup/teardown, CLI options, report hooks
│   ├── test_account_registration.py
│   ├── test_login_account.py
│   └── test_logout_account.py
├── Test_Data/
│   └── Opencart_Login_Data.xlsx   # data-driven login test inputs
├── Utilities/
│   ├── readproperty.py       # reads config.ini (env vars override for CI)
│   ├── customlogger.py       # logging setup
│   ├── XLutils.py            # Excel helper
│   └── random_string.py      # random string generator (e.g. unique emails)
├── Report/                   # generated HTML test reports (gitignored)
├── Screenshots/               # failure screenshots (gitignored)
├── Logs/                      # run logs (gitignored)
├── pytest.ini                 # test markers: sanity / smoke / regression
├── requirements.txt
└── run.bat                    # Windows convenience runner
```

## Setup

1. Clone the repo and create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Update `Configuration/config.ini` with your target OpenCart URL and test account details, **or** set the equivalent environment variables (useful for CI):
   - `AUT_BASE_URL`
   - `AUT_EMAIL`
   - `AUT_PASSWORD`

## Running Tests

Run the full suite:
```bash
pytest Test_cases -v
```

Run against a specific browser, headless (e.g. on CI):
```bash
pytest Test_cases -v -s --browser=edge --headless
```

Run only a specific marker:
```bash
pytest Test_cases -m sanity
pytest Test_cases -m regression
```

On Windows, `run.bat` wraps the headless Edge run above.

HTML reports are written to `Report/` with a timestamped filename per run; failure screenshots are saved to `Screenshots/`.

## Test Coverage

| Test | Marker | Description |
|---|---|---|
| `test_account_registration.py` | `regression` | Registers a new account with a randomly generated identity |
| `test_login_account.py` | `sanity` | Logs in with configured credentials and verifies the My Account page |
| `test_logout_account.py` | `regression` | Data-driven login test reading multiple credential sets from Excel |

## Notes

- `Framework/` (the bundled virtual environment) is intentionally excluded from version control — install dependencies fresh via `requirements.txt` instead.
- Generated artifacts (`Report/`, `Screenshots/`, `Logs/`, `__pycache__/`) are also gitignored and recreated on every run.
