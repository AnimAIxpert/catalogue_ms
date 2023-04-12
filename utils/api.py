from dotenv import load_dotenv
import os

load_dotenv()

# CROS Origins
API_PROTOCOL = os.environ.get('API_PROTOCOL')
API_HOST = os.environ.get('API_HOST')
API_PORT = os.environ.get('API_PORT')
API_URL = f"{API_PROTOCOL}://{API_HOST}:{API_PORT}"
origins = [API_URL]