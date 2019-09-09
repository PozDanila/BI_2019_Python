a = float(input())
znak = input()
b = float(input())
# наверно можно как-то сделать так, чтоб он читал все сразу без if, но я пока не знаю как
if b == 0 and znak == '/':
    print('hren tam plaval')
elif znak == '-' :
  print( a - b)
elif znak == '+':
    print(a+b)
elif znak == '*':
    print(a*b)
elif znak == '/':
    print(a//b)