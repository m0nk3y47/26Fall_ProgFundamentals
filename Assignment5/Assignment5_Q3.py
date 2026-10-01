#Write a function called check_number that takes one parameter, number
def check_number(number):
  #if the remainder of dividing the number by 2 = 0
  if number % 2 == 0:
    #print that the number is even with an f-string
    print(f"{number} is an even number.")
  #for enything else  
  else:
    #print that the number is odd with an f-string
    print(f"{number} is an odd number.")
    #return the function
    return
#ask the user for a number
num = int(input("Pick a number: "))

#call the function
check_number(num)
