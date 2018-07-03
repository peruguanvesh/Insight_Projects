from collections import defaultdict
from datetime import datetime,timedelta
fmt = '%d/%m/%Y:%H:%M:%S'
#li = []


def get_seconds_list():
    tim = datetime.strptime('01/07/1995:00:00:00',fmt)
    #dict = {}
    li = []
    #li = default.dict(int)
    for i in range(0,25000000):
        tim += timedelta(seconds=1)
        #dict[tim] = 0
        li.append(tim)
        if tim.day == 28 and tim.hour == 13 and tim.minute == 32 and tim.second == 25:
            break
    return li

#def get_hour_count_dict(li):
    #with open('log.txt','r') as f:


def get_hour_count_dict(list):
    with open('log.txt', 'r') as f:
        dict = {}
        dict = defaultdict(int)
        new_list = []
        count = 0
        for line in f:
            count += 1
            if count == 50000:
                break
            #count += 1
            #print(len(line))
            elements = line.replace('[',"").replace(']',"").split(' ')
            ele = elements[3]
            required1 = ele.replace('Jul','07')
            #print(required1)
            a = datetime.strptime(required1,fmt)
            b = int((a - list[0]).total_seconds())
            index1 = int(b - 3600)
            if index1 < 0:
                index1 = 0
            index2 = b
            #li.append(a)
            #print(a)
            #if a-timedelta(seconds = 3600) >
            #counter = 0
            for i in range(index1,index2 +1):
                #new = i.replace('Jul','07')
                #tms = datetime.strptime(new,fmt)
                #print i
                dict[list[i]] += 1
                #if a >= list[i]:
                    #if int((a - list[i]).total_seconds()) <= 3600:
                    #print(int((i-a).total_seconds()))
                        #dict[list[i]] += 1
                    #if int((a-list[i]).total_seconds()) > 3600 and int((a-list[i+1]).total_seconds()) <= 3600:
                        #new_index = i
                #else:
                    #break
                #else:
                    #break
                    #index
                    #new_dict[i] = dict[i]
                    #del dict[i]
                #if i == ele:
                    #counter += 1
            #if counter < 1:
                #dict[ele] = 1
    #for i in dict:
        #new_dict[i] = dict[i]
    #print(new_dict)

    return dict


def hour_counts(dict):
    count_list = []
    for i in dict:
            count_list.append(dict[i])
    return count_list

def swap(list,index1,index2):
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp
    return list

def heap_sort(list):
    for i in range(len(list)//2 -1,-1,-1):
        heapify(list,i)
    return list

def heapify(list,i):
    if i <= len(list)-1:
        if 2*i +1 <= len(list) -1 and 2*i +2 > len(list) -1:
            if list[i] < list[2*i +1]:
                swap(list,i,2*i +1)
                heapify(list,2*i +1)
        elif 2*i +1 <= len(list) -1 and 2*i +2 <= len(list) -1:
            if list[i] < list[2*i +1]:
                greater = list[2*i +1]
                if list[2*i +1] < list[2*i +2]:
                    swap(list,i,2*i +2)
                    heapify(list,2*i +2)
                else:
                    swap(list,i,2*i +1)
                    heapify(list,2*i +1)
            else:
                greater = list[i]
                if list[i] < list[2*i +2]:
                    swap(list,i,2*i +2)
                    heapify(list,2*i +2)

def extract_max(list):
    top_10_list = []
    for i in range(0,10):
        top_10_list.append(list[0])
        swap(list,0,-1)
        del list[-1]
        heapify(list,0)
    return top_10_list

def top_10_hour(dict,top_10_list):
    for i in top_10_list:
        for j in dict:
            if i == dict[j]:
                with open('hours.txt','a') as f:
                    f.write('{} : {}\n'.format(j,i))

def main():
    list = get_seconds_list()
    new_dict = get_hour_count_dict(list)
    #required_dict = new_fun(new_list,list)
    list_of_count = heap_sort(hour_counts(new_dict))
    top_10_hour(new_dict,extract_max(list_of_count))

    #print(list[0],list[-1])
    #new_dict = get_hour_count_dict(list,dict)
    #print(new_dict)
    #print(new_dict)
    #print(int((li[1] - li[0]).total_seconds()))
    #list_of_count = heap_sort(hour_counts(dict))
    #top_10_hour(dict,extract_max(list_of_count))

main()

