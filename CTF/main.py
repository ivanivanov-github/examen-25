with open('q2.enc', 'rb') as fd:
    with open('temp.enc', 'wb') as fd2:
        for line in fd:
            for sub_line in line.split(b'\r'):
                if not sub_line:
                    continue
                fd2.write(sub_line)

with open('q2.png', 'rb') as fd:
    with open('temp.png', 'wb') as fd2:
        for line in fd:
            for sub_line in line.split(b'\r'):
                if not sub_line:
                    continue
                fd2.write(sub_line)

with open('q4.txt', 'rb') as fd:
    with open('q4temp', 'wb') as fd2:
        for line in fd:
            for sub_line in line.split(b'\r'):
                if not sub_line:
                    continue
                fd2.write(sub_line)

# do = True
with open('q1.png', 'rb') as fd:
    with open('q1temp.png', 'wb') as fd2:
        for line in fd:
            for sub_line in line.split(b'\r'):
                # if not do:
                #     fd2.write(sub_line)
                #     do = True
                # else:
                #     do = False
                if not sub_line:
                    continue
                fd2.write(sub_line)