
class Gumball:

    gumball_machine = {}
    wasted_gumball_cost = 0

    def __init__(self, ref):
        self.refills = ref

    def daily_sales(self):
        for machine in self.gumball_machine:
            self.gumball_machine[machine] -= 10
            if self.gumball_machine[machine] < 0:
                _ = self.replace_gumballs()

    def replace_gumballs(self):
        min_gumballs = 1001
        min_gumball_key = ""

        for key, gumballs in self.gumball_machine.items():
            if gumballs < min_gumballs:
                min_gumballs = gumballs
                min_gumball_key = key
        return self.gumball_machine.pop(min_gumball_key)

    def wasted_gumballs(self):
        for refill in refills:
            if refill not in self.gumball_machine.keys():
                if len(self.gumball_machine.keys()) == 3:
                    self.wasted_gumball_cost += self.replace_gumballs()
                self.gumball_machine[refill] = 1000
            else:
                self.gumball_machine[refill] = 1000

            self.daily_sales()

        return self.wasted_gumball_cost/100


if __name__ == '__main__':
    num_refills = 5
    refills_string = "red green blue red white"
    refills = refills_string.split()
    gumball_obj = Gumball(refills)
    print("${:.2f}".format(gumball_obj.wasted_gumballs()))
