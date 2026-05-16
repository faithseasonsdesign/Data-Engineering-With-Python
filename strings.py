

#point of this exercise is to understand strings and methods of strings in python.

#length of the string
#first character of the string
#search if a validate exist in a string
#modifiy a string
#string methods.

firstName = "Rebaone"
thirdName = "Tshepiso"
fullNames = "Rebaone Faith Matlaba"
casingName = "reRabewe"
whiteSpaceName = " Rebaone  " #this will simply increase the length of this name from 7 TO ABOUT 12?
noWhiteSpace = whiteSpaceName.strip()

#first character in a string
firstChar = firstName[0]
print(firstChar)

#uppercase
print(casingName.upper())
#lowercase
print(casingName.lower())
#print with whitespace
print("Length of name with white space :" ,len(whiteSpaceName))
print("Length of name with white space removed : " ,len(whiteSpaceName.strip()))
print("Name with white space: " , whiteSpaceName)
print("Name with white space removed:",noWhiteSpace)

#spliting strings my favourite exercise actually
grade12AStudentsUnOrg = "Rebaone#25#Male,Kabelo#34#Female,#Letuma@38#male" #in here we have 3 people we want to split them
grade12AStudentsOrg = grade12AStudentsUnOrg.split(",") 
# now this variable above have grade12AStudentsOrg = [Rebaone#25#Male , Kabelo#34#Female , #Letuma@38#male] 
print( "This is length of the array : " , len(grade12AStudentsOrg))
print( "This is length of the actual unorganised string " , len(grade12AStudentsUnOrg))

print("THE STRING BELOW IS A CENTEREDNSTRING")
print("name".center(50))

#on line 33 if you were to want count/length it was going to return number of charactors
#on line 34 if you were to want count/length it was going to return number of stuff in an array. which is 3

#length of the firstName
lengthOfFirstName = len(firstName)
print("Length of : " , firstName , " is : " , lengthOfFirstName)

#check if first name is IN there
firstNameExist = firstName in fullNames #returns a boolean value either true or false
if(firstNameExist):
    print( firstName , " exist in | is IN :" , fullNames)
else:
    print(firstName , " does not exist :" , fullNames)

#check other name NOT IN
thirdNameNotInFullnames = thirdName not in fullNames #account that thirdName is a string hence comparison works it can't be a integer or double
if(thirdNameNotInFullnames):
    print(thirdName ," does is NOT IN : " , fullNames)
else:
    print(thirdName , " is IN " , fullNames)

#looping through the string : also accessing every single character in that string
for counter in firstName:
    print("This will loop 7 times I guess")
