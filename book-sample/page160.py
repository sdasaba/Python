class PublicPrivateExample:
    def __init__(self):
        self.public = 'safe'
        self._unsafe = 'unsafe'

    def public_method(self):
        # client가 사용해도 된다
        pass
    
    def _unsafe_method(self):
        # client가 사용하면 안된다
        pass
    

print('hello, world')
print(200)
print(200.1)


print(type('hello, world'))
print(type(200))
print(type(200.1))

