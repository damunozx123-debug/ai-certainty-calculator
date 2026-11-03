"""Scenario calculator; no cloud billing integrations or audit booking."""
import streamlit as st
from calculator import calculate

st.set_page_config(page_title="AI Infrastructure Cost Sensitivity", layout="wide")
st.title("AI Infrastructure Cost Sensitivity")
st.caption("Hypothetical scenario • no real spending audit or validated savings estimate")

col1, col2, col3 = st.columns(3)
with col1:
    monthly_spend = st.number_input("Assumed monthly AI spend ($)", min_value=0.0, value=200000.0, step=1000.0)
with col2:
    model = st.selectbox("Reference model (does not change calculation)", ["GPT-4o", "Llama 70B", "Claude 3.5", "Custom"])
with col3:
    variance_pct = st.slider("User-assumed variance (%)", min_value=0, max_value=100, value=35)

fee = st.number_input("Hypothetical one-time audit fee ($)", min_value=0.0, value=5000.0, step=100.0)
result = calculate(monthly_spend, variance_pct, fee)

st.metric("Illustrative monthly difference", f"${result.monthly_variance:,.0f}")
st.metric("Annualised scenario difference", f"${result.annual_variance:,.0f}")
if result.hypothetical_payback_days is None:
    st.info("Payback not defined when the assumed variance is zero.")
else:
    st.info(f"Illustrative fee / variance ratio: {result.hypothetical_payback_days:,.1f} days, assuming the full variance were recoverable.")

st.warning("This is a sensitivity model, not evidence of waste, attainable savings, demand, a consulting offer or a customer ROI. The reference model selection is informational only.")
