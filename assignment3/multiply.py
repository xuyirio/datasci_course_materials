import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
  if record[0] == 'a':
    i = record[1]
    for k in range(5):
      mr.emit_intermediate((i, k), record)
  else:
    k = record[2]
    for i in range(5):
      mr.emit_intermediate((i, k), record)

def reducer(key, list_of_values):
  # key: (i, k)
  # value: matrix record
  A_values = []
  B_values = []
  for v in list_of_values:
    if v[0] == 'a':
      A_values.append(v)
    else:
      B_values.append(v)

  output = 0
  for a in A_values:
    for b in B_values:
      if a[2] == b[1]:
        output += a[3]*b[3]
  mr.emit((key[0], key[1], output))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
