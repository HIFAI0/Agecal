# ===============================================================
# Currect Age Calculator For Python
# Author = HIFAI0
# GITHUB = https://github.com/HIFAI0
# ===============================================================


import time


# code for intro
print("="*70)
print("SIMPLE CURRENT AGE CALCULATOR FOR PYTHON")
print("                               AUTHOR - HIFAI0")
print("="*70)
time.sleep(5)

# code for input's
name = str(input("Input Name: "))
cy = int(input("Input Current Year: "))
by = int(input("Input Birth Year: "))

# formula for current age calculation
ca = int(cy) - int(by)

# code for result
msg1 = "You Are "
msg2 = "Year Old Now"
print("X"*70)
print("X"*70)
print(name,msg1,ca,msg2)
print("X"*70)
print("X"*70)

time.sleep(5)






