from fastapi import FastAPI
import pandas as pd

app = FastAPI()
df = None

@app.on_event('startup')
def load_csv():
    global df
    try:
        df = pd.read_csv('modified.csv')
        df["month"] = pd.to_datetime(df["month"], format="%d.%m.%Y")
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
        "row_count": int(len(df)),
        "total_income": float(df["income"].sum()),
        "average_hourly_rate": round(float(df["hourly_rate"].mean()), 2),
        "unique_clients": int(df["client"].nunique()),
        "most_common_project_type": df["project_type"].mode()[0],    
    }
    return stats

# `/clients` – Return a list of unique clients
@app.get('/clients')
def get_clients():
     global df
     if df is None:
        return{"error" : "data not loaded" }
    
     clients = sorted(df["client"].dropna().unique().tolist())

     return {"clients" : clients}

# `/projects` – Return a count of each project type
@app.get('/projects')
def get_projects():
    global df
    if df is None:
        return{"error": "data not loaded"}
    
    projects = {
        "SEO" : df[df["project_type"] == "SEO"].shape[0],
        "Web Dev" :df[df["project_type"] == "Web Dev"].shape[0],
        "App Dev" :df[df["project_type"] == "App Dev"].shape[0],
        "Design":df[df["project_type"] == "Design"].shape[0],
        "Marketing":df[df["project_type"] == "Marketing"].shape[0],
    }

    return projects

# `/monthly-income` – Return income totals grouped by month
@app.get('/monthly-income')
def get_income():
    global df
    if df is None:
        return{"error": "data not loaded"}
    
    df["month_name"] = df["month"].dt.strftime("%B")

    income_by_month = df.groupby("month_name")["income"].sum()

    month_order = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    monthly_income = {month: round(float(income_by_month.get(month, 0)), 2)
                     for month in month_order if month in income_by_month}

    return monthly_income

