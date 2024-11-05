import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1

def selection_sort_books(lista:list)->list:
    alphabet = "abcdefghgklmnopqrstuvwxyz"
    for i in range(len(lista)-1):
        swap = i
        for j in range(i+1, len(lista)):
            if lista[swap].title.lower() > lista[j].title.lower():
                swap = j
        temp = lista[swap]
        lista[swap] = lista[i]
        lista[i] = temp
    return lista
books = [data.Book("percy","olympian"), data.Book("durk", "apples"),data.Book("Amy", "dirty")]
print(selection_sort_books(books))

# Part 2
def swap_case(words:str)->str:
    word = list(words)
    for i in range(len(word)):
        if word[i].isupper() and word[i].isalpha():
            word[i] = word[i].lower()
        elif word[i].islower() and word[i].isalpha():
            word[i] = word[i].upper()
    return "".join(word)
word = "HELLO world"
print(swap_case(word))




# Part 3
def str_translate(word :str,old :str,new :str)->str:
    word = list(word)
    for i in range(len(word)):
        if word[i] == old:
            word[i] = new
    return "".join(word)


# Part 4
def histogram(word:str)->dict:
    word = word.lower().split()
    dictionary = {}
    for i in word:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return dictionary
