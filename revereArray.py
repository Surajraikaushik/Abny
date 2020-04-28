def reverseArray(array , rev_order):
  ws =[]
  f = len(sd)
  for i in range(rev_order , f):
    ws.append(array[i])
  for j in range(rev_order):
    d = len(ws)
    ws.insert(d, array[j])
  print(ws)
sd= [1,2,3,4,5,6,7,8]
reverseArray(sd,3)
