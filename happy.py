import time
import argparse

# cheap way to do squares
squares = dict([(c, int(c)**2) for c in "0123456789"])

# list of numbers in the never-ending sequence
bad_nums = sorted([4, 16, 37, 58, 89, 145, 42, 20])

def midpoint(low, high):
    ''' gets the midpoint of two ints. If the ints sum to an odd number,
    we round using Python's integer division.

    low: int; lower int
    high: int; higher int

    returns: int; the midpoint (low + high)/2
    '''
    # calculate to avoid overflow
    return (low + ((high - low)/2))

def bin_search(target, lst, low, high):
    ''' binary search a list for a number (either a float or int) between
    indices low and high (inclusive) 

    target: int or float; number to search for
    lst: list of ints or floats; list to search in
    low: int; lower bound on index to search for
    high: int; upper bound on index to search for

    returns: bool; True if the target was found, False otherwise
    '''

    if low == high:
        return(lst[low] == target)

    while low <= high:
        mid = midpoint(low, high)
        elt = lst[mid]
        if elt == target:
            return True
        elif elt < target:
            low = mid + 1
        elif elt > target:
            high = mid - 1
    return False
    

def is_happy(n):
    ''' determine if a number is happy or not

    n: int; the number in question

    returns: bool; True if the number is happy, False otherwise
    '''

    num = n
    # testing three conditions 
    #while (num > 1) and (not bin_search(num, bad_nums, 0, 7)):
    #while (num > 1) and (num != 4):
    while (num > 1) and (not (num in bad_nums)):
        num = sum(squares[digit] for digit in str(num))
    return (num == 1)

def main():

    # measure real and CPU time
    real_time = time.time()
    cpu_time = time.clock()
    for n in xrange(1,10000+1):
        print("%d\t%s" %(n, is_happy(n)))

    real_time = time.time() - real_time
    cpu_time = time.clock() - cpu_time

    print("\n\n")
    print("Real time: %f" %real_time)
    print("CPU time: %f" %cpu_time)

if __name__ == '__main__':
    main()
