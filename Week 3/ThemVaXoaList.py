class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_to_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def add_after(self, key, data):
        new_node = Node(data)
        current_node = self.head
        while current_node:
            if current_node.data == key:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next
        self.add_to_beginning(data)

    def remove_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev_node.next = current_node.next
        current_node = None

    def remove_all_nodes(self, key):
        current_node = self.head
        prev_node = None
        while current_node:
            if current_node.data == key:
                if prev_node:
                    prev_node.next = current_node.next
                    current_node = current_node.next
                else:
                    self.head = current_node.next
                    current_node = current_node.next
            else:
                prev_node = current_node
                current_node = current_node.next

    def remove_first_node(self):
        if self.head is None:
            return
        self.head = self.head.next

    def print_list(self):
        current_node = self.head
        if current_node is None:
            print("blank")
            return
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next


linked_list = LinkedList()

while True:
    try:
        query = input().split()
        if query[0] == "0":
            linked_list.add_to_beginning(int(query[1]))
        elif query[0] == "1":
            linked_list.add_to_end(int(query[1]))
        elif query[0] == "2":
            linked_list.add_after(int(query[1]), int(query[2]))
        elif query[0] == "3":
            linked_list.remove_node(int(query[1]))
        elif query[0] == "4":
            linked_list.remove_all_nodes(int(query[1]))
        elif query[0] == "5":
            linked_list.remove_first_node()
        elif query[0] == "6":
            linked_list.print_list()
            break
    except:
        break
