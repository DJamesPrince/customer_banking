# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
ba_attempts = 0
balance_correct = False
while not balance_correct:
    savings_balance = input("Enter the balance of the savings account: ")
    try:
        savings_balance = float(savings_balance)
        balance_correct = True
    except ValueError:
        print("Invalid entry. Please enter a valid number.")
        ba_attempts += 1
        print(f"You have tried this {ba_attempts} times.")
        
        
ic_attempts = 0
interest_correct = False
while not interest_correct:
    savings_interest_rate = input("Enter the interest rate of the account: ")
    try:
        savings_interest_rate = float(savings_interest_rate)
        print(f"{savings_interest_rate}. Understood.")
        interest_correct = True
        
    except ValueError:
        input("Invalid entry. Please enter a valid number.")
        ic_attempts += 1
        print(f"You have tried this {ic_attempts} time(s).")

interest_correct = False
while not interest_correct:
    response = input(f"You said your interest rate was: {savings_interest_rate}%. Is this correct? (y/n)").lower()
    if response == "y" and type(savings_interest_rate) != int:
        try:
            savings_interest_rate = float(savings_interest_rate)
            interest_correct = True
        except ValueError:
            savings_interest_rate = input("Invalid entry. Please enter a valid number.")
            ic_attempts += 1
            print(f"You have tried this {ic_attempts} times.")
    else: 
        ic_attempts += 1
        savings_interest_rate = (input("What is your correct interest rate?"))
        try:
            savings_interest_rate = float(savings_interest_rate)
            interest_correct = True
        except ValueError:
            print("Invalid entry. Please enter a valid number.")
            ic_attempts += 1
            print(f"You have tried this {ic_attempts} times.")

samc_attempts = 0
sa_months_correct = False
while not sa_months_correct:
    savings_months = (input("Enter the months for the account: "))
    try:
        savings_months = int(savings_months)
        sa_months_correct = True
    except ValueError:
        print("Invalid entry. Please enter a valid number of Months.")
        samc_attempts += 1
        print(f"You have tried this {samc_attempts} times.")

    # Call the create_savings_account function and pass the variables from the user.
savings_updated_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest_rate, savings_months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.

print(f"Interest earned on savings account: {savings_interest_earned:.2f}")
print(f"Updated savings account balance: {savings_updated_balance:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.

cdba_attempts = 0
cdbalance_correct = False
while not cdbalance_correct:
    cd_balance = input("Enter the balance of the checking account: ")
    try:
        cd_balance = float(cd_balance)
        cdbalance_correct = True
    except ValueError:
        print("Invalid balance entry. Please enter a valid number.")
        cdba_attempts += 1
        print(f"You have tried this {cdba_attempts} times.")
        
        
cdic_attempts = 0
cdinterest_correct = False
while not cdinterest_correct:
    cd_interest_rate = input("Enter the interest rate of the checking account: ")
    try:
        cd_interest_rate = float(cd_interest_rate)
        print(f"{cd_interest_rate}. Understood.")
        cdinterest_correct = True
        
    except ValueError:
        input("Invalid entry. Please enter a valid number.")
        cdic_attempts += 1
        print(f"You have tried this {cdic_attempts} time(s).")

cdinterest_correct = False
while not cdinterest_correct:
    cdresponse = input(f"You said your interest rate was: {cd_interest_rate}%. Is this correct? (y/n)").lower()
    if cdresponse == "y" and type(cd_interest_rate) != int:
        try:
            cd_interest_rate = float(cd_interest_rate)
            cdinterest_correct = True
        except ValueError:
            cd_interest_rate = input("Invalid entry. Please enter a valid number.")
            cdic_attempts += 1
            print(f"You have tried this {cdic_attempts} times.")
    else: 
        cdic_attempts += 1
        cd_interest_rate = (input("What is your correct interest rate?"))
        try:
            cd_interest_rate = float(cd_interest_rate)
            cdinterest_correct = True
        except ValueError:
            print("Invalid entry. Please enter a valid number.")
            cdic_attempts += 1
            print(f"You have tried this {cdic_attempts} times.")

cdsamc_attempts = 0
cdsa_months_correct = False
while not cdsa_months_correct:
    cd_months = (input("Enter the months for the account: "))
    try:
        cd_months = int(cd_months)
        cdsa_months_correct = True
    except ValueError:
        print("Invalid entry. Please enter a valid number of Months.")
        cdsamc_attempts += 1
        print(f"You have tried this {cdsamc_attempts} times.")

    # Call the create_cd_account function and pass the variables from the user.
cd_updated_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest_rate, cd_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
print(f"Interest earned on CD account: {cd_interest_earned:.2f}")
print(f"Updated CD account balance: {cd_updated_balance:.2f}")

if __name__ == "__main__":
    main()
