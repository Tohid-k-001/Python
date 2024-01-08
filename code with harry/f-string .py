letter="hey my name is {} and i am from {}"
country="India"
name="Harry"

# new .format => It will format the string



print(letter.format(country,name)) # if you put like a string it will directly pput value
# the code get increase and you have to remember where the thing is

# So to overcome the problem we use ,
# F-String

print(f"hey my name is {name} and i am from {country}")

# if you want to show curly bracket 
# This called Raw f-string
print(f"heyy we use f string like this hey my name is {{name}} and i am from {{country}}")

"""
Display only 2 digits eg. 67.98 
 """
# txt="for only {price:.4f} dollers !!"
price=49.765468
# print(txt.format(price))
""" 
                 :.   important !!!!
 """

txt=f"for only {price:.4f} dollers !!"
print(txt)
print(type(f"value {2 * 60}"))
print(f"value {2 * 60}")





