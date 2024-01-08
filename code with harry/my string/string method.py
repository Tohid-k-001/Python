#string are immutable

a="harry!!  !!!!!!!!!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))                                     
print(a.replace("harry","jhon"))
print("my name is ",a.replace("harry","tohid"))

print(a.split("ar"))                #converts string into list and then seprate 

blogheading='introDucTio to js'
print(blogheading.capitalize())


str1='welcome to the consoller!!!'
print(len(str1))
space=str1.center(100)   #it adds 73 spaces to move it to the centre
print(space)
# print(len(space))        output:100

print(a.count('harry'))

print(str1.endswith("!!!"))
print("mala shodhatoy ka",str1.endswith("er"))

#find method

str1="his name is dann he is an honest man"
print(str1.find("is"))                #output: 1 (true)
print(str1.find("tohid"))             #output: -1(false)

#index method
# print(str1.index("ishhh"))

#isalnum
str1="howareyo5\n67u"
print(str1.isalnum())     #no puntuation    true
print(str1.isalpha())     #no numbers       true     
print(str1.islower())     #all lower
print(str1.isprintable())  #not printing eg.\n
print(f"\n {str1.isnumeric()}")    # string made up of numbers return true

str1="     "
print(str1.isspace())
str1="Bhguyg"
print(str1.isspace())

print(str1.istitle())                  #start with capital letter
print(str1.startswith("Bh"))           #start with given letter

print(str1.swapcase())             #it swap the cases=> convert capital to small and small to capital























