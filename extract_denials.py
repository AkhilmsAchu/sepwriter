f = open("denials.txt", "a")


with open("dmesg.txt") as origin:
    for line in origin:
        if not "avc:" in line:
           continue
        try:
            print (line.split(':',2)[2])
            f.write(line.split(':',2)[2])
        except IndexError:
            print
    f.close()
