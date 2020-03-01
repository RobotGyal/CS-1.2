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
            print(pos.data)
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
            count +=1  # increase count
            pos =pos.next  # move to next node
        return count


    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) Why and under what conditions?"""
        n_node = Node(item)
        if self.head is None:  # if no head
            self.head = n_node   # make new node head
        else:
            pos = self.head #start at beginning
            while(pos.next):    #go until hit 'next is  Null'/tail
                pos = pos.next
            pos.next = n_node #at tail, make next node the new node


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
         Running time: O(1) Why and under what conditions?"""
        n_node = Node(item)
        if self.head: #if head exists
            n_node.next = self.head  # set the new nodes next position to current head
        return n_node


    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(1) Why and under what conditions?
        TODO: Worst case running time: O(n) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function

        #FIXME:
        # loop until data matches return node
        # if data = node, return node
        pos = self.head
        while(pos.next):
            if pos.data == quality:
                return True
            pos = pos.next
        return False


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(1) Why and under what conditions?
        TODO: Worst case running time: O(n) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))

        #FIXME:
        # loop through to find data
        # keep track of previous node
        # loop through when found
        # delete
        # reconnect references(previous.next = node(current/to be deleted).next)

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

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