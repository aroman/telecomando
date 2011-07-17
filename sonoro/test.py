class Foo:
    def __init__(self):
        self.mylist = ['cat', 'dog']

class Bar(Foo):
    def __init__(self):
        print self.mylist

if __name__ == '__main__':
    Bar()
