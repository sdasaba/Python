class Person:
    def __init__(self):
        self.name = 'LEE'

wangi = Person()
same_wangi = wangi

print(wangi is same_wangi)

other_wangi = Person()
print(wangi is other_wangi)