import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    names = min(record)+max(record)
    mr.emit_intermediate(names, record)

def reducer(key, list_of_values):
    if len(list_of_values) == 1:
        relationship = list_of_values[0]
        mr.emit((relationship[1], relationship[0]))
        mr.emit((relationship[0], relationship[1]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
