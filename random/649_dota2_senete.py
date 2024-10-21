class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senators = [x for x in senate]
        while True:
            for i in range(len(senators)):
                if senators[i] == "D":
                    if "R" not in senators:
                        return "Dire"
                    else:
                        try:
                            next_r = senators.index("R", i + 1)
                            senators[next_r] = "x"
                        except:
                            next_r = senators.index("R")
                            senators[next_r] = "x"
                elif senators[i] == "R":
                    if "D" not in senators:
                        return "Radiant"
                    else:
                        try:
                            next_d = senators.index("D", i + 1)
                            senators[next_d] = "x"
                        except:
                            next_d = senators.index("D")
                            senators[next_d] = "x"
