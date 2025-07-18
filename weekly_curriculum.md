```markdown
# 17-Week AI & Agent-Building Curriculum

 This curriculum focuses on building core Python, data, ML, and AI agent skills with accessible projects and clear learning paths. 

---

## Week 1: Python Setup & Scripting Basics

**Key Topics & Resources**
- [AI Python for Beginners](https://learn.deeplearning.ai/courses/ai-python-for-beginners/)
<!--[Google’s Python Class (videos & written)](https://developers.google.com/edu/python)-->
- [Codecademy: Learn Python 3 (free)](https://www.codecademy.com/learn/learn-python-3)
- [Python for Everybody (audit free)](https://www.coursera.org/specializations/python)
- [Python scripting project video](https://www.youtube.com/watch?v=dQlw1Cdd3pw)
- [Python full course](https://www.youtube.com/watch?v=K5KVEU3aaeQ)
• [Python `venv` Primer – Real Python](https://realpython.com/python-virtual-environments-a-primer/) 

**Project**: Write a Python script that pings a REST endpoint and logs JSON results.

**Project Outline**

- Objective: Write a Python script that pings a REST endpoint and logs JSON results.
- Steps:
  - Set up a virtual environment.
  - Use `requests` to GET API data.
  - Print/log the results to a file.
- Deliverable: Python file with README for setup.

1. Install Python 3.12 and create a project folder.
2. Create and activate a virtual environment with `python -m venv .venv`.
3. Write `ping_api.py` that sends a GET request to https://httpbin.org/get and prints the JSON.
4. Push the script and a one-paragraph README to GitHub.

**Checklist**
- [ ] Virtual environment set up
- [ ] Installed `requests` package
- [ ] Script fetches data from [sample API](https://jsonplaceholder.typicode.com/posts)
- [ ] Results are printed and saved
- [ ] README with exact setup steps

**Common Issues & Quick Tips**
- No module error: `pip install <package>`
- API 403: Add authentication header

**Weeks workflow**

- Monday
- Tuesday started [AiPython for beginners]
- Wednesday continued [AiPython for beginners]
- Thursday continues [AiPython for beginners] tried [Google's Python class] didn't like it way it teaches
- Friday 
- Friday
- Saturday
- Sunday

**Checklist**

- [ ] Setup a virtual environment
- [ ] Use requests to get api data
- [ ] Print/log the results to a file.
- [ ] README updated

**Reflection:**

- What were the main challenges this week?
- What did I learn

---

## Week 2: Data Wrangling Foundations

**Key Topics & Resources**

- [NumPy Quickstart (docs)](https://numpy.org/devdocs/user/quickstart.html)
- [Pandas Official Tutorials](https://pandas.pydata.org/pandas-docs/stable/getting_started/tutorials.html)
- [YouTube: Pandas, NumPy, and Matplotlib for ML](https://www.youtube.com/watch?v=vmEHCJofslg)(https://www.youtube.com/watch?v=VX6kCjwdNPw)

**Project Outline**

- Objective: Load a CSV, clean data, and plot a column histogram.
- Steps:
  - Read CSV using pandas.
  - Apply basic cleaning (drop NAs, fix types).
  - Use matplotlib to plot.
- Deliverable: Jupyter notebook with code and histogram.

**Weeks workflow**

- Monday
- Tuesday
- Wednesday
- Thursday
- Friday
- Saturday
- Sunday

**Checklist**

- [ ]
- [ ]
- [ ]
- [ ] README updated

**Reflection:**

- What were the main challenges this week?
- What did I learn

---

## Week 3: Python Web APIs

**Key Topics & Resources**

- [FastAPI Official Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Real Python: Python Requests](https://realpython.com/python-requests/)
- [ScrapingBee: API Calls in Python](https://www.scrapingbee.com/blog/python-requests/)

**Project Outline**

- Objective: Build a FastAPI endpoint that returns cleaned stats from a CSV.
- Steps:
  - Load CSV at server startup.
  - Build an endpoint returning aggregate stats.
  - Test with curl/Postman.
- Deliverable: GitHub project with API repo and setup steps.

**Weeks workflow**

- Monday
- Tuesday
- Wednesday
- Thursday
- Friday
- Saturday
- Sunday

**Checklist**

- [ ]
- [ ]
- [ ]
- [ ] README updated

**Reflection:**

- What were the main challenges this week?
- What did I learn

---

## Weeks 4–5: Relational Databases & SQL

**Key Topics & Resources**

- [CS50’s Intro to Databases (edX)](https://www.edx.org/learn/sql)
- [FreeCodeCamp: SQL Course](https://www.freecodecamp.org/news/learn-sql-free-relational-database-courses-for-beginners/)
- [Udemy: Free SQL for Beginners](https://www.udemy.com/topic/sql/free/)

**Project Outline**

- Objective: Import a dataset, run SQL queries, and visualize results in pandas.
- Steps:
  - Spin up SQLite locally.
  - Import data and run JOIN/SELECT queries.
  - Use pandas to analyze and plot.
- Deliverable: Notebook with queries, plots, and sample outputs.

**Weeks workflow**

- Monday
- Tuesday
- Wednesday
- Thursday
- Friday
- Saturday
- Sunday

**Checklist**

- [ ]
- [ ]
- [ ]
- [ ] README updated

**Reflection:**

- What were the main challenges this week?
- What did I learn

---

## Week 6: Data Visualization

**Key Topics & Resources**

- [Udemy: Free Data Visualization Courses](https://www.udemy.com/topic/data-visualization/free/)
- [Noble Desktop Free Tutorials](https://www.nobledesktop.com/learn/data-visualization/free-resources-and-tutorials)
- [Simplilearn: Data Visualization (SkillUp)](https://www.simplilearn.com/quick-guide-data-visualization-article)
- [Figma UI Design Basics (YouTube)](https://www.youtube.com/results?search_query=figma+ui+basics) 

**Project Outline**

- Objective: Build a Streamlit mini-dashboard showing key metrics.
- Steps:
  - Choose KPIs from SQL data.
  - Plot with matplotlib/seaborn.
  - Deploy with Streamlit.
- Deliverable: Live dashboard link (or screenshots) and code.

**Weeks workflow**

- Monday
- Tuesday
- Wednesday
- Thursday
- Friday
- Saturday
- Sunday

**Checklist**

- [ ]
- [ ]
- [ ]
- [ ] README updated

**Reflection:**

- What were the main challenges this week?
- What did I learn

---

## Weeks 7–8: Classical ML Toolkit

**Key Topics & Resources**

- [Scikit-learn Crash Course](https://www.youtube.com/watch?v=0B5eIE_1vpU)
- [LabEx scikit-learn Tutorials](https://labex.io/tutorials/category/sklearn)
- [Simplilearn: Free ML Basics (SkillUp)](https://www.simplilearn.com/free-ai-program-skillup)
  - [Khan Academy: Intro to ML](https://www.khanacademy.org/computing/computer-science/algorithms)
  - [Overfitting & Regularization](https://towardsdatascience.com/overfitting-and-regularization-6f12dd38b10b)


**Project Outline**

- Objective: Train a classifier on open data, evaluate with F1/confusion.
- Steps:
  - Use scikit-learn’s train/test split.
  - Explore metrics and confusion matrix.
- Deliverable: Notebook with code, plots, and results.

**Weeks workflow**

- Monday
- Tuesday
- Wednesday
- Thursday
- Friday
- Saturday
- Sunday

**Checklist**

- [ ]
- [ ]
- [ ]
- [ ] README updated

**Reflection:**

- What were the main challenges this week?
- What did I learn

---

## Weeks 9–11: Deep Learning Core

**Key Topics & Resources**

- [TensorFlow Tutorials](https://www.tensorflow.org/tutorials)
- [YouTube: TensorFlow 2.0 Course](https://www.youtube.com/watch?v=tPYj3fFJGjk)
- [PyTorch Tutorials](https://docs.pytorch.org/tutorials/)
- [FreeCodeCamp: Learn PyTorch](https://www.freecodecamp.org/news/learn-pytorch-for-deep-learning-in-day/)

**Project Outline**

- Objective: Replicate MNIST digit classifier in both TF & PyTorch, compare.
- Steps:
  - Follow beginner notebook in both frameworks.
  - Document setup and results differences.
- Deliverable: Two notebooks and a comparison report.

**Weeks workflow**

- Monday
- Tuesday
- Wednesday
- Thursday
- Friday
- Saturday
- Sunday

**Checklist**

- [ ]
- [ ]
- [ ]
- [ ] README updated

**Reflection:**

- What were the main challenges this week?
- What did I learn

---

## Week 12: Modern LLMs & GPT

**Key Topics & Resources**

- [Simplilearn: Introduction to AI (SkillUp)](https://www.simplilearn.com/ai-for-everyone-free-course-skillup)
- [edX AI & Machine Learning Courses](https://www.edx.org/learn/artificial-intelligence)
- [CS50’s Introduction to AI with Python](https://pll.harvard.edu/course/cs50s-introduction-artificial-intelligence-python)

**Project Outline**

- Objective: Probe GPT-4 (or public GPT-3.5 API) with structured prompts.
- Steps:
  - Document prompt variations.
  - Analyze strengths/weaknesses ("black box" effects).
- Deliverable: Notebook of results and reflection.

**Weeks workflow**

- Monday
- Tuesday
- Wednesday
- Thursday
- Friday
- Saturday
- Sunday

**Checklist**

- [ ]
- [ ]
- [ ]
- [ ] README updated

**Reflection:**

- What were the main challenges this week?
- What did I learn

---

## Week 13: No-Code AI Tools

**Key Topics & Resources**

- [LangFlow (GitHub)](https://github.com/logspace-ai/langflow)
- [CrewAI: Free Community Tooling](https://crewai.com/)
- [Simplilearn n8n Tutorial](https://www.simplilearn.com/tutorials/n8n-tutorial)

**Project Outline**

- Objective: Recreate FAQ agent with a no-code AI agent builder.
- Steps:
  - Choose a no-code tool (LangFlow, CrewAI, n8n).
  - Import docs/setup flow visually.
- Deliverable: Video/screenshot walkthrough of flow.

**Weeks workflow**

- Monday
- Tuesday
- Wednesday
- Thursday
- Friday
- Saturday
- Sunday

**Checklist**

- [ ]
- [ ]
- [ ]
- [ ] README updated

**Reflection:**

- What were the main challenges this week?
- What did I learn

---

## Week 14: RAG, LangChain & Agent Frameworks

**Key Topics & Resources**

- [LangChain Official Docs](https://python.langchain.com/docs/get_started/introduction)
- [edX: Building AI Apps](https://www.edx.org/learn/machine-learning)
- [YouTube: Free LangChain Tutorials](https://www.youtube.com/results?search_query=langchain+tutorial)
- [3 python ai projects for beginners](https://www.youtube.com/watch?v=XZdY15sHUa8)

**Project Outline**

- Objective: Create a retrieval-augmented (RAG) FAQ bot on docs.
- Steps:
  - Index docs with free vector DB (FAISS).
  - Use LangChain to build bot logic.
- Deliverable: Notebook or repo with demo queries.

**Weeks workflow**

- Monday
- Tuesday
- Wednesday
- Thursday
- Friday
- Saturday
- Sunday

**Checklist**

- [ ]
- [ ]
- [ ]
- [ ] README updated

**Reflection:**

- What were the main challenges this week?
- What did I learn

---



## Week 15: AI Code Editors & MCP

**Key Topics & Resources**

- [Replit AI (free tier)](https://replit.com/site/ai)
- [Cursor IDE (preview free)](https://www.cursor.so/)
- [YouTube: MCP server demo](https://www.youtube.com/results?search_query=mcp+server+ai)

**Project Outline**

- Objective: Refactor ML project with AI-powered code editor, deploy via MCP.
- Steps:
  - Try AI suggestion features.
  - Deploy project on MCP.
- Deliverable: Refactored codebase with AI assist notes.

**Weeks workflow**

- Monday
- Tuesday
- Wednesday
- Thursday
- Friday
- Saturday
- Sunday

**Checklist**

- [ ]
- [ ]
- [ ]
- [ ] README updated

**Reflection:**

- What were the main challenges this week?
- What did I learn

---

## Week 16: Capstone—Autonomous Business Agent

**Key Topics & Resources**

- [edX: Applied Machine Learning](https://www.edx.org/learn/machine-learning)
- [Simplilearn: Agents & Automation](https://www.simplilearn.com/tutorials/artificial-intelligence-tutorial/ai-automation)
- [LangChain Open-Source Tutorials](https://python.langchain.com/docs/get_started/introduction)
- [FreeCodeCamp Machine Learning](https://www.freecodecamp.org/learn/machine-learning-with-python/)

**Project Outline**

- Objective: Ship an agent that triages emails, queries DB, drafts responses.
- Steps:
  - Integrate NLP, DB, and web interface.
  - Add logging, monitor outputs.
- Deliverable: Live demo (or video/screenshots), deployment guide, post-mortem blog.

**Weeks workflow**

- Monday
- Tuesday
- Wednesday
- Thursday
- Friday
- Saturday
- Sunday

**Checklist**

- [ ]
- [ ]
- [ ]
- [ ] README updated

**Reflection:**

- What were the main challenges this week?
- What did I learn

---


## Optional Week 17: Career & Portfolio Prep 

**Topics**:
- How to showcase your GitHub projects
- Writing technical blogs or case studies
- Resume building and freelancing platforms

**Resources**:
- [Data Science Portfolio Tips](https://elitedatascience.com/data-science-portfolio)
- [Awesome GitHub README Templates](https://github.com/kautukkundan/Awesome-Profile-README-templates)

**Project**: Polish your GitHub, create a LinkedIn post, or write a blog post on your capstone.

---

## Study Cadence

- **Mon–Wed:** Learn via video, docs, notebooks.
- **Thu:** Code-along and push to GitHub.
- **Fri:** Build project and write README.
- **Weekend:** Reflect, blog, plan next week.

---

## Additional Free Resource Lists

- [edX Free AI/Machine Learning Courses](https://www.edx.org/courses?q=free+online+courses&skills.skill=Artificial+Intelligence&skills.skill=Machine+Learning)
- [Simplilearn SkillUp AI & Data Science](https://www.simplilearn.com/introducing-simplilearn-skillup-program-article)

---

_Export or print this Markdown as a PDF for a single, link-enabled study package. Happy building!_
```
