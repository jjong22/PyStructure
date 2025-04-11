"""
Queue can be implemented using a list

Q = <a1, a2, a3, ..., an>
    Front            Rear

- All insertion takes place at the rear and all deletion takes place at the front
- FIFO (First In First Out)

@ Enqueue(x, Q): insert x at the rear of queue Q
@ Dequeue(Q): delete the element at the front of queue Q
@ Front(Q): return the element at the front of queue Q
@ MakeNull(): create a new empty queue
@ IsEmpty(Q): return True if queue Q is empty, False otherwise

Python impelentation of Stack
"""

Q = [1, 2, 3, 4, 5]
idx = 2

Q.append(0) # Enqueue()
Q.pop(0) # Dequeue()
Q[idx] # Front()
Q = [] # MakeNull()
is_empty = (Q == []) # IsEmpty()