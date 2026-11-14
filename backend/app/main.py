from fastapi import FastAPI

app = FastAPI(
    title="FaultLens AI",
    description="Intelligent Bug Diagnosis and Fix Recommendation Platform",
    version="0.1.0",
)

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "FaultLens AI"}
