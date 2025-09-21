import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import datetime

st.set_page_config(page_title="DAAS Dashboard", layout="wide")

# ---- HEADER ----
st.title("DAAS Dashboard")
st.caption("Dewatering Analytics & Automation")

st.subheader("Solar & Optimization Analytics")
st.write("AI-driven energy insights and operational efficiency recommendations")

st.caption(f"Last updated: {datetime.datetime.now().strftime('%B %d, %Y at %I:%M %p')}")

# ---- KPI CARDS ----
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("kWh Today", "937", "+18% vs yesterday")
with col2:
    st.metric("kWh Used", "1,352", "-5% efficiency gain")
with col3:
    st.metric("Credits This Month", "129", "+23% growth")
with col4:
    st.metric("Saved This Month", "$3,479", "+15% vs last month")

st.markdown("---")

# ---- FILTERS ----
col1, col2 = st.columns([1,1])
with col1:
    time_filter = st.selectbox("Time Period", ["Last 7 Days", "Last 30 Days", "Last 12 Months"])
with col2:
    chart_type = st.selectbox("Chart Type", ["Line Chart", "Bar Chart"])

st.markdown("---")

# ---- CHARTS ----
col1, col2 = st.columns(2)

# Fake Data
days = pd.date_range(end=datetime.date.today(), periods=30)
solar_gen = np.random.randint(0, 80, size=30)
grid_con = 80 - solar_gen + np.random.randint(-10, 10, size=30)

df_solar = pd.DataFrame({"Date": days, "Solar Generation": solar_gen, "Grid Consumption": grid_con})

with col1:
    st.subheader("Solar Energy Usage")
    if chart_type == "Line Chart":
        fig = px.line(df_solar, x="Date", y=["Solar Generation", "Grid Consumption"])
    else:
        fig = px.bar(df_solar, x="Date", y=["Solar Generation", "Grid Consumption"])
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Pump Efficiency Trends")
    pump_data = pd.DataFrame({
        "Date": days,
        "Pump A-1": np.random.randint(80, 100, size=30),
        "Pump B-2": np.random.randint(65, 85, size=30),
        "Pump C-3": np.random.randint(50, 70, size=30),
    })
    fig2 = px.line(pump_data, x="Date", y=["Pump A-1", "Pump B-2", "Pump C-3"])
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# ---- CARBON CREDIT TRENDS ----
st.subheader("Carbon Credit Trends")
credits = np.cumsum(np.random.randint(50, 100, size=12))
df_credits = pd.DataFrame({"Month": pd.date_range("2025-01-01", periods=12, freq="M"), "Credits": credits})
fig3 = px.area(df_credits, x="Month", y="Credits")
st.plotly_chart(fig3, use_container_width=True)

c1, c2, c3 = st.columns(3)
c1.metric("Total Credits Earned", "1,863", "since Jan 2025")
c2.metric("Projected Annual", "2,433", "+27% above target")
c3.metric("Market Value", "$18,630", "@ $10 per credit")

st.markdown("---")

# ---- AI OPTIMIZATION RECOMMENDATIONS ----
st.subheader("AI Optimization Recommendations")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### High Priority")
    st.error("**Optimize Pump C-3 Schedule**  \n💰 Potential savings: $847/month  \nAI suggests running Pump C-3 during off-peak hours (11 PM - 6 AM).")
    st.button("Implement Pump C-3 Schedule")

    st.warning("**Increase Solar Panel Angle**  \n⚡ Potential gain: 15% efficiency  \nAdjusting solar panel angle to 32° for autumn season.")
    st.button("Implement Solar Angle Change")

with col2:
    st.markdown("### Medium / Low Priority")
    st.info("**Battery Storage Optimization**  \n💰 Potential savings: $425/month  \nStore excess solar energy during peak generation hours.")
    st.button("Implement Battery Optimization")

    st.success("**Carbon Credit Maximization**  \n➕ Additional credits: 45/month  \nImplement advanced monitoring for credit programs.")
    st.button("Implement Carbon Credit Strategy")

st.markdown("#### Implementation Tracking")
st.progress(7/12)
st.caption("Total Savings: $2,847/month | ROI: 247%")
