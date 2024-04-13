#Рівень 8: https://www.codewars.com/kata/53dc54212259ed3d4f00071c/train/python
#Початковий розвʼязок ШІ: коротка умова
#Проста фундаментальна задача, передбачає використання базових вбудованих функцій
#Chat GPT використовує цикли та прості арифметичні операції, замість вбудованих функцій, проте генерує повністю правильний код;
#враховує перевірки на коректність вводу

def sum_array(arr):
    # Initialize sum to 0
    total_sum = 0
    
    # Iterate through each element in the array
    for num in arr:
        # Check if the element is a number
        if isinstance(num, (int, float)):
            # Add the number to the sum
            total_sum += num
    
    # Return the total sum
    return total_sum

#Повна умова з прикладами та уточнення щодо використання вбудованих функцій
def sum_array(arr):
    return sum(arr) if arr else 0
