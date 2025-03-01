import asyncio
import uvicorn
from src.bot.telegram_bot import create_application
from src.api.routes import app as fastapi_app
from src.database.models import init_db
import threading

async def run_bot():
    """Run the bot."""
    application = create_application()
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    
    try:
        # Just hang tight for now
        await asyncio.Event().wait()
    finally:
        await application.stop()

def run_api():
    """Run the FastAPI server."""
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)

async def main():
    """Run both the bot and API server."""
    # Initialize the database
    init_db()
    
    # Start the API server in a separate thread
    api_thread = threading.Thread(target=run_api)
    api_thread.daemon = True
    api_thread.start()
    
    # Run the bot in the main thread
    await run_bot()

if __name__ == "__main__":
    asyncio.run(main())