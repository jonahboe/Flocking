import copy
import operator


BORDA = "borda"
PLURALITY = "plurality"
VETO = "veto"


# Voting main class
class Voting:
    def borda(self, agents):
        rankings = dict()
        if len(agents[0].votes) == 0:
            return None
        for agent in agents:
            points = len(agent.votes)
            for vote in agent.votes:
                rankings[vote] = rankings.get(vote, 0) + points
                points -= 1
        rankings = dict(sorted(rankings.items(), key=operator.itemgetter(1), reverse=True))
        places = list(rankings.values())
        ranks = list(rankings.keys())
        if len(ranks) == 0:
            return None
        if len(ranks) == 1:
            return None
        if places[0] == places[1]:
            if len(ranks) <= 2:
                return None
            for agent in agents:
                if ranks[-1] in agent.votes:
                    agent.votes.remove(ranks[-1])
                else:
                    agent.votes.remove(agent.votes[-1])
            return self.borda(agents)
        else:
            return ranks[0]

    def plurality(self, agents):
        rankings = dict()
        if len(agents[0].votes) == 0:
            return None
        for vote in agents[0].votes:
            rankings[vote] = 0
        for agent in agents:
            rankings[agent.votes[0]] = rankings.get(agent.votes[0], 0) + 1
        rankings = dict(sorted(rankings.items(), key=operator.itemgetter(1), reverse=True))
        places = list(rankings.values())
        ranks = list(rankings.keys())
        if len(ranks) == 0:
            return None
        if len(ranks) == 1:
            return None
        if places[0] == places[1]:
            if len(ranks) <= 2:
                return ranks[0]
            for agent in agents:
                if ranks[-1] in agent.votes:
                    agent.votes.remove(ranks[-1])
            return self.plurality(agents)
        else:
            return ranks[0]

    def veto(self, agents):
        rankings = dict()
        if len(agents[0].votes) == 0:
            return None
        for vote in agents[0].votes:
            rankings[vote] = 0
        for agent in agents:
            rankings[agent.votes[-1]] = rankings.get(agent.votes[-1], 0) + 1
        rankings = dict(sorted(rankings.items(), key=operator.itemgetter(1)))
        places = list(rankings.values())
        ranks = list(rankings.keys())
        if len(ranks) == 0:
            return None
        if len(ranks) == 1:
            return None
        if places[0] == places[1]:
            if len(ranks) <= 2:
                return ranks[0]
            for agent in agents:
                if ranks[-1] in agent.votes:
                    agent.votes.remove(ranks[-1])
            return self.veto(agents)
        else:
            return ranks[0]


class ag:
    def __init__(self, id, votes, x, y):
        self.id = id
        self.votes = votes
        self.x = x
        self.y = y


if __name__ == '__main__':
    agents = [ag(id=1, votes=[2, 3, 5, 4]),
              ag(id=2, votes=[5, 4, 3, 1]),
              ag(id=3, votes=[5, 4, 1, 2]),
              ag(id=4, votes=[3, 2, 5, 1]),
              ag(id=5, votes=[2, 3, 1, 4])]
    voting = Voting()
    print("Borda winner: " + str(voting.borda(copy.deepcopy(agents))) + "\n")
    print("Plurality winner: " + str(voting.plurality(copy.deepcopy(agents))) + "\n")
    print("Veto winner: " + str(voting.veto(copy.deepcopy(agents))) + "\n")
