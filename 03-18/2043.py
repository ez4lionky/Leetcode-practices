class Bank:

    def __init__(self, balance: List[int]):
        self.balances = balance
        self.n = len(balance)


    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if 0<account1<=self.n and 0<account2<=self.n:
            if self.balances[account1-1] >= money:
                self.balances[account1-1] -= money
                self.balances[account2-1] += money
                return True
        return False


    def deposit(self, account: int, money: int) -> bool:
        if 0<account<=self.n:
            self.balances[account-1] += money
            return True
        return False


    def withdraw(self, account: int, money: int) -> bool:
        if 0<account<=self.n:
            if self.balances[account-1] >= money:
                self.balances[account-1] -= money
                return True
        return False



