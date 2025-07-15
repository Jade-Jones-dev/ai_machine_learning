# 16-Week AI & Agent-Building Curriculum

A linked schedule with **clickable resources** and detailed **weekly project outlines**. Open this markdown in any browser or Markdown viewer, then choose _Print ➜ Save as PDF_ to obtain an offline PDF with live links.

---

## Week-by-Week Roadmap

### Week 1 – Python Foundations & Environments

**Key Topics**  
• [Python for Everybody (Coursera)](https://www.coursera.org/learn/python)  
• [Python `venv` Primer – Real Python](https://realpython.com/python-virtual-environments-a-primer/)  
**Weekly Project Outline**

1. Install Python 3.12 and create a project folder.
2. Create and activate a virtual environment with `python -m venv .venv`.
3. Write `ping_api.py` that sends a GET request to https://httpbin.org/get and prints the JSON.
4. Push the script and a one-paragraph README to GitHub.

---

### Week 2 – NumPy ✚ Pandas ✚ Matplotlib

**Key Topics**  
• [NumPy Getting Started](https://www.w3schools.com/python/numpy/numpy_getting_started.asp)  
• [15-min NumPy/Pandas/Matplotlib Video](https://www.youtube.com/watch?v=NZ0laizc4ug)  
**Weekly Project Outline**

1. Download the public “Iris” CSV from UCI ML repo.
2. Load into a Pandas DataFrame, clean column names.
3. Plot a histogram of sepal length and save `hist.png`.
4. Commit `notebook.ipynb`, `hist.png`, and a short findings blurb.

---

### Week 3 – Building & Consuming Python APIs

**Key Topics**  
• [FastAPI 15-Minute Tutorial](https://fastapi.tiangolo.com/)  
• [Python Requests Guide – Real Python](https://realpython.com/python-requests/)  
**Weekly Project Outline**

1. Scaffold a FastAPI app with one `/stats` route.
2. Inside the route, fetch live JSON from `https://api.coindesk.com/v1/bpi/currentprice.json`.
3. Return BTC price and timestamp as JSON.
4. Test with `requests` and document the curl command in README.

---

### Week 4–5 – SQL for Developers

**Key Topics**  
• [Mode SQL Tutorial (Basic→Advanced)](https://mode.com/sql-tutorial/)  
• [SQL JOINs – GeeksforGeeks](https://www.geeksforgeeks.org/sql/sql-join-set-1-inner-left-right-and-full-joins/)  
• [Pandas vs SQL (Video)](https://www.youtube.com/watch?v=4GhcNuOXJLU)  
**Weekly Project Outline**

1. Spin up SQLite DB, import the “Nashville Housing” CSV.
2. Write four queries: top-10 prices, avg price by year, INNER JOIN with a lookup table, and a LEFT JOIN example.
3. Replicate each query in Pandas and compare runtimes.
4. Produce `report.md` with screenshots of SQL outputs and Pandas code.

---

### Week 6 – Data Visualization in Practice

**Key Topics**  
• [Pandas Plotting – W3Schools](https://www.w3schools.com/python/pandas/pandas_plotting.asp)  
• [PyData “Plotting in Pandas” Tutorial](https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html)  
**Weekly Project Outline**

1. Choose any Kaggle dataset > 10 k rows.
2. Build a Streamlit dashboard with two charts (line + scatter) and one KPI metric.
3. Deploy to Streamlit Cloud; include dashboard URL in README.

---

### Week 7–8 – Classical Machine Learning with scikit-learn

**Key Topics**  
• [scikit-learn Basic Tutorial](https://scikit-learn.org/stable/tutorial/basic/tutorial.html)  
• [Zero-to-Mastery ML Crash Course (Video)](https://www.youtube.com/watch?v=r67SfaiYaDI)  
**Weekly Project Outline**

1. Split the Titanic dataset into train/test.
2. Train a RandomForest classifier; tune `n_estimators`.
3. Evaluate accuracy, precision, recall, F1.
4. Expose the model behind a `/predict` FastAPI endpoint that takes JSON passenger data.

---

### Week 9–11 – Deep Learning Essentials

**Key Topics**  
• [TensorFlow Beginner Tutorials](https://www.tensorflow.org/tutorials)  
• [PyTorch Quickstart](https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html)  
• [CNNs with TensorFlow](https://www.tensorflow.org/tutorials/images/cnn)  
**Weekly Project Outline**

1. Train an MNIST digit classifier in TensorFlow (Keras).
2. Re-implement the same architecture in PyTorch.
3. Compare training times & accuracy in a table.
4. Save both models and write a reflection blog post (≈500 words).

---

### Week 12 – LLM Fundamentals & GPT

**Key Topics**  
• [OpenAI Cookbook – Function Calling](https://github.com/openai/openai-cookbook)  
• [Hugging Face Transformers Docs](https://huggingface.co/transformers/)  
**Weekly Project Outline**

1. Design 5 systematic prompts to query GPT-4 about a product spec.
2. Log responses and token counts to a CSV.
3. Summarize strengths & limits you observed; include examples of hallucinations.
4. Track all calls with LangSmith and include trace link.

---

### Week 13 – Retrieval-Augmented Generation & Agents

**Key Topics**  
• [LangChain Quickstart](https://python.langchain.com/docs/get_started/quickstart)  
• [LangGraph Overview](https://python.langchain.com/docs/guides/langgraph/introduction)  
**Weekly Project Outline**

1. Load 20 internal PDF docs with `UnstructuredLoader`.
2. Create a FAISS vector store.
3. Build a LangChain agent that answers questions with citations.
4. Add a simple Gradio chat UI and record a demo GIF.

---

### Week 14 – No-Code Agent Builders

**Key Topics**  
• [CrewAI Docs](https://docs.crewai.com/)  
• [LangFlow Canvas](https://github.com/langflow/langflow)  
• [n8n Workflow Automation](https://n8n.io/)  
**Weekly Project Outline**

1. Re-create Week 13 bot visually in LangFlow.
2. Build an n8n workflow that triggers the bot on new Zendesk tickets.
3. Compare dev time vs. coded approach in a short write-up.

---

### Week 15 – AI-Enhanced IDEs & MCP Servers

**Key Topics**  
• [Cursor IDE](https://www.cursor.sh/)  
• [Replit AI Overview](https://blog.replit.com/ide-ai)  
• [Model-Centric-Product Server Pattern (Blog)](https://replicate.com/blog/model-centric-product)  
**Weekly Project Outline**

1. Refactor Week 7 model code inside Cursor with inline GPT suggestions.
2. Containerize the FastAPI service using Docker.
3. Deploy to an MCP-style server (e.g., Docker-compose on Render).
4. Measure latency before & after deployment.

---

### Week 16 – Capstone: Autonomous Business Agent

**Key Topics**  
• [LangSmith Monitoring](https://docs.langchain.com/docs/guides/langsmith)  
• [Streamlit Components](https://docs.streamlit.io/)  
**Weekly Project Outline**

1. Goal: triage incoming customer emails, query product DB, draft replies.
2. Architect multi-tool LangGraph (email › classify › retrieve › draft › send).
3. Instrument with LangSmith and set up alerting on error rate.
4. Deliverables: live demo video, GitHub repo, post-mortem report.

---

### After Graduation

- Take Stanford CS25 (Agents) or similar MOOC.
- Contribute a pull request to an open-source LangChain module.

---

**How to Export as PDF**

1. Click the **Download** button in this chat to save `ai-curriculum-roadmap.md`.
2. Open the file in any markdown viewer or VS Code preview.
3. Select **Print ➜ Save as PDF** – all links remain clickable offline.
