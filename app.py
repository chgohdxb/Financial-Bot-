"""Streamlit Financial Education Bot - Lightweight Version"""
import streamlit as st
import os

st.set_page_config(page_title="💰 Financial Bot", layout="wide")

# Try to load API key
api_key = None
try:
    api_key = st.secrets.get("MISTRAL_API_KEY")
except:
    api_key = os.getenv("MISTRAL_API_KEY")

# Initialize session state
if 'history' not in st.session_state:
    st.session_state.history = []

# Sidebar
with st.sidebar:
    st.title("🤖 Financial Bot")
    if st.button("Clear Chat"):
        st.session_state.history = []

# Main UI
st.title("💰 Financial Education Bot")
st.warning("⚠️ Educational only - Not investment advice")

# Check API key
if not api_key:
    st.error("❌ API Key not configured. Add MISTRAL_API_KEY to Streamlit Secrets.")
    st.info("Steps: App Settings → Advanced settings → Secrets → Add MISTRAL_API_KEY")
else:
    st.success("✅ API Key loaded successfully!")
    
    # Import Mistral only if key exists
    from mistralai import Mistral
    
    client = Mistral(api_key=api_key)
    
    # Helper functions
    def calc_return(buy, sell):
        if buy <= 0:
            return "Error: Buy price must be positive"
        pct = ((sell - buy) / buy) * 100
        return f"Return: {pct:.2f}% | Profit: ${sell-buy:.2f}"
    
    def calc_compound(principal, rate, years, compounds=1):
        if principal <= 0 or rate < 0 or years <= 0:
            return "Error: Invalid values"
        amount = principal * (1 + rate/100/compounds)**(compounds*years)
        return f"Final: ${amount:,.2f} | Interest: ${amount-principal:,.2f}"
    
    def call_api(messages):
        try:
            response = client.chat.complete(
                model="mistral-small-latest",
                messages=messages,
                temperature=0.7,
                max_tokens=512
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"
    
    def process_input(user_input):
        lower = user_input.lower().strip()
        
        if lower.startswith('/calc_return'):
            try:
                parts = user_input.split()
                return calc_return(float(parts[1]), float(parts[2]))
            except:
                return "Usage: /calc_return <buy_price> <sell_price>"
        
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
            return """**Commands:**
- `/calc_return 100 150` - Investment ROI
- `/compound 1000 5 10` - Compound interest
- Just ask questions! (e.g., "What is a stock?")"""
        
        else:
            # Add user message to history
            st.session_state.history.append({"role": "user", "content": user_input})
            
            # Get AI response
            response = call_api(st.session_state.history)
            
            # Add to history
            st.session_state.history.append({"role": "assistant", "content": response})
            
            # Keep history manageable
            if len(st.session_state.history) > 20:
                st.session_state.history = st.session_state.history[-20:]
            
            return response
    
    # Display chat history
    st.subheader("💬 Chat")
    for msg in st.session_state.history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
    
    # Chat input
    user_input = st.chat_input("Ask a question or use a command...")
    if user_input:
        with st.chat_message("user"):
            st.write(user_input)
        
        with st.chat_message("assistant"):
            with st.spinner("⏳ Thinking..."):
                response = process_input(user_input)
            st.write(response)
    
    # Help section
    with st.expander("�� Help"):
        st.markdown("""
        **Try these:**
        - What is a stock?
        - Explain P/E ratio
        - /calc_return 100 150
        - /compound 1000 5 10
        - /help
        """)

st.markdown("---")
st.markdown("[GitHub](https://github.com/chgohdxb/Financial-Bot-) | Powered by Mistral AI")
