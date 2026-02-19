# Personal Financial Management Program - TODO

## Task Requirements Analysis
1. Ask user to enter a non-negative budget amount at start ✅
2. Allow user to enter at least 5 financial transactions (description + amount) ✅
3. Keep running total and check if budget exceeded after each transaction ✅
4. Allow sentinel value "done" to stop entering transactions ✅
5. Display summary report with: initial budget, total expenses, balance/deficit, list of transactions ✅

## Implementation Status - COMPLETED ✅
- [x] Create Python file `finance_tracker.py`
- [x] Implement input validation for budget (non-negative)
- [x] Implement transaction entry loop with validation
- [x] Implement budget warning system
- [x] Implement summary report display
- [x] Test the program functionality

## Functions Implemented
- `get_budget()` - Get and validate budget input
- `get_transaction()` - Get transaction description and amount
- `display_warning()` - Show warning when budget exceeded
- `display_summary()` - Show final report
- `main()` - Main program flow

## Test Results
Program was tested with:
- Budget: $100.00
- 5 Transactions: Textbooks ($25.50), Coffee ($3.50), Bus pass ($30.00), Lunch ($8.75), Notebook ($5.00)
- Total Expenses: $72.75
- Remaining Balance: $27.25
- All functionality working correctly!
