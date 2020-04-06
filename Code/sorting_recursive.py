#!python
from sorting_iterative import selection_sort

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    merged_lst = []
    i, j = 0, 0
    m, n = len(items1), len(items2)

    while i < m and j < n:
        if items1[i] < items2[j]:
            merged_lst.append(items1[i])
            i+=1
        else:
            merged_lst.append(items2[j])
            j+=1

    merged_lst.extend(items1[i:])
    merged_lst.extend(items2[j:])

    return merged_lst


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    n = len(items)

    if n >= 2:
        mid = len(items)//2
        l = items[:mid]
        r = items[mid:]

        l = selection_sort(l)
        r = selection_sort(r)

        merged = merge(l, r)
        for i in range(len(merged)):
            items[i] = merged[i]
    return items   

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    n = len(items)
    if n >= 2:
        mid = len(items)//2
        l = items[:mid]
        r = items[mid:]

        merge_sort(l)
        merge_sort(r)

        merged = merge(l, r)

        for i in range(len(merged)):
            items[i] = merged[i]
        return items 

    return items

def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort

if __name__ == '__main__':
    a = [1,2,3,4,5,6]
    b = [20,25, 40, 45, 50]
    test_l = [1, 10, 2 , 5, 8, 7, 30, 25 ]
    
    # test = merge(c, d)
    # test = split_sort_merge(test_l)
    test = merge_sort(test_l)
    print(test)