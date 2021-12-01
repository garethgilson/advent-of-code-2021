import fileinput

print("Starting program...")

depthMeasurementIncreases = 0
with fileinput.input(files=('input/20211201-sonar-sweep.txt')) as input:
    lastLine = 0
    for line in input:
        if 0 < lastLine < int(line):
            depthMeasurementIncreases += 1
        lastLine = int(line)

print("The depth measurement increased " + str(depthMeasurementIncreases) + " times.")