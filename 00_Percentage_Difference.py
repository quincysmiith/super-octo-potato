import streamlit as st
from streamlit.components.v1 import html
from utils import matomo_tracking, make_logo

st.set_page_config(
    page_title="Percentage Difference Calculator",
    page_icon="🧊",
    layout="wide",
)

make_logo()



def calculate_percentage_difference(num1, num2):
    if num1 == 0 and num2 == 0:
        return "Both numbers are zero. Percentage difference is undefined."
    elif num1 == 0 or num2 == 0:
        return "One of the numbers is zero. Percentage difference is undefined."
    else:
        return ((num2 - num1) / abs(num1)) * 100


def main():
    st.title("Percentage Difference Calculator")

    num1 = st.number_input("Enter the first number:", step=0.01)
    num2 = st.number_input("Enter the second number:", step=0.01)

    if st.button("Calculate Percentage Difference"):
        percentage_difference = calculate_percentage_difference(num1, num2)
        st.write(
            f"The percentage difference between {num1} and {num2} is: {percentage_difference:.2f}%"
        )

    matomo_tracking()


if __name__ == "__main__":
    main()
