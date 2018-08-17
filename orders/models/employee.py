
class Employee :
    """docstring for Employee"""
    def __init__(self, first , last , pay ):
        super(Employee, self).__init__()
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@mei.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)