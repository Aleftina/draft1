class A:
    def __init__(self):
        self.a = 42
    def __setattr__(self, name, value):
        if name == 'a' and hasattr(self, 'a'):
            raise AttributeError('a is read only')
        super().__setattr__(name, value)
    def __delattr__(self, name):
        if name == 'a':
            raise AttributeError('a is read only')
        super().__delattr__(name)