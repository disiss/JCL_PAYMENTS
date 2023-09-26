import uvicorn

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
	return {"greeting":"Hello world"}

@app.get("/OAuth")
async def root():
	return {"greeting":"Hello world"}

@app.get("/notification")
async def root():
	return {"greeting":"Hello world"}


uvicorn.run(app, host="localhost", port=443)