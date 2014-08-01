import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
  mr.emit_intermediate(record[0], 1)

def reducer(key, list_of_values):
    # key: person
    # value: friend count
    count = 0
    for v in list_of_values:
      count += 1
    mr.emit((key, count))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
