portfolio = []

while True:
    print("\n1. Add contract")
    print("2. View portfolio")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        contract_name = input("Enter contract name: ")
        csm = float(input("Enter CSM amount: "))
        duration = int(input("Enter duration in years: "))

        contract = {
            "name": contract_name,
            "csm": csm,
            "duration": duration
        }
        
        portfolio.append(contract)
        print(f"\n{contract_name} added to portfolio!")

    elif choice == "2":
        if len(portfolio) == 0:
            print("\nNo contracts in portfolio yet!")
        else:
            print("\n--- Portfolio Summary ---")
            total_csm = 0
            for contract in portfolio:
                print(f"Contract: {contract['name']} | CSM: {contract['csm']:,.2f} | Duration: {contract['duration']} years")
                total_csm += contract['csm']
            print(f"Total Portfolio CSM: {total_csm:,.2f}")

    elif choice == "3":
        print("\nExiting portfolio tracker!")
        break