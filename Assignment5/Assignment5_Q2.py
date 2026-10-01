#Write a function called rectangle_stats that takes two parameters, length and width
def rectangle_stats(lenth, width):
  #find the perimeter
  per = lenth+lenth+width+width
  #find the area
  area = lenth*width
  #print the area with a f-string
  print(f"The area of your rectangle is {area}in.")
  #print the perimeter with a f-string
  print(f"The perimeter of your rectangle is {per}in.")
  #return the function
  return
 #ask the user for the length
lenth = int(input("Choose the lenth of your rectangle: "))

#ask the user for the width.
width = int(input("Choose the width of your rectangle: "))

#spacing
print()
#call the function
rectangle_stats(lenth, width)
