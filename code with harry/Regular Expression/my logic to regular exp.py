text="""Sport pertains to any form of physical activity or game, [1] often competitive and organized, 
that aims to use, maintain, or improve physical ability and skills while providing enjoyment to participants
and, in some cases, entertainment to spectators.[2] Sports can, through casual or organized participation, 
improve participants' physical health. Hundreds of sports exist, from those between single contestants, through
to those with hundreds of simultaneous participants, either in teams or competing as individuals. In certain
sports such as racing, many contestants may compete, simultaneously or consecutively, with one winner; in others, 
the contest (a match) is between two sides, each attempting to exceed the other. Some sports allow a "tie" or "draw", 
in which there is no single winner; others provide tie-breaking methods to ensure one winner. A number of contests 
may be arranged in a tournament producing a champion. Many sports leagues make an annual champion by arranging games 
in a regular sports season, followed in some cases by playoffs."""

words=text.split(" ")
print(words) #--> It print as a list
print("The words in a text are: ",len(words))

for index,word in enumerate(words,start=1):
    if word=="each":
        print(index-1)    # To get accurate index 
        # op:- 96
print(words[96])
# op:- each

# when complicate expression will be there then we have to make a complex logic so se use Regular expression