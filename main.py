import pidprocesssor

my_pid = pidprocesssor.PIDProcessor(0.8, 0.0, 0, 1.0)
current = 0
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
    power = my_pid.output_normal(current)
    current += power
    print(current)
