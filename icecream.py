class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl:
    MAX_SCOOPS = 3

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *args):
        for one_scoop in args:
            if len(self.scoops) >= MAX_SCOOPS:
                break
            self.scoops.append(one_scoop)

    def flavors(self):
        output = []
        for one_scoop in self.scoops:
            output.append(one_scoop.flavor)
        return output
