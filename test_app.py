from flask import Flask
import os

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def hello_world():
    return "Hello,  World!"

if __name__ == "__main__":
    # Get the port from environment variable or use default (8080)
    port = int(os.environ.get("PORT", 8085))
    
    # Enable debugging in development
    debug_mode = os.environ.get("FLASK_ENV") == "development"

    try:
        app.run(host='0.0.0.0', port=port, debug=debug_mode)
    except Exception as e:
        print(f"Error starting the app: {e}")
