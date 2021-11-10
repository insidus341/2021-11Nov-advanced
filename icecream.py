class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl:
    def __init__(self):
        self.scoops = []

    def add_scoops(self, *args):
        for one_scoop in args:
            self.scoops.append(one_scoop)

    def flavors(self):
        output = []
        for one_scoop in self.scoops:
            output.append(one_scoop.flavor)
        return output
