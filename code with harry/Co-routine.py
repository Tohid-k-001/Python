import time

def searcher():
    # Some time consuming task is performing eg. downloading,reading a file etc.
    book="this is book from code with harry"
    time.sleep(4)

    while True:
        text=(yield)        # The word passes in the yield
        if text in book:
            print("Text is in the book")
        else:
            print("Text is not in the book")

search=searcher()       # --> start the co-routine
# Search is started 
next(search)        # --> It runs from start of the searcher function to read the text file 
                            # which takes so much time to read the file                             
search.send("harry")    # --> it finds the word in the file

""" 1)Here I have started the co-routine in line-17  
    2)after that we dont have to stop for 4 sec to run the file. It takes no time to search """

input("press any key: ")
search.send("tohid")
input("press any key: ")
search.send("joker")
search.close()              # --> Stopping co-routine
# When I stop the co-routine then it gives iteration error:-
# input("press any key: ")
# search.send("from")
# op:-  search.send("from")
#       StopIteration



