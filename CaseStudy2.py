#Eshaan Vora
#Case Study 2
#Stout: Full Stack Data Analyst

from rich.console import Console
console = Console(record=True)

import os
import matplotlib.pyplot as plt
import pandas as pd

#Load data
filePath = "/Users/eshaan/Downloads/CaseStudy_Stout/casestudy.csv"
#Read CSV into Pandas Dataframe
customerOrders = pd.read_csv(filePath)

baseYear = 2015
previousYear = 2016
currentYear = 2017

#TOTAL REVENUE FOR CURRENT YEAR
totalCurrentRevenue = customerOrders.groupby("year")['net_revenue'].sum()
console.print("Total Revenue Per Year: ")
console.print(totalCurrentRevenue)

#customer list per year
allCustomers2015 = customerOrders.query("year == @baseYear")['customer_email'].tolist()
allCustomers2016 = customerOrders.query("year == @previousYear")['customer_email'].tolist()
allCustomers2017 = customerOrders.query("year == @currentYear")['customer_email'].tolist()

#LIST OF NEW CUSTOMERS
newCustomers2017 = list(set(allCustomers2017) - set(allCustomers2016))
newCustomers2016 = list(set(allCustomers2016) - set(allCustomers2015))

#NEW CUSTOMER REVENUE PER YEAR
newCustomerRevenue2017 = customerOrders.query("(customer_email in @newCustomers2017) and (year == @currentYear)")['net_revenue'].sum()
newCustomerRevenue2016 = customerOrders.query("(customer_email in @newCustomers2016) and (year == @previousYear)")['net_revenue'].sum()
console.print("\n" + "New Customer Revenue in 2017: ")
console.print(newCustomerRevenue2017)
console.print("New Customer Revenue in 2016: ")
console.print(newCustomerRevenue2016)

#EXISTING CUSTOMER REVENUE PER YEAR
existingCustomerRevenue2017 = customerOrders.query("(customer_email in @allCustomers2016) and (year == @currentYear)")['net_revenue'].sum()
console.print("\n" + "Existing Customer Revenue in 2017: ")
console.print(existingCustomerRevenue2017)
existingCustomerRevenue2016 = customerOrders.query("(customer_email in @allCustomers2015) and (year == @previousYear)")['net_revenue'].sum()
console.print("Existing Customer Revenue in 2016: ")
console.print(existingCustomerRevenue2016)
existingCustomerRevenue2015 = customerOrders.query("year == @baseYear")['net_revenue'].sum()
console.print("Existing Customer Revenue in 2015: ")
console.print(existingCustomerRevenue2015)

totalCustomerRevenue2016 = customerOrders.query("year == @previousYear")['net_revenue'].sum()

#EXISTING CUSTOMER GROWTH PER YEAR
existingCustomerGrowth2016 = (existingCustomerRevenue2016 - existingCustomerRevenue2015)
existingCustomerGrowth2017 = (existingCustomerRevenue2017 - totalCustomerRevenue2016)
console.print("\n" + "Existing Customer Growth in 2016: ")
console.print(existingCustomerGrowth2016)
console.print("Existing Customer Growth in 2017: ")
console.print(existingCustomerGrowth2017)

#LIST OF LOST CUSTOMERS PER YEAR
lostCustomers2017 = list(set(allCustomers2016) - set(allCustomers2017))
lostCustomers2016 = list(set(allCustomers2015) - set(allCustomers2016))

#REVENUE LOST FROM ATTRITION PER YEAR
console.print("\n" + "Revenue Lost from Attrition")
lostCustomerRevenue2016 = customerOrders.query("(customer_email in @lostCustomers2016) and (year == @baseYear)")['net_revenue'].sum()
console.print("Customers who did not order in 2016, had spent, in 2015, : ")
console.print(lostCustomerRevenue2016)
lostCustomerRevenue2017 = customerOrders.query("(customer_email in @lostCustomers2017) and (year == @previousYear)")['net_revenue'].sum()
console.print("Customers who did not order in 2017, had spent, in 2016, : ")
console.print(lostCustomerRevenue2017)

#NUMBER OF CUSTOMERS PER YEAR
customerCount2017 = customerOrders.query("year == @currentYear")['customer_email'].count()
console.print("\n" + "Number of Customers in 2017: ")
console.print(customerCount2017)
customerCount2017 = customerOrders.query("year == @previousYear")['customer_email'].count()
console.print("Number of Customers in 2016: ")
console.print(customerCount2017)
customerCount2017 = customerOrders.query("year == @baseYear")['customer_email'].count()
console.print("Number of Customers in 2015: ")
console.print(customerCount2017)

#Write to HTML
console.save_html("CaseStudy2.html")
