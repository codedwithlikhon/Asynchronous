import os
from dotenv import load_dotenv

from browser_use import Agent, Browser
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env file
load_dotenv()

async def run_browser_agent():
    """
    Initializes and runs the browser agent.
    """
    # --- LLM Configuration ---
    # Make sure you have GOOGLE_API_KEY set in your .env file
    # You can get a key from https://aistudio.google.com/app/apikey
    llm = ChatGoogleGenerativeAI(model="gemini-pro")


    # --- Browser Configuration ---
    # This configuration connects to your existing Chrome browser.
    # IMPORTANT: You may need to adjust the paths below to match your system.
    #
    # macOS:
    # executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    # user_data_dir='~/Library/Application Support/Google/Chrome'
    #
    # Windows:
    # executable_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
    # user_data_dir='%LOCALAPPDATA%\\Google\\Chrome\\User Data'
    #
    # Linux:
    # executable_path='/usr/bin/google-chrome'
    # user_data_dir='~/.config/google-chrome'

    # NOTE: You need to fully close Chrome before running this script.
    browser = Browser(
        executable_path='/usr/bin/google-chrome',
        user_data_dir='~/.config/google-chrome',
        profile_directory='Default',
    )


    # --- Agent Configuration ---
    agent = Agent(
        task='Visit https://duckduckgo.com and search for "Google Gemini"',
        browser=browser,
        llm=llm,
    )

    await agent.run()
