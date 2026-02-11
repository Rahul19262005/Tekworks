import streamlit as st
#header
st.header("Student Records Management")
#title
st.title("Welcome to the Student Management System")
#subheader
st.subheader("Manage student records efficiently and effectively.")
#horizontal line
st.markdown("--------------------------------------------------------------------")
#text
st.text("Hello!")
#write
st.write({"Name": "Rahul","Section":"DS-c"})
st.write("C27")
#markdown font styles
st.markdown("**Sports**")
st.markdown("*select any option*")
st.markdown("* Cricket\n* Basket Ball")
#caption
st.caption("Every Student must choose a Sport")

#code
st.code("""
def add(a,b):
return a+b
""",language="python")

#latex
st.latex(r'''
a^2+b^2=c^2
''')

#divider 
st.divider()

#button
if st.button("Click Me"):
    st.write("Submitted")
    st.success("operation successful")
    st.balloons()
else:
    st.write("Button not ckicked yet.")
    st.error("connection error!")

#text input 
name = st.text_input("enter your name:")
if name=="":
    st.warning("name cannot be empty")
elif not name.isalpha():
    st.error("name should only consist alphabets")
else:
    st.write(f"hello,{name}!")
feedback=st.text_area("enter feedback")
st.write(feedback)

#checkbox
if st.checkbox("i agree to terms and conditions"):
    st.write("thank yoou!")

#radio button
gender=st.radio("select your gender:", ("male","female","other"))
st.write("you selected",{gender})

#selectbox
country=st.selectbox("select your country:",("india","dubai"))
st.write("you have selected",(country))
skills=st.multiselect("select skills:",("python","c","c++"))
st.write("skills:",skills)
age=st.slider("select your age:",1,100)
st.write(f"your age is: {age}")
uploaded_file=st.file_uploader("choose a file")
if uploaded_file is not None:
    st.success("file uploaded successfully")
    st.write(f"Filename: {uploaded_file.name}")

st.divider()

#form method
with st.form("my_form"):
    name= st.text_input("Name: ")
    age=st.number_input("age:")
    submit=st.form_submit_button("submit")
if submit:
    st.balloons()
    st.write("ur done!")

st.divider()

with st.form("login_form"):
    id= st.text_input("username: ")
    password=st.text_input("pass:",type="password")
    login=st.form_submit_button("login")
if login:
    st.balloons()
    st.write("ur done!")   

st.divider()

#column method
col1,col2,col3=st.columns(3)
with col1:
    st.header("column 1")
    st.write("this is column 1")
with col2:
    st.header("column 2")
    st.write("this is column 2")
with col3:
    st.header("column 3")
    st.write("this is column 3")

st.divider()

#table
data = {
    'Name': ['Anurag', 'Sumit', 'Rohit'],
    'Age': [21, 22, 20],
    'Course': ['B.Tech', 'M.Tech', 'BBA']
}
st.table(data)

#sidebar
st.sidebar.title("Menu")
option = st.sidebar.selectbox(
"Choose page",
["Home", "About", "Contact"]
)
st.sidebar.write(f"You selected: {option}")

st.divider()

