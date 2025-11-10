class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.table = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)
        node = self.table[index]
        if not node:
            self.table[index] = Node(key, value)
            return
        while node.next:
            if node.key == key:
                node.value = value
                return
            node = node.next
        node.next = Node(key, value)

    def get(self, key):
        index = self._hash(key)
        node = self.table[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

if __name__ == "__main__":
    ht = HashTable()
    for i in range(10000):
        ht.insert(f"key{i}", i)
    print(ht.get("key9999"))
