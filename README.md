# HNG12-0  Documentation

This is a simple public API developed using FastAPI for the HNG12 Stage 0 task. The API provides basic information, including the registered email, the current datetime in ISO 8601 format, and the GitHub repository URL.


## Features

- Returns JSON-formatted response with email, current datetime, and GitHub URL.

- Handles Cross-Origin Resource Sharing (CORS).

- Lightweight and fast using FastAPI.

## Setup Instructions
### Prerquisites
### 1. Clone the Repository
```
    git clone http://github.com/eniolaomotee/HNG12_Internship
    cd eniolaomotee
```

### 2. Create and Activate Virtual Environment
```
    python3 -m venv venv  
    source venv/bin/activate 
```

### 3. Install Dependencies
```
    pip install fastapi uvicorn
```

### 4. Run the API Locally
```
    uvicorn main:app --host 0.0.0.0 --port 8000
```

### 5. Access the API
Omce the server is running visit:
```
    http://127.0.0.1:8000/
```

## API Documentation
### Endpoint
## GET/

### Response Format (200 OK)
```
    {
  "email": "eniolaomotomi@gmail.com",
  "current_datetime": "2025-01-29T23:33:42.232609Z",
  "github_url": "https://github.com/eniolaomotee/HNG12_Internship"
    }
```
### Example Usage
You can test the API using CURL
```
    curl -X GET http://127.0.0.1:8000/
```
