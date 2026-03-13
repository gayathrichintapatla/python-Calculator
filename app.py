# import streamlit as st
# st.title("Basic Calculator")
# num1=st.number_input("Enter first number",value=0,step=1)
# num2=st.number_input("Enter second number",value=0,step=1)
# operation=st.selectbox("Select Operation",
#                        ("Addition","Subtraction","Multiplication","Division"))
# result=0
# if st.button("Calculate"):
#     if operation == "Addition":
#         result=num1+num2
#     elif operation=="Subtraction":
#         result=num1-num2
#     elif operation=="Multiplication":
#         result=num1*num2
#     elif operation=="Division":
#         result=num1/num2
#     st.success(f"Result: {result:.2f}")

import streamlit as st
import math

st.set_page_config(page_title="Scientific Calculator", layout="centered")

# ---------- Styling ----------
st.markdown("""
<style>
.stApp {
    background-color:#0f172a;
    color:white;
}

div.stButton > button {
    height:40px;
    width:100%;
    font-size:14px;
    border-radius:6px;
    background-color:#1e293b;
    color:white;
}

div.stButton > button:hover {
    background-color:#334155;
}

input {
    text-align:right;
    font-size:22px !important;
}
</style>
""", unsafe_allow_html=True)

st.title("Scientific Calculator")

# ---------- Memory ----------
if "expr" not in st.session_state:
    st.session_state.expr = ""

# ---------- Display ----------
st.session_state.expr = st.text_input("", st.session_state.expr)

# ---------- Functions ----------
def add(val):
    st.session_state.expr += val

def clear():
    st.session_state.expr = ""

def delete():
    st.session_state.expr = st.session_state.expr[:-1]

def calculate():
    try:
        st.session_state.expr = str(eval(st.session_state.expr))
    except:
        st.session_state.expr = "Error"

def apply_func(func):
    try:
        value = eval(st.session_state.expr)
        st.session_state.expr = str(func(value))
    except:
        st.session_state.expr = "Error"

# ---------- Button Layout ----------

buttons = [
    ["7","8","9","/"],
    ["4","5","6","*"],
    ["1","2","3","-"],
    ["0",".","=","+"]
]

for row in buttons:
    cols = st.columns(4)
    for i,val in enumerate(row):

        if val == "=":
            cols[i].button(val, on_click=calculate)

        else:
            cols[i].button(val, on_click=add, args=(val,))

# ---------- Scientific Buttons ----------

s1,s2,s3,s4,s5 = st.columns(5)

s1.button("√", on_click=apply_func, args=(math.sqrt,))
s2.button("sin", on_click=apply_func, args=(math.sin,))
s3.button("cos", on_click=apply_func, args=(math.cos,))
s4.button("tan", on_click=apply_func, args=(math.tan,))
s5.button("log", on_click=apply_func, args=(math.log10,))

# ---------- Utility Buttons ----------

u1,u2,u3 = st.columns(3)

u1.button("^", on_click=add, args=("**",))
u2.button("X", on_click=delete)  # delete last character
u3.button("C", on_click=clear)