readings = [25, -999, 30, 22, -999, 35, 28, -999]
clean_readings = []
for num in readings:
    if num!= -999:
        clean_readings.append(num)

print(clean_readings)