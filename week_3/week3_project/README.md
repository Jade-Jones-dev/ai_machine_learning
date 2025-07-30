Freelancer Stats API

Simple FASTAPI application that loads freelance job data

Loads and processes data from csv on server sartup
Returns aggregated stats

Setup
- Clone the repo
- Create virtual enviroment: python3 - m venv venv
                             source venv/bin/activate
- install dependencies: pip install -r requirements.txt
- run the server: uvicorn main:app --reload
- endpoints: root: http://127.0.0.1:8000/
             stats: http://127/0.0.1:8000/stats