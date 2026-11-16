import streamlit as st

st.set_page_config(page_title="Khenchela-Sun", layout="wide")

st.title("☀️ Khenchela-Sun - Terrestrial Solar")

st.write("Tazoult - Batna - Algeria - 3200h Sun / Year")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Area", "90.02 m²", "Target 90.0 m² - 100.02%")

with col2:
    st.metric("Cost", "$15,275", "ROI 3.6 Months")

with col3:
    st.metric("Water", "33.3 Tons/Year", "100% Solar Pumping")

st.divider()

st.success("✅ Solar System for Agriculture - Khenchela")

st.write("Grounding: 40x40x40 cm, 1m copper rod, Charcoal+Salt - Khenchela 3200h Sun")

if st.button("Calculate My House"):
    st.balloons()
    st.write("Your system is ready for Khenchela!")
