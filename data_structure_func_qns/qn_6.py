def distribute_tasks(server_loads,new_tasks):
    for i in range(new_tasks):
        server_loads.sort()
        server_loads[0]+=1
    return server_loads
server_loads = [10, 5, 2, 8]
new_tasks = 5
print(distribute_tasks(server_loads,new_tasks))