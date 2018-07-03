from collections import defaultdict
dict={}
dict = defaultdict(int)

def get_count():
    with open('log.txt','r') as f:
        l = f.readlines()
        for line in l:
             k=line.split('- -')
             dict[k[0]]+=1
    return dict
def to_sorte(k):
    b=[]
    for i in k:
        b.append(k[i])
    return b

def heapsort(b):
    l = len(b)
    for i in range(l//2 -1,-1,-1):
         heapify(i,b)
    return b

def heapify(a,b):
    if 2*a +2 > len(b)-1 and 2*a +1 <= len(b)-1:
        if b[a] < b[2*a +1]:
            temp = b[a]
            b[a] = b[2*a +1]
            b[2*a +1] = temp
            heapify(2*a +1,b)
    elif 2*a +1 < len(b) -1 and 2*a +2 <= len(b) -1:
        if b[a] < b[2*a +1]:
            greater = b[2*a +1]
            if greater < b[2*a +2]:
                temp = b[a]
                b[a] = b[2*a +2]
                b[2*a +2] = temp
                heapify(2*a +2,b)
            else:
                temp =b[a]
                b[a] = b[2*a +1]
                b[2*a +1] = temp
                heapify(2*a +1,b)
        else:
            greater = b[a]
            if greater < b[2*a +2]:
                temp = b[a]
                b[a] = b[2*a +2]
                b[2*a +2] = temp
                heapify(2*a +2,b)

def extract_max(sorted_list):
    top_10_count = []
    for i in range(0,10):
        top_10_count.append(sorted_list[0])
        temp = sorted_list[0]
        sorted_list[0] = sorted_list[-1]
        sorted_list[-1] = temp
        del sorted_list[-1]
        heapify(0,sorted_list)
    return top_10_count

def top_10_site(values,dict):
    top_10_sorted_dict = {}
    for value in values:
        for key in dict:
            if value == dict[key]:
                with open('hosts.txt', 'a') as f:
                    f.write('{} : {} \n'.format(key,value))



def main():
    site_visit_count_dict = get_count()
    sorted_list = heapsort(to_sorte(site_visit_count_dict))
    top_10_site(extract_max(sorted_list),site_visit_count_dict)

main()







