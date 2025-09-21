from fastapi import FastAPI
from main import run_browser_agent
import traceback

app = FastAPI()

@app.get("/api/run")
async def run_agent_endpoint():
    """
    An endpoint to trigger the browser agent.
    It calls the agent function and returns its result directly.
    """
    try:
        result = await run_browser_agent()
        return result
    except Exception as e:
        # This is a fallback for errors that might occur outside of run_browser_agent
        print(f"Error in run_agent_endpoint: {e}")
        print(traceback.format_exc())
        return {
            "status": "error",
            "message": f"An unexpected error occurred in the API endpoint: {str(e)}",
            "traceback": traceback.format_exc()
        }

# The root endpoint can be a simple health check
@app.get("/")
def read_root():
    return {"status": "ok"}
