def calculate_risk_adjustment(bel, risk_factor):

    risk_adj = bel * risk_factor

    return risk_adj

portfolio = []

while True:
    print("\n1. Add contract")
    print("2. View portfolio")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        contract_name = input("Enter contract name: ")
        bel = float(input("Enter Best Estimate Liability (BEL) amount: "))
        risk_factor = float(input("Enter risk factor (as %): ")) / 100
        risk_adjustment = calculate_risk_adjustment(bel, risk_factor)
        total_liability = bel + risk_adjustment

        contract = {
            "name": contract_name,
            "bel": bel,
            "risk_adjustment": risk_adjustment,
            "total_liability": total_liability
        }
        portfolio.append(contract)
        print(f"\n{contract_name} added to portfolio!")

    elif choice == "2":
        if len(portfolio) == 0:
            print("\nNo contracts in portfolio yet!")
        else:
            total_bel = sum(c['bel'] for c in portfolio)
            total_ra = sum(c['risk_adjustment'] for c in portfolio)
            total_tl = sum(c['total_liability'] for c in portfolio)
            
            print("\n--- Risk Adjustment Summary ---")
            print(f"\n{'Contract':<10} {'BEL':>12} {'Risk Adj':>12} {'Total' :>15}")
            print("-" * 56)
            for contract in portfolio:
                print(f"{contract['name']:<10} {contract['bel']:>12,.2f} {contract['risk_adjustment']:>12,.2f} {contract['total_liability']:>15,.2f}")
            
            print("-" * 56)
            print(f"{'Total':<10}{total_bel:>12,.2f} {total_ra:>12,.2f} {total_tl:>15,.2f}")

    elif choice == "3":
        print("\nExiting portfolio tracker!")
        break
