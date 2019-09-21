print("Добропожаловать в калькулятор!", " ", "Введи циферку")
a = float(input())
print("Молодец!" " " "А теперь значок")
sign = input()
print("И еще одну циферку")
b = float(input())
# наверно можно как-то сделать так, чтоб он читал все сразу без if, но я пока не знаю как
if b == 0 and sign == '/':
    print('hren tam plaval')
elif sign == '-':
    print(a - b)
elif sign == '+':
    print(a + b)
elif sign == '*':
    print(a * b)
elif sign == '/':
    print(a / b)
print("Отличная работа, дружок")
