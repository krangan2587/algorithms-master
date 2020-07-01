
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if not self.cache:
            raise ValueError("Cache is empty")
        else:
            if key in self.cache:
                return self.cache.get(key)
            else:
                return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache)!= self.cap:
            self.cache[key] = value
        else:
            self.cache.popitem(last=False)

if __name__ == '__main__':
    obj = LRUCache(5)
    # param_1 = obj.get(key)
    obj.put(1,"Kasturi")
    obj.put(2,"Rangan")

    print(obj.get(2))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)