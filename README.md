# 🏥 LangChain RAG Chatbot with Neo4j

This project implements a Retrieval-Augmented Generation (RAG) chatbot using **LangChain**, **OpenAI**, and **Neo4j**. It follows the architecture and best practices outlined in the [Real Python guide](https://realpython.com/build-llm-rag-chatbot-with-langchain/#step-4-build-a-graph-rag-chatbot-in-langchain), with enhancements for structured prompt design and secure deployment.

---

## 🧰 Tools & Technologies Used

| Tool             | Purpose |
|------------------|---------|
| **LangChain**    | Orchestrates LLM chains, prompt templates, agents, and retrievers |
| **OpenAI (GPT-3.5 Turbo)** | Generates responses based on patient reviews and graph data |
| **Neo4j**        | Stores hospital-related entities and relationships as a graph, used for Cypher-based RAG |
| **ChromaDB**     | Stores vectorized patient reviews for semantic retrieval |
| **Python 3.11.9**| Core language used for scripting and app logic |
| **Docker**       | Containerizes the app for consistent local and cloud deployment |
| **FastAPI (optional)** | Powers the REST API if deployed via a server backend |

---

## 🧠 How the Components Work Together

1. **Patient reviews** are embedded using OpenAI's embedding model and stored in **ChromaDB** for vector-based retrieval.
2. **Structured hospital data** (e.g., patients, physicians, hospitals) is loaded into **Neo4j** as a knowledge graph.
3. **LangChain** connects both:
   - A **vector retriever chain** to answer review-based questions.
   - A **graph Cypher QA chain** to answer structured queries from the Neo4j knowledge base.
4. The chatbot dynamically chooses which retriever/chain to use, and routes the query accordingly.

---

## 🚀 Deployment Structure

- `main.py` – Entry point to run the chatbot API or CLI
- `chains/` – LangChain components like vector QA and graph Cypher chains
- `agents/` – Routing agent to select the appropriate retriever
- `data/` – CSV files for reviews and Cypher templates
- `docker-compose.yml` – Orchestrates Docker containers (app + Neo4j + Chroma)
- `Dockerfile` – Builds the chatbot container
- `.env` – Required for API keys and DB credentials (not committed)

---

## ▶️ How to Run Locally

1. **Install Python 3.11.9**  
   Make sure you're using Python `3.11.9` (recommended via `pyenv` or `python.org`).

2. **Create a virtual environment**  
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Add a `.env` file**  
   Create a `.env` file in the root of the project with the following environment variables. Refer to the [Real Python article](https://realpython.com/build-llm-rag-chatbot-with-langchain/#step-2-understand-the-business-requirements-and-data) for the exact structure and values:

   ```env
   OPENAI_API_KEY=your-api-key
   NEO4J_URI=neo4j+s://your-neo4j-instance.databases.neo4j.io
   NEO4J_USERNAME=neo4j
   NEO4J_PASSWORD=your-password
   ```

5. **(Optional) Run with Docker**
   ```bash
   docker-compose up --build
   ```

6. **Start the app**
   You can run the chatbot or API using:

   ```bash
   python main.py
   ```

---

## 📄 References

- Real Python Tutorial: [Build an LLM RAG Chatbot with LangChain](https://realpython.com/build-llm-rag-chatbot-with-langchain/)
- LangChain Docs: https://docs.langchain.com/
- Neo4j AuraDB: https://neo4j.com/cloud/aura/

---

## 🛡️ Note

This project uses OpenAI’s GPT APIs and should be used responsibly. When running graph-based chains, you must explicitly set `allow_dangerous_requests=True` in the `GraphCypherQAChain` to allow Cypher execution — only do this if you understand the risks.

---