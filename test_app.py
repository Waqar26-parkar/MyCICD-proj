from flask import Flask, jsonify, request
import os
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG if os.environ.get("FLASK_ENV") == "development" else logging.INFO)
logger = logging.getLogger(__name__)

# Flask app setup
app = Flask(__name__)

# Load configuration from environment variables or config.py
class Config:
    """Base configuration class."""
    SECRET_KEY = os.environ.get("SECRET_KEY", "mydefaultsecret")
    DEBUG = os.environ.get("FLASK_ENV") == "development"
    PORT = int(os.environ.get("PORT", 8085))

class DevelopmentConfig(Config):
    """Development environment config."""
    DEBUG = True

class ProductionConfig(Config):
    """Production environment config."""
    DEBUG = False

# Select the configuration based on environment
if os.environ.get("FLASK_ENV") == "development":
    app.config.from_object(DevelopmentConfig)
else:
    app.config.from_object(ProductionConfig)

# Route for the homepage
@app.route('/')
def hello_world():
    """Test route for homepage."""
    logger.info("Hello World route was accessed.")
    return jsonify(message="Hello, World!")

# Route for another page
@app.route('/info', methods=["GET"])
def get_info():
    """Return some info as JSON."""
    data = {"app_name": "Flask CI/CD App", "version": "1.0.0"}
    logger.debug(f"Returned info: {data}")
    return jsonify(data)

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    logger.error(f"Error 404: {e}")
    return jsonify(error="Not found"), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors."""
    logger.error(f"Error 500: {e}")
    return jsonify(error="Internal server error"), 500

# Main entry point for the app
if __name__ == "__main__":
    try:
        # Run the app on the defined port and environment
        logger.info(f"Starting the app on port {app.config['PORT']} with debug={app.config['DEBUG']}")
        app.run(host="0.0.0.0", port=app.config["PORT"], debug=app.config["DEBUG"])
    except Exception as e:
        logger.error(f"Error starting the app: {e}")
