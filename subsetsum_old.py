## This is the original code I put together quickly to solve a real world problem that did not require a clean solution.
## A cleaner version is in subsetsum.py
## This version may not find every answer.


starting_nums = [1,3,-6,-3,7,3,23,4]
goal_summ = -2

starting_nums = sorted(starting_nums)
print('numbers', starting_nums)
print('desired sum:', goal_summ)
print('')

answer = []
answers = []
def sum_recursion_may_be_required(nums, summ, level):
    print('level',level)
    #loop through each number in list and see if that number gives us a match to required sum.
    for i in range(len(nums)):
        if summ - nums[i] == 0:
            #We WIN! record the result and return it
            answer.append(nums[i])
            return nums[i]
        elif summ - nums[i] < 0: #The list is ordered by size, so if this number was bigger than desired sum, everything left will be too, so just break the loop
            break

    if len(nums) > 1: 
        #We failed to match with a single value. We need more terms, so lets remove the smallest value from our sum, remove it from the list of numbers, then call the attempt again in a recursive manner
        rest = sum_recursion_may_be_required(nums[1::],summ-nums[0], level+1)
        #If a match is found in a lower level it is returned. Adding it to what we just removed should equal the goal. 
        if nums[0]+rest == summ:
            #Horray! Return again in order to dig out of this recursive hole.
            answer.append(nums[0])
            return summ

    return 0 #Total failure :(

def find_sum():
    #n is the offset into nums list. 
    #We try all combinations with the first entry in the list, but if we fail, we exlude it (add offset). Rinse and repeat.
    for n in range(len(starting_nums)):
        print('')
        print('Offset', n)
        result = sum_recursion_may_be_required(starting_nums[n::], goal_summ, 0)
        if result == goal_summ:
            print('')
            print('Tada!',answer)
            return True

# In case there are multiple combinations, remove the one we found and try again.
while find_sum():
    answers.append(answer)
    for a in answer:
        starting_nums.remove(a)
    answer = []

print('')   
print('All matches:', answers)
