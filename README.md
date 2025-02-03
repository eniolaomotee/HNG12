# HNG12-1  Documentation

The Number Classifier API is a FastAPI-based service that classifies a given number based on various mathematical properties. It determines whether a number is prime, perfect, Armstrong, and also provides additional properties like whether the number is odd or even. Additionally, it fetches an interesting fact about the number from the Numbers API.

## Features
- Prime Number Check: Checks if the number is prime.

- Perfect Number Check: Checks if the number is a perfect number.

- Armstrong Number Check: Checks if the number is an Armstrong number.

- Digit Sum Calculation: Computes the sum of the digits in the number.

- Odd/Even Classification: Determines if the number is odd or even.

- Fun Fact: Fetches an interesting fact about the number from Numbers API.


## Setup Instructions
### Prerequisites
### 1. Clone the Repository
```
    git clone http://github.com/eniolaomotee/HNG12
    cd eniolaomotee
```

### 2. Create and Activate Virtual Environment
```
    python3 -m venv venv  
    source venv/bin/activate 
```

### 3. Install Dependencies
```
    pip install -r requirements.txt
```

### 4. Run the API Locally
```
    uvicorn main:app --reload --port=8000
```

### 5. Access the API
Omce the server is running visit:
```
    http://127.0.0.1:8000/
```

## API Documentation
### Classify Number
### Endpoint ```/api/classify-number ```
### Method:  GET
### Query Parameter:
- ``` number ```(required): The number to classify 

### Example Request
``` GET http://127.0.0.1:8000/api/classify-number?number=371 ```


### Example Response


```
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": [
    "Armstrong",
    "odd"
  ],
  "digit_sum": 11,
  "fun_fact": "371 is the number of three-dimensional partitions of 12."
}
```
### Error Handling
If an invalid number is provided:
``` GET http://127.0.0.1:8000/api/classify-number?number=abc```
Response
```
    {
    "number": "abc",
    "error": "true"
    }
 ```

### Back Link
[text](https://hng.tech/hire/python-developers)