from redis_connection import get_con
from priority_logic import get_data as file
r = get_con()

for doc in file():
    if doc["priority"] == "URGENT":
        r.lpush("queue_urgent",doc)
    else:
        r.lpush("queue_normal",doc)
