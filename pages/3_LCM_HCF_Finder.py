import streamlit as st
import math

st.set_page_config(
    page_title="LCM & HCF Finder",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 LCM & HCF Finder")

st.info("Only positive numbers greater than 0 are allowed.")

# ---------------------------------------------------
# RESET SESSION STATE
# ---------------------------------------------------

if "lcm_num1" not in st.session_state:
    st.session_state.lcm_num1 = 1

if "lcm_num2" not in st.session_state:
    st.session_state.lcm_num2 = 1

if "hcf_num1" not in st.session_state:
    st.session_state.hcf_num1 = 1

if "hcf_num2" not in st.session_state:
    st.session_state.hcf_num2 = 1

# ---------------------------------------------------
# RESET BUTTON
# ---------------------------------------------------

if st.button("Reset All Inputs"):

    st.session_state.lcm_num1 = 1
    st.session_state.lcm_num2 = 1
    st.session_state.hcf_num1 = 1
    st.session_state.hcf_num2 = 1

    st.rerun()

# ---------------------------------------------------
# LCM SECTION
# ---------------------------------------------------

st.markdown("---")

st.subheader("📌 Find LCM")

lcm_num1 = st.number_input(
    "Enter First Number for LCM",
    min_value=0,
    step=1,
    format="%g",
    key="lcm_num1"
)

lcm_num2 = st.number_input(
    "Enter Second Number for LCM",
    min_value=0,
    step=1,
    format="%g",
    key="lcm_num2"
)

if st.button("Calculate LCM"):

    if lcm_num1 <= 0 or lcm_num2 <= 0:

        st.error("Only positive numbers greater than 0 are allowed.")

    else:

        try:

            lcm_result = abs(
                int(lcm_num1 * lcm_num2)
            ) // math.gcd(int(lcm_num1), int(lcm_num2))

            st.success(
                f"LCM of {int(lcm_num1)} and {int(lcm_num2)} = {lcm_result}"
            )

        except ZeroDivisionError:

            st.error("Division by zero occurred.")

# ---------------------------------------------------
# HCF SECTION
# ---------------------------------------------------

st.markdown("---")

st.subheader("📌 Find HCF")

hcf_num1 = st.number_input(
    "Enter First Number for HCF",
    min_value=0,
    step=1,
    format="%g",
    key="hcf_num1"
)

hcf_num2 = st.number_input(
    "Enter Second Number for HCF",
    min_value=0,
    step=1,
    format="%g",
    key="hcf_num2"
)

if st.button("Calculate HCF"):

    if hcf_num1 <= 0 or hcf_num2 <= 0:

        st.error("Only positive numbers greater than 0 are allowed.")

    else:

        try:

            hcf_result = math.gcd(
                int(hcf_num1),
                int(hcf_num2)
            )

            st.success(
                f"HCF of {int(hcf_num1)} and {int(hcf_num2)} = {hcf_result}"
            )

        except ZeroDivisionError:

            st.error("Division by zero occurred.")