import streamlit as st
from multiapp import MultiApp
from apps import home, predictor # import your app modules here

app = MultiApp()

st.markdown("""
# m1A-Pred
""")

st.subheader("Predictor for 1-mehtyladenosine prediction in RNA sequences")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Predictor", predictor.app)
# The main app
app.run()
