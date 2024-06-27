# 4th Commit 


test = "JamesisOld"
first_char = test[0]

print(first_char.isupper())

# islower()

print(test.find("a") )
# Return the index if it finds it
# Returns -1 if it can't find it


# Step 1:
# Prompt the user to enter their password
# Check the following:
#   - If The Password contains the letter z
#   - If The Password ends with an a
#   - If The Password beguins with any uppercase Letter
# If yes to all three, Print "Accsept!"
# If any of these are not true, print "Reject!"

# Step 2: Implement the more generic rules on the whiteboard
#   -Hint:  You may want to put the symbols into a list of symbols,
#           Which you can check against










password = input("What is Your password?")

if password .find('z') == -1:
    print("Rejected")
else:
    if password [-1] == "!" and password [0].isupper():
        print("Accsepted")
    else:
        print("rejected")
