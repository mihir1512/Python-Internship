class publisher:

    def titlee(self):
        self.title = "Ertugrul Ghazi"
        print(" book title is ", self.title)


class book(publisher):

    def memberdata(self):
        print("page no. of books are 500")


class tape(publisher):

    def time(self):
        print("the time of laying tap is 4hours")


b = book()
b.titlee()
b.memberdata()
t = tape()
t.time()
