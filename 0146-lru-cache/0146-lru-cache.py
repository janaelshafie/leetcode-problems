class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.val = value
        self.key = key
        self.prev = prev
        self.next = next
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity, self.size = capacity, 0
        self.hashmap = {}
        self.left, self.right = Node(-1,-1), Node(-1,-1)
        self.left.next = self.right
        self.right.prev = self.left
    
    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.remove(node)
            self.insert(node)
            return

        if self.size == self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.hashmap[lru.key]
            self.size -= 1

        new_Node = Node(key,value)
        self.insert(new_Node)
        self.hashmap[key] = new_Node
        self.size += 1

    
    def insert(self, node):
        node.prev = self.right.prev
        node.next = self.right

        self.right.prev.next = node
        self.right.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)