Initialize min_price to the first element: min_price = 7, max_profit = 0
    Iterate through the prices array:
        price = 7, min_price = 7 (unchanged), max_profit = 0
        price = 1, min_price = 1, max_profit = max(0, 1 - 7) = 0
        price = 5, min_price = 1 (unchanged), max_profit = max(0, 5 - 1) = 4
        price = 3, min_price = 1 (unchanged), max_profit = max(4, 3 - 1) = 4
        price = 6, min_price = 1 (unchanged), max_profit = max(4, 6 - 1) = 5
        price = 4, min_price = 1 (unchanged), max_profit = max(5, 4 - 1) = 5

        Return max_profit = 5
Output: 5

Example 2:
Input: prices = [7,6,4,3,1]

Initialize min_price to the first element: min_price = 7,       max_profit = 0
        Iterate through the prices array:
        price = 7, min_price = 7 (unchanged), max_profit = 0
        price = 6, min_price = 6, max_profit = max(0, 6 - 7) = 0
        price = 4, min_price = 4, max_profit = max(0, 4 - 6) = 0
        price = 3, min_price = 3, max_profit = max(0, 3 - 4) = 0
        price = 1, min_price = 1, max_profit = max(0, 1 - 3) = 0

        Return max_profit = 0
Output: 0