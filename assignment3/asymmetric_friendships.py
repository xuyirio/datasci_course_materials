import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
  if record[0] > record[1]:
    pair = (record[1], record[0])
  else:
    pair = (record[0], record[1])
  mr.emit_intermediate(pair, record)

def reducer(key, list_of_values):
  # key: pair
  # value: friendship
  if len(list_of_values) == 1:
    mr.emit(key)
    mr.emit((key[1], key[0]))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
