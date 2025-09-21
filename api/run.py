from fastapi import FastAPI
from main import run_browser_agent
import asyncio

app = FastAPI()

@app.get("/api/run")
async def run_agent_endpoint():
    """
    An endpoint to trigger the browser agent.
    """
    try:
        # Running the agent in a background task to avoid blocking the response
        # This is a simple way, but for production, you might want a more robust
        # task queue system like Celery.
        asyncio.create_task(run_browser_agent())
        return {
            "status": "success",
            "message": "Browser agent task started in the background."
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

# The root endpoint can be a simple health check
@app.get("/")
def read_root():
    return {"status": "ok"}
