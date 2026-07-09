def classify_contract(contract_type, duration):
    if contract_type == "short" and duration <= 1:
        return "PAA (Premium Allocation Approach)"
    elif contract_type == "long" or duration > 1:
        return "GMM (General Measurement Model)"
    else:
        return "Unable to classify contract"
    
portfolio = []

while True:
    print("\n1. Add contract")
    print("2. View portfolio")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        contract_name = input("Enter contract name: ")
        duration = float(input("Enter contract duration in years: "))
        contract_type = input("Enter contract type (short/long): ")

        classification = classify_contract(contract_type, duration)

        contract = {
            "name" : contract_name,
            "duration" : duration,            
            "classification" : classification,
        }
        portfolio.append(contract)
        print(f"\n{contract_name} added!")

    elif choice == "2":
        if len(portfolio) == 0:
            print("\nNo contracts in portfolio yet!")
        else:
            print("\n--- Portfolio Summary ---")
            for contract in portfolio:
                print(f"Contract: {contract['name']} | Duration: {contract['duration']} years | Classification: {contract['classification']}")
    
    elif choice == "3":
        print("Exiting...")
        break

