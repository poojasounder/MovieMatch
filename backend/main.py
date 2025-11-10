import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from model import recommend_movies

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return {"message": "MovieMatch API running"}

@app.post("/recommend")
async def recommend(request: Request):
    payload = await request.json()
    favorites = payload.get("favorites", [])
    start_time = time.time()
    recommendations = recommend_movies(favorites)
    latency = time.time() - start_time
    print(f"Recommendation latency: {latency:.3f} seconds")
    return {"recommendations": recommendations, "latency": latency}
