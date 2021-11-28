import math


def find_sums(target, nums, n=None):
    """
    Finds all subsets of a given set of numbers that sum to a given target.
    
    @param target:  the target sum
    @param nums: the set of numbers to find subsets of
    @param n: (optional) the number of numbers to use in the sum
    """
    
    S = SubsetSum(target, nums)
    if not n:
        return S.find_all_sums()
    else:
        return S.find_sum_of_n(target, nums, n)


class SubsetSum():
    answers = []

    def __init__(self, target=None, nums=[]):
        self.target = target
        self._nums = nums

    @property
    def nums(self):
        return self._nums
    
    @nums.setter
    def nums(self, value):
        if not value or not isinstance(value, list):
            raise Exception('Available numbers must be non empty list.')
        self._nums = sorted(value)

    #returns a list of lists of numbers that sum to target
    def find_all_sums(self):
        answers = []
        min_n, max_n = self.get_n_length_bounds(self.target, self._nums)
        for n in range(min_n, max_n+1):
            answer = self.find_sum_of_n(self.target, self._nums, n)
            if answer:
                answers.extend(answer)
        
        return answers

    #returns the minimum and maximum number of numbers that can be used to sum to target
    def get_n_length_bounds(self, target, nums):
        #We could do some math to bound possible lenths of answers. However for now just return the full range.
        return 1, len(nums)

        min_ = abs(min(nums, key=abs))
        max_ = abs(max(nums, key=abs))

        min_n = math.ceil(abs(target)/max_ if max_ != 0 else 0)
        max_n = min(math.ceil(abs(target)/min_ if min_ !=0 else 0), len(nums))
        return min_n, max_n

    #returns a list of lists of numbers that sum to target
    #Note: This is not optimal speed wise, but it does find every answer
    def find_sum_of_n(self, target, nums, n):
        if n == 1:
            for num in nums:
                if num == target:
                    return [[num]]
            return None
        
        new_nums = list(nums)
        answers = []
        for i in range(len(nums)-n):
            current_num = new_nums.pop(0)
            sub_answers = self.find_sum_of_n(target-current_num, new_nums, n-1)
            if sub_answers:
                for sub_answer in sub_answers:
                    new_answer = sorted([current_num] + sub_answer)
                    if new_answer not in answers:
                        answers.append(new_answer)

        return answers if answers else None


if __name__ == "__main__":
    starting_nums = [1,3,-6,-3,7,3,23,4]
    goal_summ = -2

    print(f'target: {goal_summ}')
    print(f'numbers: {starting_nums}')

    print('All matches:', find_sums(goal_summ, starting_nums))
