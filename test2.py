import sys
from collections import defaultdict

resource_count = {}
resource_count = defaultdict(int)


def resource_band():
    with open('log.txt','rb') as f:
        reader = f.readlines()
        count = 0
        for line in reader:
            ele = line.strip('\n')
            elements = ele.split(' ')
            resource = elements[6]
            bandwidth = elements[-1]
            if bandwidth == '-':
                bandwidth = 0
                resource_count[resource] += int(bandwidth)
            else:
                resource_count[resource] += int(bandwidth)
    return resource_count

def list_of_count(dict):
    list_of_bytes = []
    for i in dict:
        list_of_bytes.append(dict[i])
    return list_of_bytes


def partition(list,swapping_index,pivoting_index):
    current_index = swapping_index
    for i in range(current_index,pivoting_index+1):
        if i == pivoting_index:
            swap(list,swapping_index,pivoting_index)
            partition_index = swapping_index
        else:
            if list[i] >= list[pivoting_index]:
                current_index = i
                swap(list,swapping_index,current_index)
                swapping_index += 1
    return partition_index


def swap(list,index1,index2):
    if index1 < index2:
        temp = list[index1]
        list[index1] = list[index2]
        list[index2] = temp
    return list


def quick_sort(list,start_index,pivoting_index):
    if start_index<pivoting_index:
        splitter_index = partition(list,start_index,pivoting_index)
        quick_sort(list,start_index,splitter_index-1)
        quick_sort(list,splitter_index+1,pivoting_index)


def top_10_resources(dict,top_10_list):
    for i in top_10_list:
        for j in dict:
            if i == dict[j]:
                with open('resources.txt','a') as f:
                    f.write('{} \n'.format(j))



def main():
    top_10_list = []
    sys.setrecursionlimit(2800)
    dict = resource_band()
    list_of_bytes = list_of_count(dict)
    quick_sort(list_of_bytes,0,len(list_of_bytes)-1)
    for i in range(0,10):
        top_10_list.append(list_of_bytes[i])
    top_10_resources(dict,top_10_list)

main()
