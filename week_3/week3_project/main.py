from fastapi import FastAPI
import pandas as pd

app = FastAPI()
df = None

@app.on_event('startup')
def load_csv():
    global df
    try:
        df = pd.read_csv('modified.csv')
        print('csv loaded successfully')
    except Exception as e:
        print('Failed to load csv')

@app.get('/')
def root():
    return{"message": "Welcome to the Freelancer Stats API"}

@app.get('/stats')
def get_stats():
    global df
    if df is None:
        return{"error" : "data not loaded" }
    
    stats = {
        "row_count": len(df),
        "total_income": df["income"].sum(),
        "average_hourly_rate": round(df["hourly_rate"].mean(), 2),
        "most_common_project_type": df["project_type"].mode()[0],
        "unique_clients": df["client"].nunique(),
    }

    
    return stats

