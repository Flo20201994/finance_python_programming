import pandas as pd
from dataclasses import dataclass

class Portfolio:
    def __init__(self, year_established:int, capital: int):
        self.year_established = year_established
        ### Capital deployed to begin business operations
        self.capital = capital
        ### This is an ID counter for property objects, ID begins at 1
        self.property_counter = 1
        ### This is our initial state of the database
        self.property_database = {}

        self.model_lifetime = '2070'

        self.portfolio_operations_df = None
        self.portfolio_debt_df = None

    def purchase_property(self, property_attributes: list):

        for attributes in property_attributes:
            ### DECISION: EACH NEW PROPERTY IS PROVIDED 10% OF CAPITAL
            startup_capital = 0.1 * self.capital 
            if startup_capital > self.capital:
                ## Cannot Purchase Property
                return None
            else:
                self.capital -= startup_capital
                down_payment_percentage = (startup_capital/attributes['PROPERTY_VALUE']) * 100

                key = 'PROPERTY_' + str(self.property_counter)
       
                self.property_database[key] = ResidentialProperty(attributes['PROPERTY_VALUE'],attributes['REGULAR_UNITS'],
                                                                  attributes['LUXARY_UNITS'],attributes['LOAN_YEARS'],
                                                                  attributes['INTEREST_RATE'],down_payment_percentage,
                                                                  attributes['ESCALATION'],attributes['DATE_OF_PURCHASE'])    
                self.property_counter += 1
     
    def query_property(self, property_key: str):

        return self.property_database[property_key]

    def aggregate_property_data(self):
        
        ### Values reset upon every run of the method. 
        self.portfolio_operations_df = pd.DataFrame(columns=['REVENUE','EXPENSE','NET_INCOME','TOTAL_SQFT','TOTAL_UNITS'],
                                                    index=pd.date_range(str(self.year_established),self.model_lifetime, freq='M',))
        
        self.portfolio_operations_df.fillna(0,inplace=True)

        ### Values reset upon every run of the method. 
        self.portfolio_debt_df = pd.DataFrame(columns=['BEGINNING_BALANCE','PAYMENT','INTEREST_PAID',
                                                       'PRINCIPAL_PAID','ENDING_BALANCE','EQUITY'],
                                              index=pd.date_range(str(self.year_established),self.model_lifetime, freq='M',))
        
        self.portfolio_debt_df.fillna(0,inplace=True)
        
        ### Loop over all ResidentialProperties
        for property in self.property_database.values():
            ## Loop over column count to update all target operations categories. 
            # for column_idx, column_name in enumerate(self.portfolio_operations_df.columns):
            for column_idx in range(len(self.portfolio_operations_df.columns)):
            
                self.portfolio_operations_df.iloc[:,column_idx] = pd.concat([self.portfolio_operations_df.iloc[:,column_idx],
                                                                              property.operations_report_df.iloc[:,column_idx]], 
                                                                              axis=1).fillna(0).sum(axis=1)
            # ### Loop over all ResidentialProperties
            for column_idx in range(len(self.portfolio_debt_df.columns)):
            #     ## Loop over column count to update all target operations categories. 
                self.portfolio_debt_df.iloc[:,column_idx] = pd.concat([self.portfolio_debt_df.iloc[:,column_idx],
                                                                             property.loan_df.iloc[:,column_idx]], 
                                                                             axis=1).fillna(0).sum(axis=1)
