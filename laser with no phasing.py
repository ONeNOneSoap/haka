import math


t0 = 0.         #начало работы лазерной системы
t1 = 10.        #конец работы лазерной системы
dt = 0.001      #шаг времени
t = t0          #произвольный момент времени

mean_intensity = 0.                 #средняя интенсивность
mean_calc = 3.8369984809748714      #заранее вычисленное значение средней интенсивности
dispersion = 0.                     #дисперсия значения интенсивности
fileas = open("newnew.txt", "w")    #запись данных в файл newnew.txt
def f(i, t):                        #функции, описывающие фазовые неоднородности внутри системы
    return 2*3.14*math.sin(0.5*(i-1)+(5+0.5*i)*t)


#вычисление максимальной интенсивности
i = 1
sum1 = 0
while i < 5:
    sum1 += math.cos(0)
    i = i + 1
sum1 = sum1*sum1
i = 1
sum2 = 0
while i < 5:
    sum2 += math.sin(0)
    i = i + 1
sum2 = sum2*sum2
I_max = sum1 + sum2
print(I_max)
mean_relation = 0.


#вычисление интенсивности в произвольный момент времени без фазировки
while t < t1:
    i = 0
    sum1 = 0
    sum12 = 0
    #сумма косинусов
    while i < 4:
        sum1 += math.cos(f(i, t))
        i = i + 1
    sum12 = sum1*sum1
    i = 1
    sum2 = 0
    sum22 = 0
    #сумма синусов
    while i < 4:
        sum2 += math.sin(f(i, t))
        i = i + 1
    sum22 = sum2*sum2
    print(sum12+sum22, file = fileas)
    mean_intensity = mean_intensity + (sum12+sum22) * dt
    dispersion = dispersion + ((sum12+sum22)-mean_calc)*((sum12+sum22)-mean_calc)*dt
    mean_relation = mean_relation + (sum12+sum22)/I_max * dt
    t = t + dt
    
print(mean_intensity/(t1-t0))
print(math.sqrt(dispersion/(t1-t0)))
print(mean_relation/(t1-t0))
fileas.close()





