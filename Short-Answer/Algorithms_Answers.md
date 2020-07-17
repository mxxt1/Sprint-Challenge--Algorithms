#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This is O(n) because number of operations increases in proportion to increase in input. If n=3, recurses 3 times, if n=4, 4 times, etc, effectively creating a loop with n iterations.


b) This is O(n)*O(log n) = O(nlogn) because the function's outer loop executes n times O(n) but the inner loop halves the number of iterations with each subsequent iteration. 


c) This is O(n) because the function operates recursively, dependent on the size of bunnies, so if bunnies = 5, the function recurses 5 times, if bunnies = 4, 4 times, etc. While the recursive call reduces the size of bunnies by 1, this isn't reduction isn't happening as part of the algorithm itself.

## Exercise II

<!-- list of size n = number floors doesn't need to be a list, just need the numbers really
f = breaking floor (given value)
incrementer = .5 -->

<!-- 1) n_array = 
2) test_array_length = n*incrementer
3) test_array = n[:test_array_length]
4) Test test_array[n-1] for egg break 
breaks, test test_array[n-2] for break loop from n-1 to 0 until non-breaking floor found, and then f = non-breaking floor + 1
    4a) if egg doesn't break on test_array[n-1], increase size of test_array_size = len(test_array) + len(test_array)*incrementer
    4b) test test_array[n-1] for break, if break, test n-2 until f found
        4ba) if no break, increase size of test array -->

1) Set incrementer (1/2)
2) Set starting sample size length (n*incrementer)
3) Set while condition (floor_found = false)
4) if test_array_length is less than f, loop range test_array_length starting from n-1 until floor is found and return the breaking floor
5) if test_array_length is greater than f, increment the size of test_array_length such that test_array_length = test_array_length + test_array_length*incrementer and recurse the function
6) if f == test_array_length, return the breaking floor

def find_f(n, f):
    incrementer = .5
                #if n=10. test_array_length is 5
    test_array_length = n * incrementer
    floor_found = False

    while floor_found == false:
        if f  < test_array_length: 
        #if the floor is below the test array length, iterate down until floor is #found
            for i in range(test_array_length, 0, -1):
                if i == f:
                    return print(f'Breaking floor is {i}')
        elif f > test_array_length:
        ## if floor is higher than test_array_length = 10+2.5
            test_array_length = n + test_array_length*incrementer
        ## recurse, passing n=12.5, f=f
            return find_f(test_array_length,f)
        elif f == test_array_length:
            floor_found = True
            return print(f'Breaking floor is {test_array_length}')

the worst case complexity for this function would be O(n^2) due to a nested for loop O(n) within a while loop O(n) resulting in O(n)* O(n).

