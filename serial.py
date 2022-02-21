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

    def __init__(self, start=0):
        """Make a new serial generator, starting at the start value"""
        
        self.start = self.next = start 


    def __repr__(self):
        """Show representation of serial generator"""
        
        return f"SerialGenerator start={self.start} next={self.next}"
    

    def generate(self):
        """Return next serial number in sequence"""

        # make self.next 1 higher than start value, so start = 100 and start.next = 101
        # Add one everytime we use generate()
        self.next += 1

        # return value of self.next - 1 to show current serial number
        return self.next - 1


    def reset(self):
        """Reset number to original start value"""
        
        self.next = self.start

