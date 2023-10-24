class LRUCache:
    def __init__(self, capacity):
        self.map = {}
        self.cap = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.map:
            ans = self.map[key]
            self.remove(ans)
            self.insert(ans)
            return ans.value
        else:
            return -1

    def put(self, key, value):
        if key in self.map:
            self.remove(self.map[key])
        if len(self.map) == self.cap:
            self.remove(self.tail.prev)
        self.insert(Node(key, value))

    def insert(self, node):
        self.map[node.key] = node
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head

    def remove(self, node):
        del self.map[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev

class Node:
    def __init__(self, key, value):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value
