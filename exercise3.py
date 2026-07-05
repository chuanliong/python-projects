contract_name = input("Enter contract name: ")
csm = float(input("Enter initial CSM amount: "))
coverage_years = int(input("Enter coverage period in years: "))

annual_release = csm / coverage_years

print(f"\nCSM Amortization Schedule for {contract_name}")
print("-" * 40)

for year in range(1, coverage_years + 1):
    remaining_csm = csm - (annual_release * year)
    print(f"Year {year} | Released: {annual_release:,.2f} | Remaining CSM: {remaining_csm:,.2f}")

print("-" * 40)
print(f"Total CSM Released: {csm:.2f}")