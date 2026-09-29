def rectangle_stats(len, width):
  per = len+len+width+width
  area = len*width
  print(f"The area of your rectangle is {area}in.")
  print(f"The perimeter of your rectangle is {per}in.")
  return
  
len = input("Choose the lenth of your rectangle")
width = input("Choose the width of your rectangle")

rectangle_stats(len, width)
