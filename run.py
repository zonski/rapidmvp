import os
from src.app import create_app

app = create_app()

if __name__ == '__main__':
    # Use Gunicorn for production
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 8080)), debug=True)
