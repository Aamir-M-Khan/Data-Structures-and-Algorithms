class Queue:
    """
    A simple implementation of a queue data structure.

    Methods:
    --------
    enqueue(item):
        Adds an item to the end of the queue.

    dequeue():
        Removes and returns the item at the front of the queue. Raises an IndexError if the queue is empty.

    is_empty():
        Checks if the queue is empty.

    peek():
        Returns the item at the front of the queue without removing it. Raises an IndexError if the queue is empty.

    size():
        Returns the number of items in the queue.

    clear():
        Removes all items from the queue.

    __iter__():
        Returns an iterator for the queue.

    __len__():
        Returns the number of items in the queue.

    __contains__(item):
        Checks if the item is in the queue.
    """

    def __init__(self):
        """Initializes an empty queue."""
        self._items = []

    def enqueue(self, item):
        """Adds an item to the end of the queue.

        Parameters:
        -----------
        item : any
            The item to be added to the queue.
        """
        self._items.append(item)

    def dequeue(self):
        """Removes and returns the item at the front of the queue.

        Returns:
        --------
        any
            The item at the front of the queue.

        Raises:
        -------
        IndexError
            If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Can't remove item from an empty Queue.")
        return self._items.pop(0)

    def is_empty(self):
        """Checks if the queue is empty.

        Returns:
        --------
        bool
            True if the queue is empty, False otherwise.
        """
        return len(self._items) == 0

    def peek(self):
        """Returns the item at the front of the queue without removing it.

        Returns:
        --------
        any
            The item at the front of the queue.

        Raises:
        -------
        IndexError
            If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Nothing here.")
        return self._items[0]

    def size(self):
        """Returns the number of items in the queue.

        Returns:
        --------
        int
            The number of items in the queue.
        """
        return len(self._items)

    def clear(self):
        """Removes all items from the queue."""
        self._items.clear()

    def __iter__(self):
        """Returns an iterator for the queue.

        Returns:
        --------
        iterator
            An iterator for the queue.
        """
        return iter(self._items)

    def __len__(self):
        """Returns the number of items in the queue.

        Returns:
        --------
        int
            The number of items in the queue.
        """
        return self.size()

    def __contains__(self, item):
        """Checks if the item is in the queue.

        Parameters:
        -----------
        item : any
            The item to check for in the queue.

        Returns:
        --------
        bool
            True if the item is in the queue, False otherwise.
        """
        return item in self._items
