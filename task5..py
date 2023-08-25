score = float(input("enter the mark"))
if score > 1.0 or score < 0.0:
    print("not determine score")
elif score>=0.9:
    print("A")
elif score>=0.8:
    print("B")
elif score>=0.7:
    print("c")
elif score>=0.6:
    print("D")
else:
    print("E")