class Category:
    def __init__(self, name: str):
        self.name = name
        self.ledger = []
        self.balance = 0.00
        self.totalSpend = 0.00

    def deposit(self, amount: float, description: str = ""):
        self.ledger.append({'amount': amount, 'description': description})
        self.balance = self.balance + amount

    def withdraw(self, amount: float, description: str = ""):
        if amount > self.balance:
            return False
        else:
            self.ledger.append({'amount': -amount, 'description': description})
            self.balance = self.balance - amount
            self.totalSpend = (self.totalSpend + amount).__round__(2)
            return True

    def get_balance(self):
        return self.balance

    def get_total_spend(self):
        return self.totalSpend

    def transfer(self, amount: float, destination):
        if amount > self.balance:
            return False
        else:
            self.withdraw(amount, 'Transfer to ' + destination.name)
            destination.deposit(amount, 'Transfer from ' + self.name)
            return True

    def check_funds(self, amount: float):
        if amount > self.balance:
            return False
        else:
            return True

    def __str__(self):
        title = self.name.center(30, "*") + '\n'
        ledgerItems = ''
        for ledgerItem in self.ledger:
            ledgerTitle = (ledgerItem['description'][0:23]).ljust(23, ' ')
            ledgerAmount = "{:.2f}".format(ledgerItem['amount']).rjust(7, " ")
            ledgerLineItem = ledgerTitle + ledgerAmount + '\n'
            ledgerItems = ledgerItems + ledgerLineItem
        total = 'Total: ' + str(self.balance)

        return title + ledgerItems + total


def create_spend_chart(categories):
    totalSpend = 0.00
    percentages = []
    catNameLens = []

    for category in categories:
        totalSpend = totalSpend + category.get_total_spend()

    for category in categories:
        percentage = int(((category.get_total_spend() / totalSpend) * 100).__round__(0))
        percentages.append({'category': category.name, 'percentage': percentage})
        catNameLens.append(len(category.name))

    maxCatNameLen = max(catNameLens)
    graph = ''
    percentageTest = 100
    while percentageTest >= 0:
        graph = graph + str(percentageTest).rjust(3, ' ') + '| '
        for percentage in percentages:
            if percentage['percentage'] >= percentageTest:
                graph = graph + 'o  '
            else:
                graph = graph + '   '
        graph = graph + '\n'
        percentageTest = percentageTest - 10
    graph = graph + '    ' + ('---' * len(categories)) + '-\n     '

    justifiedCatNames = []

    for category in categories:
        justifiedCatNames.append(category.name.ljust(maxCatNameLen, ' '))

    for index in range(0, maxCatNameLen - 1):
        for justName in justifiedCatNames:
            graph = graph + justName[index] + '  '
        graph = graph + '\n     '

    for justName in justifiedCatNames:
        graph = graph + justName[maxCatNameLen - 1] + '  '

    graph = 'Percentage spent by category\n' + graph

    return graph
