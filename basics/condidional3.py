temperature = input("introduce the current temperaure")

humidity = 0.2
#idea general: crear un programa que toma decisiones de riesgo 
# dependiendo de los factores de temperatura 
if temperature >50:
    if humidity > 0 and humidity < 0.2:
        print("irrigate 1L per square meter")


money = input("enter the current money")
taxes =1,7 

#idea genearla crear un programa de compra dependiendo de los factores
# depiendiendo del dinero de impeustos 
if money >100: 
    if taxes >1 and taxes <2:
        print("buy 1 product")

if money <=100:
    print("do not buy any product")