class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = dict()

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.nums[number] = self.nums.get(number, 0) + 1
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for i in self.nums.keys():
            j = value - i
            if i == j and self.nums[i] > 1 or i != j and self.nums.get(j, 0) > 0:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)