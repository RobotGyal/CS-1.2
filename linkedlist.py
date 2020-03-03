#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items=[]
        pos = self.head 
        while(pos):
            items.append(pos.data)
            # print(pos.data)
            pos = pos.next
        return items

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(n) Why and under what conditions?"""
        count = 0
        pos = self.head  # starts at the head
        while pos:  #while true or not Nonetype
            pos =pos.next  # move to next node
            count +=1  # increase count
        return count


    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) Why and under what conditions?"""
        new_node = Node(item)
        if self.is_empty():  # if no head
            self.head = new_node   # make new node head
            # self.tail = new_node
        else:
            self.tail.next = new_node #at tail, make next node the new node
        self.tail = new_node


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
         Running time: O(1) Why and under what conditions?"""
        new_node = Node(item)
        if self.head is None:
            self.tail = new_node
            # self.head = new_node
        else:
            new_node.next = self.head
        self.head = new_node



    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        est case running time: O(1) Why and under what conditions?
        Worst case running time: O(n) Why and under what conditions?"""
        pos = self.head
        while pos:
            if quality(pos.data) is True:
                return pos.data
            else:
                pos = pos.next


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) Why and under what conditions?
        Worst case running time: O(n) Why and under what conditions?"""
        pos = self.head
        prev = None
        while pos is not None:
            if item == pos.data:
                if prev is None:
                    #make head next node
                    self.head = pos.next
                    if pos.next is None:
                        self.tail = prev
                elif pos.next is None:
                    prev.next = None
                    self.tail = prev
                else:
                    prev.next = pos.next
                return
            else:
                prev = pos
                pos = pos.next

        raise ValueError(f'Item not found: {item}')
        

def test_linked_list():
    ll = LinkedList()
    print("\n")

    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print("\n")

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    print("\n")

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()