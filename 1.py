connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]

Rome = 0
Average_Time = 0

for details in connections:
    cityfrom, cityto, time = details
    if cityto == 'Rome':
        Rome += 1
        Average_Time += time

if Rome == 0:
    print('There are no connections to Rome')
else:
    averagetime = Average_Time / Rome
    print(f"{Rome} connections lead to Rome with an average flight time of {averagetime} minutes")
    