from fastapi import FastAPI


app = FastAPI()


@app.get("/analytics/alerts-by-border-and-priority")
def alerts_by_border_and_priority():
    return "😊"


@app.get("/analytics/top-urgent-zones")
def top_urgent_zones():
    return "😊"


@app.get("/analytics/distance-distribution")
def distance_distribution():
    return "😊"

@app.get("/analytics/low-visibility-high-activity")
def low_visibility_high_activity():
    return "😊"


@app.get("/analytics/hot-zones")
def hot_zones():
    return "😊"
