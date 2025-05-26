# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Append a new node to the end of the list
    def append(self, data): # 
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next: # 만약에 last_node.next가 있으면 무한정으로 돌리는거 아니야?
            last_node = last_node.next # 그러네 last_node의!! next니까.
        last_node.next = new_node

    # Prepend a new node to the beginning of the list
    def prepend(self, data): # 그냥 단순히 마지막것과 처음으로 바꾼 것
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Delete a node with the given data
    def delete(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next

        if current_node.next:
            current_node.next = current_node.next.next

    # Display the linked list
    def display(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(str(current_node.data))
            current_node = current_node.next # 현재 노드에서 다음 노드를 지정.
        return " -> ".join(elements) if elements else "비어 있음"