from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI, HTTPException
from app.routes import restaurant, user

app = FastAPI()


# health check
@app.get("/health_check/")
def health_check():
    return "OK"


app.include_router(restaurant.router, prefix="/restaurants", tags=["Restaurants"])
app.include_router(user.router, prefix="/users", tags=["Users"])

if __name__ == "__main__":
    import uvicorn
    import os

    uvicorn.run(
        "main:app",
        host=os.getenv("HOST", "127.0.0.1"),
        port=int(os.getenv("PORT", 8001)),
        reload=True,
    )
