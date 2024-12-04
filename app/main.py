from dotenv import load_dotenv

load_dotenv()

from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from app.routes import restaurant, user, rating

app = FastAPI()

# Add CORS middleware to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (you can restrict this to specific domains)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# health check
@app.get("/health_check/")
def health_check():
    return "OK"


app.include_router(restaurant.router, prefix="/restaurants", tags=["Restaurants"])
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(rating.router, prefix="/ratings", tags=["Ratings"])

if __name__ == "__main__":
    import uvicorn
    import os

    uvicorn.run(
        "main:app",
        host=os.getenv("HOST", "127.0.0.1"),
        port=int(os.getenv("PORT", 8000)),
        reload=True,
    )
