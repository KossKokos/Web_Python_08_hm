import redis
from redis_lru import RedisLRU

from models import Authors, Qoutes

# client = redis.StrictRedis(host="localhost", port=6379, password=None)
# cache = RedisLRU(client)


# @cache
def main(x):
    print(f'hello{x}')
    return x**x

if __name__ == '__main__':
    main()
