from collections import defaultdict
import pyinputplus as pyip


from bank_account_hw.bank_account import Bank


class ATM:
    def __init__(self, bank: Bank):
        self.bank = bank
        self.logged_in = False
        self.current_account = None
        self.menu_options = {"Show balance": self.show_balance,
                             "Deposit cash": self.make_deposit,
                             }

    def login_page(self):
        print(f'Welcome to {self.bank.bank_name}')
        account_valid = False
        password_valid = False
        number_tries = defaultdict(int)

        while not (account_valid and password_valid):
            ac_num = pyip.inputInt("Enter account number: ")
            password = pyip.inputStr("Enter your password: ")

            account_valid = self.bank.check_account_number(ac_num)

            if account_valid:
                current_account = self.bank.accounts[ac_num]
                if current_account.blocked:
                    print(f'{current_account} is blocked')
                    account_valid = False
                    number_tries[ac_num] += 1
                    continue

                password_valid = current_account.check_password(password)
                if password_valid:
                    self.logged_in = True
                    self.current_account = current_account
                    print(f'You are logged in to account {self.current_account}')
                else:
                    number_tries[ac_num] += 1
                    if number_tries[ac_num] >= 3:
                        current_account.blocked = True
                        print(f'{current_account} has been blocked')
                        continue

            if not not account_valid or not password_valid:
                print('Account number or password are invalid')

    def show_option_menu(self):
        if self.logged_in:
            while True:
                choice = pyip.inputMenu(list(self.menu_options), numbered=True)
                self.menu_options[choice]()
        else:
            print('ATM user is not validated')
            self.login_page()

    def show_balance(self):
        print(f'Current Balance on account {self.current_account}')
        print(f'£{self.current_account.get_balance()}')

    def make_deposit(self):
        ...


if __name__ == "__main__":
    my_bank = Bank("Highgate Bank")
    account_1 = my_bank.add_account("qwerty", 1000)
    account_2 = my_bank.add_account("password", 2000)
    my_atm = ATM(my_bank)
    my_atm.login_page()
    my_atm.show_option_menu()
