import streamlit as st
import random

st.set_page_config(
    page_title="Fun Math Facts",
    page_icon="🎲",
    layout="centered"
)

st.title("🎲 Fun Math Facts")

math_facts = [

    "Zero is the only number that cannot be represented in Roman numerals.",

    "A circle has infinite lines of symmetry.",

    "The number 1089 always produces a special pattern in math tricks.",

    "Pi never ends and never repeats.",

    "A googol is the number 1 followed by 100 zeros.",

    "The symbol for division (÷) is called an obelus.",

    "7 is often considered the world's favorite number.",

    "There are infinitely many prime numbers."
]

st.markdown(
    """
    Click the button below to discover a random fun math fact.
    """
)

if st.button("Show Random Math Fact"):

    random_fact = random.choice(math_facts)

    st.info(random_fact)