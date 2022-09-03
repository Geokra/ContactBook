class contact:

    def __init__(self, first, last, email_, age):
        self.first = first
        self.last = last
        self.email_ = email_
        self.age = age

    # @property
    # def email(self):
    #     return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Contact('{}', '{}', '{}')".format(self.first, self.last, self.age, self.email_)
