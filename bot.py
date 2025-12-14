"""
Financial Bot - Uses Mistral AI API for financial information and calculations
This bot provides educational information about finance and investing.
"""
import requests
import json
import re
from typing import Optional, Dict, Any
from config import MISTRAL_API_KEY, MISTRAL_MODEL, MISTRAL_API_URL

# ============================================================================
# DISCLAIMER
# ============================================================================
DISCLAIMER = """
╔════════════════════════════════════════════════════════════════════════════╗
║                        ⚠️  IMPORTANT DISCLAIMER ⚠️                         ║
║                                                                            ║
║  This Financial Bot is for EDUCATIONAL PURPOSES ONLY and provides         ║
║  general financial information. It does NOT provide:                      ║
║                                                                            ║
║  • Personalized financial advice                                          ║
║  • Investment recommendations                                             ║
║  • Trading advice or signals                                              ║
║  • Tax or legal advice                                                    ║
║                                                                            ║
║  Always consult with qualified financial advisors, tax professionals,     ║
║  and/or legal experts before making any financial decisions.              ║
║                                                                            ║
║  Past performance does not guarantee future results.                      ║
║  All investments carry risk, including potential loss of principal.       ║
╚════════════════════════════════════════════════════════════════════════════╝
"""


class FinancialBot:
    """Financial assistant bot powered by Mistral AI"""
    
    def __init__(self):
        self.api_key = MISTRAL_API_KEY
        self.model = MISTRAL_MODEL
        self.api_url = MISTRAL_API_URL
        self.conversation_history = []
        
    def _call_mistral_api(self, user_message: str) -> Optional[str]:
        """Call Mistral AI API with OpenAI-compatible format"""
        try:
            # Add user message to history
            self.conversation_history.append({
                "role": "user",
                "content": user_message
            })
            
            # Prepare the request
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": self.model,
                "messages": self.conversation_history,
                "temperature": 0.7,
                "max_tokens": 1024,
            }
            
            # Call the API
            response = requests.post(self.api_url, headers=headers, json=payload, timeout=30)
            response.raise_for_status()
            
            result = response.json()
            
            # Extract the assistant's response
            if 'choices' in result and len(result['choices']) > 0:
                assistant_message = result['choices'][0]['message']['content']
                
                # Add assistant response to history for context
                self.conversation_history.append({
                    "role": "assistant",
                    "content": assistant_message
                })
                
                # Keep conversation history manageable (last 10 exchanges)
                if len(self.conversation_history) > 20:
                    self.conversation_history = self.conversation_history[-20:]
                
                return assistant_message
            else:
                return "Error: Could not parse API response"
                
        except requests.exceptions.RequestException as e:
            return f"API Error: {str(e)}"
        except json.JSONDecodeError:
            return "Error: Could not parse JSON response from API"
        except Exception as e:
            return f"Unexpected error: {str(e)}"
    
    def calculate_percentage_return(self, buy_price: float, sell_price: float) -> str:
        """Calculate percentage return on investment"""
        try:
            if buy_price <= 0:
                return "Error: Buy price must be positive"
            
            percentage_return = ((sell_price - buy_price) / buy_price) * 100
            profit_loss = sell_price - buy_price
            
            return f"""
Calculation Results:
─────────────────────
Buy Price:        ${buy_price:,.2f}
Sell Price:       ${sell_price:,.2f}
Profit/Loss:      ${profit_loss:,.2f}
Return %:         {percentage_return:.2f}%
"""
        except ValueError:
            return "Error: Please provide valid numeric values"
    
    def calculate_compound_interest(self, principal: float, annual_rate: float, years: int, compounds_per_year: int = 1) -> str:
        """Calculate compound interest"""
        try:
            if principal <= 0 or annual_rate < 0 or years <= 0:
                return "Error: Principal and years must be positive; rate cannot be negative"
            
            rate_decimal = annual_rate / 100
            amount = principal * (1 + rate_decimal / compounds_per_year) ** (compounds_per_year * years)
            interest_earned = amount - principal
            
            return f"""
Compound Interest Calculation:
──────────────────────────────
Principal:        ${principal:,.2f}
Annual Rate:      {annual_rate}%
Time Period:      {years} years
Compounds:        {compounds_per_year}x per year
─────────────────────────────
Final Amount:     ${amount:,.2f}
Interest Earned:  ${interest_earned:,.2f}
"""
        except (ValueError, ZeroDivisionError):
            return "Error: Please provide valid numeric values"
    
    def currency_conversion(self, amount: float, from_currency: str, to_currency: str, exchange_rate: float) -> str:
        """Simple currency conversion with provided exchange rate"""
        try:
            if exchange_rate <= 0:
                return "Error: Exchange rate must be positive"
            
            converted_amount = amount * exchange_rate
            
            return f"""
Currency Conversion:
────────────────────
Amount:           {amount:,.2f} {from_currency.upper()}
Exchange Rate:    1 {from_currency.upper()} = {exchange_rate} {to_currency.upper()}
Result:           {converted_amount:,.2f} {to_currency.upper()}
"""
        except ValueError:
            return "Error: Please provide valid numeric values"
    
    def explain_financial_term(self, term: str) -> str:
        """Get AI explanation of a financial term"""
        prompt = f"""Explain the financial term '{term}' in simple terms suitable for beginners. 
Include a practical example if relevant. Keep the explanation concise (2-3 sentences)."""
        
        return self._call_mistral_api(prompt)
    
    def answer_financial_question(self, question: str) -> str:
        """Answer general financial questions"""
        system_context = """You are a friendly financial educator. Answer questions about:
- Basic investing concepts (stocks, bonds, ETFs, mutual funds)
- Financial terms and metrics (P/E ratio, market cap, dividend yield, ROI, etc.)
- Risk and diversification principles
- Basic financial calculations and concepts
- Market fundamentals

IMPORTANT: Always remind users that you provide educational information only, not investment advice.
Do not make specific investment recommendations or predict market movements.
Keep responses concise and clear."""
        
        prompt = f"{system_context}\n\nUser Question: {question}"
        return self._call_mistral_api(prompt)
    
    def summarize_market_text(self, text: str) -> str:
        """Summarize pasted market news or company information"""
        prompt = f"""Summarize the following market/financial text in 3-4 key points. 
Highlight the main investment-relevant facts. Keep it concise.

Text to summarize:
{text}"""
        
        return self._call_mistral_api(prompt)
    
    def process_user_input(self, user_input: str) -> str:
        """Process user input and route to appropriate handler"""
        user_input_lower = user_input.lower().strip()
        
        # Check for calculation commands
        if user_input_lower.startswith('/calc_return'):
            try:
                parts = user_input.split()
                buy_price = float(parts[1])
                sell_price = float(parts[2])
                return self.calculate_percentage_return(buy_price, sell_price)
            except (IndexError, ValueError):
                return "Usage: /calc_return <buy_price> <sell_price>\nExample: /calc_return 100 150"
        
        elif user_input_lower.startswith('/compound'):
            try:
                parts = user_input.split()
                principal = float(parts[1])
                rate = float(parts[2])
                years = int(parts[3])
                compounds = int(parts[4]) if len(parts) > 4 else 1
                return self.calculate_compound_interest(principal, rate, years, compounds)
            except (IndexError, ValueError):
                return "Usage: /compound <principal> <annual_rate> <years> [compounds_per_year]\nExample: /compound 1000 5 10 12"
        
        elif user_input_lower.startswith('/convert'):
            try:
                parts = user_input.split()
                amount = float(parts[1])
                from_curr = parts[2]
                to_curr = parts[3]
                rate = float(parts[4])
                return self.currency_conversion(amount, from_curr, to_curr, rate)
            except (IndexError, ValueError):
                return "Usage: /convert <amount> <from_currency> <to_currency> <exchange_rate>\nExample: /convert 100 USD EUR 0.92"
        
        elif user_input_lower.startswith('/explain'):
            term = user_input[8:].strip()
            if not term:
                return "Usage: /explain <financial_term>\nExample: /explain P/E ratio"
            return self.explain_financial_term(term)
        
        elif user_input_lower.startswith('/summarize'):
            return "Please paste the market/financial text you'd like summarized. Type on the next line:"
        
        elif user_input_lower.startswith('/help'):
            return self.show_help()
        
        else:
            # General financial question
            return self.answer_financial_question(user_input)
    
    def show_help(self) -> str:
        """Show available commands"""
        return """
╔════════════════════════════════════════════════════════════════════════════╗
║                    📊 FINANCIAL BOT - HELP MENU 📊                        ║
╚════════════════════════════════════════════════════════════════════════════╝

AVAILABLE COMMANDS:
──────────────────

💰 CALCULATIONS:
  /calc_return <buy_price> <sell_price>
    Calculate percentage return on investment
    Example: /calc_return 100 150

  /compound <principal> <annual_rate> <years> [compounds_per_year]
    Calculate compound interest
    Example: /compound 1000 5 10 12

  /convert <amount> <from_currency> <to_currency> <exchange_rate>
    Convert between currencies
    Example: /convert 100 USD EUR 0.92

📚 EDUCATION:
  /explain <term>
    Get explanation of a financial term
    Example: /explain dividend yield

  /summarize
    Summarize pasted market/financial text

❓ GENERAL:
  Just type any financial question!
  Examples:
    - What is an ETF?
    - How does compound interest work?
    - What's the difference between stocks and bonds?

⚠️  /disclaimer
    Show the important disclaimer

📖 /help
    Show this help menu

❌ /exit or /quit
    Exit the bot

╔════════════════════════════════════════════════════════════════════════════╗
║  Remember: This bot provides EDUCATIONAL information only.                ║
║  Consult qualified financial advisors for personalized advice.            ║
╚════════════════════════════════════════════════════════════════════════════╝
"""


def main():
    """Main bot loop"""
    print("\n" + "="*80)
    print(" "*20 + "🤖 FINANCIAL EDUCATION BOT 🤖")
    print("="*80)
    print(DISCLAIMER)
    
    bot = FinancialBot()
    print("\n✅ Bot initialized successfully!")
    print("Type '/help' for available commands or ask any financial question.\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            # Check for exit commands
            if user_input.lower() in ['/exit', '/quit', 'exit', 'quit']:
                print("\nBot: Thank you for using the Financial Bot! Always make informed financial decisions. 👋")
                break
            
            # Check for disclaimer
            if user_input.lower() == '/disclaimer':
                print("\nBot:" + DISCLAIMER)
                continue
            
            # Process input
            print("\nBot: ", end="", flush=True)
            response = bot.process_user_input(user_input)
            print(response + "\n")
            
        except KeyboardInterrupt:
            print("\n\nBot: Goodbye! Remember to consult with financial professionals. 👋")
            break
        except Exception as e:
            print(f"Bot: An error occurred: {str(e)}\n")


if __name__ == "__main__":
    main()
