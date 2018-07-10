# coding: utf-8
import time
import redis
import random
import redis

from setting import HOST_PROXY, PORT_PROXY
from untils import generate_logger


class RedisClient():
    """
    By now, only (a) random IP proxy(s) from the proxy-pool is/are provided.
    """

    def __init__(self, DB_NAME_PROXY, host=HOST_PROXY, port=PORT_PROXY, ):
        pool = redis.ConnectionPool(host=host, port=port, db=0)
        # [redis连接对象是线程安全的](http://www.cnblogs.com/clover-siyecao/p/5600078.html)
        # [redis是单线程的](https://stackoverflow.com/questions/17099222/are-redis-operations-on-data-structures-thread-safe)
        self._db = redis.Redis(connection_pool=pool)
        self.logger = generate_logger("JJ_RedisClient")
        self.DB_NAME_PROXY = DB_NAME_PROXY

    def get(self):
        
        proms = []
        if(self._db.llen(self.DB_NAME_PROXY) == 0):
            time.sleep(random.random()*10)
            return proms
        try:
            prom = self._db.lpop(self.DB_NAME_PROXY)  # 从队列头读取出来
            # print("Using IP proxy:", proxy)  # req.text: "119.75.213.61:80"
            proms.append(prom)
        except ValueError as ve:
            self.logger.error("ValueError:queue_len is too short(<1).\n{0}".format(ve))
        except Exception as e:
            self.logger.error("Unexpected Error.\n{0}".format(e))
        finally:
            # self.logger.info("Using proxies:{0}".format(proxies))
            return proms

    def put(self, prom):
        """
        add proxy to right top
        # zset
        self._db.zadd("proxy_zset", proxy, self._INITIAL_SCORE)
        """
        self._db.rpush(self.DB_NAME_PROXY, prom)  # list

    @property
    def queue_len(self):
        """
        get length from queue.
        """
        return self._db.llen(self.DB_NAME_PROXY)

    def showall(self):
        """
        show all elements in the list.
        """
        #print(self._db.lrange(DB_NAME, 0, -1))
        self.logger.info(repr(self._db.lrange(self.DB_NAME_PROXY, 0, -1)))

    def del_all_proxies(self):
        """
        delete all the proxies in DB_NAME
        """
        self._db.delete(self.DB_NAME_PROXY)


    def flush(self):
        """
        flush db
        """
        # self._db.flushall()    # DO NOT DO THIS.
        pass


if __name__ == "__main__":
    # """
    client = RedisClient()
    client.del_all_proxies()
    client.get_new()
    client.get()
