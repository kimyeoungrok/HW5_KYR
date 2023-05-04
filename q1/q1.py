#!/usr/bin/env python
# coding: utf-8

# In[6]:


import csv
def main():
    f = open('q1.csv', 'r')

    data = csv.reader(f)

    header = next(data)
    temp = 0
    count = 0
    min_temp = 0
    max_temp = 0
    for row in data:
        count+=1
        t = row[2]
        t = float(t)
        temp += t
        if(row[3] != ''):
            row[3] = float(row[3])
        row[4] = float(row[4])
        if(row[3] != ''):
            min_temp += row[3]
        max_temp += row[4]

    average = round(temp/count, 2)
    min_temp = round(min_temp/count,2)
    max_temp = round(max_temp/count,2)


    print("*** Annual Temperature Report for Seoul in 2022 ***")
    print("Average Temperature: {:.2f} Celsius".format(average))
    print("Average Minimum Temperature: {:.2f} Celsius".format(min_temp))
    print("Average Maximum Temperature: {:.2f} Celsius".format(max_temp))
    
    f.close()
if __name__ == '__main__':
    main()

    


# In[ ]:





# In[ ]:




