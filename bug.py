def my_function(x):
    if x == 0:
        return 0
    else:
        return 1 / x

#This will cause ZeroDivisionError when x = 0
print(my_function(0))