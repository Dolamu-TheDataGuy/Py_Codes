import math

for i in range(8):
    mark = ""
    work_session = math.floor(i/2)
    for tick in range(work_session):
        mark += "✔"
    print(mark)
