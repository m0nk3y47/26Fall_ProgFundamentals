def rectangle_stats(lenth, width):
  per = lenth+lenth+width+width
  area = lenth*width
  print(f"The area of your rectangle is {area}in.")
  print(f"The perimeter of your rectangle is {per}in.")
  return
  
lenth = int(input("Choose the lenth of your rectangle: "))
width = int(input("Choose the width of your rectangle: "))

print()
rectangle_stats(lenth, width)
