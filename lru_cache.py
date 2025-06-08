class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        next_node = node.next
        prev_node = node.prev
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int):
        if key not in self.cache:
            return "There is no key in cache"
        node = self.cache[key]
        self._remove(node)
        self._add_to_head(node)
        return node.value

    def put(self, key: int, value: int):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_head(node)
        else:
            if len(self.cache) >= self.capacity:
                last_node = self.tail.prev
                self._remove(last_node)
                del self.cache[last_node.key]
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)

    def print_cache(self):
        items = []
        current = self.head.next
        while current != self.tail:
            items.append((current.key, current.value))
            current = current.next
        print("Current LRU Cache:", items)
