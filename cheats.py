# %% Functii pentru citirea și formatarea datelor de intrare

#%%
def multi_spilt(str, separators):
	output = [str]
	for c in list(separators):
		output = [x for s in output for x in s.split(sep=c)]
		output = list(filter(lambda s: s != '', output))
	return output

print(multi_spilt("Ana, are, mere. Radu## Are#pere.", ".#,"))
# OUTPUT: ['Ana', ' are', ' mere', ' Radu', ' Are', 'pere']

#%% format_string_list(lista, functii conversie tipuri de date)
def format_string_list(l, *types):
	return [types[i](l[i]) for i in range(0, len(types))]

print(format_string_list(["PP", "12", "13.5"], str, int, float))

#%% Read file and tokenize
import re

infile = open("file.in","r")
outfile = open("file.out")

s = infile.readline()
print(s)
print(re.findall("[\w-]+", s, flags=0))

# decimals
print(re.findall('\d+\.+?\d+', s, flags=0))

# sentences
print(re.findall('[^!?.]+', s, flags=0))

#%% Binary search

def bsearch(list, val):
   list_size = len(list) - 1
   idx0 = 0
   idxn = list_size
   # Find the middle most value
   while idx0 <= idxn:
      midval = (idx0 + idxn)// 2
      if list[midval] == val:
         return midval
      # Compare the value the middle most value
      if val > list[midval]:
         idx0 = midval + 1
      else:
         idxn = midval - 1
      if idx0 > idxn:
         return None

# Initialize the sorted list
list = [2,7,19,34,53,72]

# Print the search result
print(bsearch(list,72))
print(bsearch(list,11))

#%% Recursive binsearch

def bsearch(list, idx0, idxn, val):
   if (idxn < idx0):
      return None
   else:
      midval = idx0 + ((idxn - idx0) // 2)
   # Compare the search item with middle most value
      if list[midval] > val:
         return bsearch(list, idx0, midval-1,val)
      elif list[midval] < val:
         return bsearch(list, midval+1, idxn, val)
      else:
         return midval
list = [8,11,24,56,88,131]
print(bsearch(list, 0, 5, 24))
print(bsearch(list, 0, 5, 51))

#%% lucru cu date

import datetime as dt
d = dt.datetime.strptime(f'{1}.{12}.{2021}', '%d.%m.%Y')

acum = dt.datetime.now()

an_curent = int(acum.strftime("%Y"))
saptamana_curenta = int(acum.strftime("%U"))

aniversare = d.replace(year=an_curent)

zi = aniversare.weekday()
ziua = aniversare + dt.timedelta(days=5 - zi)

import calendar

zile_februarie = 28
if calendar.isleap(an_curent):
   zile_februarie = 29
ultima_zi_luna = ["luna 0 nu exista", 31, zile_februarie, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

months = ["zero", "Ianuarie", "Februarie", "Martie", "Aprilie", "Mai", "Iunie", "Iulie", "August", "Septembrie", "Octombrie",
              "Noiembrie", "Decembrie"]
days = ['Luni', 'Marti', 'Miercuri', 'Joi', 'Vineri', 'Sambata', 'Duminica']

#%% frecv

import re
import collections as c

f = open("date.txt", "r")
s = f.read()
cuv = re.findall('[\w-]+', s)

d = c.Counter(cuv)
lista_cuvinte = sorted(d, key=d.get, reverse=True)
# met 2
for cuvant in lista_cuvinte:
   print(cuvant, d[cuvant])

#%% DI
l={1,2,3,4,5}
def DI (l,p,u):
   if p != u:
      m=(p+u)//2
      r1=DI(l, p, m)
      r2=DI(l, m+1, u)
      return max(r1,r2)
   else:
      return l[p]

print(DI (l,0,len(l)-1))

#%% Parse CNP
import datetime as dt
cnp="5020904070135"

def prefix_an(n):
   if n == 1 or n == 2:
      return "19"
   elif n == 3 or n == 4:
      return "18"
   elif n == 5 or n == 6:
      return "20"
   else:
      return "err"
b = dt.datetime.strptime(f'{int(cnp[5:7])}.{int(cnp[3:5])}.{prefix_an(int(cnp[0]))+cnp[1:3]}', '%d.%m.%Y')
print(f'{int(cnp[5:7])}.{int(cnp[3:5])}.{prefix_an(int(cnp[0]))+cnp[1:3]}')