from L11_DATABASE import Database


### ID 47
### Initial Capital 10m
### Reserve Rate 10%
database = Database(47, 10000000,0.1)

######## System output only, nothing really occurs. ########
# print(database)

######## After we add __str__ ########

# print(database)

######## Update Reserves Exists ########

# ### Credit -- decrease -- by 10000
# database.update_reserves(True, 10000)
# print(database)

# ### Debit -- increase -- by 10000
# database.update_reserves(False, 10000)
# print(database)

######## Update Deposits ########

# ## Credit -- Increase -- by 10000
# database.update_deposits(True, 10000)
# print(database)

# ## Credit -- Increase -- by 10000
# database.update_deposits(False, 10000)
# print(database)

######## Update Loans ########

# # ## Open -- 10000, 500, (10k @ 5% for 1 year)
# database.update_loans(False, 10000, 500,)
# print(database)

# # ## Close -- 10000, 500, (10k @ 5% for 1 year)
# database.update_loans(True, 10000, 500,)
# print(database)

######## Create and Check Account ########

# database.create_account(1, 10000)
# print(database.check_account(1))
# print(database.check_account(47))
# print(database.check_account_checking_balance(1))

######## Update Account ########

# database.create_account(1, 10000)
# print(database.check_account(1))
# ### Credit - Increase - 10000
# database.update_account(1, 10000, False)
# print(database.check_account(1))
# ### Debit - Decrease - 1000
# database.update_account(1, 1000, True)
# print(database.check_account(1))

######## Update Account ########
# database.create_account(1, 10000)
# print(database.check_account(1))
# # # ## Open -- 10000, 500, (10k @ 5% for 1 year)
# database.update_account_loans(1, 10000, 500, False)
# print(database.check_account(1))
# # # ## Open -- 10000, 500, (10k @ 5% for 1 year)
# database.update_account_loans(1, 10000, 500, True)
# print(database.check_account(1))


######## Display Balance Sheet ########

# database = Database(47, 10000000,0.1)
# database.create_account(1, 10000)
# # ### Credit - Increase - 10000
# database.update_account(1, 10000, False)
# ## Update Balance Sheet
# database.update_deposits(True, 10000)
# database.update_account(1, 10000, False)
# ## Update Balance Sheet
# database.update_deposits(True, 10000)


# # # # ## Open -- 10000, 500, (10k @ 5% for 1 year)
# database.update_account_loans(1, 10000, 500, False)
# # # ## Open -- 10000, 500, (10k @ 5% for 1 year)
# database.update_loans(False, 10000, 500,)
# print(database)

# # # # ## Open -- 10000, 500, (10k @ 5% for 1 year)
# database.update_account_loans(1, 10000, 500, True)
# # # ## Close -- 10000, 500, (10k @ 5% for 1 year)
# database.update_loans(True, 10000, 500,)

# print(database)
