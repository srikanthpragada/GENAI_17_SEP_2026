import os
from dotenv import load_dotenv

# Load variables from .env into the system memory
load_dotenv(override = True)

# Access the variable
api_key = os.getenv("TAVILY_KEY")
print(api_key)
