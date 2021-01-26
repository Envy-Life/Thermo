import csv

temp = input("Enter material to refer : ")
temp_t = float(input("Enter temperature(K) : "))
temp_p = float(input("Enter pressure(KPa) : "))
list_t = []
list_p = []
list_v = []
with open(f'{temp}.csv','r') as file :
    temp_list = csv.reader(file,delimiter = '\n')
    for row in temp_list :
        split = row[0].split(",")
        list_t.append(float(split[0]))
        list_p.append(float(split[1]))
        list_v.append(float(split[2]))
if temp_t > list_t[-1] :
    print("super critical fluid")
    exit()
for i in range(len(list_t)) :
    if temp_t >= list_t[i] and temp_t <= list_t[i+1] :
        calc_pressure = list_p[i] + (((list_p[i+1]-list_p[i])/(list_t[i+1]-list_t[i]))*(temp_t-list_t[i]))
        if calc_pressure > temp_p :
            print("super heated vapour")
        elif calc_pressure < temp_p :
            print("subcooled liquid")
        else :
            print("super heated vapour and subcooled liquid mixture")
        break




