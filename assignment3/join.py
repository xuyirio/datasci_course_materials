import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
  order_id = record[1]
  mr.emit_intermediate(order_id, record)

def reducer(key, list_of_values):
  # key: order_id
  # value: record
  orders = []
  items = []
  for v in list_of_values:
    if v[0] == 'order':
      orders.append(v)
    elif v[0] == 'line_item':
      items.append(v)

  if len(orders) == 0 or len(items) == 0:
    return

  output = []
  for order in orders:
    for item in items:
      output = order + item
      mr.emit(output)

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
