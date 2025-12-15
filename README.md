# Reliable Data Pipeline with Dashboard

## Overview
This project demonstrates a reliable data pipeline that:
- Fetches public crypto data from CoinGecko API
- Transforms and enriches the data
- Stores it in a SQL database (SQLite)
- Displays it in a simple dashboard
- Tracks pipeline health and failures

## Tech Stack
- Python
- SQLite
- FastAPI
- React
- Logging & Monitoring

## Pipeline Flow
Fetch → Transform → Store → Monitor → Display

## Setup Instructions

### FrontEnd
```bash
cd frontend/dashboard
npm install
npm start


### Backend
```bash
cd backend
pip install -r requirements.txt
python database.py
python fetch_data.py
uvicorn api:app --reload  # python -m uvicorn api:app --reload





