"""

problem uses O(nxk)
Because Python lists are arrays

A Python list is basically:

a contiguous block of memory

So elements are stored like:

index:  0  1  2  3  4
       [1][2][3][4][5]
What happens when you insert at index 0?

You want:

insert 9 at front → [9,1,2,3,4,5]

But memory is contiguous → so Python must:

Step 1: shift everything right
[1][2][3][4][5]
 ↓  ↓  ↓  ↓  ↓
[?][1][2][3][4][5]

That shifting is:

one move per element -> O(n)

class Solution:
    def rotate(self, nums, k):
        for _ in range(k):
            nums.insert(0, nums.pop())

"""


"""

problem uses extra space in memory

Why does nums[:] = ... use extra memory?

There are TWO operations happening:

RHS
nums[-k:] + nums[:-k]

This creates a NEW list

So memory used here:

first slice → new list
second slice → new list
concatenation → new list

This is O(n) extra space

LHS (nums[:])
nums[:] = ...

This means:

overwrite existing list contents

NOT replace variable.

So why “in-place”?

Because:

the list object stays the same
but its content is replaced

So:

same reference
but new memory used internally for RHS

class Solution:
    def rotate(self, nums, k):
        k = k % len(nums)
        nums[:] = nums[-k:]+nums[:-k]
        
"""

"""

Why does swap reversing work?
nums[l], nums[r] = nums[r], nums[l]
Python supports:

tuple unpacking swap

Internally it does:

temp = nums[l]
nums[l] = nums[r]
nums[r] = temp


"""


class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l = l+1
                r = r-1

        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)
