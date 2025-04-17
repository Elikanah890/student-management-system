# Step 1: Use a Python base image from Docker Hub
FROM python:3.10-slim

# Step 2: Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Step 3: Set the working directory inside the container
WORKDIR /app

# Step 4: Copy requirements.txt into the container
COPY requirements.txt /app/

# Step 5: Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Step 6: Copy the entire project into the container
COPY . /app/

# Step 7: Expose port 8000 for the FastAPI app
EXPOSE 8000

# Step 8: Run the FastAPI app using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
