import copy
import operator


# Voting main class
class Voting:
    def process(self, agents):
        results = None;


# Algorythm for Borda voting
class Borda(Voting):
    def process(self, agents):
        Voting.process(self, agents)
        rankings = dict()
        for agent in agents:
            points = len(agent.votes)
            for vote in agent.votes:
                rankings[vote] = rankings.get(vote, 0) + points
                points -= 1
        rankings = dict(sorted(rankings.items(), key=operator.itemgetter(1), reverse=True))
        print("Rankings: " + str(rankings))
        places = list(rankings.values())
        ranks = list(rankings.keys())
        if places[0] == places[1]:
            for agent in agents:
                if ranks[-1] in agent.votes:
                    agent.votes.remove(ranks[-1])
                else:
                    agent.votes.remove(agent.votes[-1])
                print(agent.votes)
            return self.process(agents)
        else:
            return ranks[0]


# Algorythm for Plurality with Elimination voting
class Plurality:
    def process(self, agents):
        Voting.process(self, agents)
        rankings = dict()
        for vote in agents[0].votes:
            rankings[vote] = 0
        for agent in agents:
            rankings[agent.votes[0]] = rankings.get(agent.votes[0], 0) + 1
        rankings = dict(sorted(rankings.items(), key=operator.itemgetter(1), reverse=True))
        print("Rankings: " + str(rankings))
        places = list(rankings.values())
        ranks = list(rankings.keys())
        if places[0] == places[1]:
            for agent in agents:
                if ranks[-1] in agent.votes:
                    agent.votes.remove(ranks[-1])
                print(agent.votes)
            return self.process(agents)
        else:
            return ranks[0]


# Algorythm for Veto with Elimination voting
class Veto:
    def process(self, agents):
        Voting.process(self, agents)
        rankings = dict()
        for vote in agents[0].votes:
            rankings[vote] = 0
        for agent in agents:
            rankings[agent.votes[-1]] = rankings.get(agent.votes[-1], 0) + 1
        rankings = dict(sorted(rankings.items(), key=operator.itemgetter(1)))
        print("Rankings: " + str(rankings))
        places = list(rankings.values())
        ranks = list(rankings.keys())
        if places[0] == places[1]:
            for agent in agents:
                if ranks[-1] in agent.votes:
                    agent.votes.remove(ranks[-1])
                print(agent.votes)
            return self.process(agents)
        else:
            return ranks[0]


class ag:
    def __init__(self, id, votes):
        self.id = id
        self.votes = votes


if __name__ == '__main__':
    agents = [ag(id=1, votes=[2, 3, 5, 4]),
              ag(id=2, votes=[5, 4, 3, 1]),
              ag(id=3, votes=[5, 4, 1, 2]),
              ag(id=4, votes=[3, 2, 5, 1]),
              ag(id=5, votes=[2, 3, 1, 4])]
    voting = Borda()
    print("Borda winner: " + str(voting.process(copy.deepcopy(agents))) + "\n")

    voting = Plurality()
    print("Plurality winner: " + str(voting.process(copy.deepcopy(agents))) + "\n")

    voting = Veto()
    print("Veto winner: " + str(voting.process(copy.deepcopy(agents))) + "\n")
