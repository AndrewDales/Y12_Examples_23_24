import pyinputplus
import pyinputplus as pyip

from bank_account import Bank


class ATM:
    def __init__(self, the_bank):
        self.bank = the_bank
        self.current_user_account = None
        self.current_user_validated = False
        self.menu_choices = {"Show Balance": self.show_balance,
                             "Take cash from account": self.remove_cash,
                             "Deposit cash in account": self.deposit_cash,
                             "Transfer cash to another account": self.transfer_cash,
                             "Exit": self.exit}
        # self.atm_menu()

    def validate_account(self):
        ac_num = 0
        while not ac_num:
            ac_num = pyip.inputInt("Enter account number\n:",
                                   min=10_000,
                                   max=Bank.next_account_number,
                                   limit=3)
            if not self.bank.check_account_number(ac_num):
                print(f'Bank Account with account number {ac_num} not found')
                ac_num = 0
        return self.bank.accounts[ac_num]

    def validate_password(self):
        self.current_user_validated = False
        while not self.current_user_validated:
            current_pass = pyip.inputStr("Enter your password\n:")
            if self.current_user_account.check_password(current_pass):
                self.current_user_validated = True
            else:
                print("Password not correct")

    def show_balance(self):
        print(f"Current Balance on {self.current_user_account}:")
        print(f"£{self.current_user_account.get_balance():.2f}\n")

    def remove_cash(self):
        cash_requested = pyip.inputInt("Enter the amount of cash that your require: ", min=0, max=400)
        if cash_requested > self.current_user_account.get_balance():
            print("You do not have sufficient funds in your account")
        else:
            input(f"Take £{cash_requested:.0f} from the slot")
            self.current_user_account.debit(cash_requested)
        print()
        self.show_balance()

    def deposit_cash(self):
        cash_deposited = pyip.inputInt("Enter the amount of cash that your wish to deposit: ", min=0, max=1000)
        input(f"Put £{cash_deposited:.0f} in the deposit area")

        self.current_user_account.credit(cash_deposited)
        print()
        self.show_balance()

    def transfer_cash(self):
        print("Enter the account that you wish to transfer money to")
        destination = self.validate_account()
        transfer_amount = pyip.inputInt("Enter the amount of money that you wish to transfer: ",
                                        min=1,
                                        max=self.current_user_account.get_balance()
                                        )
        print("Re-enter your password")
        self.validate_password()
        if self.current_user_validated:
            self.bank.transact(self.current_user_account, destination, transfer_amount)
            print(f"You transferred £{transfer_amount:.0f} to {destination}")

    def exit(self):
        self.current_user_account = None
        self.current_user_validated = False
        print("Goodbye\n")
        self.atm_menu()

    def atm_menu(self):
        print(f"Welcome to {self.bank}\n")
        try:
            self.current_user_account = self.validate_account()
        except pyinputplus.RetryLimitException:
            print("Number of tries exceeded")
            return
        self.validate_password()

        if self.current_user_validated:
            while True:
                choice = pyip.inputMenu(list(self.menu_choices), numbered=True)
                self.menu_choices[choice]()

    def login_menu(self):
        print(f"Welcome to {self.bank}\n")

        logged_in = False

        while not logged_in:
            ac_num = pyip.inputInt("Enter account number\n:",
                                   min=10_000,
                                   # max=Bank.next_account_number,
                                   )
            password = pyip.inputStr("Enter your password\n:")

            ac_num_ok = self.bank.check_account_number(ac_num)
            password_ok = False

            if ac_num_ok:
                password_ok = self.bank.accounts[ac_num].check_password(password)
                if password_ok:
                    self.current_user_account = self.bank.accounts[ac_num]
                    self.current_user_validated = True
                    logged_in = True

            if not (ac_num_ok and password_ok):
                print("Error in account number or password")

        self.choice_menu()

    def choice_menu(self):
        if self.current_user_validated:
            while True:
                choice = pyip.inputMenu(list(self.menu_choices), numbered=True)
                self.menu_choices[choice]()
        else:
            print('ATM user is not validated')

if __name__ == "__main__":
    my_bank = Bank("Highgate Bank")
    account_1 = my_bank.add_account("qwerty", 1000)
    account_2 = my_bank.add_account("password", 2000)
    my_atm = ATM(my_bank)
