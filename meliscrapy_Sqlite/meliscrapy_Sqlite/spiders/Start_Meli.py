import os
import melisql
#Ejecutamos n veces melisql.py para poblar tabla con datos
for x in range(1):
  print(x)
  os.system('scrapy runspider melisql.py')
