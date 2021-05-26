from collections import deque


class Queue:
    def __init__(self):
        self.nodes = deque()

    def is_empty(self, nodes):
        return len(nodes) == 0

    def enqueue(self, node):
        self.nodes.append(node)

    def dequeue(self):
        if not self.is_empty(self.nodes):
            return self.nodes.popleft()

    def peek(self):
        if not self.is_empty(self.nodes):
            return self.nodes[0]

    def get_len(self):
        return len(self.nodes)

    def print_queue(self):
        print(self.nodes)
