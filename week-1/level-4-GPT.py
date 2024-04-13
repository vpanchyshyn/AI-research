#Рівень 4: https://www.codewars.com/kata/5a3af5b1ee1aaeabfe000084
#Початковий розвʼязок ШІ: коротка умова без прикладів
#Chat GPT вказує, що ця задача є класичним зразком динамічного програмування і одразу генерує код, що коректно працює для більшості випадків
#Проте код time out на дуже великих числах, через занадто багато потрібних ітерацій 
#(код не оптимізовано для роботи з великими наборами даних)

import math
def min_perfect_squares(n):
    # Initialize a list to store the minimum number of perfect squares for each number up to n
    dp = [0] * (n + 1)
    
    # Iterate through each number up to n
    for i in range(1, n + 1):
        # Set the initial minimum value to infinity
        min_squares = float('inf')
        
        # Iterate through each perfect square less than or equal to i
        for j in range(1, int(math.sqrt(i)) + 1):
            # Update the minimum number of perfect squares for i
            min_squares = min(min_squares, dp[i - j*j] + 1)
        
        # Store the minimum number of perfect squares for i in the dp array
        dp[i] = min_squares
    
    # Return the minimum number of perfect squares for n
    return dp[n]

#Після уточнення про оптимізацію ШІ використовує базові алгоритми, наприклад BFS (все ще недостатньо)
#(також імпортує додаткові бібліотеки)

import math
from collections import deque

def min_perfect_squares(n):
    # Generate perfect squares less than or equal to n
    squares = [i*i for i in range(1, int(math.sqrt(n)) + 1)]
    
    # Initialize a queue for BFS
    queue = deque([(n, 0)])
    
    # Initialize a set to store visited numbers
    visited = set()
    
    # Perform BFS
    while queue:
        num, count = queue.popleft()
        if num == 0:
            return count
        for square in squares:
            if num - square >= 0 and (num - square) not in visited:
                queue.append((num - square, count + 1))
                visited.add(num - square)
    
    # If no solution is found
    return -1

#При повторному уточненні про time out та завданні максимально оптимізувати код,
#використовує фундаментальні теореми

#ПОВНІСТЮ ПРАВИЛЬНИЙ КОД:
def min_perfect_squares(n):
    # Check if n is already a perfect square
    if int(n**0.5)**2 == n:
        return 1
    
    # Check if n can be represented as the sum of two perfect squares
    for i in range(1, int(n**0.5) + 1):
        if int((n - i*i)**0.5)**2 == (n - i*i):
            return 2
    
    # Check if n can be represented as the sum of three perfect squares
    while n % 4 == 0:
        n //= 4
    if n % 8 == 7:
        return 4
    
    # In all other cases, n can be represented as the sum of four perfect squares
    return 3
