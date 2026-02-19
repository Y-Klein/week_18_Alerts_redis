from redis_connection import get_con
from priority_logic import get_data as file
import json
r = get_con()

for doc in file():
    if doc["priority"] == "URGENT":
        j = json.dumps(doc)
        r.lpush("queue_urgent",j)
    else:
        j = json.dumps(doc)
        r.lpush("queue_normal",j)
