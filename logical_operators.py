x=10
y=20
z=30
if x<y and y<z:
    print("x is less than y and y is less than z")  #Output: x is less than y and y is less than z
else:
    print("Condition not met")
if x<y or y>z:
    print("At least one condition is true")  #Output: At least one condition is true    
else:
    print("Both conditions are false")
if not x>y:
    print("x is not greater than y")  #Output: x is not greater than y
else:
    print("x is greater than y")