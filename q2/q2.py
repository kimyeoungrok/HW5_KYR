#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv

def main():
    f = open('2022_Seoul_Temp.csv', 'r')

    data = csv.reader(f)

    header = next(data)
    max_d = -999
    max_date =''
    min_d = 999
    min_date = ''
    for row in data:
        if(row[-1] != '' and row[-2] != ''):
            row[-1] = float(row[-1])
            row[-2] = float(row[-2])
            d = row[-1] - row[-2]
            if(max_d < d):
                max_d = d
                max_date = row[0]
            if(min_d > d):
                min_d = d
                min_date = row[0]

    max_d = round(max_d,2)
    min_d = round(min_d,2)

    print("*** Annual Temperature Report for Seoul in 2022 ***")
    print("Day with the Largest Temperature Variation: {}".format(max_date))
    print("Maximum Temperature Difference: {} Celsius".format(max_d))
    print("Day with the Smallest Temperature Variation: {}".format(min_date))
    print("Miniimum Temperature Difference: {} Celsius".format(min_d))
    
    f.close()

if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:




