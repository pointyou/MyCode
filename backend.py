from datetime import date

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from services import (
    calculate,
    convert_length,
    convert_weight,
    convert_temperature,
    calculate_bmi,
    date_difference,
)

app = FastAPI()


class CalcRequest(BaseModel):
    num1: float
    op: str
    num2: float


@app.post("/calculator")
def calculator_endpoint(req: CalcRequest) -> dict:
    try:
        result = calculate(req.num1, req.op, req.num2)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


class LengthRequest(BaseModel):
    meters: float


@app.post("/convert/length")
def convert_length_endpoint(req: LengthRequest) -> dict:
    return convert_length(req.meters)


class WeightRequest(BaseModel):
    kg: float


@app.post("/convert/weight")
def convert_weight_endpoint(req: WeightRequest) -> dict:
    return convert_weight(req.kg)


class TempRequest(BaseModel):
    celsius: float


@app.post("/convert/temperature")
def convert_temperature_endpoint(req: TempRequest) -> dict:
    return convert_temperature(req.celsius)


class BMIRequest(BaseModel):
    height_cm: float
    weight_kg: float


@app.post("/bmi")
def bmi_endpoint(req: BMIRequest) -> dict:
    try:
        bmi = calculate_bmi(req.height_cm, req.weight_kg)
        return {"bmi": bmi}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


class DateDiffRequest(BaseModel):
    date1: date
    date2: date


@app.post("/date-diff")
def date_diff_endpoint(req: DateDiffRequest) -> dict:
    days = date_difference(req.date1, req.date2)
    return {"days": days}
