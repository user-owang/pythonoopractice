"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        '''create serial number generator that starts at start'''
        self.start = start
        self.gen_count = -1
    
    def __repr__(self):
        return f'Serial number generator with initial value of {self.start}. Next value will be {self.start +1}'

    def generate(self):
        '''generate next serial number'''
        self.gen_count += 1
        return self.start + self.gen_count
    
    def reset(self):
        '''reset serial number to initial start value'''
        self.gen_count = -1

        

