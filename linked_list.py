class Node:

    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


class LinkedList:
  
    def __init__(self):
        self.head = None
        self.tail = None

    def iterate(self):
        print('--Start iterate--')
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next_item
        print('--End iterate--')

    def append(self, value):
        new_node = Node(value)
        if self.tail is not None:
            self.tail.next_item = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node

    def contains(self, value):
        current_node = self.head
        while current_node is not None:
            if value == current_node.value:
                return True
            current_node = current_node.next_item
        return False

    def get_value_by_index(self, index):
        if self.head is None:
            return
        current_node = self.head
        index_counter = 0
        while index_counter < index:               
            index_counter += 1
            current_node = current_node.next_item
            if current_node is None:
                return
        return current_node.value
            
    def remove(self, index):
        if self.head is None:
            return
        current_node = self.head
        if index == 0:
            self.head = self.head.next_item
        else:
            index_counter = 0
            while index_counter < index:               
                index_counter += 1
                previous_node = current_node
                current_node = current_node.next_item
                if current_node is None:
                    return
            previous_node.next_item = current_node.next_item

        del current_node


if __name__ == '__main__':
    head_node = Node('head')
    middle_node = Node('middle')
    tail_node = Node('tail')

    head_node.next_item = middle_node
    middle_node.next_item = tail_node

    linked_list = LinkedList()

    linked_list.head = head_node
    linked_list.tail = tail_node
