# AI-Powered Civic Hazard Detection and Human Safety Assistant System

A smart civic hazard reporting and safety assistant that:

- accepts a citizen photo + description
- detects likely civic hazards
- assesses severity and risk
- explains possible human impact
- suggests safety precautions
- generates a civic complaint report

This project is designed as a working MVP based on the research direction you studied.

## Tech stack

- Backend: Python, FastAPI
- Frontend: React + Vite
- Detection layer: rule-based classifier for MVP
- Upgrade path: YOLOv8 / YOLOv11 for real object detection

## Folder structure

```text
civic-hazard-system/
├── README.md
├── backend/
│   ├── .env.example
│   ├── requirements.txt
│   └── app/
│       ├── __init__.py
│       ├── config.py
│       ├── main.py
│       └── services/
│           ├── __init__.py
│           ├── hazard_detector.py
│           ├── severity_engine.py
│           ├── recommendation_engine.py
│           └── report_service.py
├── frontend/
│   ├── package.json
│   ├── vite.config.js
│   ├── index.html
│   └── src/
│       ├── App.jsx
│       ├── main.jsx
│       └── styles.css
└── .gitignore
```

## Backend setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# or .\.venv\Scripts\Activate.ps1  # Windows PowerShell
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Frontend setup

```bash
cd frontend
npm install
npm run dev
```

Open:
- Frontend: http://localhost:5173
- API docs: http://localhost:8000/docs

## Features included

- image upload
- hazard classification
- severity assessment
- human impact explanation
- safety recommendations
- civic complaint report generation

## Notes

This is a functional MVP. For production, replace the rule-based hazard detection with a real YOLO model and add:
- geolocation validation
- database storage
- authorities dashboard
- user auth
- duplicate complaint detection
- multilingual report generation
