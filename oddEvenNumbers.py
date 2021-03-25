############################################################################
# Task
# Given an integer, perform the following conditional actions:
#
# If is odd, print Weird
# If is even and in the inclusive range of 2 to 5, print Not Weird
# If is even and in the inclusive range of 6 to 20, print Weird
# If is even and greater than 20, print Not Weird
#
# Input Format
#
# A single line containing a positive integer, n
#
# Constraints
# 1<= n <= 100
#
# Output Format
# Print Weird if the number is weird. Otherwise, print Not Weird.

n = 2
# even = [2,4,6,8,0]
# odd = [1,3,5,7,9]
############################################################################

if (n % 2) == 0 and (2 <= n <= 5):
    print("Not Weird")
elif (n % 2) == 0 and (6 <= n <= 20):
    print("Weird")
elif (n % 2) == 0 and (n > 20):
    print("Not Weird")
else:
    print("Weird")