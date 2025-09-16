def summary():
    nums = get_nums()
    print(f"total sum is = {sum(nums)}")
    
def multyply():
    nums = get_nums()
    print(f"work is = {nums[0] * nums[1]}")
   
   
def get_nums():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    return [num1, num2] 

multyply()
    