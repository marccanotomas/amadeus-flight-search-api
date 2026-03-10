# ✈️ Amadeus Flight Search API (Containerized)

A professional, lightweight API wrapper that acts as a bridge between end-users and the Amadeus Travel ecosystem. This project demonstrates high-level skills in **API Integration**, **Containerization (Docker)**, and **Modern DevOps (CI/CD)**, all operating within a strictly **100% Free Tier** architecture.

## 🚀 Live Demo

**Production URL:** https://possible-florina-vpt-33b3e3c0.koyeb.app/docs

> **Note:** As the service is hosted on a Free Tier instance, the container may take up to 30 seconds to "wake up" during the first request if it has been inactive.

---

## 🛠️ Tech Stack & Architecture

This project implements a robust "cost-zero" stack:

| Layer | Technology |
|---|---|
| **Backend** | Python 3.12 with FastAPI (high performance, auto-generated OpenAPI docs) |
| **Data Source** | Amadeus for Developers (GDS Test Environment) |
| **Containerization** | Docker (multi-stage-like build using `python-slim`) |
| **CI/CD** | GitHub Actions (Automated build and push to GHCR) |
| **Cloud Infrastructure** | Koyeb (Serverless container deployment) |

---

## 💎 Key Quality Standards

- **Security-First:** Implementation of `.env` patterns and GitHub Secrets to prevent API key leaks.
- **Architecture:** Decoupled authentication logic (OAuth2) from the search business logic.
- **Portability:** Dockerized environment ensuring *"it works on my machine"* translates to *"it works in production."*
- **Documentation:** Interactive Swagger UI available at the `/docs` endpoint.

---

## 📡 API Reference

### Flight Search
```
GET /api/flights
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| `origin` | `string` | ✅ | IATA code of the departure airport (e.g., `BCN`) |
| `destination` | `string` | ✅ | IATA code of the arrival airport (e.g., `JFK`) |
| `date` | `string` | ✅ | Departure date in `YYYY-MM-DD` format |

---

## 💻 Local Setup & Development

### 1. Clone the repository
```bash
git clone https://github.com/marccanotomas/amadeus-flight-search-api.git
cd amadeus-flight-search-api
```

### 2. Configure Environment Variables

Create a `.env` file in the root directory:
```env
AMADEUS_CLIENT_ID=your_api_key_here
AMADEUS_CLIENT_SECRET=your_api_secret_here
```

### 3. Run with Docker *(Recommended)*
```bash
docker build -t amadeus-flight-api .
docker run -p 8000:8000 --env-file .env amadeus-flight-api
```

### 4. Run without Docker
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload
```

---

## 🤖 CI/CD Workflow

The project includes a GitHub Action (`deploy.yml`) that automates the following on every push to `main`:

1. Checks out the code
2. Logs into the GitHub Container Registry (GHCR)
3. Builds the Docker image
4. Pushes the image with automated metadata tags