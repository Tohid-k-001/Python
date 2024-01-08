class library:
    def __init__(self) -> None:
        self.no_books=0
        self.books=[]

    def addbooks(self,book):
        self.books.append(book)
        self.nobooks=len(self.books)

    def showinfo(self):
        print(f"The Library has {self.nobooks} books" )
        print(f" The books are : {self.books}")

l1=library()
l1.addbooks("Harry Potter")    # If the class strats from the begining then it will start adding books from 0
l1.addbooks("Ramayan")
l1.addbooks("Mahabhaarat")
l1.addbooks("Physics")
l1.showinfo()




        