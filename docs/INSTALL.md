# Install AI Infrastructure Cost Sensitivity Calculator

This Streamlit application models **hypothetical cost variances**. It does not inspect real invoices or optimise cloud accounts.

## Prerequisites

Python 3.10 or later and an internet connection for the first dependency installation.

```sh
git clone https://github.com/damunozx123-debug/ai-certainty-calculator.git
cd ai-certainty-calculator
python3 -m venv .venv
. .venv/bin/activate
python -m pip install streamlit
streamlit run "app.py"
```

On Windows PowerShell use `py -m venv .venv`, `.venv\Scripts\Activate.ps1` and `py -m streamlit run "app.py"`.

## Using the app

Enter monthly spend and a scenario variance percentage; the two dollar amounts are `spend × percentage` and `12 × monthly variance`. The displayed payback uses a user-adjustable hypothetical audit fee (default $5,000), not an offer or measured ROI. The model selector is informational only.

The retired booking button was removed because no booking service exists. **Do not send actual client billing documents to the repo or GitHub issues.**

## Screenshots

Use the app in an empty local session and label screenshots **hypothetical scenario**. No audit or commercial outcome has been validated.
