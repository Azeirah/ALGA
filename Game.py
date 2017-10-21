from main import Dungeon
from cellLookup import printSymbolLegend
from defaultConfig import dungeonConfig
from talisman import talisman


class Game():
    def __init__(self, config):
        self.dungeon = Dungeon(config)
        self.map = self.dungeon.map

    def startLoop(self):
        print("Starting game!")
        printSymbolLegend()

        while True:
            self.map.redraw()
            print(self.dungeon)
            self.printAvailableCommands()
            answer = self.input()
            output = self.processAnswer(answer)

            print("\n" * 80)
            if len(output):
                print("**")
                print(output)
                print("**")

    def printAvailableCommands(self):
        print("(m)ove <id>, (g)renade, (t)alisman")

    def input(self):
        ans = input("> ")
        return ans

    def processAnswer(self, answer):
        command = answer[0]
        if command[0] == "m":
            try:
                position = int(answer[2:])
                return "moving to position {p}".format(p=position)
                self.map.player.move(position)
            except:
                return "Warning, wrong input"
        if command == "g":
            grenade = self.dungeon.map.grenade
            if grenade.hasExploded():
                return "Throwing another grenade is a bad idea"
            else:
                # more points is more better.
                self.dungeon.map.grenade.explode()
                return "BOOOM"
        if command == "t":
            talisman(self.dungeon)

        return ""


if __name__ == "__main__":
    game = Game(dungeonConfig)
    game.startLoop()
