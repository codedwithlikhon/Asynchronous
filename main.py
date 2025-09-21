import os
from dotenv import load_dotenv
import traceback

from browser_use import Agent, Browser
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env file
load_dotenv()

async def run_browser_agent():
    """
    Initializes and runs the browser agent.
    Returns a dictionary with the result.
    """
    try:
        # --- LLM Configuration ---
        # Make sure you have GOOGLE_API_KEY set in your .env file
        # You can get a key from https://aistudio.google.com/app/apikey
        llm = ChatGoogleGenerativeAI(model="gemini-pro")


        # --- Browser Configuration ---
        # We use the Browser-Use cloud service, which is ideal for cloud environments like Vercel.
        # This requires the BROWSER_USE_API_KEY environment variable to be set.
        # You can get a key from https://cloud.browser-use.com
        browser = Browser(use_cloud=True)


        # --- Agent Configuration ---
        agent = Agent(
            task='Visit https://duckduckgo.com and search for "Google Gemini"',
            browser=browser,
            llm=llm,
        )

        # Assuming agent.run() returns something meaningful. If not, we'll just report success.
        result = await agent.run()

        return {"status": "success", "result": result if result else "Task completed."}

    except Exception as e:
        print(f"Error in run_browser_agent: {e}")
        print(traceback.format_exc())
        return {
            "status": "error",
            "message": str(e),
            "traceback": traceback.format_exc()
        }
