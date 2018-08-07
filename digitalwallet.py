import csv
from collections import defaultdict
from datetime import datetime,timedelta

def get_onedegreefriends():
    with open('batch_payment_new.txt','r') as f:
        next(f)
        dict1 = {}
        dict1 = defaultdict(list)
        count = 0
        for line in csv.reader(f):
            if dict1[line[1]] == []:
                dict1[line[1]].append(float(line[3]))
                dict1[line[1]].append([line[2]])
            elif line[2] not in dict1[line[1]][1]:
                dict1[line[1]][1].append(line[2])
                if float(line[3]) > dict1[line[1]][0]:
                    dict1[line[1]][0] = float(line[3])
            elif float(line[3]) > dict1[line[1]][0]:
                dict1[line[1]][0] = float(line[3])

            if dict1[line[2]] == []:
                dict1[line[2]].append(float(line[3]))
                dict1[line[2]].append([line[1]])
            elif line[1] not in dict1[line[2]][1]:
                dict1[line[2]][1].append(line[1])
                if float(line[3]) > dict1[line[2]][0]:
                    dict1[line[2]][0] = float(line[3])
            elif float(line[3]) > dict1[line[2]][0]:
                dict1[line[2]][0] = float(line[3])
    return dict1

def get_twodegreefriends(dict1):
    dict2 = {}
    dict2 = defaultdict(list)
    for i in dict1:
        dict2[i].insert(0,dict1[i][0])
        dict2[i].insert(1,[])
        for j in dict1[i][1]:
            if j not in dict2[i][1]:
                dict2[i][1].append(j)
            for k in dict1[j][1]:
                if i != k and k not in dict2[i][1]:
                    dict2[i][1].append(k)
    return dict2

def get_threedegreefriends(dict1,dict2):
    dict3 = {}
    dict3 = defaultdict(list)
    for i in dict2:
        dict3[i].insert(0,dict2[i][0])
        dict3[i].insert(1,[])
        for j in dict2[i][1]:
            if j not in dict3[i][1]:
                dict3[i][1].append(j)
            for k in dict1[j][1]:
                if i != k and k not in dict3[i][1]:
                    dict3[i][1].append(k)
    return dict3

def get_fourdegreefriends(dict1,dict3):
    dict4 = {}
    dict4 = defaultdict(list)
    for i in dict3:
        dict4[i].insert(0,dict3[i][0])
        dict4[i].insert(1,[])
        for j in dict3[i][1]:
            if j not in dict4[i][1]:
                dict4[i][1].append(j)
            for k in dict1[j][1]:
                if i != k and k not in dict4[i]:
                    dict4[i][1].append(k)
    return dict4

def payment_graph(line,dict5,deadline_time):

    fmt = '%Y-%m-%d %H:%M:%S'
    current_time1 = datetime.strptime(line[0],fmt)
    if deadline_time == []:
        deadline_time.append(datetime.strptime(line[0],fmt))
        dict5[line[1]].append(line[2])
        dict5[line[2]].append(line[1])
        return 'correct'
    elif int((current_time1 - deadline_time[0]).total_seconds()) > 60:
        deadline_time[0] = datetime.strptime(current_time1,fmt)
        for i in dict5:
            del dict5[i]
        dict5[line[1]].append(line[2])
        dict5[line[2]].append(line[1])
        return 'correct'
    else:
        dict5[line[1]].append(line[2])
        dict5[line[2]].append(line[1])
        if len(dict5[line[1]]) > 10 or len(dict5[line[2]]) > 10:
                return 'unverified'
        else:
            return 'correct'

def get_output(dict1,dict4):
    dict5 = {}
    dict5 = defaultdict(list)
    fmt = '%Y-%m-%d %H:%M:%S'
    current_time = '2016-11-01 17:38:25'
    deadline_time = []
    time1 = datetime.strptime(current_time,fmt)
    with open('stream_payment_new.txt','r') as f:
        next(f)
        for line in csv.reader(f):
            time2 = datetime.strptime(line[0],fmt)
            if (time1 - time2).days > 2:
                with open('output4.txt','a') as f:
                    f.write('{},{}\n'.format('unverified','Reason:Expired'))
            elif dict4[line[2]] == [] or dict4[line[1]] == []:
                with open('output4.txt','a') as f:
                    f.write('{}\n'.format('unverified'))
            elif float(line[3]) > dict4[line[1]][0]:
                with open('output4.txt','a') as f:
                    f.write('{},{}\n'.format('unverified','Reason:exceeded'))
            elif payment_graph(line,dict5,deadline_time) == 'unverified':
                with open('output4.txt','a') as f:
                    f.write('{},{}\n'.format('unverified','Reason:suspicious'))
            elif line[1] not in dict4[line[2]][1]:
                    with open('output4.txt','a') as f:
                        f.write('{}\n'.format('unverified'))
            else:
                with open('output4.txt','a') as f:
                    f.write('{}\n'.format('trusted'))

def main():
    fmt = '%Y-%m-%d %H:%M:%S'
    dict1 = get_onedegreefriends()
    dict2 = get_twodegreefriends(dict1)
    dict3 = get_threedegreefriends(dict1,dict2)
    dict4 = get_fourdegreefriends(dict1,dict3)
    get_output(dict1,dict4)

main()
