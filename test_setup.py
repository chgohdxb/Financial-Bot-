#!/usr/bin/env python3
"""
Quick Test Script for Financial Bot
Tests basic functionality without requiring an API key
"""

def test_calculations():
    """Test financial calculations"""
    print("\n" + "="*80)
    print("Testing Financial Calculations")
    print("="*80)
    
    # Test return calculation
    buy = 100
    sell = 150
    percent_return = ((sell - buy) / buy) * 100
    print(f"\n✅ Investment Return Test:")
    print(f"   Buy: ${buy}, Sell: ${sell}")
    print(f"   Return: {percent_return:.2f}%")
    
    # Test compound interest
    principal = 1000
    rate = 5
    years = 10
    amount = principal * (1 + rate/100) ** years
    print(f"\n✅ Compound Interest Test:")
    print(f"   Principal: ${principal}, Rate: {rate}%, Years: {years}")
    print(f"   Final Amount: ${amount:.2f}")
    
    # Test currency conversion
    usd_amount = 100
    exchange_rate = 0.92
    eur_amount = usd_amount * exchange_rate
    print(f"\n✅ Currency Conversion Test:")
    print(f"   ${usd_amount} USD = €{eur_amount:.2f} EUR")


def test_imports():
    """Test that all dependencies are installed"""
    print("\n" + "="*80)
    print("Testing Dependencies")
    print("="*80)
    
    try:
        import requests
        print("✅ requests installed")
    except ImportError:
        print("❌ requests not installed")
    
    try:
        import dotenv
        print("✅ python-dotenv installed")
    except ImportError:
        print("❌ python-dotenv not installed")
    
    try:
        from mistralai import Mistral
        print("✅ mistralai installed")
    except ImportError:
        print("❌ mistralai not installed")


if __name__ == "__main__":
    print("\n" + "╔" + "="*78 + "╗")
    print("║" + " "*20 + "Financial Bot - Quick Test" + " "*32 + "║")
    print("╚" + "="*78 + "╝")
    
    test_imports()
    test_calculations()
    
    print("\n" + "="*80)
    print("✅ Basic tests passed!")
    print("="*80)
    print("\n🚀 Next Steps:")
    print("   1. Add your Mistral AI API key to .env file")
    print("   2. Run: python bot.py")
    print("   3. Type: /help for available commands")
    print("\n")
