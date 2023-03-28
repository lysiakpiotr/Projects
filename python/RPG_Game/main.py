from time import sleep
from warrior import WarriorFactory


class Game():
    def __init__(self, player1, player2):
        self.player1 = player1  
        self.player2 = player2
    
    def start(self):
        while self.player1.hp > 0 and self.player2.hp > 0:
            self.player1.attack(self.player2)
            print(self.player1)
            sleep(0.7)
            self.player2.attack(self.player1)
            print(self.player2)
            sleep(0.7)
            print("")

        if self.player1.hp == 0 and self.player2.hp == 0:
            print("It's a draw!")
        elif self.player1.hp > 0:
            print(f"{self.player1.name} won!")
        else:
            print(f"{self.player2.name} won!")


def main():
    print("There are 4 fractions: Knight, Orc, Mage, Archer")
    print("Each fraction has its own attack rules")
    print("You'll witness a great battle between two players!\n")
    print("Enter fraction name, name, hp, damage for each player (separated by spaces):\n")

    players = []
    for _ in range(2):
        playerClass, playerName, playerHp, playerDamage = input("Player data: ").split()
        player = WarriorFactory().createWarrior(playerClass, playerName, float(playerHp), float(playerDamage))
        players.append(player)

    game = Game(players[0], players[1])
    game.start()


if __name__ == "__main__":
    main()