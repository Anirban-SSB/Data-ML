#  Data ML Platform

End-to-end ETL + ML + Dashboard system.

## Features
- Modular ETL pipeline
- Anomaly Detection (ML)
- KPI Metrics
- Data Validation
- Streamlit Dashboard
- Docker Deployment

## Run
python run_pipeline.py

## Dashboard
streamlit run dashboard/app.py

## Docker
docker build -t DATA_ML .
docker run DATA_ML