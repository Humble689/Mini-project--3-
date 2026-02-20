
def get_budget():
    """
    Ask the user to enter a non-negative budget amount.
    Returns the validated budget as a float.
    """
    while True:
        try:
            budget_input = input("Enter your budget amount: Ugx")
            budget = float(budget_input)
            if budget < 0:
                print("Error: Budget cannot be negative. Please enter a non-negative amount.")
                continue
            if budget == 0:
                print("Warning: Your budget is Ugx0. You won't be able to spend anything.")
            return budget
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")


def get_transaction():
    """
    Ask the user to enter a transaction description and amount.
    Returns a tuple (description, amount) or (None, None) if done.
    """
    # Get description
    print("\n--- Enter Transaction ---")
    description = input("Enter transaction description (or 'done' to finish): ").strip()
    
    if description.lower() == "done":
        return None, None
    
    if not description:
        print("Error: Description cannot be empty.")
        return get_transaction()
    
    # Get amount
    while True:
        try:
            amount_input = input("Enter transaction amount: Ugx")
            amount = float(amount_input)
            if amount < 0:
                print("Error: Amount cannot be negative. Please enter a positive amount.")
                continue
            return description, amount
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")


def display_warning(total_expenses, budget):
    """
    Display a warning message when expenses exceed the budget.
    """
    exceeded_by = total_expenses - budget
    print("\n" + "=" * 50)
    print("WARNING: BUDGET EXCEEDED! ⚠️")
    print("=" * 50)
    print(f"Total Expenses: Ugx{total_expenses:.2f}")
    print(f"Budget:         Ugx{budget:.2f}")
    print(f"Exceeded by:    Ugx{exceeded_by:.2f}")
    print("=" * 50 + "\n")


def display_summary(budget, transactions):
    """
    Display a summary report of all financial information.
    
    Parameters:
    - budget (float): The initial budget amount
    - transactions (list): List of tuples (description, amount)
    """
    total_expenses = sum(amount for _, amount in transactions)
    remaining_balance = budget - total_expenses
    
    print("\n" + "=" * 60)
    print("              FINANCIAL SUMMARY REPORT")
    print("=" * 60)
    
    # Budget Information
    print(f"\nINITIAL BUDGET:        Ugx{budget:.2f}")
    
    # Total Expenses
    print(f"TOTAL EXPENSES:        Ugx{total_expenses:.2f}")
    
    # Balance or Deficit
    if remaining_balance >= 0:
        print(f"REMAINING BALANCE:    Ugx{remaining_balance:.2f}")
        if remaining_balance > 0:
            print("You are within your budget! Great job!")
        else:
            print("You have spent exactly your budget.")
    else:
        print(f"DEFICIT:              Ugx{abs(remaining_balance):.2f}")
        print("You have exceeded your budget!")
    
    # Transaction List
    print("\n" + "-" * 60)
    print("                    TRANSACTION LIST")
    print("-" * 60)
    
    if not transactions:
        print("No transactions recorded.")
    else:
        print(f"{'No.':<5} {'Description':<30} {'Amount':>15}")
        print("-" * 60)
        for i, (description, amount) in enumerate(transactions, 1):
            print(f"{i:<5} {description:<30} Ugx{amount:>14.2f}")
    
    print("-" * 60)
    print(f"{'TOTAL':<35} Ugx{total_expenses:>14.2f}")
    print("=" * 60 + "\n")
 

def main():
    """
    Main function to run the financial management program.
    """
    print("=" * 60)
    print("   PERSONAL FINANCIAL MANAGEMENT PROGRAM")
    print("   Designed for First-Year Students")
    print("=" * 60)
    
    # Step 1: Get budget
    print("\n--- Step 1: Set Your Budget ---")
    budget = get_budget()
    print(f"\n Budget set to: Ugx{budget:.2f}")
    
    # Step 2: Collect transactions
    transactions = []
    total_expenses = 0
    transaction_count = 0
    min_transactions = 5
    
    print(f"\n--- Step 2: Enter Transactions ---")
    print(f"Enter at least {min_transactions} transactions.")
    print("Type 'done' when finished (you can enter more than {0} transactions).".format(min_transactions))
    
    while True:
        description, amount = get_transaction()
        
        if description is None:  # User typed 'done'
            if transaction_count < min_transactions:
                print(f"\nNote: You have only entered {transaction_count} transaction(s).")
                print(f"Please enter at least {min_transactions} transactions or press Enter to continue...")
                continue_input = input("Press Enter to continue or type 'done' to finish: ").strip().lower()
                if continue_input != 'done':
                    # Get another transaction instead
                    continue
            break
        
        # Add transaction to list
        transactions.append((description, amount))
        transaction_count += 1
        total_expenses += amount
        
        print(f"✅ Transaction added: {description} - Ugx{amount:.2f}", end="")
        
        # Check if budget exceeded
        if total_expenses > budget:
            display_warning(total_expenses, budget)
        
        # Show running total
        remaining = budget - total_expenses
        print(f"   Running total: Ugx{total_expenses:.2f} | Remaining: Ugx{remaining:.2f}")
    
    # Step 3: Display summary
    display_summary(budget, transactions)
    
    print("Thank you for using the Personal Financial Management Program!")
    print("Good luck with your finances! 🎓\n")


if __name__ == "__main__":
    main()
