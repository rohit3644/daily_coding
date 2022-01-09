class Solution:
    def twoSum(self, nums, target):
        length = len(nums)
        d = {}
        for i in range(length):
            if nums[i] in d:
                if isinstance(d[nums[i]], list):
                    d[nums[i]].append(i)
                else:
                    d[nums[i]] = [d[nums[i]], i]
            else:
                d[nums[i]] = i
        nums = sorted(nums)
        i = 0
        j = length - 1
        n1 = None
        n2 = None
        while i < j:
            if (nums[i] + nums[j]) > target:
                j -= 1
            elif (nums[i] + nums[j]) < target:
                i += 1
            else:
                n1 = nums[i]
                n2 = nums[j]
                break
        if isinstance(n1, int) and isinstance(n2, int):
            if n1 == n2:
                return d[n1][:2]
            return [d[n1], d[n2]]
        else:
            return []
