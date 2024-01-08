
marks=[56, 67, "harry",  43, True, "hii", 567, 89]
print(marks)
print(type(marks))              # op:- class<list>
print(marks[0])                 # 0, 1, 2 etc. are the index
print(marks[1])                  
print(marks[2])
print(marks[3])
print(marks[4])
# print(marks[5])         error occure
# length of list can be change but tuple not
print(len(marks))

# Slicing of list:-
print(marks)
print(marks[:])             #it prints all by default
print(marks[1:])            #directly take upto last
print(marks[1:-1])
print(marks[-1])           # Gives last element
print(marks[0:6:2])        # last element gives difference between them

# If - else in loop:-
if 56 in marks:             # "56" wont print coz 56 is stored as an integer not as string.
    print("yes")
else:
    print("no")

# also in array:-
if "arr" in "harry":
    print("yes")

# important topic for list
# list comprehension:-
lst=[5*(i+1) for i in range(5)]             #write i for i in range()
print(lst)
lst=[i*i for i in range(20) if i%2==0]
print(lst)

word="hello"
ln1=[i for i in range(9)]   #op:- [0, 1, 2, 3, 4, 5, 6, 7, 8]
ln2=[word for i in range(5)]   #op:- ['hello', 'hello', 'hello', 'hello', 'hello']
print(ln1,"\n",ln2)

names=["tohid_kazi","rahul_pawale","tejas_pawale","hasan_kazi","mujif_kazi","nitin_patil"]
kazi_names=[name for name in names if "kazi" in name]

#82 day
# kazi_names=[name for name in names if name.endswith("kazi")]
print(kazi_names)

limit_names=[name for name in names if (len(names)<4)]
print(limit_names)







