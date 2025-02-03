from fastapi import FastAPI,Query
from pydantic import BaseModel
from typing import List,Union
import httpx

app = FastAPI()

# Response Model
class NumberResponse(BaseModel):
    number: int
    is_prime: bool
    is_perfect: bool
    properties: List[str]
    digit_sum:int
    fun_fact: str
    
    
# Utility functions
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_perfect(n):
    return n > 1  and sum(i for i in range(1, n) if n % i == 0) == n


def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return sum( d**len(digits) for d in digits) == n 


def get_digit_sum(n):
    return sum([int(d) for d in str(n)])



async def get_fun_fact(n):
    url = f"http://numbersapi.com/{n}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.text if response.status_code == 200 else "No Fun Fact Found"


# Main Route
@app.get("/api/classify-number",response_model=Union[NumberResponse,dict])
async def classify_number(number: str = Query(...)):
    if not number.isdigit():
        return {"number":number,"error":"true"}
    
    num = int(number)
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
        digit_sum=  digit_sum,
        fun_fact=fun_fact
    )