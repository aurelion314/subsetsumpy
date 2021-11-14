# subsetsumpy
Code to solve the subset sum problem for a subset of any length.

By default, it will find every possible combination of numbers that sum to the target. You can limit how many numbers should be used in the sum as an optional arguement.

## usage

     from subsetsum import find_sums

     target = 10
     numbers = [2,5,5]

     print('All matches:', find_sums(target, numbers))

