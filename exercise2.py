contract_type = input("Enter contract type (short/long): ")
duration = float(input("Enter contract duration in years: "))

if contract_type == "short" and duration <=1:
    print("This contract qualified for PAA (Premium Allocation Approach)")
elif contract_type == "long" and duration > 1:
    print("This contract requires GMM(General Measurement Model)")
else:
    print("Unable to classify contract")

    