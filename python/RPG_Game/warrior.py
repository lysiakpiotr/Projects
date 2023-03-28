from random import randint


class Warrior():
    def __init__(self, name, hp, damage):
        self.name = name
        self.fullHp = hp
        self.hp = hp
        self.damage = damage
        self.committedAttacks = 0

    def attack(self, enemy):
        enemy.hp -= self.countAttack(enemy)
        if enemy.hp < 0:
            enemy.hp = 0
        self.committedAttacks += 1

    def countAttack(self):
        pass

    def criticalAttack(self, enemy):
        if randint(1, 100) < 10:
            enemy.hp -= self.damage * 2
            if enemy.hp < 0:
                enemy.hp = 0
            return True

    def __str__(self):
        return f"Name:\t\t{self.name}, \nFraction:\t{self.__class__.__name__},\nHP:\t\t{self.hp}\n"


class Knight(Warrior):
    def __init__(self, name, hp, damage):
        super ().__init__(name, hp, damage)

    def countAttack(self, enemy):
        if enemy.hp < enemy.fullHp * 0.3:
            return self.damage * 1.5
        else:
            return self.damage
    

class Orc(Warrior):
    def __init__(self, name, hp, damage):
        super ().__init__(name, hp, damage)

    def countAttack(self, enemy):
        if self.committedAttacks < 3:
            return self.damage * 1.2
        return self.damage
    

class Mage(Warrior):
    def __init__(self, name, hp, damage):
        super ().__init__(name, hp, damage)

    def attack(self, enemy):
        if isinstance(enemy, Mage):
            enemy.hp -= self.damage
        else:
            enemy.hp -= self.damage * 0.8
            enemy.damage -= 1
        if enemy.hp < 0:
            enemy.hp = 0
        
    
class Archer(Warrior):
    def __init__(self, name, hp, damage):
        super ().__init__(name, hp, damage)

    def countAttack(self, enemy):
        return self.damage*randint(1, 5)



class WarriorFactory():
    def createWarrior(self, dudeClass, name, hp, damage):
        match dudeClass:
            case "Knight":
                return Knight(name, hp, damage)
            case "Orc":
                return Orc(name, hp, damage)
            case "Mage":
                return Mage(name, hp, damage)
            case "Archer":
                return Archer(name, hp, damage)
            case _:
                raise Exception("Unknown fraction!")
