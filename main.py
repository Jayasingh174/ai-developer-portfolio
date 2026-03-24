from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI(title="Jaya Singh | AI Developer Portfolio")

@app.get("/")
async def serve_portfolio():
    # This serves your HTML file when someone visits the root URL
    return FileResponse("index.html")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)