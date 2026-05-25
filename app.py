import streamlit as st

st.title("🧮 Calculator")

num1 = st.number_input("Enter the First Number")
num2 = st.number_input("Enter the Second Number")

operation = st.selectbox(
    "Operation",
    ["Add", "Subtract", "Multiply", "Divide"]
)

if st.button("Calculate"):

    if operation == "Add":
        result = num1 + num2

    elif operation == "Subtract":
        result = num1 - num2

    elif operation == "Multiply":
        result = num1 * num2

    elif operation == "Divide":

        if num2 == 0:
            st.error("Cannot divide by zero")
        else:
            result = num1 / num2

    if operation != "Divide" or num2 != 0:
        st.success(f"Result: {result}")