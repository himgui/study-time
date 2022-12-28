# Collatz - Function Exercise
print('Check if a number is // 2 until your find number 1')
def collatz(number):
    if number % 2==0: ## Checks if the number is even
        print(number // 2)
        return number // 2
    elif number % 2 ==1: ## Checks if the number is odd       
        result = 3 * number + 1
        print(result)
        return(result)

n = input("Type a number: ")
while n != 1:
    n = collatz(int(n))