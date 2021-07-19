from math import sqrt


class MathDojo:
     def __init__(self) -> None:
         self.result = 0

     def add(self, num, *nums):
          suma = num
          for n in nums:
               suma += n
          self.result += suma
          return self

     def subtract(self, num, *nums):
          resta = num
          for n in nums:
               resta += n
          self.result -= resta
          return self

     def avg(self, num, *nums):
          suma = num
          for n in nums:
               suma += n
          self.result = suma / (1 + len(nums) )
          return self

     def desvStandar(self,num,*nums):
          # calcula promedio, variable avg
          suma = num
          for n in nums:
               suma += n
          avg = suma / (1 + len(nums) )
          # print(f"Promedio = {avg}")

          # calcula la suma de los cuadrados de las diferencias
          sumdiff = (num - avg)**2
          for n in nums:
               sumdiff += (n - avg)**2
          # print(f"Suma diferencias = {sumdiff}")

          # calcula la raíz cuadrada de la suma de los cuadrados delas diferencias dividido por (N-1)
          self.result = sqrt( sumdiff / ( len(nums) ) )

          return self

 


# md1 = MathDojo()
# x = md1.add(2,3,5)
# print(x.result)

# md1 = MathDojo()
# x = md1.add(2)
# print(x.result)

# md1 = MathDojo()
# x = md1.add(10,15,20,25,30)
# print(x.result)


# md2 = MathDojo()
# y = md2.subtract(10,3,1)
# print(y.result)

# md2 = MathDojo()
# y = md2.subtract(10)
# print(y.result)

# md2 = MathDojo()
# y = md2.subtract(3,1)
# print(y.result)


# md3 = MathDojo()
# x = md3.add(2).add(2,5,1).subtract(3,2)
# print(x.result) # debe imprimir 5


md4 = MathDojo()
x = md4.add(3).avg(2,4,6)
print(x.result)
x = md4.avg(2)
print(x.result)
x = md4.desvStandar(727.7,1086.5,1091,1361.3,1490.5,1956.1)
print(x.result) # debe imprimir 420.96...

