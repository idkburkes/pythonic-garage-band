from abc import ABC

class Band:
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)
        
    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    @classmethod
    def to_list(self):
        return Band.instances
        



class Musician(ABC):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{type(self).__name__} instance. Name = {self.name}'


class Guitarist(Musician):

    def play_solo(self):
        return 'face melting guitar solo'

    def get_instrument(self):
        return 'guitar'

    def __str__(self):
        return f'My name is {self.name} and I play guitar'



class Bassist(Musician):


    def play_solo(self):
        return 'bom bom buh bom'

    def get_instrument(self):
        return 'bass'

    def __str__(self):
        return f'My name is {self.name} and I play bass'

    

class Drummer(Musician):

    def play_solo(self):
        return 'rattle boom crash'

    def get_instrument(self):
        return 'drums'

    def __str__(self):
        return f'My name is {self.name} and I play drums'
    