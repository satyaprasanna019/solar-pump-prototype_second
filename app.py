import streamlit as st
import pandas as pd
import numpy as np

# Page Config
st.set_page_config(page_title="DAAS Dashboard", layout="wide")

# Sidebar
st.sidebar.title("Navigate")
page = st.sidebar.radio(" ", ["Dashboard", "Billing & Credits", "Solar & Optimization"])

# Page Header
st.title("DAAS Dashboard")
st.subheader("Dewatering Analytics & Automation")

# ------------------ MAIN DASHBOARD ------------------
if page == "Dashboard":
    st.header("Main Dashboard")
    st.write("📊 Overview of operations, pump status, and energy analytics.")

    # Example pump performance chart
    st.subheader("Pump Performance (kWh)")
    pump_data = pd.DataFrame({
        "Pump": ["Pump A", "Pump B", "Pump C", "Pump D"],
        "Energy (kWh)": [420, 380, 500, 450]
    })
    st.bar_chart(pump_data.set_index("Pump"))

    # Example energy trend
    st.subheader("Energy Usage Trend")
    dates = pd.date_range("2025-09-01", periods=10)
    usage = np.random.randint(300, 600, size=10)
    usage_data = pd.DataFrame({"Date": dates, "Usage (kWh)": usage})
    st.line_chart(usage_data.set_index("Date"))

# ------------------ BILLING & CREDITS ------------------
elif page == "Billing & Credits":
    st.header("Billing & Credits")
    st.write("💰 Billing information and credit usage.")

    col1, col2 = st.columns(2)
    col1.metric("Current Month Bill", "$1,245")
    col2.metric("Credits Remaining", "320 kWh")

    # Monthly billing trend
    st.subheader("Monthly Billing Trend")
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"]
    bills = [1200, 1100, 1250, 1350, 1400, 1300, 1280, 1245]
    billing_data = pd.DataFrame({"Month": months, "Bill ($)": bills})
    st.line_chart(billing_data.set_index("Month"))

    # Credits usage
    st.subheader("Credit Usage")
    days = ["Day 1", "Day 5", "Day 10", "Day 15", "Day 20", "Day 25"]
    credits = [400, 380, 360, 340, 330, 320]
    credits_data = pd.DataFrame({"Day": days, "Credits (kWh)": credits})
    st.bar_chart(credits_data.set_index("Day"))

# ------------------ SOLAR & OPTIMIZATION ------------------
elif page == "Solar & Optimization":
    st.header("AI Optimization Recommendations")
    st.write("⚡ Actionable insights for energy savings and operational efficiency.")

    # High Priority
    st.subheader("High Priority")
    col1, col2 = st.columns(2)

    with col1:
        st.error("🔴 Optimize Pump C-3 Schedule\nPotential savings: $847/month")
        if st.button("Implement Pump C-3"):
            st.success("✅ Pump C-3 optimization implemented! New schedule will take effect at 11 PM.")

    with col2:
        st.warning("☀️ Increase Solar Panel Angle\nPotential gain: 15% efficiency")
        if st.button("Implement Panel Angle"):
            st.success("✅ Solar panel angle adjustment scheduled.")

    # Medium Priority
    st.subheader("Medium Priority")
    col3, col4 = st.columns(2)

    with col3:
        st.info("🔋 Battery Storage Optimization\nPotential savings: $425/month")
        if st.button("Implement Battery Optimization"):
            st.success("✅ Battery storage optimization implemented!")

    with col4:
        st.success("🌱 Carbon Credit Maximization\nAdditional credits: 45/month")
        if st.button("Implement Carbon Credits"):
            st.success("✅ Carbon credit maximization applied.")

    # Implementation Tracking
    st.subheader("Implementation Tracking")
    st.progress(7/12)
    st.write("**Total Savings:** $2,847/month")
    st.write("**ROI:** 247%")
