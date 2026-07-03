import streamlit as st

# NOTE: hardcoded on purpose for a simple demo gate. The repo is public, so
# this is a soft "keep casual visitors out" check, not real access control.
PASSWORD = "pass"


def check_password() -> bool:
    """Gates a page behind a shared password. Returns True once unlocked."""
    if st.session_state.get("authenticated"):
        return True

    st.title("🔒 LNG Topics")
    pwd = st.text_input("Password", type="password")
    if st.button("Enter"):
        if pwd == PASSWORD:
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("Incorrect password")
    return False
