from datetime import datetime
from pathlib import Path

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.services.hazard_detector import detect_hazard
from app.services.recommendation_engine import generate_recommendations
from app.services.report_service import generate_complaint_report
from app.services.severity_engine import evaluate_hazard

app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = Path(settings.upload_dir)
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@app.get("/api/health")
def health_check():
    return {"status": "ok", "service": settings.app_name}

@app.post("/api/analyze")
async def analyze_hazard(
    file: UploadFile = File(...),
    description: str = Form(""),
    location_name: str = Form(""),
    latitude: float | None = Form(None),
    longitude: float | None = Form(None),
    context: str = Form("busy_road"),
    area_type: str = Form("urban")
):
    if not file.content_type or "image" not in file.content_type:
        raise HTTPException(status_code=400, detail="Only image files are allowed.")

    file_bytes = await file.read()
    max_size = settings.max_upload_size_mb * 1024 * 1024
    if len(file_bytes) > max_size:
        raise HTTPException(status_code=400, detail="File too large.")

    file_ext = Path(file.filename or "upload.jpg").suffix or ".jpg"
    unique_name = f"{datetime.utcnow().strftime('%Y%m%d%H%M%S%f')}{file_ext}"
    file_path = UPLOAD_DIR / unique_name

    with open(file_path, "wb") as f:
        f.write(file_bytes)

    hazard_name = detect_hazard(file.filename or "upload", description, file_bytes)
    severity = evaluate_hazard(hazard_name, context=context, area_type=area_type)
    recommendations = generate_recommendations(hazard_name, context)
    report = generate_complaint_report(
        hazard_name=hazard_name,
        description=description,
        location_name=location_name,
        latitude=latitude,
        longitude=longitude,
        severity=severity
    )

    return {
        "hazard_detected": hazard_name,
        "severity": severity,
        "recommendations": recommendations,
        "report": report,
        "image_url": f"/uploads/{unique_name}"
    }

@app.get("/uploads/{filename}")
async def get_upload(filename: str):
    file_path = UPLOAD_DIR / filename
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found.")
    return {"file": str(file_path)}
