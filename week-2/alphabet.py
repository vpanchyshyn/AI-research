# Завдання alphabet triangle: https://cms.ucu.edu.ua/mod/vpl/view.php?id=361858
# Для кращого порівняння ми переписали alphabet triangle через функції, після оптимізації коду ChatGPT час виконання скоротився з 0.12 с до 0.02

def version_1(letters):
    lines = 0
    index = 0
    k = letters

    while k > 0:
        k -= lines + 1
        lines += 1

    for i in range(1, lines + 1):
        print(" " * (2 * (lines - i)), end="")

        for j in range(i):       
            if index==letters-1:
                print(f'{chr(65 + index)}', end="")           
            elif j==i-1:
                print(f'{chr(65 + index)}', end="")           
            else:
                print(f'{chr(65 + index)}', end=" ")
            index += 1

            if index >= letters:
                break

        print()

def version_gpt(letters):
    lines = 0
    index = 0
    k = letters

    while k > 0:
        k -= lines + 1
        lines += 1

    for i in range(1, lines + 1):
        print(" " * (2 * (lines - i)), end="")
        for j in range(i):
            print(chr(65 + index), end="")
            index += 1

            if index >= letters:
                break

            if j < i - 1:
                print(" ", end="")

        print()
