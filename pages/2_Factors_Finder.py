import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Factors Finder",
    page_icon="🔢",
    layout="centered"
)

st.title("🔢 Factors Finder")

st.info("Enter a number less than 1000")

number = st.number_input(
    "Enter the Number:",
    min_value=1,
    step=1,
    format="%g"
)

if number >= 1000:
    st.error("Please enter a number less than 1000")

if st.button("Find Factors") and number < 1000:

    factors = []

    for i in range(1, int(number) + 1):

        if number % i == 0:
            factors.append(i)

    factors_df = pd.DataFrame({

        "Factor Number": range(1, len(factors) + 1),
        "Factor": factors

    })

    st.success(f"Factors of {int(number)}")

    st.dataframe(
        factors_df,
        use_container_width=True
    )