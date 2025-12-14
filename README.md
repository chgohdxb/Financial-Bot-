# Financial Bot - README

## 🤖 Financial Education Bot with Mistral AI

A terminal-based financial assistant bot powered by Mistral AI's API. Provides educational information about investing, financial concepts, and simple calculations.

### Features

✅ **Educational Information**
- Explains financial terms (P/E ratio, market cap, dividend yield, etc.)
- Answers questions about basic investing concepts (stocks, ETFs, bonds, diversification, risk)
- Discusses market fundamentals and financial principles

✅ **Calculations**
- Calculate investment returns (buy/sell price → percentage return)
- Compound interest calculator
- Currency conversions

✅ **Content Summarization**
- Summarizes pasted market news or company information

✅ **Conversational AI**
- Maintains conversation history for context-aware responses
- Natural language understanding via Mistral AI API

⚠️ **Important Disclaimers**
- Educational purposes only
- NO personalized investment advice
- NO trading signals or recommendations
- Always consult qualified financial professionals

---

## 🚀 Setup Instructions

### 1. Prerequisites
- Python 3.8 or higher
- Mistral AI API key (get from https://console.mistral.ai/)

### 2. Install Dependencies

```bash
# Navigate to the financial_bot directory
cd /path/to/financial_bot

# Create and activate virtual environment (macOS/Linux)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure API Key

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env file and add your Mistral AI API key
nano .env
```

Add your API key:
```
MISTRAL_API_KEY=sk-proj-YOUR_API_KEY_HERE
MISTRAL_MODEL=mistral-small
```

### 4. Run the Bot

```bash
python bot.py
```

---

## 📖 Available Commands

### 💰 Calculations

**Calculate Investment Return:**
```
/calc_return 100 150
```
Calculates percentage return from buy price to sell price.

**Compound Interest:**
```
/compound 1000 5 10 12
```
Args: principal, annual_rate, years, compounds_per_year (optional, default=1)

**Currency Conversion:**
```
/convert 100 USD EUR 0.92
```
Args: amount, from_currency, to_currency, exchange_rate

### 📚 Education

**Explain Financial Term:**
```
/explain P/E ratio
/explain dividend yield
/explain ETF
```

**Summarize Market Text:**
```
/summarize
```
Then paste the text you want summarized.

### ❓ General

**Ask Financial Questions:**
```
What is an ETF?
How does compound interest work?
What's the difference between stocks and bonds?
```

**Show Help:**
```
/help
```

**Show Disclaimer:**
```
/disclaimer
```

**Exit Bot:**
```
/exit
or
/quit
```

---

## 📋 Example Conversation

```
You: What is compound interest?
Bot: Compound interest is the process where interest earned on an initial investment 
     generates its own interest, leading to exponential growth...

You: /explain dividend yield
Bot: Dividend yield is the annual dividend payment divided by the stock price,
     expressed as a percentage...

You: /calc_return 100 150
Bot: 
Calculation Results:
─────────────────────
Buy Price:        $100.00
Sell Price:       $150.00
Profit/Loss:      $50.00
Return %:         50.00%

You: /convert 100 USD EUR 0.92
Bot:
Currency Conversion:
────────────────────
Amount:           100.00 USD
Exchange Rate:    1 USD = 0.92 EUR
Result:           92.00 EUR
```

---

## ⚙️ Configuration

Edit `config.py` to modify:
- Default Mistral AI model (currently: `mistral-small`)
- API endpoint (defaults to official Mistral API)

---

## 🛡️ Safety Features

- ✅ Clear disclaimer on startup
- ✅ No investment advice or recommendations
- ✅ Educational focus only
- ✅ Error handling for invalid inputs
- ✅ API timeout protection (30 seconds)
- ✅ Conversation history limit (last 20 exchanges)

---

## 📝 Notes

### API Key Security
- **Never** commit your `.env` file with API keys to version control
- Use `.env` files only for local development
- For production, use secure environment variable management

### Conversation History
- The bot maintains conversation context for better responses
- History is limited to the last 20 messages to manage token usage
- History resets when you restart the bot

### Rate Limiting
- Be aware of Mistral AI's rate limits and token usage
- Monitor your API usage at https://console.mistral.ai/

---

## 🤝 Limitations & Disclaimers

This bot:
- ❌ Does NOT provide personalized investment advice
- ❌ Does NOT predict market movements
- ❌ Does NOT provide tax or legal advice
- ❌ Does NOT give trading signals or recommendations
- ⚠️ Is for educational purposes only

**Always consult with:**
- Licensed financial advisors
- Tax professionals
- Investment managers

---

## 🐛 Troubleshooting

### API Key Error
```
ValueError: MISTRAL_API_KEY not found in environment variables
```
**Solution:** Make sure you have a `.env` file with `MISTRAL_API_KEY=your_key`

### Connection Timeout
```
API Error: Connection timed out
```
**Solution:** Check your internet connection and Mistral AI API status

### Module Not Found
```
ModuleNotFoundError: No module named 'mistralai'
```
**Solution:** Run `pip install -r requirements.txt`

---

## 📚 Resources

- [Mistral AI Documentation](https://docs.mistral.ai/)
- [Investment Basics](https://www.investopedia.com/financial-education)
- [SEC Investor Education](https://www.investor.gov/)

---

## 📄 License

Educational project. Use responsibly and always consult qualified professionals for financial decisions.

---

**Last Updated:** December 2024
**Version:** 1.0

