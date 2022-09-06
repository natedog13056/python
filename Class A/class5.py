# create a function to sum a list

nums = [23, 65, 87, 30]

# sum is a built-in function
# print('Total sum is ' + str(sum(nums)))

# create our own sum function to sum a list
def mySum(list):
    total = 0
    for num in list:
        total = total + num

    return total

print('My own sum is ' + str(mySum(nums)))