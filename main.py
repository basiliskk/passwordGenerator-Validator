print ("Hello! Welcome to my password generator and validator program.")
print ("Here are the following qualifications for what your password must contain: ")
print ("1. It must be at least 8 characters long")
print ("2. It must contain at least one capital letter")
print ("3. It must contain at least one number ")
print("If you find it difficult to think of a password that satisfies these conditions ")
print("you can always enter one to have a candidate password generated for you.")


def validate(x):
  contains_num = False
  contains_cap = False


  for i in x:
    if(i.isdigit()):
      contains_num = True
    elif(i.isupper()):
      contains_cap = True

  if(contains_cap & contains_num & (len(x) >= 8)):
    return True
  else:
    return False

	
		
x = 4


while ( x != 0):
  password = input("Enter your chosen password: ")
  valid = validate(password)
  
  if(valid):
    print("You entered a valid password, great job!. Your password is ", password)
    break
  else:
    print("You did not enter a valid password, try again")
    continue




