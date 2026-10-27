grade = float(input("Enter your Grade: "))
if grade<0 or grade>20:
    print("Invalid Grade")
elif grade<20 and grade>=16:
    print("Very Good")
elif grade<16 and grade>=14:
    print("Good")
elif grade<14 and grade>=12:
    print ("Fairly Good")
elif grade<12 and grade>=10:
    print("Pass")
else:
    print("Fail")