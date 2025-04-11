"""
python provide a default list implementation

L = <a1, a2, a3, ...>

- a finite, ordered collection of elements

@ Insert(x, i, L): insert x at index i in list L
@ Delete(i, L): delete the element at index i in list L
@ Next(i, L): return the next element in list L after index i
@ Previous(i, L): return the previous element in list L before index i
@ Locate(x, L): return the index of element x in list L
@ Retrieve(i, L): return the element at index i in list L
@ MakeNull(): create a new empty list
@ First(L): return the first element in list L

Python impelentation of list
"""

L = [1, 2, 3, 4, 5]
idx = 2

L.insert(0, 0) # Insert()
L.remove(0) # Delete()
L[idx+1] # Next()
L[idx-1] # Previous()
L.index(3) # Locate()
L[idx] # Retrieve()
L = [] # MakeNull()
L[0] # First()