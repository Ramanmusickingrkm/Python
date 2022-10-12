f = open("States.txt", "rb")
s = f.readlines()
f.close()
f = open("newstates2.txt", "wb")
s.reverse()
for line in s:
    f.write(line)
f.close()


for line in reversed(s):
    f.write(line)


