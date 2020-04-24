cents = int(input("Please insert amount of money in cents: "))
toonies = 0
loonies = 0
quarters = 0
dimes = 0
nickles = 0
pennies = 0

toonies = toonies + cents // 200
cents = cents % 200
loonies = loonies + cents // 100
cents = cents % 100
quarters = quarters + cents // 25
cents = cents % 25
dimes = dimes + cents // 10
cents = cents % 10
nickles = nickles + cents // 5
cents = cents % 5
pennies = pennies + cents // 1

print(toonies, "toonies,", loonies, "loonies,", quarters, "quarters,", dimes, "dimes,", nickles, "nickles,", cents, "cents")
