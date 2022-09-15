#!/usr/bin/python3
"""Module for task 1"""


class MyList(list):
    """Adds print_sorted to list class"""

    def print_sorted(self):
        """List sorting method"""

        print(sorted(self))
