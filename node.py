# Implement your Node class here
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

"""
Design memo:
Why is a stack the right choice for undo/redo?
A stack is the correct choice for undo/redo because it's only concern is what was done most recently. A stack conveniently leaves the most recent item on the top, meaning you can undo and redo to your heart's content. If a queue was used, you would undo things starting at the beginning of the changes you made, which would be horrendous. 
Why is a queue better suited for the help desk? 
A queue is better for the help desk because it makes logical sense that the first person in who wants help, should be the first person to receive help, no matter how long the line is. The 20th person in will be the 20th to get helped. If a stack was used, it would be unjust. 
How do your implementations differ from Python’s built-in lists?
These implementations differ from Python's built-in lists because the data structures are made using nodes and pointers. Python's list has pre-made functions, whereas my stack and queue are manually created. 
"""