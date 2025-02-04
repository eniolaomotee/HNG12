from fastapi import FastAPI, Query
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from typing import List, Union
import httpx

app = FastAPI()

# Response Models
class NumberResponse(BaseModel):
    number: int
    is_prime: bool
    is_perfect: bool
    properties: List[str]
    digit_sum: int
    fun_fact: str

class ErrorResponse(BaseModel):
    number: str
    error: bool

# Utility functions (definitions remain the same)
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    return n > 1 and sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n: int) -> bool:
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

def get_digit_sum(n: int) -> int:
    return sum(int(d) for d in str(n))

async def get_fun_fact(n: int) -> str:
    url = f"http://numbersapi.com/{n}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.text if response.status_code == 200 else "No Fun Fact Found"

# Optional Root Route: Redirect to your main endpoint
@app.get("/")
async def root():
    return RedirectResponse(url="/api/classify-number")

# Main API Route
@app.get("/api/classify-number", response_model=Union[NumberResponse, ErrorResponse])
async def classify_number(number: str = Query(default="")):
    # If the number parameter is missing or invalid, return the error response.
    if not number or not number.lstrip('-').isdigit():
        return ErrorResponse(number="alphabet", error=True)
    
    num = int(number)
    if num < 0:
        return ErrorResponse(number="alphabet", error=True)
    
    # Compute number properties
    prime = is_prime(num)
    perfect = is_perfect(num)
    armstrong = is_armstrong(num)
    digit_sum = get_digit_sum(num)
    fun_fact = await get_fun_fact(num)
    
    properties = []
    if armstrong:
        properties.append("Armstrong")
    properties.append("odd" if num % 2 else "even")
    
    return NumberResponse(
        number=num,
        is_prime=prime,
        is_perfect=perfect,
        properties=properties,
        digit_sum=digit_sum,
        fun_fact=fun_fact
    )
