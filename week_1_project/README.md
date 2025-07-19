**Project**: Write a Python script that pings a REST endpoint and logs JSON results.

**Project Outline**

- Objective: Write a Python script that pings a REST endpoint and logs JSON results.

1. Install Python 3.12 and create a project folder.
2. Create and activate a virtual environment with `python -m venv .venv`.
3. Write `ping_api.py` that sends a GET request to https://httpbin.org/get and prints the JSON.
  - Use `requests` to GET API data.
  - Print/log the results to a file.
4. Push the script and a one-paragraph README to GitHub.
6. Deliverable: Python file with README for setup.

**Checklist**
- [ ] Virtual environment set up
- [ ] Installed `requests` package
- [ ] Script fetches data from [sample API](https://jsonplaceholder.typicode.com/posts)
- [ ] Results are printed and saved
- [ ] README with exact setup steps

**Common Issues & Quick Tips**
- No module error: `pip install <package>`
- API 403: Add authentication header