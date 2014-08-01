import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    trimed = record[1][:-10]
    mr.emit_intermediate(trimed, 1)

def reducer(key, list_of_values):
    # key: trimed nucleotides
    # value: count
    mr.emit(key)

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
