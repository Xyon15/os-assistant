import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

# Connexion PostgreSQL (comme memory.py)
DATABASE_URL = os.getenv("DATABASE_URL")
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

# Création table users avec contraintes
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        hashed_password VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

conn.commit()
cursor.close()
conn.close()

print("Table 'users' créée avec succès !")