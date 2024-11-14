import warnings
import sys

warnings.filterwarnings('ignore')
# prevents pycache
sys.dont_write_bytecode = True

class Database:
    def __init__(self, branch_id, total_reserves, reserve_rate):

        self.__assets = {'TOTAL_RESERVES':round(float(total_reserves),2),
                         'REQUIRED_RESERVES':round(total_reserves * reserve_rate,2),
                         'EXCESS_RESERVES':round(total_reserves * (1 - reserve_rate),2),
                         'LOAN_BALANCE': 0.0}
        self.__liabilities = {'CHECKED_DEPOSITS': 0.0,
                               ### Is meant to equal owners equity.                                             
                              'OWNERS_EQUITY':float(total_reserves),}
        ### Initially empty.
        ### ID, $ Balance, Loan Count, Current Principal, Current Interest
        #{ account_id: {'BALANCE':0,'LOAN_COUNT':0,'CURRENT_PRINCIPAL':0,'CURRENT_INTEREST':0}}
        self.__accounts = {}

        self.__database = {'BRANCH': branch_id,
                           'BALANCE_SHEET': {'ASSETS':self.__assets,
                                             'LIABILITIES': self.__liabilities},
                           'ACCOUNTS':self.__accounts}
        
        self.reserve_rate = reserve_rate

### RUN CLASS    
    def __str__(self):
        branch_id = self.__database['BRANCH']
        assets = self.__database['BALANCE_SHEET']['ASSETS']
        liabilities = self.__database['BALANCE_SHEET']['LIABILITIES']
        accounts = self.__database['ACCOUNTS']

        output = f'''
BRANCH ID: {branch_id}
ACCOUNTS: {len(accounts)}
BALANCE SHEET:
    ASSETS - {round(assets['TOTAL_RESERVES'] + assets['LOAN_BALANCE'],2):,.0f}: 
        - TOTAL RESERVES: {assets['TOTAL_RESERVES']:,.0f}
            - REQUIRED: {assets['REQUIRED_RESERVES']:,.0f}
            - EXCESS: {assets['EXCESS_RESERVES']:,.0f}
            - LOANS RECEIVABLE: {assets['LOAN_BALANCE']:,.0f}
    LIABILITES - {round(liabilities['CHECKED_DEPOSITS'] + liabilities['OWNERS_EQUITY'],2):,.0f}: 
        - CHECKED_DEPOSITS: {liabilities['CHECKED_DEPOSITS']:,.0f}
        - OWNERS EQUITY: {liabilities['OWNERS_EQUITY']:,.0f}
        '''
        return output
    
# ### RUN CLASS
    def update_reserves(self, credit, dollar_value):
        
        initial_required_reserves = self.__database['BALANCE_SHEET']['ASSETS']['REQUIRED_RESERVES']
        initial_excess_reserves = self.__database['BALANCE_SHEET']['ASSETS']['EXCESS_RESERVES']
        initial_total_reserves = self.__database['BALANCE_SHEET']['ASSETS']['TOTAL_RESERVES']

        ### Credit is decrease
        if credit:
            new_total_reserves = initial_total_reserves - dollar_value
            new_excess_reserves = new_total_reserves - (new_total_reserves * self.reserve_rate)
            new_required_reserves = new_total_reserves - new_excess_reserves

            self.__database['BALANCE_SHEET']['ASSETS']['REQUIRED_RESERVES'] = new_required_reserves
            self.__database['BALANCE_SHEET']['ASSETS']['EXCESS_RESERVES'] = new_excess_reserves
            self.__database['BALANCE_SHEET']['ASSETS']['TOTAL_RESERVES'] = round(new_required_reserves + new_excess_reserves,2)
        else:
            new_required_reserves = (dollar_value * self.reserve_rate) + initial_required_reserves
            new_excess_reserves = ((1-self.reserve_rate) * dollar_value) + initial_excess_reserves
            
            self.__database['BALANCE_SHEET']['ASSETS']['REQUIRED_RESERVES'] = new_required_reserves
            self.__database['BALANCE_SHEET']['ASSETS']['EXCESS_RESERVES'] = new_excess_reserves
            self.__database['BALANCE_SHEET']['ASSETS']['TOTAL_RESERVES'] = round(new_required_reserves + new_excess_reserves,2)

# ### RUN CLASS
    def update_deposits(self, credit, dollar_value):
 
        initial_balance = self.__database['BALANCE_SHEET']['LIABILITIES']['CHECKED_DEPOSITS']
        if credit:
            new_balance = initial_balance + dollar_value 
        else:
            new_balance = initial_balance - dollar_value

        self.__database['BALANCE_SHEET']['LIABILITIES']['CHECKED_DEPOSITS'] = new_balance

# ### RUN CLASS
    def update_loans(self, payoff, principal, interest):
        ### Excess Reserves decrease, Loan value increases, interest paid is owners equity...
        ### Interest is in whole dollars over the whole lifetime of the loan. 

        initial_total_reserves = self.__database['BALANCE_SHEET']['ASSETS']['TOTAL_RESERVES']
        initial_required_reserves = self.__database['BALANCE_SHEET']['ASSETS']['REQUIRED_RESERVES']
        initial_excess_reserves = self.__database['BALANCE_SHEET']['ASSETS']['EXCESS_RESERVES']
        initial_loan_receivables = self.__database['BALANCE_SHEET']['ASSETS']['LOAN_BALANCE']
        initial_owners_equity = self.__database['BALANCE_SHEET']['LIABILITIES']['OWNERS_EQUITY']

        if payoff:
            
            new_total_reserves = round(initial_total_reserves + principal + interest, 2)
            new_excess_reserves = round(initial_excess_reserves + principal + interest, 2)
            ### We recognize interest revenue here
            new_owners_equity = initial_owners_equity + interest

            self.__database['BALANCE_SHEET']['ASSETS']['EXCESS_RESERVES'] = new_excess_reserves
            self.__database['BALANCE_SHEET']['ASSETS']['TOTAL_RESERVES'] = new_total_reserves
            self.__database['BALANCE_SHEET']['LIABILITIES']['OWNERS_EQUITY'] = new_owners_equity
            self.__database['BALANCE_SHEET']['ASSETS']['LOAN_BALANCE'] = 0
            
        else:
            ### We are issuing a loan
            new_total_reserves = initial_total_reserves - principal
            new_excess_reserves = initial_excess_reserves - principal
            new_loan_balance = initial_loan_receivables + principal

            self.__database['BALANCE_SHEET']['ASSETS']['EXCESS_RESERVES'] = new_excess_reserves
            self.__database['BALANCE_SHEET']['ASSETS']['TOTAL_RESERVES'] = new_total_reserves
            self.__database['BALANCE_SHEET']['ASSETS']['LOAN_BALANCE'] = new_loan_balance

            ### WE ARE NOT ACCOUNTING FOR INTEREST RECEIVABLE, WE RECOGNIZE IT UPON PAYMENT. 
### RUN CLASS

    def create_account(self, account_id, initial_balance):
        self.__database['ACCOUNTS'][account_id] = {'BALANCE':initial_balance,
                                                   'LOAN_COUNT':0,
                                                   'CURRENT_PRINCIPAL':0,
                                                   'CURRENT_INTEREST':0}            
    def check_account(self, account_id):
        # accounts_table = self.__database['ACCOUNTS']
        # if len(accounts_table[accounts_table.ACCOUNT_ID==account_id])==0:
        if account_id not in self.__database['ACCOUNTS']:                
            return "Account Does Not Exist."
        else:
            # return accounts_table[accounts_table.ACCOUNT_ID==account_id].copy()  
            return self.__database['ACCOUNTS'][account_id]

    def check_account_checking_balance(self, account_id):
        if account_id not in self.__database['ACCOUNTS']:        
            return "Account Does Not Exist."
        else:
            return self.__database['ACCOUNTS'][account_id]['BALANCE']
### RUN CLASS

    def update_account(self, account_id, dollar_value, credit):
        if account_id not in self.__database['ACCOUNTS']:             
            return "Account Does Not Exist."           
        else:
           account_balance = self.__database['ACCOUNTS'][account_id]['BALANCE']

           if credit:
               ## Decrease Account
               new_account_balance = account_balance - dollar_value
               self.__database['ACCOUNTS'][account_id]['BALANCE'] = new_account_balance
               return new_account_balance
           else:
                ## Increase account 
                new_account_balance = account_balance + dollar_value          
                self.__database['ACCOUNTS'][account_id]['BALANCE'] = new_account_balance
                return new_account_balance 
### RUN CLASS           
    ### We set initial None values here to make the input optional for payoff activity. 
    def update_account_loans(self, account_id, principal=None, interest=None, payoff=False):
        ### Loans can only be approved, we assume everyone doesn't default. (haha)
        if account_id not in self.__database['ACCOUNTS']:                        
            return "Account Does Not Exist."            
        else:
            if payoff:
                self.__database['ACCOUNTS'][account_id]['LOAN_COUNT'] = 0                
                self.__database['ACCOUNTS'][account_id]['CURRENT_PRINCIPAL'] = 0
                self.__database['ACCOUNTS'][account_id]['CURRENT_INTEREST'] = 0
            else:
                self.__database['ACCOUNTS'][account_id]['LOAN_COUNT'] = 1          
                self.__database['ACCOUNTS'][account_id]['CURRENT_PRINCIPAL'] = principal
                self.__database['ACCOUNTS'][account_id]['CURRENT_INTEREST'] = interest
# ### RUN CLASS        
    def data_output(self):    
        return self.__database
