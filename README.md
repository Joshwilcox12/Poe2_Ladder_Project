# 🧩 Path of Exile 2 Ladder & Item Tracker

This project is a work-in-progress data pipeline that collects and analyzes leaderboard and trade data from the Path of Exile 2 API. It started as a learning tool to help me understand **data engineering workflows**, and has evolved into a modular ETL system that integrates data collection, transformation, storage, and (soon) cloud automation and analytics.

---

## 🌟 Project Goals

This project was built to help me gain real-world experience in:

- Python scripting and automation
- Working with REST APIs
- Data cleaning and transformation
- SQL and database operations
- Building data pipelines
- Eventually deploying and scheduling these systems in the cloud

---

## 📈 Current Pipeline Flow (Local)

1. **`POE2_Ladder.py`**  
   - Pulls the top 1000 players from the current hardcore ladder.
   - Saves data as a CSV file.
   - Uploads it to a PostgreSQL database (using `psycopg2` and SQLAlchemy).
   - Runs daily at noon using Task Scheduler.

2. **`Grab_Trade.py`**  
   - Reads the top 100 players from the ladder data.
   - Uses the trade API to retrieve item listings for each player.
   - Cleans and formats item data for later analysis.
   - Outputs transformed data to CSV and stores it in the database.

---

## 🧠 Skills Learned So Far

- Navigating and reverse-engineering undocumented APIs via browser dev tools
- Using Python to extract, transform, and load structured and nested JSON
- Writing efficient loops and handling API rate limits using `time.sleep()`
- Building structured tables in PostgreSQL via pgAdmin
- Uploading data both via CSV and directly from pandas
- Automating local tasks using Windows Task Scheduler

---

## 🚀 Next Steps & Future Goals

I'm currently upgrading this project to become **cloud-based and fully automated**, and making it **reusable for any PoE 2 league**.

Planned improvements:
- [ ] Refactor the codebase to support dynamic league names
- [ ] Move storage from local machine to **Google Cloud Platform (GCP)** or similar
- [ ] Send processed data from GCP → Supabase (PostgreSQL hosting)
- [ ] Run the daily job from the cloud using Prefect Cloud
- [ ] Remove item data older than 2 weeks to manage storage usage
- [ ] Write reusable SQL queries in Supabase to answer business-style questions
- [ ] Bring the final output back into Python for **data analysis and visualizations** (e.g., item price trends, meta builds)
- [ ] Build dashboards using Streamlit or Tableau

---

## 🔍 Technologies Used

- **Python** (`requests`, `pandas`, `sqlalchemy`, `psycopg2`)
- **PostgreSQL** (local, moving to Supabase)
- **Task Scheduler** (for local automation; moving to cloud)
- **Path of Exile 2 internal API** and trade API
- **CSV/JSON** for intermediate storage and transformation

---

## 📌 Long-Term Vision

> To build a complete, reusable, cloud-hosted data pipeline that tracks top PoE2 players and their gear over time — and provides meaningful insights into the in-game economy and meta shifts.

This project reflects my journey from basic scripting to applied data engineering. Every improvement I make is a step toward a job-ready portfolio that proves I can build real pipelines, extract insights, and solve problems with data.

