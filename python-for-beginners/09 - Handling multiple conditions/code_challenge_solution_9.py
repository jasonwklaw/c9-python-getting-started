# Ask a user their name
# name = input('Please enter your name: ')

# name = name.split()
# firstname_start = name[0][0].upper()
# lastname_start = name[-1][0].upper()

firstname = input('Please enter your name: ')
firstname_start = firstname[0].upper()

# If their first name starts with A or B 
# tell them they go to room AB
# IF their first name starts with C
# tell them to go to room CD
# If their first name starts with another letter, ask for their last name
# IF their last name starts with Z, tell them to go to room Z
# if their last name starts with any other letter, tell them to go to room OTHER
# When you are done
# Anna should be in room AB
# Bob should be in room AB
# Charlie should be in room C
# Khalid Haque should be in room OTHER
# Xin Zhao should be in room Z
if firstname_start == 'A' or firstname_start == 'B':
    room = 'AB'
elif firstname_start == 'C':
    room = 'CD'
else:
    lastname = input('Please enter your last name: ')
    lastname_start = lastname[0].upper()
    if lastname_start == 'Z':
        room = 'Z'
    else:
        room = 'OTHER'
print('Please go to room ' + room + '.')