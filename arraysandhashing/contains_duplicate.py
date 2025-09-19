#   217 - Contains Duplicate
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
# iterate through the array
# record values in set
# if the record already exists then return true, else return false
        duplicate = set()
        for num in nums:
            if num in duplicate:
                return True
            else:
                duplicate.add(num)
        return False