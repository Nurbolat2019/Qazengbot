from dotenv import load_dotenv
import os

# .env файлын жүктеу, толық жолды көрсету
env_path = "C:/Python/engbot/.env"
load_dotenv(env_path)

BOT_TOKEN = "7090625287:AAGZB7MeQlpuHJrLgcZi5cyOjrTrcSkYlsQ"
print(f"Loaded BOT_TOKEN: {BOT_TOKEN}")  # Токеннің мәнін шығару
if BOT_TOKEN is None:
    raise ValueError("BOT_TOKEN is not set! Check your .env file at: " + env_path)