import streamlit as st
from demo import area_of_circle

# Create a simple multipage app using Streamlit's sidebar
page = st.sidebar.selectbox("Select a page", ["Home", "Circle Area Calculator"])

if page == "Home":
    st.title("Welcome to the Hello World App")
    st.write("Use the sidebar to navigate between pages.")
    st.stop()

if page == "Circle Area Calculator":
    st.title("Circle Area Calculator")
    st.write("This is a simple calculator app to compute the area of a circle.")

    radius = st.slider("Select the radius of the circle:", min_value=0.0, max_value=100.0, value=1.0, step=0.1)

    if st.button("Calculate Area"):
        area = area_of_circle(radius)
        st.write(f"The area of the circle is: {area:.2f}")
