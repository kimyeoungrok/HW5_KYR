#!/usr/bin/env python
# coding: utf-8

# In[9]:


import csv
def main():
    f = open('q3.csv', 'r')

    data = csv.reader(f)

    header = next(data)

    station = [0]*9
    
    for row in data:
        s = row[1]
        try:
            if(int(s[0]) >= 1 and int(s[0]) <= 9 and len(s) <= 3):
                station[int(s[0])-1] += int(row[4])
        except ValueError as v:
            pass
        finally:
            pass
            
    large_first = station[0]
    large_station = 0
    second_first = station[0]
    second_station = 0
    small_first = station[0]
    small_station = 0
    small_second = station[0]
    small_second_station = 0
    count = 0
    for d in station:
        
        if(large_first < d):
            large_first = d
            large_station = count
        elif(second_first < d):
            second_first = d
            second_station = count
            
        if small_first > d:
            small_first = d
            small_station = count
        elif small_second > d:
            small_second = d
            small_second_station = count
        count+=1
        
        
        
    
    print("*** Subway Report seoul on March 2023 ***")
    print("1st Buiest Line: Line {} ({})".format(large_station + 1, large_first))
    print("2nd Buiest Line: Line {} ({})".format(second_station + 1, second_first))  
    print("1st Least Line: Line {} ({})".format(small_station + 1, small_first))
    print("2nd Least Line: Line {} ({})".format(small_second_station + 1, small_second))  
    
    f.close()
if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:




