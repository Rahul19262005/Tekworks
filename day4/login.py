import streamlit as st

st.header("Registration Form")

with st.form("login"):
    surname = st.text_input("Enter your surname")
    name = st.text_input("Enter your first name")
    email = st.text_input("Enter your email")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    submit = st.form_submit_button("Register")

if submit:
    if password != confirm_password:
        st.error(" Passwords do not match")
    else:
        st.success(" Registration successful!")
        st.write("Name:", name)
        st.write("Surname:", surname)
        st.write("Email:", email)
        st.write("Username:", username)

st.sidebar.title("Menu")
option = st.sidebar.selectbox(
"Choose page",
["Home", "About", "Contact"]
)
st.sidebar.write(f"You selected: {option}")