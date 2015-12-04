import MapReduce
import sys


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    matrix = record[0]
    i = record[1]
    j = record[2]
    value = record[3]
    for k in range(5):
        if matrix == 'a':
            mr.emit_intermediate((i,k), (j,value))
        else:
            mr.emit_intermediate((k,j), (i,value))

def reducer(key, list_of_values):
    a = [0]*5
    b = [0]*5
    for v in list_of_values:
        if a[v[0]] == 0:
            a[v[0]] = v[1]
        else:
            b[v[0]] = v[1]

    total =  sum(x*y for (x,y) in zip(a,b))
    mr.emit((key[0],key[1],total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
