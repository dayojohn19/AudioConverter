class PolishMp3():
    def __init__(self, album=None, artist=None):
        self.album = album
        self.myfunct('we', 'wa', 'were', 'wu')
    def myfunct(self, a, b, e, f):
        # do something
        print(a,b,e,f)
        if self.album is not None:
            print(self.album)

PolishMp3('John')