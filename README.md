# 🎮 Game Scout Backend

A **real-time video game price tracker** backend built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **Selenium**.  
This service scrapes live game data from Steam, stores it in PostgreSQL, and exposes RESTful APIs for consumption by a frontend React.js dashboard.

---

## 🚀 Features

- Scrapes **top-selling games** from Steam using **Selenium**
- Extracts title, price, discount, rating, platform, release date, and link
- Stores data in **PostgreSQL** using **SQLAlchemy ORM**
- Provides RESTful APIs via **FastAPI**
- Supports live data updates and efficient querying
- Ready for deployment in a **containerized environment** (Docker-ready)

---

## 🧠 Tech Stack

| Component | Technology |
|------------|-------------|
| **Backend Framework** | FastAPI |
| **Database** | PostgreSQL |
| **ORM** | SQLAlchemy |
| **Web Scraping** | Selenium (Chrome WebDriver) |
| **Data Model** | Python Dataclasses & SQLAlchemy Models |
| **Environment Management** | dotenv / settings.py |
| **Web Server** | Uvicorn |
| **Package Management** | pip / requirements.txt |

---

## 📁 Project Structure

```
src/
├── includes/
│   ├── db.py                # Database connection and session helpers
|   |── schema.py            # Tables
│   ├── models.py            # SQLAlchemy models (Game schema)
│   ├── common.py            # Shared datetime and utility functions
│
├── v1/
│   ├── controller.py        # Request handling and response formatting
│   ├── services/            # Logger and Crons microservices
|   ├── steam.py             # Selenium-based Steam data scraper
|   ├── games.py             # Logic for API response
│
├── settings.py              # Environment configuration (imported from dev/prod folder CI/CD)
├── main.py                  # FastAPI app entry point
├
└── requirements.txt         # Python dependencies
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/jawwadabbasi/game-scout-webscraper-fastapi-react-selenium-postgresql.git
cd game-scout-webscraper-fastapi-react-selenium-postgresql
```

### 2️⃣ Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables
Copy `settings.py` file from `dev` folder and paste it under `src`


### 5️⃣ Run the FastAPI app
```bash
python src/main.py
```

Visit your docs at 👉 **http://localhost:8001/docs**

---

## 🧩 API Endpoints

| Method | Endpoint | Description |
|--------|-----------|-------------|
| `GET` | `/api/v1/Games` | Fetch all games |
| `GET` | `/api/v1/Games/{id}` | Fetch game by ID |
| `POST` | `/api/v1/Scraper/Steam` | Trigger live Steam scraping and update database |

---

## 🧰 Web Scraper Details

The **Steam Scraper** (Selenium-based) dynamically loads Steam’s *Top Sellers* page, scrolls to fetch all available games, and extracts:

- 🎮 Game Title  
- 💰 Price & Discounts  
- ⭐ Rating  
- 🧩 Platforms  
- 📅 Release Date  
- 🔗 Store Link  

Data is stored in PostgreSQL using the `Game` model in `includes/models.py`.

---

## 🌐 Integration with Frontend

This backend is designed to be consumed by a **React.js frontend**, which will render the scraped data, display analytics, and allow users to search and filter results in real-time.

---

## 🧪 Future Enhancements

- Add scheduler for automatic scraping (using Celery or APScheduler)  
- Add multi-store support (Epic Games, PlayStation Store, Xbox)  
- Implement authentication for API endpoints  
- Add pagination, sorting, and search filters to the API  

---

## 🧑‍💻 Author

**Jawwad Ahmed Abbasi**  
`Senior Software Developer`  
jawwad@kodelle.com

---

## 🏁 License

This project is licensed under the **MIT License** — free for personal and commercial use.