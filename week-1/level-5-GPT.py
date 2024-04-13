#Рівень 5: https://www.codewars.com/kata/5547cc7dcad755e480000004
#Розвʼязок ШІ: повна умова з прикладами
#Chat GPT не враховує всі можливі випадки, проте складає правильний алгоритм для розрахунку
def removNb(n):
    result = []
    total_sum = n * (n + 1) // 2  # Sum of all numbers from 1 to n
    
    for a in range(1, n + 1):
        b = (total_sum - a) / (a + 1)
        if b.is_integer() and 1 <= b <= n and a < b:
            result.append((a, int(b)))
    
    return result

#Навіть, якщо вказати помилку, дає не до кінця коректний вивід, тому що не використовує оптимальні структури та типи даних (тут доречно set)
def removNb(n):
    result = []
    total_sum = n * (n + 1) // 2  # Sum of all numbers from 1 to n
    
    for a in range(1, n + 1):
        b = (total_sum - a) / (a + 1)
        if b.is_integer() and 1 <= b <= n:
            result.append((a, int(b)))
            result.append((int(b), a))  # Append the pair in reverse order
    
    return result

#Якщо уточнити всі деталі окремими промтами, ШІ генерує правильний код
def removNb(n):
    result = set()
    total_sum = n * (n + 1) // 2  # Sum of all numbers from 1 to n
    
    for a in range(1, n + 1):
        b = (total_sum - a) / (a + 1)
        if b.is_integer() and 1 <= b <= n:
            result.add((a, int(b)))
            result.add((int(b), a))  # Append the pair in reverse order
    
    return sorted(list(result))
