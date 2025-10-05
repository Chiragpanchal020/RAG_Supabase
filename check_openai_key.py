#!/usr/bin/env python3
"""
Simple script to check if OpenAI API key is valid and working.
"""

import os
import sys
from openai import OpenAI

def check_openai_key():
    """Check if OpenAI API key is valid and working."""
    
    # Get API key from environment variable
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("❌ Error: OPENAI_API_KEY environment variable not set")
        print("Please set your OpenAI API key:")
        print("  Windows: set OPENAI_API_KEY=your_api_key_here")
        print("  Linux/Mac: export OPENAI_API_KEY=your_api_key_here")
        return False
    
    try:
        # Initialize OpenAI client
        client = OpenAI(api_key=api_key)
        
        # Test the API with a simple completion request
        print("🔍 Testing OpenAI API key...")
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Hello! This is a test message."}
            ],
            max_tokens=10
        )
        
        # If we get here, the API key is valid
        print("✅ OpenAI API key is valid and working!")
        print(f"📝 Test response: {response.choices[0].message.content}")
        return True
        
    except Exception as e:
        print(f"❌ Error testing OpenAI API key: {str(e)}")
        
        # Provide specific error messages
        if "Invalid API key" in str(e):
            print("💡 The API key appears to be invalid or malformed")
        elif "Insufficient credits" in str(e):
            print("💡 The API key is valid but you have insufficient credits")
        elif "Rate limit" in str(e):
            print("💡 API key is valid but you've hit the rate limit")
        else:
            print("💡 Check your internet connection and try again")
        
        return False

if __name__ == "__main__":
    print("🔑 OpenAI API Key Checker")
    print("=" * 30)
    
    success = check_openai_key()
    
    if success:
        print("\n🎉 Your OpenAI API key is ready to use!")
        sys.exit(0)
    else:
        print("\n💔 API key check failed. Please fix the issues above.")
        sys.exit(1)
