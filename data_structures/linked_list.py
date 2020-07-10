
class Node:
    def __init__(self, data=None, next_node=None):
        self.next_node = next_node
        self.data = data

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.get_next()
        return count

    def search(self, data):
        curr = self.head
        found = False
        while curr and not found:
            if curr.get_data() == data:
                found = True
            else:
                curr = curr.get_next()
        if curr is None:
            raise ValueError("Data not in linked list")
        return curr

    def delete(self, data):
        curr = self.head
        prev = None
        found = False
        while curr and not found:
            if curr.get_data() == data:
                found = True
            else:
                prev = curr
                curr = curr.get_next()
        if curr is None:
            raise ValueError("Data not in linked list")
        if prev is None:
            self.head = curr.get_next()
        else:
            prev.set_next(curr.get_next())

    def print_nodes(self):
        curr = self.head
        while curr:
            print(curr.get_data())
            curr = curr.get_next()


if __name__ == '__main__':
    my_list = LinkedList()
    my_list.insert(5)
    my_list.insert(10)
    my_list.insert(25)
    print(my_list.size())
    print(my_list.print_nodes())
    my_list.delete(10)
    print(my_list.print_nodes())
    print(my_list.size())