# Saathi — Maternal & Child Healthcare Support Platform

Saathi is an academic full-stack project focused on organizing maternal and child healthcare information and supporting pregnancy-journey tracking through a FastAPI backend, PostgreSQL database, and Flutter application.

> **Project status:** Prototype / active development. The repository contains working backend API routes and pregnancy-journey logic, alongside an early Flutter UI. The mobile UI is not yet connected to the backend, and authentication, clinical validation, and production deployment are not implemented in the inspected code.

## Table of contents

- [What Saathi currently includes](#what-saathi-currently-includes)
- [Technology stack](#technology-stack)
- [Repository structure](#repository-structure)
- [Getting started](#getting-started)
- [Running the backend](#running-the-backend)
- [API endpoints](#api-endpoints)
- [Pregnancy journey logic](#pregnancy-journey-logic)
- [Flutter app](#flutter-app)
- [Current limitations and future work](#current-limitations-and-future-work)
- [Healthcare disclaimer](#healthcare-disclaimer)

## What Saathi currently includes

### Backend and data

The FastAPI backend currently defines API routes and SQLAlchemy models/schemas for:

- Mother records
- Pregnancy records linked to a mother
- Child records linked to a pregnancy
- Health events linked to a pregnancy
- User and appointment data models/schemas (models exist; CRUD routes are not currently exposed in `main.py`)

Pydantic schemas define request and response shapes, and SQLAlchemy maps Python models to PostgreSQL tables.

### Pregnancy journey tracking

The backend includes a rule-based journey module that:

- Defines pregnancy milestones, including four ANC visit milestones, lab test, ultrasound, delivery, and postnatal visit.
- Categorizes milestones as completed, current, upcoming, or requiring verification.
- Calculates pregnancy age in weeks from the recorded last menstrual period (when available).
- Produces a next-milestone field and verification-gap messages through the journey API.

This is prototype rule-based tracking, not a clinically validated decision-support or diagnostic system. Milestone timing and outputs require review by qualified healthcare professionals before any real-world use.

## Technology stack

| Layer | Technologies |
|---|---|
| Backend API | Python, FastAPI, Uvicorn |
| Data and ORM | PostgreSQL, SQLAlchemy, psycopg2 |
| Request/response validation | Pydantic |
| Mobile UI | Flutter, Dart |

## Repository structure

```text
Saathi/
├── backend/
│   ├── journey/
│   │   ├── engine.py
│   │   ├── gap_detector.py
│   │   └── milestones.py
│   ├── models/
│   ├── schemas/
│   ├── main.py
│   ├── database.py
│   ├── create_tables.py
│   ├── requirements.txt
│   └── test_journey.py
├── saathi_app/
│   ├── lib/
│   │   └── main.dart
│   └── pubspec.yaml
└── README.md
```

## Getting started

### Prerequisites

Install the following:

- Python (compatible with the versions supported by the packages in `backend/requirements.txt`)
- PostgreSQL
- Flutter SDK (for the mobile UI)

### 1. Clone the repository

```powershell
git clone https://github.com/sejal6787/Saathi.git
cd Saathi
```

### 2. Create and activate a Python virtual environment

Run these commands in Windows PowerShell:

```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If PowerShell blocks activation, review your local PowerShell execution-policy settings rather than running project commands outside the intended environment.

### 3. Configure PostgreSQL

Create a PostgreSQL database named `saathi` (or choose another name and configure the connection accordingly).

**Database configuration note:** The current `backend/database.py` contains a database connection string in source code. Before running the project, replace it with your own local connection details and do not commit passwords or other secrets. For a safer setup, read the connection string from an environment variable and keep credentials in a local, untracked `.env` file. Never use real patient data in this academic prototype.

The current table-creation script imports the SQLAlchemy models and runs `Base.metadata.create_all()`. From the activated backend virtual environment:

```powershell
python create_tables.py
```

This creates missing tables; it is not a database migration system.

### 4. Start the FastAPI server

From `D:\Saathi\backend` with the virtual environment activated:

```powershell
uvicorn main:app --reload
```

The local API is served at `http://127.0.0.1:8000`.

- Interactive Swagger documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
- Health check: [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)

## API endpoints

The routes currently declared in `backend/main.py` are:

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Basic API status message |
| GET | `/health` | Health-check response |
| POST | `/mothers` | Create a mother record |
| GET | `/mothers/{mother_id}` | Retrieve a mother record |
| POST | `/pregnancies` | Create a pregnancy record |
| GET | `/mothers/{mother_id}/pregnancy` | Retrieve a mother's pregnancy |
| POST | `/children` | Create a child record |
| GET | `/mothers/{mother_id}/child` | Retrieve a child associated with a mother's pregnancy |
| POST | `/health-events` | Create a health event |
| GET | `/pregnancies/{pregnancy_id}/health-events` | List pregnancy health events by event date |
| GET | `/health-events/{event_id}` | Retrieve a health event |
| GET | `/mothers/{mother_id}/journey` | Return journey milestones, next milestone, gaps, and recorded events |

Open `/docs` while the server is running to inspect request and response schemas and try the routes.

## Pregnancy journey logic

The journey engine uses the milestone definitions in `backend/journey/milestones.py` and recorded pregnancy dates/events to build a structured journey response.

The response includes:

- `completed`
- `current`
- `upcoming`
- `verification_needed`
- `next_milestone`
- `gaps`
- Recorded health events

When key dates or records are missing, the prototype can mark items as requiring verification. These are software-generated tracking statuses and must not be interpreted as medical assessments.

## Flutter app

The Flutter project is located in `saathi_app/`. The currently inspected `lib/main.dart` contains a welcome screen, a login-form UI, and a sample home screen. The login button currently navigates locally to the sample home screen; it does not authenticate a user with the backend.

To run the Flutter app, open a separate PowerShell terminal:

```powershell
cd D:\Saathi\saathi_app
flutter pub get
flutter run
```

A Flutter-supported device, emulator, or configured desktop target must be available. Backend integration is future work.

## Current limitations and future work

The following are not represented as completed features in the inspected code:

- Backend-connected authentication and authorization
- CRUD API routes for users and appointments
- Flutter-to-FastAPI integration and persistent login
- Clinically reviewed and validated milestone rules or recommendations
- Production-grade security, privacy controls, deployment, monitoring, and healthcare compliance
- Automated test suite and comprehensive integration testing

Planned development may include completing frontend/backend integration, expanding maternal and child tracking, implementing appropriate professional review workflows, and conducting security, usability, and clinical validation.

## Healthcare disclaimer

Saathi is an academic software-development prototype. It is not a medical device and must not be used as a substitute for professional medical advice, diagnosis, treatment, or emergency care. Do not enter identifiable or real patient health information. Any future healthcare recommendations or clinical workflows require appropriate clinical oversight, validation, privacy safeguards, and applicable regulatory review.

## Author

**Sejal**

## Repository

[github.com/sejal6787/Saathi](https://github.com/sejal6787/Saathi)
