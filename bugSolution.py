def my_function(x):
    try:
        if x == 0:
            return 0
        else:
            return 1 / x
    except ZeroDivisionError:
        return float('inf')

# This will not cause an error anymore
print(my_function(0))
print(my_function(5))