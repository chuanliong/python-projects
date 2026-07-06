def calculate_closing_csm(init_csm, nb_added, int_act, exp_var, csm_rel):
    
    closing_csm = init_csm + nb_added + int_act + exp_var - csm_rel

    return closing_csm

init_csm = float(input("Enter initial CSM amount: "))
nb_added = float(input("Enter new business added: "))
int_act = float(input("Enter interest on CSM: "))
exp_var = float(input("Enter experience variance: "))
csm_rel = float(input("Enter CSM released: "))

closing_csm = calculate_closing_csm(init_csm, nb_added, int_act, exp_var, csm_rel)

print("\n--- CSM Calculation Summary ---")
print(f"Initial CSM: {init_csm:,.2f}")
print(f"New Business Added: {nb_added:,.2f}")
print(f"Interest on CSM: {int_act:,.2f}")
print(f"Experience Variance: {exp_var:,.2f}")
print(f"CSM Released: -{csm_rel:,.2f}")
print("-" * 40)
print(f"Closing CSM: {closing_csm:,.2f}")

