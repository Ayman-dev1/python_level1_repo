ips_List = [
    ('192.168.0.15', 'y'),
    ('192.168.0.22', 'y'),
    ('192.168.0.14', 'y'),
    ('192.168.0.24', 'n'),
    ('192.168.0.81', 'n'),
    ('192.168.0.11', 'y')
]

print(ips_List[3])

print(ips_List[4][0])

print('---- program to print only the yes ips ----')

for item in ips_List:
    if item[1] == 'y':
        last_part = item[0].split('.')[-1]
        print(last_part)

# h.w task ;
# print only the last part of the ip for the valid ips
# 15, 22, 14, 11