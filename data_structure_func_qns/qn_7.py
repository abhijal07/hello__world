def simulate_movement(size,moves):
    result=0
    for i in moves:
        result+=i
        if result<0:
            result=0
        elif result>=size:
            result=size-1
    
    return result
size=10
moves = [3, 2,-1, 5,-8, 2]
print(simulate_movement(size,moves))
            
