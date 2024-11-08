import redis
from redis import Redis

r: Redis = redis.Redis(host='localhost', port=6379)

# print(r.set('foo', 'bar'))
print(r.get('foo'))
print(r.get("test"))
