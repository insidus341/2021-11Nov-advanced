class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor

    def __repr__(self):
        return f'Scoop of {self.flavor}'


class Bowl:
    MAX_SCOOPS = 3   # class attribute MAX_SCOOPS

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *args):
        for one_scoop in args:
            if len(self.scoops) >= self.MAX_SCOOPS:
                break
            self.scoops.append(one_scoop)

    def flavors(self):
        return [one_scoop.flavor
                for one_scoop in self.scoops]

        # output = []
        # for one_scoop in self.scoops:
        #     output.append(one_scoop.flavor)
        # return output

    def __repr__(self):
        output = 'Bowl of: '
        return output


class BigBowl(Bowl):
    MAX_SCOOPS = 5


# bb.__init__() # does bb have __init__? No.  Does BigBowl have __init__? No.  Does Bowl have __init__? Yes.
