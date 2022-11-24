"""
How much would it cost for 5 people if each person needs:
A pack of tomatoes
3 washing sponges
A litre of juice
20m of foil
180g sugar
Assign the value to total
Provide your answer as a printed variable called total.
These prices do not include VAT. Calculate the VAT on the total, assuming that VAT is 20%.
Then round it appropriately to two decimal places.
"""
#%%
tomatoes=1
washing_sponges=3
juice=1
foil=20
sugar=180
total= tomatoes+washing_sponges+juice+foil+sugar
total=5*total
print(f'The total is {total}')
print(f'The VAT on total is {(round(total*0.2,2))}' )
# %%
207*5

# %%

"""
Assign variables for each of these items and their prices
Tomatoes cost 87p for a pack of 6
500g sugar costs £1.09
Washing sponges cost 29p for a pack of 10
Juice is £1.89 per 1.5l bottle
Foil is £1.29 per 30m roll
Using arithmetic operations in Python, calculate the price of 1kg sugar
What is the price of 20 washing sponges, 3l of juice, and 2 packs of tomatoes?
"""
Sugar_price=2*109
print(Sugar_price/100)
Total_cost=(29*2)+(189*2)+((87/6)*2)
print(Total_cost/100)
# %%
