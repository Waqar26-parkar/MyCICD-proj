# Use Python 3.9 slim as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install dependencies from requirements.txt
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . /app/

# Set environment variables (optional but recommended)
ENV FLASK_APP=app.py
ENV FLASK_ENV=production  
# Use 'development' if you want to run it in debug mode

# Expose the port on which the app will run
EXPOSE 8085

# Run the app with 'flask run'
CMD ["flask", "run", "--host=0.0.0.0", "--port=8085"]
