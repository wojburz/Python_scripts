import os
import random
import sys


class Player:
    def __init__(self, name, bet):
        self.name = name
        self.currentBet = set(bet)
        self.wonGames = []
        self.lostGames = []

        print("Player '{}' has been created, with bet: {}".format(self.name, self.currentBet))

    def strList(self, list):
        res = ""
        for num in list:
            res += str(num) + ', '
        return res[:-2]

    def getName(self):
        return str(self.name)

    def getBet(self):
        if len(self.currentBet) > 0:
            return self.strList(self.currentBet)
        else:
            return 'No bet?'

    def getWonGames(self):
        if len(self.wonGames) > 0:
            return self.strList(self.wonGames)
        else:
            return 'None... sorry'

    def getLostGames(self):
        if len(self.lostGames) > 0:
            return self.strList(self.lostGames)
        else:
            return ' '

    def setBet(self, bet):
        self.currentBet = bet

    def addWin(self, num):
        self.wonGames.append(num)

    def addLose(self, num):
        self.lostGames.append(num)

    def resetScore(self):
        self.wonGames = []
        self.lostGames = []


class Game:
    def __init__(self, players, games, mode):
        self.playersNr = players
        self.gamesNr = games
        self.mode = mode
        self.playersList = []
        self.wonInGame = []
        self.resultTracking = []

        self.playGame(self.mode)

    def clearWindow(self):
        if(os.name == "nt"):
            os.system('cls')

        elif(os.name == "posix"):
            os.system("clear")

        else:
            for i in range(40): print()
        print("------------ROULETTE------------\n\n")

    def validateInput(self, name):
        correct = False
        while not correct:
            correct = True
            betStr = str(input("\nEnter '{}s' bet numbers: ".format(name)))
            betStr = betStr.replace(",", " ")
            betStr = betStr.replace(".", " ")
            betNumbers = betStr.split()
            if len(betNumbers) > 0:
                for i in range(len(betNumbers)):
                    betNumbers[i] = int(betNumbers[i])
                    if int(betNumbers[i]) > 36 or int(betNumbers[i]) < 0:
                        correct = False
                        print("Enter correct values!")
                        break
                if correct:
                    return list(betNumbers)
            else:
                correct = False
                print("Enter at least one bet!")

    def strList(self, l):
        result = ""
        for el in l:
            result += str(el) + ", "
        return result[:-2]

    def getAllBets(self):
        allBets = []
        for player in self.playersList:
            for bet in player.currentBet:
                allBets.append(bet)
        allBets = set(allBets)
        return self.strList(allBets)

    def createPlayers(self):
        n = 1

        while n <= self.playersNr:
            try:
                correctFlag = True
                self.clearWindow()
                name = str(input("Enter {} player name: ".format(n)))
                betNumbers = self.validateInput(name)
                if correctFlag:
                    self.playersList.append(Player(name, betNumbers))
                    n += 1

            except:
                self.clearWindow()
                input("Enter correct input! [Press ENTER]")

    def printSummary(self):
        self.clearWindow()
        if self.mode == 1:
            print("RESULTS:")
            print("GAME      WIN NUMBER")
            for result in self.wonInGame:
                game = result[0]
                won = result[1]
                print(" {:<13}{}".format(game, won))
            print("\n")
            print("| {:<15}  | {:<15}  | {:<15}  | {:<15}  |\n{}".format("PLAYER", "BET NUMBERS", "WON GAMES", "LOST GAMES", "-"*69))
            for player in self.playersList:
                print("| {:<15}  | {:<15}  | {:<15}  | {:<15}  |".format(player.getName(), player.getBet(),
                                                             player.getWonGames(), player.getLostGames()))
        elif self.mode == 2:
            print("TOTAL NUMBER OF PLAYERS: {}".format(len(self.playersList)))
            print("TOTAL NUMBER OF GAMES: {}\n".format(self.gamesNr))
            for game in range(1, self.gamesNr + 1):
                print("GAME NUMBER: {}".format(str(game)))
                print("BET NUMBERS: {}".format(self.resultTracking[game-1][0]))
                print("WIN NUMBER: {}".format(self.resultTracking[game-1][1]))
                print("WINNERS: {}\n".format(self.resultTracking[game-1][2]))
        else:
            raise ValueError("Incorrect mode")

    def playRound(self, gameNr):
        if len(self.playersList) > 0:
            winners = []
            num = random.randint(0, 36)
            self.wonInGame.append([gameNr, num])
            for player in self.playersList:
                if num in player.currentBet:
                    player.addWin(gameNr)
                    winners.append(player.getName())
                else:
                    player.addLose(gameNr)

            self.resultTracking.append([self.getAllBets(), str(num), self.strList(winners)])

    def playGame(self, mode):
        if mode == 1:
            self.createPlayers()
            for game in range(1, self.gamesNr+1):
                self.playRound(game)
            self.printSummary()
        elif mode == 2:
            self.createPlayers()
            for game in range(1, self.gamesNr+1):
                if game == 1:
                    self.playRound(game)
                else:
                    self.clearWindow()
                    print("ROUND: {}".format(str(game)))
                    for player in self.playersList:
                        newBet = self.validateInput(player.getName())
                        player.setBet(newBet)
                    self.playRound(game)
            self.printSummary()

        else:
            raise ValueError("Incorrect mode value")


if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            raise ValueError("Not enough arguments")
        else:
            correct = True
            playersNr = int(sys.argv[1])
            gamesNr = int(sys.argv[2])
            modeNr = int(sys.argv[3])
            if playersNr <= 0:
                raise ValueError("Incorrect number of players")
            if gamesNr <= 0:
                raise ValueError("Incorrect number of games")
            if modeNr < 1 or modeNr > 2:
                raise ValueError("Incorrect mode! It could be only 1 or 2")
            Game(playersNr, gamesNr, modeNr)

    except ValueError:
        print("Enter correct arguments")