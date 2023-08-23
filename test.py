spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]
 
low = 0
normal = 0   
high = 0 

for spending in spendings:
    if spending < 1000:
        low = low + 1 
    elif spending <= 2500:
        normal = normal + 1
    else:
        high = high + 1

print('Numbers of months with low spendings:', str(low), 'normal spendings:', str(normal), 'high spendings:', str(high), '.')