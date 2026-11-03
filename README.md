# AI Infrastructure Cost Sensitivity Calculator

> **👋 Made by Daniel Munoz** · [Meet the maker](https://github.com/damunozx123-debug/ventoy-fetch/blob/master/PORTFOLIO.md) · [Other projects](https://github.com/damunozx123-debug/ventoy-fetch/blob/master/PROJECTS.md) · [Hire / contact](mailto:damunozx123@gmail.com?subject=Technical%20work%20opportunity)

**Interested in trying it?** [Browse source](https://github.com/damunozx123-debug/ai-certainty-calculator) · [Download source ZIP](https://github.com/damunozx123-debug/ai-certainty-calculator/archive/refs/heads/main.zip) · [Report an issue](https://github.com/damunozx123-debug/ai-certainty-calculator/issues) · ⭐ Star the repository if it helped.


> A compact Streamlit experiment for exploring the financial effect of a **user-specified cost variance**. **Not an audit, billing integration, or validated savings forecast.**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/) [![Streamlit](https://img.shields.io/badge/Streamlit-prototype-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)

## What it does

Give the calculator a monthly AI infrastructure spend and an assumed variance. It displays the hypothetical difference at a monthly and annual scale. The model selection is a UI field only and currently **does not change the calculation**.

| Input | Purpose |
| --- | --- |
| Monthly AI spend | Base amount for the scenario |
| Primary model | Descriptive selection; not used by the formula |
| Typical surprise percentage | User-chosen scenario assumption, **not** observed waste |

The calculations are deliberately simple:

```text
estimated monthly variance = monthly spend × (assumed variance % / 100)
estimated annual variance = estimated monthly variance × 12
illustrative payback days = 5,000 / estimated monthly variance × 30
```

**Important:** The original UI calls these values an “uncertainty tax”, “annual waste” and “audit pays back” but **no underlying billing, measurement, auditing, or customer validation exists**. The `$5,000` audit fee in the formula is an assumed constant. The “Book Audit” button is not connected to a booking service.

## Run locally

The source is currently a single Python script named `App. Py` (with a space in the filename).

```bash
python -m pip install streamlit
streamlit run "App. Py"
```

Open the local address printed by Streamlit. No API key, external billing connection or remote database is required by this prototype.

## Current limitations

- No real cloud billing or GPU usage data is imported.
- No evidence that the assumed variance represents recoverable cost.
- No benchmark, workload optimisation, cost attribution or currency conversion.
- No verified financial ROI; the payback figure is illustrative.
- No automated test suite or hosted deployment documented in this repository.

## Next development priorities

1. Rename the source to `app.py`, add pinned dependencies and reproducible tests.
2. Replace “waste” wording with “scenario variance” throughout the UI and remove the inactive booking button.
3. Add explicit currency and unit labels, input validation and downloadable scenarios.
4. Introduce a documented real-cost data input with provenance, then compare scenarios against actual invoices.
5. Publish a worked example with labelled synthetic data before making any commercial claims.

## Maintainer

Created by [Daniel Munoz](https://github.com/damunozx123-debug). Related public project: [Ventoy Fetch](https://github.com/damunozx123-debug/ventoy-fetch).
