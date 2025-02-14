"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    ### TODO
    if x <= 1:
        return x
    else:
        ra = foo(x-1)
        rb = foo(x-2)
        return ra + rb

def longest_run(mylist, key):
    ### TODO
    max_count = 0
    current_count = 0

    for num in mylist:
        if num == key:
            current_count+=1
            max_count = max(max_count, current_count)
        else: current_count = 0

    return max_count


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    ### TODO
    if not mylist:
        return Result (0, 0, 0, False)
    if len(mylist) == 1:
        count = 1 if mylist[0] == key else 0
        return Result(count, count, count, count == 1)
    middle = len(mylist)//2
    left_result = longest_run_recursive(mylist[:middle], key)
    right_result = longest_run_recursive(mylist[middle:], key)

    left_size = left_result.left_size
    if left_result.is_entire_range:
        left_size += right_result.left_size

    right_size = right_result.right_size
    if right_result.is_entire_range:
        right_size += left_result.right_size

    combined_size = left_result.right_size + right_result.left_size if mylist[middle-1] == key and mylist[middle] == key else 0
    longest_size = max(left_result.longest_size, right_result.longest_size, combined_size)

    is_entire_range = left_result.is_entire_range and right_result.is_entire_range
    return Result(left_size, right_size, longest_size, is_entire_range)



