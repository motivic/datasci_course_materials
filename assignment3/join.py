import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    value = []
    for s in record:
        value.append(s.encode('utf8'))
    order_id = int(value[1])
    mr.emit_intermediate(order_id, value)

def reducer(key, list_of_values):
    for l in list_of_values:
        if l[0] == 'order':
            for m in list_of_values:
                if m[0] == 'line_item':
                    mr.emit(l+m)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
