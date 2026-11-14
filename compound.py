principal = float(input("Principal amount: "))  # Initial amount
rate = float(input("Annual interest rate (e.g. 0.07): "))  # Annual interest rate (7%)
years = int(input("Number of years: "))  # Number of years

for year in range(1, years + 1):
    value = principal * (1 + rate) ** year
    print(f"Year {year}: €{value:.2f}")