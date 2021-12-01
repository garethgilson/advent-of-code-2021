import fileinput

print("Starting program...")

# start at -1 to allow the first measurement (where there is no comparison) to set the count to 0
depthMeasurementIncreases = -1

measurements = list()

with fileinput.input(files='input/20211201-sonar-sweep.txt') as input:
    for line in input:
        measurements.append(int(line))

last_measurement = 0
window_start = 0
window_end = 3
still_looping = 1
while still_looping:
    new_measurement = 0
    for measurement in measurements[window_start:window_end]:
        new_measurement += measurement

    if new_measurement > last_measurement:
        depthMeasurementIncreases += 1

    last_measurement = new_measurement
    new_measurement = 0
    window_start += 1
    window_end += 1
    if window_end > len(measurements):
        still_looping = 0

print("The depth measurement increased " + str(depthMeasurementIncreases) + " times.")
