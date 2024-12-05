class Functor:
    def __call__(self,*args):
        print('Call functor with arguments', args)

if __name__ == '__main__':
    functor = Functor()
    functor("Hello, world",121)