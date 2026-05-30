import streamlit as st

st.set_page_config(
    page_title="Prime Number Checker",
    page_icon="🔍",
    layout="centered"
)

st.title("🔍 Prime Number Checker")

st.markdown(
    """
    Check whether a number is prime or not.
    """
)

prime_number = st.number_input(
    "Enter a Number",
    min_value=0,
    step=1,
    format="%g"
)

if st.button("Check Prime Number"):

    is_prime = True

    if prime_number < 2:
        is_prime = False

    else:

        for i in range(2, int(prime_number ** 0.5) + 1):

            if prime_number % i == 0:
                is_prime = False
                break

    if is_prime:
        st.success(f"{int(prime_number)} is a Prime Number ✅")

    else:
        st.error(f"{int(prime_number)} is NOT a Prime Number ❌")