from app import get_app_with_config
from dotenv import load_dotenv
from config import RunConfig

app, mongodb = get_app_with_config(RunConfig)
if __name__ == "__main__":
    load_dotenv()
    app.run(debug=True)
