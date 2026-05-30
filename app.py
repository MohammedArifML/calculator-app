import streamlit as st
import pandas as pd
from datetime import datetime

if "history" not in st.session_state:
    st.session_state.history = []

st.set_page_config(
    page_title="Smart Calculator",
    page_icon="🧮",
    layout="centered"
)

st.sidebar.title("Maryam's Calculator App")

st.sidebar.info(
    """
    Built using:
    - Python
    - Streamlit
    """
)



st.title("🧮 Maryam's Calculator")

num1 = st.number_input(
    "Enter the First Number",
    format="%g"
)

num2 = st.number_input(
    "Enter the Second Number",
    format="%g"
)


operation = st.selectbox(
    "Operation",
    [
    "Add",
    "Subtract",
    "Multiply",
    "Divide"
]
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

        st.session_state.history.append({

        "Number 1": num1,
        "Operation": operation,
        "Number 2": num2,
        "Result": result,
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    })    
   

st.subheader("📊 Calculation History")

if st.session_state.history:

    history_df = pd.DataFrame(st.session_state.history)

    st.dataframe(
        history_df,
        use_container_width=True
    )

