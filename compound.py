principal = 1000  # Initial amount
rate = 0.07  # Annual interest rate (7%)
years = 10  # Number of years


for year in range(1, years + 1):
    value = principal * (1 + rate) ** year
    print(f"Year {year}: ${value:.2f}")