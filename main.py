from fastapi import FastAPI

from routes import 

app = FastAPI()

FastAPI(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)