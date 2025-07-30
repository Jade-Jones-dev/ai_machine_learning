# Freelancer Stats API – Project Backlog

##  Core Project Tasks
- [x] Load CSV on startup
- [x] Build `/stats` endpoint
- [x] Fix type casting & NumPy errors
- [x] Set up `.gitignore`
- [x] Migrate to `venv` environment
- [x] Write a clear `README.md` with setup + usage
- [x]Push project to GitHub

---

##  Stretch Goals (Python Practice + API Features)

### Additional API Endpoints
- [ ] `/clients` – Return a list of unique clients
- [ ] `/projects` – Return a count of each project type
- [ ] `/monthly-income` – Return income totals grouped by month
- [ ] `/stats?client=X` – Add optional query param filtering to `/stats` endpoint

###  Python Practice Tasks
- [ ] Create a `get_filtered_df(client=None, project_type=None)` utility function
- [ ] Use rounding consistently (e.g., `round(x, 2)` for floats)
- [ ] (Optional) Wrap job data in a class for structured access

---
##  If I have time
- [ ] Add a helpful root `/` route explaining available endpoints
- [ ] Add error handling for missing/invalid columns in CSV
- [ ] Format currency in a more readable way (e.g., `"£1,250.00"`)

---
