import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    words_nonrepeated = []
    for w in words:
      if w not in words_nonrepeated:
        words_nonrepeated.append(w)
        mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    # key: word
    # value: document identifier
    doc_ids = []
    for v in list_of_values:
      doc_ids.append(v)
    mr.emit((key, doc_ids))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
