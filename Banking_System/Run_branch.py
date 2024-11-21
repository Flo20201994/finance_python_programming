from L12_BANK_BRANCH import Branch, Bank

####### BRANCH #######

# test_branch = Branch(1, 10000000, 0.10)

### Initial Methods ###
### Initial Branch, 10m Capital, 10% Reserve Rate
# print(test_branch)
# print(test_branch.check_branch_accounts())

### Create and Check Account ###
## Initial Cash Balance of 10k
# test_branch.create_account(10000)
# print(test_branch.check_account(1))
# print(test_branch.check_account(47))


### Deposit and Withdraw ###
## Initial Cash Balance of 10k
# test_branch.create_account(10000)
# test_branch.deposit(1,15000)
# test_branch.withdraw(1, 1000)
# print(test_branch.check_account(1))
# ### Attempt to withdraw 10m
# print(test_branch.withdraw(1, 10000000))

### Loans ### 
# test_branch.create_account(10000)

# ### 36 months 100k loan for an Rurual resident. 
# print(test_branch.consumer_credit_model(1, 36, 2, 100000))
# ### 72 months 400k loan for an Urban resident. 
# print(test_branch.consumer_credit_model(1, 72, 1, 400000))
# print(test_branch.check_account(1))

# print(test_branch.payoff_account_loan(1))
# print(test_branch.check_account(1))

####### BANK #######

### Initial ####
# zions = Bank("ZIONS",2023, 10000000)
# print(zions)

### Branch Related Work ###
### FIRST
# zions.open_branch()
# print(zions.branch_database[1].check_branch_accounts())
# zions.branch_database[1].create_account(100000)
# print(zions.branch_database[1].deposit(1,4000))
# print(zions.branch_database[1].withdraw(1,1000))
# ### SECOND
# zions.branch_database[1].consumer_credit_model(1,60, 2, 10000)
# print(zions.branch_database[1].check_branch_accounts())
# zions.branch_database[1].payoff_account_loan(1)
# print(zions.branch_database[1].check_branch_accounts())

### Balance Sheet Aggregation
# print(zions)
# zions.open_branch()

# for i in range(1,5):
#     zions.branch_database[1].create_account(100000)
#     print(zions.branch_database[1].deposit(i,4000))
#     print(zions.branch_database[1].withdraw(i,1000))

# zions.balance_sheet_aggregation()

# print(zions)
