def factorial(x):
    #base case 
    if x <= 1:
        return 1
    #recursive case
    else:
        return x * factorial(x-1)

# for i in range(1, 22):
    # print(f"{i}! = {factorial(i)}")

def fibonacci(x):
    #base case
    if x <= 1:
        return x
    #recursive case
    else:
        return fibonacci(x-1) + fibonacci(x-2)
    
# for i in range(1, 11):
    # print (f"fib({i}) = {fibonacci(i)}")

def prepare_string(input_string):
    output_string = ""
    for c in input_string:
        if c.isalpha():
            output_string += c.lower()
    return output_string

test_string = "go hang a salami, I'm a lasagna hog."

print(prepare_string(test_string))
    

def is_palendrome(s):
    #base case
    if len(s) <= 1: 
        return True
    #recursive case
    else:
        if s[0] == s[-1]:
            return is_palendrome(s[1:-1])
        else:
            return False

print(is_palendrome(prepare_string(test_string)))

def hanoi_solver(start, end, helper, disks):
    #base case
    if disks == 0:
        return
    #recursive case
    else:
        # solve disks -1 from start to helper
        hanoi_solver(start, helper, end, disks-1)
        print(f"Move disk from {start} to {end}")
        # solve disks -1 from helper to end
        hanoi_solver(helper, end, start, disks-1)
        

# hanoi_solver("A", "C", "B", 4)
