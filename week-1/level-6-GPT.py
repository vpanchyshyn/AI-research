#Рівень 6: https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python
#Початковий розвʼязок ШІ: коротка умова (пояснено логіку, але без прикладів)
#Ця імплементація не враховує випадок, коли потрібного числа не існує, а отже створює нескінченний цикл

def dig_pow(n, p):
    k = 1
    while True:
        result = sum(int(digit)**(p + i) for i, digit in enumerate(str(n)))
        if result == k * n:
            return k
        k += 1

#При уточненні, щодо нескінченного циклу, виправляє це, додаючи аргумент для ліміту кількості ітерацій (якого не було в умові)
def dig_pow(n, p, max_iterations=1000):
    k = 1
    iterations = 0
    while iterations < max_iterations:
        result = sum(int(digit)**(p + i) for i, digit in enumerate(str(n)))
        if result == k * n:
            return k
        k += 1
        iterations += 1
    return None

#При наданні повної умови з формулою для розрахунку та прикладами виконання коду, спочатку знову створює нескінченний цикл,
#але з уточненням цього генерує повністю правильний, хоч і не найбільш оптимальний, код:
def dig_pow(n, p):
    digits = [int(digit) for digit in str(n)]
    current_sum = sum(digit ** (p + i) for i, digit in enumerate(digits))
    k = 1
    while True:
        if current_sum == k * n:
            return k
        k += 1
        next_sum = sum(digit ** (p + i) for i, digit in enumerate(digits))
        if k * n > next_sum:  # If k * n exceeds the next sum, no solution exists
            return -1
        current_sum = next_sum

#Наша імплементація (таким чином можна скоротити код та уникнути потенційних нескінченних циклів):
def dig_pow(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1
