from app import app
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    # app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
    app.run(debug=True)
