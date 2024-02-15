time_input = input()
time = time_input.split(':')
hour = int(time[0]) + 1
minute = time[1]
print(hour,':',minute,sep='')