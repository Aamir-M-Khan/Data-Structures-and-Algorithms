class Stack:
    """
    A simple implementation of a stack data structure.

    Methods:
    --------
    push(item):
        Adds an item to the top of the stack.

    pop():
        Removes and returns the item at the top of the stack. Raises an IndexError if the stack is empty.

    peek():
        Returns the item at the top of the stack without removing it. Raises an IndexError if the stack is empty.

    is_empty():
        Checks if the stack is empty.

    size():
        Returns the number of items in the stack.

    clear():
        Removes all items from the stack.

    __iter__():
        Returns an iterator for the stack.

    __len__():
        Returns the number of items in the stack.

    __contains__(item):
        Checks if the item is in the stack.
    """

    def __init__(self):
        """Initializes an empty stack."""
        self._items = []

    def push(self, item):
        """Adds an item to the top of the stack.

        Parameters:
        -----------
        item : any
            The item to be added to the stack.
        """
        self._items.append(item)

    def pop(self):
        """Removes and returns the item at the top of the stack.

        Returns:
        --------
        any
            The item at the top of the stack.

        Raises:
        -------
        IndexError
            If the stack is empty.
        """
        if self.is_empty():
            raise IndexError('No item in the stack')
        return self._items.pop()

    def peek(self):
        """Returns the item at the top of the stack without removing it.

        Returns:
        --------
        any
            The item at the top of the stack.

        Raises:
        -------
        IndexError
            If the stack is empty.
        """
        if self.is_empty():
            raise IndexError('No item in the stack')
        return self._items[-1]

    def is_empty(self):
        """Checks if the stack is empty.

        Returns:
        --------
        bool
            True if the stack is empty, False otherwise.
        """
        return len(self._items) == 0

    def size(self):
        """Returns the number of items in the stack.

        Returns:
        --------
        int
            The number of items in the stack.
        """
        return len(self._items)

    def clear(self):
        """Removes all items from the stack."""
        self._items.clear()

    def __iter__(self):
        """Returns an iterator for the stack.

        Returns:
        --------
        iterator
            An iterator for the stack.
        """
        return iter(self._items)

    def __len__(self):
        """Returns the number of items in the stack.

        Returns:
        --------
        int
            The number of items in the stack.
        """
        return self.size()

    def __contains__(self, item):
        """Checks if the item is in the stack.

        Parameters:
        -----------
        item : any
            The item to check for in the stack.

        Returns:
        --------
        bool
            True if the item is in the stack, False otherwise.
        """
        return item in self._items
