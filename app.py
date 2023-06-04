from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field
from scipy.optimize import newton, brentq
from typing import Optional
import logging

app = FastAPI(debug=True)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
async def home():
    logger.info("GET /")
    return FileResponse('templates/index.html', media_type='text/html')
@app.get("/ytm")
def ytm(P: Optional[float], C: Optional[float], F: Optional[float], n: Optional[float], precision: Optional[float] = 4.0, r_guess: Optional[float] = None):
    def price_func(r):
        return sum([C / (1 + r) ** t for t in range(1, int(n) + 1)]) + F / (1 + r) ** n - P

    # If r_guess is not provided, use the Current Yield as an initial guess
    if r_guess is None:
        if P != 0:  # Avoid division by zero
            r_guess = C / P
        else:
            r_guess = 0

    # Convert precision to a format that newton and brentq can use
    tol = 10 ** (-precision)

    try:
        ytm_value = newton(price_func, (r_guess / 100.0), tol=tol)
    except RuntimeError:
        try:
            ytm_value = brentq(price_func, a=-100, b=+9999999, xtol=tol)
        except ValueError as e:
            raise HTTPException(status_code=400, detail="Unable to calculate YTM.")

    return {"YTM": ytm_value}


# Start of test cases
client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_ytm():
    response = client.get("/ytm?P=1000&C=100&F=1000&n=5&r_guess=0.05&precision=4")
    assert response.status_code == 200
    assert 'YTM' in response.json()
    assert isinstance(response.json()['YTM'], float)
