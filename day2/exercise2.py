#constants for tax rates
STATE_TAX_RATE = 0.05 # 5%
COUNTY_TAX_RATE = 0.025 # 2.5%

#get amount of purchase from the user
purchase=float(input("Enter the amount of a purchase"))

#calculate state sales tax
state_sales_tax = purchase * STATE_TAX_RATE

#calculate county sales tax
county_sales_tax = purchase * COUNTY_TAX_RATE

#calculate total sales tax
total_sales_tax = state_sales_tax + county_sales_tax

#calculate total sales
total_sales= purchase + total_sales_tax

#display the result
print("\n--- sales Tax Breakdown ---")
print(f"purchase: ${purchase}:.2f")
print(f"state sales tax: ${state_sales_tax}:.2f")
print(f"county sales tax: ${county_sales_tax}:.2f")
print(f"Total sales tax: ${total_sales_tax}:.2f")
print(f"Total sales: ${total_sales}:.2f")
