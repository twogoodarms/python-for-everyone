a = raw_input("Enter a string: ")
a.lower()
b = raw_input("Enter a string: ")
b.lower()
c = raw_input("Enter a string: ")
c.lower()

if a[0] < b[0] and a[0] < c[0]:
    print(a)
    
    if b[0] < c[0]:
        print(b)
        print(c)
    else:
        print(c)
        print(b)

elif b[0] < a[0] and b[0] < c[0]:
    print(b)

    if a[0] < c[0]:
        print(a)
        print(c)
    else:
        print(c)
        print(a)

elif c[0] < a[0] and c[0] < b[0]:
    print(c)

    if a[0] < b[0]:
        print(a)
        print(b)
    else:
        print(b)
        print(a)
