from mongo_connection import get_mongo_con
col = get_mongo_con()


def q1():
    border = {"egypt": {"urgent": 0, "normal": 0}, "lebanon": {"urgent": 0, "normal": 0},
              "gaza": {"urgent": 0, "normal": 0}, "syria": {"urgent": 0, "normal": 0},
              "jordan": {"urgent": 0, "normal": 0}}
    all_alerts = col.find()
    for alert in all_alerts:
        if alert["border"] == "egypt":
            if alert["priority"] == "URGENT":
                border["egypt"]["urgent"] += 1
            else:
                border["egypt"]["normal"] += 1

        elif alert["border"] == "lebanon":
            if alert["priority"] == "URGENT":
                border["lebanon"]["urgent"] += 1
            else:
                border["lebanon"]["normal"] += 1

        elif alert["border"] == "gaza":
            if alert["priority"] == "URGENT":
                border["gaza"]["urgent"] += 1
            else:
                border["gaza"]["normal"] += 1

        elif alert["border"] == "syria":
            if alert["priority"] == "URGENT":
                border["syria"]["urgent"] += 1
            else:
                border["syria"]["normal"] += 1

        elif alert["border"] == "jordan":
            if alert["priority"] == "URGENT":
                border["jordan"]["urgent"] += 1
            else:
                border["jordan"]["normal"] += 1
    return border

def q2():
    zones = {}
    all_alerts = col.find()
    for alert in all_alerts:
        if alert["priority"] == "URGENT":
            if alert["zone"] in zones:
                zones[f"{alert["zone"]}"] += 1
            else:
                zones[f"{alert["zone"]}"] = 1
    a = []
    for i in range(5):
        a.append(max(zones.values()))

    return a


def q3():
    distance_from_fence = {"A":0,"B":0,"C":0}
    all_alerts = col.find()
    for alert in all_alerts:
        if alert["distance_from_fence_m"] <= 300:
            distance_from_fence["A"] += 1
        elif 300 < alert["distance_from_fence_m"] <= 800:
            distance_from_fence["B"] += 1
        elif 800 < alert["distance_from_fence_m"] <= 1500:
            distance_from_fence["C"] += 1
    return distance_from_fence







