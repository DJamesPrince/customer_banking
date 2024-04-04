# Import the Account class from the Accounts.py file
from Account import Account
    
    # Define a function for the Savings Account  
    
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        Tuple[float, float]: The updated savings account balance and the interest earned.
    """
    # Create an instance of the `Account` class with the initial balance and interest rate set to 0
    savings_account = Account(balance, interest_rate, months)

    # Calculate interest earned
    interest_earned = balance * (interest_rate / 100) * (months / 12)
    
    # Pass the updated balance to the set balance method using the instance of the Account class
    savings_account.set_balance(balance)

    # Pass the interest earned to the set interest method using the instance of the Account class
    savings_account.set_interest(interest_earned)

    # Update the savings account balance by adding the interest earned
    updated_balance = savings_account.balance + savings_account.interest_rate

    # Return the updated balance and interest earned
    return updated_balance, interest_earned  


