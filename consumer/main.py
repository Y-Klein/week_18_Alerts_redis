from redis_connection import get_redis_con
from mongo_connection import get_mongo_con
import datetime
import json



r = get_redis_con()
col = get_mongo_con()

try:
    while True:
        alerts = r.brpop(["queue_urgent","queue_normal"])
        alerts = json.loads(alerts[1])
        print(alerts)
        time_stamp = str(datetime.datetime.now())
        alerts["time_stamp"] = time_stamp
        col.insert_one(alerts)





except KeyboardInterrupt:
    print("\n🔴 Stopping consumer")

