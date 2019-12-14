import numpy as np


class RLEParser:
    def __init__(self):
        self.parsed = []
        self.input = []
        self.deathrules = []
        self.liverules = []
        self.width = 0
        self.height = 0
        self.complete = False

    def _parsedataline(self, line):
        lines = line.split("$")
        linefound = 0
        for line in lines:
            amt = ""
            t = []
            linefound += 1
            foundthis = 0
            for char in line:
                if char in "bo":
                    if amt == "":
                        amt = "1"
                    amountof = int(amt)
                    t += [char == "o"] * amountof
                    foundthis += amountof
                    amt = ""
                elif char == "!":
                    pass
                elif char in "0123456789":
                    amt += char
                else:
                    pass
            t += [False] * (self.width - foundthis)
            self.parsed.append(t)
        blankd = [False] * self.width
        self.parsed += [blankd] * (self.height - linefound)

    def _parseheader(self, line):
        things = line.split(",")
        for thing in things:
            thing = thing.strip()
            thing = thing.split("=")
            thing = [u.strip() for u in thing if u.strip() != ""]
            if thing[0] == "x":
                self.width = int(thing[1])
            elif thing[0] == "y":
                self.height = int(thing[1])
            elif thing[0] == "rule":
                rules = thing[1].split("/")
                for rule in rules:
                    rule = list(rule)
                    selectn = rule.pop(0)
                    if selectn.lower() == "b":
                        self.liverules = rule
                    else:
                        self.deathrules = rule



    def parse(self, inp):
        self.input = inp.strip().split("!")[0].split("\n")
        hasmet = False
        for line in self.input:
            if line.strip()[0] == "#":
                continue
            else:
                if hasmet:
                    self._parsedataline(line)
                else:
                    hasmet = True
                    self._parseheader(line)
        self.completed = True

        return np.array(self.parsed).astype(int)

    def reset(self):
        self.parsed = []
        self.input = []
        self.deathrules = []
        self.liverules = []
        self.width = 0
        self.height = 0
        self.complete = False


def main():
    data = open("Patterns/block.rle").read()
    parser = RLEParser()
    pattern = parser.parse(data)
    pattern = np.pad(pattern, pad_width=1, mode='constant')
    print(pattern)



if __name__ == "__main__":
    main()