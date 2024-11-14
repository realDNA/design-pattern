class Singeleton:
    _instance = None

    def __new__(cls, *args, **kargs):
        if not cls._instance:
            print("create brand new instance")
            cls._instance = super(Singeleton, cls).__new__(cls, *args, **kargs)
        
        print("instance here")
        print("=------------------------=")
        return cls._instance
