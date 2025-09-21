import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# ---------------- Page Config ----------------
st.set_page_config(page_title="DAAS Dashboard", layout="wide")

# ---------------- Sidebar Navigation ----------------
st.sidebar.title("Navigate")
page = st.sidebar.radio("Go to", ["Dashboard", "Billing & Credits", "Solar & Optimization"])

# ---------------- Dashboard Page ----------------
if page == "Dashboard":
    st.title("DAAS Dashboard")
    st.subheader("Dewatering Analytics & Automation")
    st.write("Main Dashboard - Overview of operations...")

    # Example random data for visualization
    st.write("### Pump Performance")
    data = pd.DataFrame({
        "Time": pd.date_range("2023-01-01", periods=10, freq="D"),
        "Pump A": np.random.randint(50, 100, 10),
        "Pump B": np.random.randint(40, 90, 10)
    })

    fig = px.line(data, x="Time", y=["Pump A", "Pump B"], title="Pump Performance Over Time")
    st.plotly_chart(fig, use_container_width=True)

# ---------------- Billing Page ----------------
elif page == "Billing & Credits":
    st.title("Billing & Credits")
    st.write("Billing information and credit usage will appear here.")

    # Example billing data
    billing_data = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr"],
        "Energy Cost ($)": [1200, 1100, 1300, 1250],
        "Credits Used": [200, 180, 220, 210]
    })

    st.table(billing_data)

    fig = px.bar(billing_data, x="Month", y="Energy Cost ($)", title="Monthly Energy Costs")
    st.plotly_chart(fig, use_container_width=True)

# ---------------- Solar Optimization Page ----------------
elif page == "Solar & Optimization":
    st.title("Solar & Optimization")
    st.write("AI optimization recommendations and solar data will appear here.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Optimize Pump C-3 Schedule")
        st.write("💡 Potential savings: **$847/month**")
        if st.button("Implement Pump Optimization"):
            st.success("✅ Pump C-3 schedule optimization implemented. New schedule active at 11 PM.")

    with col2:
        st.subheader("Battery Storage Optimization")
        st.write("💡 Potential savings: **$425/month**")
        if st.button("Implement Battery Optimization"):
            st.success("✅ Battery storage optimization activated.")

    # Example solar efficiency chart
    solar_data = pd.DataFrame({
        "Day": range(1, 8),
        "Efficiency (%)": np.random.randint(60, 95, 7)
    })

    fig = px.area(solar_data, x="Day", y="Efficiency (%)", title="Solar Panel Efficiency Over a Week")
    st.plotly_chart(fig, use_container_width=True)
