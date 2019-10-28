from bdateutil import parser

year = "2019"

f = open("data.txt","r")
output = open("output.csv", "w+")
output.write("Subject,Start Date,Start Time,End Date,End Time,All Day Event,Description,Location,Private\n")

data = []
current = []
for line in f:
    if line[0:3] in ["Mon","Tue", "Wed", "Thu", "Fri"]:
        data.append(current)
        current = [line.strip()]
    else:
        current.append(line.strip())

data.append(current)
data = data[1:]
# Subject	Start Date	Start Time	End Date	End Time	All Day Event	Description	Location	Private

for day in data:
    print(len(day), day)
    date = str(parser.parse(day[0] + year))[0:10]
    for i in range(1, len(day) - 1, 3):
        first = day[i]
        second = day[i + 1]
        third = day[i + 2]
        print(first, second, third)
        pointer = 0
        while True:
            if third[pointer] == "Q" or third[pointer] == "W":
                subject = third[0:pointer]
                location = third[pointer::]
                break
            pointer += 1
        times = first.split("-")
        description = second
        initials = description.split(" ")[1:]
        subject += " - " + initials[0][0] + initials[1][0]
        print(subject)
        if "QED" not in third and "Registration" not in third:
            output.write(subject + "," + date + "," + times[0] + ","+ date + "," + times[1] + "," + "FALSE" + "," + description + "," + location + "," + "TRUE\n")

