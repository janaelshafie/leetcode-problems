class Deleted:
    pass

DELETED = Deleted()

class Pair:
    def __init__(self, key, value):
        self.key = key
        self.val = value

class MyHashMap:

    def __init__(self):
        self.size = 0
        self.capacity = 8
        self.map = [None] * self.capacity


    def hash(self, key):
        return key % self.capacity

    def rehash(self):
        self.capacity = (self.capacity * 2) + 1
        newMap = []
        for i in range(self.capacity):
            newMap.append(None)

        oldMap = self.map
        self.map = newMap
        self.size = 0
        for pair in oldMap:
            if pair and pair != DELETED:
                self.put(pair.key, pair.val)

    def put(self, key: int, value: int) -> None:
        first_deleted = None
        index = self.hash(key)

        while True:
            if self.map[index] == None:
                if first_deleted is not None:
                    self.map[first_deleted] = Pair(key,value)
                else:
                    self.map[index] = Pair(key,value)
                
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()
                return
            
            elif self.map[index] == DELETED:
                if first_deleted is None:
                    first_deleted = index

            else:
                if self.map[index].key == key:
                    self.map[index].val = value
                    return
            
            index = (index + 1) % self.capacity

    def get(self, key: int) -> int:
        index = self.hash(key)

        while self.map[index] != None:
            if self.map[index] != DELETED and self.map[index].key == key:
                return self.map[index].val
            
            index = (index + 1) % self.capacity
        
        return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)

        while True:
            if self.map[index] == None:
                return
            elif self.map[index] == DELETED:
                index = (index + 1) % self.capacity

            else:
                if self.map[index].key == key:
                    self.map[index] = DELETED
                    self.size -= 1
                    return
                index = (index + 1) % self.capacity
        


        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)