#!/usr/bin/env python
# coding: utf-8

# In[5]:


import csv

def main():
    f = open('202303_Seoul_Subway.csv', 'r')

    data = csv.reader(f)

    header = next(data)
    
    max_station = ['']*4
    max_value = [0]*4
    min_station = ['']*4
    min_value = [-1]*4
    for row in data:
        s = row[1]
        try:
            if(int(s[0]) >= 1 and int(s[0]) <= 4 and len(s) <= 3):
                if(int(s[0]) == 1):
                    row[4] = int(row[4])
                    row[5] = int(row[5])
                    if(max_value[0] < int(row[4])+int(row[5])):
                        
                        max_value[0] = row[4]+row[5]
                        max_station[0] = row[3]
                    if(min_value[0] > int(row[4])+int(row[5]) or min_value[0] == -1):
                       
                        min_value[0] = row[4]+row[5]
                        min_station[0] = row[3]
                elif(int(s[0]) == 2):
                    row[4] = int(row[4])
                    row[5] = int(row[5])
                    if(max_value[1] < int(row[4])+int(row[5])):
                        max_value[1] = row[4]+row[5]
                        max_station[1] = row[3]
                    if(min_value[1] > int(row[4])+int(row[5]) or min_value[1] == -1):
                        min_value[1] = row[4]+row[5]
                        min_station[1] = row[3]
                elif(int(s[0]) == 3):
                    row[4] = int(row[4])
                    row[5] = int(row[5])
                    if(max_value[2] < int(row[4])+int(row[5])):
                        max_value[2] = row[4]+row[5]
                        max_station[2] = row[3]
                    if(min_value[2] > int(row[4])+int(row[5]) or min_value[2] == -1):
                        min_value[2] = row[4]+row[5]
                        min_station[2] = row[3]
                elif(int(s[0]) == 4):
                    row[4] = int(row[4])
                    row[5] = int(row[5])
                    if(max_value[3] < int(row[4])+int(row[5])):
                        max_value[3] = row[4]+row[5]
                        max_station[3] = row[3]
                    if(min_value[3] > int(row[4])+int(row[5]) or min_value[3] == -1):
                        min_value[3] = row[4]+row[5]
                        min_station[3] = row[3]
                    
        except ValueError as v:
            pass
        finally:
            pass
        
    print("***Subway Report for Seoul on March 2023 ***")

    print("Line 1:")
    print("Busiest Station: {}({})".format(max_station[0], max_value[0]))
    print("Least Station: {}({})".format(min_station[0], min_value[0]))
    print("Line 2:")
    print("Busiest Station: {}({})".format(max_station[1], max_value[1]))
    print("Least Station: {}({})".format(min_station[1], min_value[1]))
    print("Line 3:")
    print("Busiest Station: {}({})".format(max_station[2], max_value[2]))
    print("Least Station: {}({})".format(min_station[2], min_value[2]))
    print("Line 4:")
    print("Busiest Station: {}({})".format(max_station[3], max_value[3]))
    print("Least Station: {}({})".format(min_station[3], min_value[3]))
        
    f.close()
if __name__ == '__main__':
    main()


# In[ ]:




