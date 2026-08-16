import streamlit as st
import requests

st.set_page_config(page_title="K8s SRE Copilot", layout="wide")
st.title("☸️ Enterprise K8s SRE Advanced RAG Copilot")

user_query = st.text_input("Enter your Kubernetes query/issue:")

if st.button("Submit Query"):
    if user_query:
        with st.spinner("Processing through Guardrails & LangGraph..."):
            try:
                res = requests.post("http://localhost:8000/api/v1/chat", json={"query": user_query})
                if res.status_code == 200:
                    data = res.json()
                    st.success(f"Source: {data['source']}")
                    st.write(data['response'])
                else:
                    st.error(res.json().get("detail", "Error processing request."))
            except Exception as e:
                st.error(f"Failed to connect to API server: {e}")