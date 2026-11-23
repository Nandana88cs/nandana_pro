def get_balance_after_withdrawal(current_balance, withdrawal_amount):
    if withdrawal_amount > current_balance:
        raise ValueError("Insufficient funds")
    return current_balance - withdrawal_amount

# Example usage:
balance = 15000s
withdraw = 200
new_balance = get_balance_after_withdrawal(balance, withdraw)
print("Balance after withdrawal:", new_balance)   