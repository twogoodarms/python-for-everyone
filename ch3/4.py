a = input("enter a number: ")
b = input("enter a number: ")
c = input("enter a number: ")

if a == b and a == c and b == c:
    print("all same!")
elif a != b and a != c and b != c:
    print("all different")
else:
    print("neither")
