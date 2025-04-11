"""
stack can be implemented using a list

S = <a1, a2, a3, ...>
    Top
    
- All insertion & deletion take place at one end (Top)
- LIFO (Last In First Out)

@ Push(x, S): insert x at the top of stack S
@ Pop(S): delete the element at the top of stack S
@ Top(S): return the element at the top of stack S
@ MakeNull(): create a new empty stack
@ IsEmpty(S): return True if stack S is empty, False otherwise

Python impelentation of Stack
"""

S = [1, 2, 3, 4, 5]
idx = 2

S.append(0) # Push()
S.pop() # Pop()
S[idx] # Top()
S = [] # MakeNull()
is_empty = (S == []) # IsEmpty()