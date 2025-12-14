# 🚀 Quick Start Guide - Financial Bot

## ⚡ Get Started in 3 Steps

### Step 1: Add Your Mistral AI API Key

1. Get your API key from: https://console.mistral.ai/

2. Open the `.env` file in the financial_bot directory:
   ```
   /Users/joeannag/Documents/AI Folder Mistral AI BOT/financial_bot/.env
   ```

3. Replace `your_api_key_here` with your actual Mistral AI API key:
   ```
   MISTRAL_API_KEY=sk-proj-YOUR_ACTUAL_API_KEY_HERE
   MISTRAL_MODEL=mistral-small
   ```

### Step 2: Activate Virtual Environment

Open Terminal and run:

```bash
cd "/Users/joeannag/Documents/AI Folder Mistral AI BOT/financial_bot"
source venv/bin/activate
```

You should see `(venv)` prefix in your terminal.

### Step 3: Run the Bot

```bash
python bot.py
```

You should see the bot startup message and disclaimer. 🎉

---

## 📖 Quick Command Examples

### Ask a Question
```
You: What is a P/E ratio?
Bot: [Detailed explanation from Mistral AI]
```

### Calculate Investment Return
```
You: /calc_return 100 150
Bot: Shows that you made a 50% return
```

### Explain a Term
```
You: /explain dividend yield
Bot: [Definition and explanation]
```

### Summarize Market News
```
You: /summarize
Bot: Paste your text, and it will be summarized
```

### View All Commands
```
You: /help
Bot: Shows complete command list
```

---

## ✅ Verify Setup

Before running the bot, verify everything is working:

```bash
cd "/Users/joeannag/Documents/AI Folder Mistral AI BOT/financial_bot"
source venv/bin/activate
python test_setup.py
```

All tests should show ✅ marks.

---

## 🛠️ Project Structure

```
financial_bot/
├── bot.py                 # Main bot application
├── config.py              # Configuration management
├── requirements.txt       # Dependencies
├── .env                   # API key (create from .env.example)
├── .env.example           # Template for .env
├── README.md              # Full documentation
├── QUICKSTART.md          # This file
├── test_setup.py          # Dependency test script
├── setup.sh               # Auto setup script
└── venv/                  # Virtual environment (created automatically)
```

---

## 🐛 Troubleshooting

### "MISTRAL_API_KEY not found"
- ✅ Solution: Make sure `.env` file exists and has your API key

### "No module named 'mistralai'"
- ✅ Solution: Run `source venv/bin/activate` then `pip install -r requirements.txt`

### "Connection error"
- ✅ Solution: Check internet connection and API key validity

---

## 💡 Tips

1. **Maintain Context**: The bot remembers the last 20 messages. Refer back to previous responses for context.

2. **Be Specific**: More detailed questions get better responses.
   - ✅ "Explain how dividend reinvestment works"
   - ❌ "Tell me about dividends"

3. **Use Commands**: For calculations, use the specific commands:
   - `/calc_return` for investment returns
   - `/compound` for interest calculations
   - `/convert` for currency

4. **Save Conversations**: Copy important responses to a text file for reference

---

## 📚 Educational Resources

- [Mistral AI Documentation](https://docs.mistral.ai/)
- [Investopedia - Free Financial Education](https://www.investopedia.com/)
- [SEC Investor Education](https://www.investor.gov/)
- [Khan Academy - Finance](https://www.khanacademy.org/economics-finance-domain)

---

## ⚠️ Important Reminders

✅ **This bot provides EDUCATIONAL INFORMATION ONLY**

❌ Does NOT provide:
- Investment advice or recommendations
- Trading signals
- Financial forecasting
- Tax or legal advice

✅ **Always consult with:**
- Licensed financial advisors
- Tax professionals
- Investment managers
- Legal experts

---

## 🆘 Need Help?

1. Type `/help` in the bot for command reference
2. Check `README.md` for detailed documentation
3. Review example conversations in `README.md`
4. Check `.env` configuration

---

**Happy learning! 🎓**

For more details, see `README.md`
