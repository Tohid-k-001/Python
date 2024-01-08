import re
# 1. Define a regular expression pattern
pattern= r"[A-Z]yclone"
# I want to search my text through pattern
text="""Sport pertains to any form of physical activity or game,[1] often competitive and organized, 
that aims to use, maintain, or improve Cyclone physical ability and skills while providing enjoyment to participants
and, in some cases, entertainment to spectators.[2] Sports can, through casual or organized participation, 
improve participants' physical health. Hundreds of sports exist, from those between single contestants, through
to those with hundreds of simultaneous Zyclone participants, either in teams or competing as individuals. In certain
sports such as racing, many contestants may compete, simultaneously or consecutively, with one winner; in others, 
the contest (a match) is Hyclone between two sides, each attempting to exceed the other. Some sports allow a "tie" or "draw", 
in which there is no single winner; others provide tie-breaking methods to ensure one winner. A number of contests 
may be arranged in a tournament producing a champion. Many sports leagues make an annual champion by arranging games 
in a regular sports season, followed in some cases by playoffs."""

# match=re.search(pattern, text)
# print(match)
""" 1)op:- <re.Match object; span=(697, 701), match='each'>
    2)conclusion:- this gives the string letter number 
    3)This says match at 697 to 701
 """
# op:- <re.Match object; span=(133, 140), match='Cyclone'>
# 1) It stops at first match sol.:-
# 2) [A-Z] we use re.finditer()
matches=re.finditer(pattern,text)
for match in matches:
    print(match.span())  
    """ (133, 140)   The span in the op is tuple
        (470, 477)
        (688, 695) """
    # print(match)  
    """ op:-<re.Match object; span=(133, 140), match='Cyclone'>
            <re.Match object; span=(470, 477), match='Zyclone'>
            <re.Match object; span=(688, 695), match='Hyclone'> """ 
    # Slicing of span to print word
    print(text[match.span()[0]:match.span()[1]])   # --> match.span()[1] because tuple contain only two element

# https://regexr.com/

