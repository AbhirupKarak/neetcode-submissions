class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.remove(node)
            self.append(node)
            return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.append(node)

        else:
            newNode = Node(key,value)
            if not self.head:
                self.cache[key]= newNode
                self.head = newNode
                self.tail = newNode
            else:
                self.append(newNode)
                self.cache[key]= newNode
                if len(self.cache) > self.capacity:
                    lru = self.head
                    self.remove(lru)
                    del self.cache[lru.key]


    
    def remove(self,node):
        if node == self.head and node == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            node.next.prev = None
            self.head = node.next
        elif node == self.tail:
            node.prev.next = None
            self.tail = node.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.next = None
        node.prev = None


    def append(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        node.next = None




class Node:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


