import collections #conta ocorrências
lista4 = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
#   unique = collections.Counter(seq) #conta ocorrências
#   var = [x for x in unique if unique[x] % 2 == 1]
#   return var[0]
########################################################
#def find_it(seq):
# for x in seq:
#if seq.count(x) % 2 != 0:
#return x
def find_it(seq):
  var = [i for i in seq if seq.count(i) % 2 == 1]
  return var[0]
print(find_it(lista4))
