"""Given list of ints, return True if any two nums in list sum to 0.

    >>> add_to_zero([])
    False

    >>> add_to_zero([1])
    False

    >>> add_to_zero([1, 2, 3])
    False

    >>> add_to_zero([1, 2, 3, -2])
    True

Given the wording of our problem, a zero in the list will always
make this true, since "any two numbers" could include that same
zero for both numbers, and they sum to zero:

    >>> add_to_zero([0, 1, 2])
    True
"""


def add_to_zero(nums):
    """Given list of ints, return True if any two nums sum to 0."""

    if not nums: #if nums is an empty list
        return False

    elif len(nums) == 1: #if nums only has 1 item in the list
        return False

    elif 0 in nums: #if nums has a zero in it
        return True 

    elif len(nums) % 2 == 0:
        for num in nums:
            if -num + num == 0: #any number and its negative will add up to one.
                return True
            else:
                return False
    else:
        return False


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NOTHING ESCAPES YOU!\n"
