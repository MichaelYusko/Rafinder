import os

from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path)

DATABASES = {
    'default': os.environ.get('DATABASE_URI')
}
