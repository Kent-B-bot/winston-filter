import streamlit as st
import sys
import os

# Add root directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

st.set_page_config(page_title="Winston Filter Dashboard", layout="wide")

# Try launching main application logic
try:
    import main
    if hasattr(main, "main"):
        main.main()
except Exception as err:
    st.error(f"Error launching application: {err}")
    
