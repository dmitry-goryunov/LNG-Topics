import hmac

import streamlit as st

# NOTE: soft "keep casual visitors out" check, not real access control — the
# repo is public. Reads from st.secrets when set (Streamlit Cloud secrets.toml:
# app_password = "..."), falling back to the demo default otherwise. Never
# reuse a real password here.
try:
    PASSWORD = st.secrets.get("app_password", "pass")
except Exception:
    # st.secrets raises instead of falling back to the default when no
    # secrets.toml exists at all (as opposed to the key just being absent).
    PASSWORD = "pass"


def check_password() -> bool:
    """Gates a page behind a shared password. Returns True once unlocked."""
    if st.session_state.get("authenticated"):
        return True

    st.title("🔒 LNG Topics")
    pwd = st.text_input("Password", type="password")
    if st.button("Enter"):
        if hmac.compare_digest(pwd, PASSWORD):
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("Incorrect password")
    return False
