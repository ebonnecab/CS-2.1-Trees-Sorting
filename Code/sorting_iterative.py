#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) worst case scenario you have to iterate through
    entire list before you know if it's sorted
    O(1) - no new memory is being allocated
    """
    i = 0
    while i < len(items)-1:
        if items[i] > items[i+1]:
            return False
        else:
            i+=1
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: Worst case is O(n^2) because you iterate over every element
                  and compare it to every other element in the array 
                  Best case is O(n) if the elements are already sorted
    Memory usage: O(1) because the array is changed inplace
    """
    n = len(items)
    for i in range(n):
        for j in range(n-i-1):
            if items[j] > items[j+1]:
                items[j],items[j+1] = items[j+1], items[j]
    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: Best Case O(N) if the list is already sorted
    Worst Case O(N^2) if you have to compare every element in the list
    Memory usage: O(1) the array is sorted in place"""

    n = len(items)
    for i in range(n):
        min_in = i
        for j in range(i+1, n):
            if items[min_in] > items[j]:
                min_in = j
        items[i], items[min_in] = items[min_in], items[i]
    return items

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: Best Case O(N) if the list is already sorted
    Worst Case O(N^2) if you have to compare every element in the list
    Memory usage: O(1) the array is sorted in place"""
    
    n = len(items)
    for i in range(1, n):
        curr = items[i]

        while i > 0 and items[i-1] > curr:
            items[i] = items[i-1]
            i-=1
        items[i] = curr
    return items
if __name__ == '__main__':
    test_arr = [1,2,3,4,5,6,2]
    test = is_sorted(test_arr)
    # test = bubble_sort(test_arr)
    # test = selection_sort(test_arr)
    test = insertion_sort(test_arr)
    print(test)
