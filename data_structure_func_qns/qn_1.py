def find_duplicate_packets(packets):
    d={}
    for i in packets:
        if i in d:
            d[i]+=1
        elif packets.count(i)>1:
            d[i]=1
    return d
packets=[1001, 1002, 1003, 1002, 1004, 1005, 1001, 1003, 1002]
print(find_duplicate_packets(packets))
