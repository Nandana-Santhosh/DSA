total=int(input("ENTER THE TOTAL MARK"))

if total>90:
    print("A grade")
elif total<90 and total>=80:
    print("B grade")
elif total<80 and total>=70:
    print("C grade")
elif total<70 and total>=60:
    print("D grade")
elif total<60 and total>=50:
    print("E grade")
else:
    print("Failed")