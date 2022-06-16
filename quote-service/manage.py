import os
from app import create_app
FLASK_ENV = os.environ.get("FLASK_ENV")
app = create_app(FLASK_ENV)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500)
