from Robot import Robot

class Human():   

    __sexe = ['Male', 'Female']
    __stomach = []
    __sex = 0

    def __init__(self, sexe) -> None:
        self.__sex = sexe

    def eat(self, food):
        self.__stomach.append(food)

    def digest(self):
        self.__stomach.clear();

    def charge(self):
        pass

    

        

class Cyborg(Robot, Human):   

    def __init__(self, name, sexe):   
        Robot.__init__(self, name)
        Human.__init__(self, sexe)


if __name__ == "__main__":
    cyborg = Cyborg('Deux Ex Machina', 'M')

    print(cyborg.name, 'sexe', cyborg.sexe)
    print('Charging battery...')
    cyborg.charge()
    cyborg.status()
    cyborg.eat('banana')
    cyborg.eat(['coca', 'chips'])
    cyborg.digest()

    # cyborg.truc_fun()