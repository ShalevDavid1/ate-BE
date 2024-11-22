from fastapi import FastAPI, HTTPException

app = FastAPI()


# health check
@app.get("/health_check/")
def health_check():
    return "OK"
