print('==============Calculadora de diretamente proporcional==============')

num1=int(input('escolha o primeiro numeros:'))
num2=int(input('escolha o segundo numeros:'))
num3=int(input('escolha o terceiro numeros:'))

total=int(input('qual o total:'))

b=num2/num1
c=num3/num1

result=1+b+c
result2=total/result

result3=b*result2
result4=c*result2

print(num1,':',result2,'\t','//',num2,':',result3,'\t','//',num3,':',result4)