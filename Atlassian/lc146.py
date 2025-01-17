class DLL:
    def __init__(self, key: int, data: int):
        self.key = key
        self.data = data
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.mpp = {}
        self.capacity = capacity
        self.head = DLL(-1, -1)
        self.tail = DLL(-1, -1)

        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        if key not in self.mpp:
            return -1
        
        node = self.mpp[key]
        self.delete(node)
        self.insert(node)
        return node.data

    def put(self, key: int, value: int) -> None:
        if key in self.mpp:
            self.delete(self.mpp[key])
            del self.mpp[key]
        
        if len(self.mpp) == self.capacity:
            to_delete = self.tail.prev
            self.delete(to_delete)
            del self.mpp[to_delete.key]

        node = DLL(key, value)
        self.mpp[key] = node
        self.insert(node)
            
    def insert(self, node: DLL) -> None:
        temp = self.head.next
        self.head.next = node
        temp.prev = node
        node.prev, node.next = self.head, temp
    
    def delete(self, node: DLL) -> None:
        node.prev.next, node.next.prev = node.next, node.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)