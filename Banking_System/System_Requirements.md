# Banking

### Scenario
We are a new bank attempting to take over west coast territory. Multiple players in the Western United States failed during the regional bank crisis of 2023. With these failures there is opportunity to seize market share. We have secured startup capital to begin operations and we will be opening multiple branches as soon as possible. Operations are on hold until we have an adequate accounting system for our organization.

### Goal
Develop a system that manages the accounting activities related to a bank and its branches. 

## Requirements

#### Bank

* Manage high level data related to the bank
    * Capital value
    * Reserve Capital Injection Rate
        * Capital provided to new branches. 
    * Branch Database
    * Year Established
    * Corporation Name

* Open Branch
    * Ability to open one or more branches.
    * Branches are injected with a certain amount of capital as startup cash to begin operations. 

* Balance Sheet Aggregation
    * Aggregate all branch data into a Bank level picture. 

#### Branch

* Handle unique instance data of a subsidary Bank branch. 
    * Can be a stand alone "branch", but will contextually be housed within a Bank instance. 

* Create, Read, and Update Accounts
    * Capability should cover both deposits and loans. 

* Deposit Business Line
    * Simply, accounts are based on deposits of cash. We do not offer interest gains on cash held in accounts.     

* Loan Business Line
    * Allow for credit risk modeling to be leveraged upon accounts requesting loan products.
        * Modeling requires Principal, Annualized Terms, APR, and Monthly Payment variables. 
    * Allow the branch to offer/reject loans as well as close out balances of offered loans. 
        * Consumers are offered three rate levels based on probability of default. 
            * Default probability greater than zero and less than 25%, offered rate is 5%.
            * Default probability greater than 25% and less than 50%, offered rate is 15%.
            * Default probability greater than 25% and less than 75%, offered rate is 30%.
            * Higher than 75% default probability is automatically rejected. 

    * Requires a payment calculator with inputs of rate, annualized term, and principal amount. 

#### Database

* Manage a balance sheet of a Branch. 
    * Including Total/Required/Excess Reserves, and Loan Balances
    * Checked Deposits and Owners Equity

* Track current reserve rate assigned by the Federal Reserve

* Update deposits, reserves, and loans accounts. 
    * All balance sheet alterations must recognize increase and decrease of accounts, i.e. credits and debits. 

* Create, Read, and Update Individual Accounts
    * Encompassing deposits and loans. 

## Class Functionality

#### Bank Class

* Initialization Method
    * Setup method for instance variables.
* Open Branch
    * Opens a new branch related to the bank instance. 
* Balance Sheet Aggregation
    * Aggregates balance sheet values at the bank level. 
* Representation String
    * Outputs all values related to aggregate bank balance sheet. 

#### Branch Class

* Initialization Method
    * Setup method for instance variables.
* Check Branch Accounts
    * Gathers instance of database of a branch.
* Create Account
    * Creates an account at the branch.
* Deposit
    * Deposits cash into a target account.
* Withdraw
    * Withdraw cash from a target account.
* Check Account
    * Gather data related to a target account.
* Payment
    * Payment value related to a potential loan.
* Consumer Credit Model
    * Handles all work related to providing loans to an account.
* Payoff Account Loan
    * Handles all work related to closing out the balance of a loan. 
* Representation String
    * Provides a Branch ID value. 

#### Database Class
--- Technially this is a balance sheet "database"

* Initialization Method
    * Setup method for instance variables.
* Update Reserves
    * Updates balance sheet reserve values. 
* Update Deposits
    * Updates balance sheet deposit values. 
* Update Loans
    * Updates balance sheet loan values. 
* Create Account
    * Creates new accounts at a given branch. 
* Check Account
    * Gathers data of a particular account. 
* Check Account Checking Balance
    * Gathers only a checking balance of a given account.
* Update Account
    * Updates account values related to deposits. 
* Update Account Loans
    * Updates account balances related to loans. 
* Data Output:
    * Returns instance of database. 
* String Representation
    * String output for a given branch.
