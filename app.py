import streamlit as st
import pandas as pd
import numpy as np
import datetime

# -------------- PAGE CONFIG --------------
st.set_page_config(page_title="DAAS Dashboard", layout="wide")

st.title("DAAS Dashboard")
st.subheader("Dewatering Analytics & Automation")

# Sidebar Navigation
page = st.sidebar.radio("Navigate", ["Dashboard", "Billing & Credits", "Solar & Optimization"])

# -----------------------------------------
# DASHBOARD PAGE
# -----------------------------------------
if page == "Dashboard":
    st.header("Main Dashboard")
    st.write("Overview of operations...")

# -----------------------------------------
# BILLING PAGE
# -----------------------------------------
elif page == "Billing & Credits":
    st.header("Billing & Credits")
    st.write("Billing information and credit usage will appear here.")

# -----------------------------------------
# SOLAR & OPTIMIZATION PAGE
# -----------------------------------------
elif page == "Solar & Optimization":
    st.header("Solar & Optimization Analytics")
    st.caption("AI-driven energy insights and operational efficiency recommendations")
    st.write(f"Last updated: {datetime.datetime.now().strftime('%B %d, %Y at %I:%M %p')}")

    # Top Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("kWh Today", "937", "+18% vs. yesterday")
    col2.metric("kWh Used", "1,352", "-5% efficiency gain")
    col3.metric("Credits This Month", "129", "+23% growth")
    col4.metric("Saved This Month", "$3,479", "+15% vs. last month")

    st.divider()

    # Fake charts placeholders
    st.subheader("Solar Energy Usage")
    st.line_chart(np.random.randn(30, 2), height=200)

    st.subheader("Pump Efficiency Trends")
    st.line_chart(np.random.randn(30, 3), height=200)

    st.subheader("Carbon Credit Trends")
    st.area_chart(np.random.randn(30, 1), height=200)

    st.divider()
    st.subheader("AI Optimization Recommendations")

    # Stateful storage
    if "implemented" not in st.session_state:
        st.session_state.implemented = {
            "pump": False,
            "solar": False,
            "battery": False,
            "carbon": False,
        }

    # High Priority
    st.markdown("### High Priority")
    col1, col2 = st.columns(2)

    with col1:
        st.error("**Optimize Pump C-3 Schedule**\nPotential savings: $847/month")
        if not st.session_state.implemented["pump"]:
            if st.button("Implement Pump C-3 Schedule"):
                st.session_state.implemented["pump"] = True
                st.success("Pump C-3 schedule optimization has been implemented. New schedule will take effect at 11 PM tonight.")
        else:
            st.success("✅ Pump C-3 optimization already implemented")

    with col2:
        st.warning("**Increase Solar Panel Angle**\nPotential gain: 15% efficiency")
        if not st.session_state.implemented["solar"]:
            if st.button("Implement Solar Panel Angle"):
                st.session_state.implemented["solar"] = True
                st.success("Solar panel angle adjusted to 32° for autumn season. Expected gain: +15%.")
        else:
            st.success("✅ Solar panel adjustment already implemented")

    # Medium Priority
    st.markdown("### Medium Priority")
    col3, col4 = st.columns(2)

    with col3:
        st.info("**Battery Storage Optimization**\nPotential savings: $425/month")
        if not st.session_state.implemented["battery"]:
            if st.button("Implement Battery Storage"):
                st.session_state.implemented["battery"] = True
                st.success("Battery storage optimization enabled. Peak-hour energy will now be stored for off-peak use.")
        else:
            st.success("✅ Battery storage already optimized")

    with col4:
        st.success("**Carbon Credit Maximization**\nAdditional credits: 45/month")
        if not st.session_state.implemented["carbon"]:
            if st.button("Implement Carbon Credit Maximization"):
                st.session_state.implemented["carbon"] = True
                st.success("Advanced monitoring enabled for additional carbon credit programs.")
        else:
            st.success("✅ Carbon credit maximization already implemented")

    st.divider()

    # Implementation Tracking
    total = len(st.session_state.implemented)
    done = sum(1 for v in st.session_state.implemented.values() if v)
    st.subheader("Implementation Tracking")
    st.progress(done / total)
    st.write(f"Recommendations Implemented: {done}/{total}")
    st.write(f"Total Savings: ${(847 + 425) if done >= 2 else 0}/month | ROI: 247% (if all applied)")
