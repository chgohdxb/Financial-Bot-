"""Streamlit Financial Education Bot"""
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="💰 Financial Bot",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Get API key
try:
    api_key = st.secrets.get("MISTRAL_API_KEY")
except:
    api_key = os.getenv("MISTRAL_API_KEY")

if not api_key:
    st.error("❌ API Key not found in secrets or .env")
    st.stop()

# Initialize Mistral
from mistralai import Mistral
client = Mistral(api_key=api_key)

# Initialize session
if 'history' not in st.session_state:
    st.session_state.history = []

# SIDEBAR
with st.sidebar:
    st.title("🤖 Financial Bot")
    st.markdown("---")
    st.info("Educational finance chatbot powered by Mistral AI")
    st.warning("⚠️ Educational only. No investment advice.")
    if st.button("Clear Chat"):
        st.session_state.history = []
        st.rerun()

# MAIN
st.title("💰 Financial Education Bot")
st.warning("⚠️ Educational only. Not investment advice. Consult professionals!")

# Helper functions
def calc_return(buy, sell):
    pct = ((sell - buy) / buy) * 100
    return f"Return: {pct:.2f}% | Profit: ${sell-buy:.2f}"

def calc_compound(principal, rate, years, compounds=1):
    amount = principal * (1 + rate/100/compounds)**(compounds*years)
    return f"Final Amount: ${amount:,.2f} | Interest: ${amount-principal:,.2f}"

def call_api(messages):
    try:
        response = client.chat.complete(
            model="mistral-small-latest",
            messages=messages,
            temperature=0.7,
            max_tokens=1024
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def process(user_input):
    lower = user_input.lower().strip()
    
    if lower.startswith('/calc_return'):
        try:
            parts = user_input.split()
            return calc_return(float(parts[1]), float(parts[2]))
        except:
            return "Usage: /calc_return <buy> <sell>"
    elif lower.startswith('/compound'):
        try:
            parts = user_input.split()
            principal = float(parts[1])
            rate = float(parts[2])
            years = int(parts[3])
            compounds = int(parts[4]) if len(parts) > 4 else 1
            return calc_compound(principal, rate, years, compounds)
        except:
            return "Usage: /compound <principal> <rate> <years> [compounds/year]"
    elif lower.startswith('/help'):
        return """
**Commands:**
- `/calc_return 100 150` - ROI
- `/compound 1000 5 10` - Compound interest
- Just ask questions!
"""
    else:
        st.session_state.history.append({"role": "user", "content": user_input})
        response = call_api(st.session_state.history)
        st.session_state.history.append({"role": "assistant", "content": response})
        if len(st.session_state.history) > 20:
            st.session_state.history = st.session_state.history[-20:]
        return response

# CHAT
st.subheader("💬 Chat")
for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Ask a question...")
if user_input:
    with st.chat_message("user"):
        st.write(user_input)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = process(user_input)
        st.write(response)

st.markdown("---")
st.markdown("[GitHub](https://github.com/chgohdxb/Financial-Bot-) | Powered by Mistral AI")
