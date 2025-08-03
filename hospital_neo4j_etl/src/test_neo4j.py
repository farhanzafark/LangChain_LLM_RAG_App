from neo4j import GraphDatabase
import os
# from dotenv import load_dotenv

# Load credentials from .env (optional)
# load_dotenv()

# Set these manually or via environment variables
NEO4J_URI = os.getenv("NEO4J_URI") #or "neo4j+s://<your-instance>.databases.neo4j.io"
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME") #or "neo4j"
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD") #or "your-password"

# Create driver
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))

# Simple test query
def test_connection():
    try:
        with driver.session() as session:
            result = session.run("RETURN 'Connected to Neo4j!' AS message")
            for record in result:
                print(record["message"])
    except Exception as e:
        print("Connection failed:", e)
    finally:
        driver.close()

if __name__ == "__main__":
    test_connection()
