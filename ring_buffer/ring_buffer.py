from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
    def append(self, item):
        # If our storage is at max capacity
        if len(self.storage) == self.capacity:
            # set current.value to the item
            self.current.value = item
            # if self.current has no next node
            if self.current.next is None:
                # set self.current node to the head start back over
                self.current = self.storage.head
            else:
                # otherwise set self.current node to the next node. move on
                self.current = self.current.next
        else:
            # if we're not at capacity, just set current to the head
            # ... start over
            self.current = self.storage.head
            # and add the new item to the tail
            self.storage.add_to_tail(item)            


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
