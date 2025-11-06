import streamlit as st

# Page configuration
st.set_page_config(page_title="Streamlit Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Streamlit Calculator")
st.write("A simple calculator built with Streamlit.")

# Input fields
a = st.number_input("Enter first number", value=0.0)
b = st.number_input("Enter second number", value=0.0)

# Select operation
operation = st.selectbox(
    "Select Operation",
    ["Add (+)", "Subtract (-)", "Multiply (×)", "Divide (÷)", "Power (^)", "Modulo (%)"]
)

# Perform calculation
if st.button("Calculate"):
    try:
        if operation == "Add (+)":
            result = a + b
        elif operation == "Subtract (-)":
            result = a - b
        elif operation == "Multiply (×)":
            result = a * b
        elif operation == "Divide (÷)":
            if b == 0:
                st.error("Division by zero is not allowed.")
            else:
                result = a / b
        elif operation == "Power (^)":
            result = a ** b
        elif operation == "Modulo (%)":
            if b == 0:
                st.error("Modulo by zero is not allowed.")
            else:
                result = a % b

        st.success(f"Result: {result}")

    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("---")
st.caption("Created with ❤️ using Streamlit")
