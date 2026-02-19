from fastapi import FastAPI
from dal import *


app = FastAPI()


@app.get("/analytics/alerts-by-border-and-priority")
def alerts_by_border_and_priority():
    result = q1()
    return result


@app.get("/analytics/top-urgent-zones")
def top_urgent_zones():
    result = q2()
    return result


@app.get("/analytics/distance-distribution")
def distance_distribution():
    result = q3()
    return result

@app.get("/analytics/low-visibility-high-activity")
def low_visibility_high_activity():
    return "😊"


@app.get("/analytics/hot-zones")
def hot_zones():
    return "😊"
