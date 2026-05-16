

#understanding type casting 
# int() float() str()

#the purpose of this exercise would be to look like I don't know what parsing numbers means
#the coding standards should not be judged either, I am a rockie learning programming again hahahaha

op = 4
option  = 4 #this is an integer
option2 = input("enter option 2 : ")

if(op==option):
    print("These numbers are integers and they are equal")
else:
    print("These numbers are both integers but they are not equal") #because we know that don't we

if(op==option2):
    print("one of these numbers is a str and another an integer so they are equal and not") #silly exercise
else:
    print("we need to parse these because one of the is a srt and another is a integer")
    parsedOption2 = int(option2)
    #check again if this was now parsed
    if(parsedOption2 == op):
        print("both of these numbers are now equal and integers because the inputed value was parsed")
    else:
        print("these numbers are still not equal this means the inputed number is not an integer still")


