import redis


def get_con():
    r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
    return r


