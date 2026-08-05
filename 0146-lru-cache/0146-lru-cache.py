from typing import Optional
from dataclasses import dataclass 

@dataclass
class Node: 
    key: int = 0
    val: int = 0
    next: Optional["Node"] = None
    prev: Optional["Node"] = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.cache: dict[int, Node] = {}
        self.head: Node = Node()
        self.tail: Node = Node()
        self.head.next = self.tail 
        self.tail.prev = self.head 
    
    def _remove(self, node: Node) -> None: 
        next_node = node.next 
        prev_node = node.prev 
        prev_node.next = next_node 
        next_node.prev = prev_node 

    def _add_to_tail(self, node: Node) -> None: 
        prev_node = self.tail.prev
        prev_node.next = node 
        node.prev =  prev_node 
        node.next = self.tail 
        self.tail.prev = node 

    def get(self, key: int) -> int:
        if key not in self.cache: 
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_to_tail(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._add_to_tail(node)
        if len(self.cache) > self.capacity: 
            lru = self.head.next 
            self._remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna