from datetime import datetime,timedelta
fmt = '%d/%m/%Y:%H:%M:%S'


def main():
    with open('log.txt','r') as f:
        dict = {}
        for line in f:
            required = line.replace('[',"").replace(']',"").replace('Jul','07').split(' ')
            if required[0] not in dict:
                if required[-2] != '200':
                    list = []
                    c = datetime.strptime(required[3],fmt)
                    list.insert(0,c)
                    list.insert(1,1)
                    dict[required[0]] = list
            else:
                if dict[required[0]][1] < 3:
                    if required[-2] != '200':
                        b = datetime.strptime(required[3],fmt)
                        if int((b-dict[required[0]][0]).total_seconds()) <= 20:
                            dict[required[0]][1] += 1
                            if dict[required[0]][1] == 3:
                                del dict[required[0]][0]
                                dict[required[0]].insert(0,b)
                else:
                    a = datetime.strptime(required[3],fmt)
                    d = int((a-dict[required[0]][0]).total_seconds())
                    if d <= 300:
                        with open('blocked.txt','a') as f:
                            f.write('{}'.format(line))
                    else:
                        if required[-2] != '200':
                            del dict[required[0]][1]
                            del dict[required[0]][0]
                            c = datetime.strptime(required[3],fmt)
                            dict[required[0]].insert(0,c)
                            dict[required[0]].insert(1,1)
    return dict

main()
