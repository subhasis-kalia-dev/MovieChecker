# 🎬 AI-Enhanced Movie/TV Series Tracker

An intelligent **Movie & TV Series Tracker** that uses **Generative AI (OpenAI)** to provide **comprehensive, summarized, and context-aware details** for any movie or series entered by the user.  
Built with a **React.js frontend** and **FastAPI backend**, fully containerized with **Docker**, and deployed on a **private VPS (Linux)** accessible via **[subhasiskalia.online](https://subhasiskalia.online)**.

---

## 🚀 Key Features

- 🔍 **Smart Movie/Series Search:** Enter any movie or TV show name — the app fetches metadata and AI-generated summaries.
- 🧠 **AI-Powered Summaries:** Uses OpenAI’s LLM to produce a human-like overview, cast insights, and genre-based recommendations.
- ⚡ **FastAPI Backend:** High-performance Python API that handles requests, integrates with external data sources, and communicates with OpenAI.
- 🌐 **Responsive Frontend:** Sleek and minimal **React.js** interface with dynamic result rendering.
- 🐳 **Dockerized Architecture:** Both frontend and backend are containerized for consistent local and production builds.
- ☁️ **Private VPS Deployment:** Securely hosted on a private Linux VPS, connected to the **subhasiskalia.online** domain.
- 🔄 **REST API Ready:** Exposes endpoints for AI summary generation, allowing easy integration with other systems.

---

## 🧩 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | React.js|
| **Backend** | FastAPI, Python, Uvicorn |
| **AI Integration** | OpenAI LLM (GPT models) |
| **Containerization** | Docker, Docker Compose |
| **Deployment** | Private VPS (Ubuntu/Linux), Nginx Reverse Proxy |
| **Version Control** | Git & GitHub |

---

## ⚙️ Project Architecture

```bash
ai-movie-tracker/
├── frontend/                # React.js app
│   ├── src/
│   │   ├── components/      # UI components
│   │   ├── pages/           # Main app pages
│   │   └── services/        # API interaction layer
│   └── Dockerfile
│
├── backend/                 # FastAPI server
│   ├── main.py              # Core API logic
│   ├── models/              # Data models (Pydantic)
│   ├── services/            # OpenAI & movie data integration
│   └── Dockerfile
│
├── docker-compose.yml       # Multi-container setup
├── requirements.txt         # Python dependencies
├── package.json             # Frontend dependencies
└── README.md
The above file strcture as present in my private VPS.
