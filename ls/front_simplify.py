#-*- coding:utf-8 -*-
"""front_simplify.py
"""
from __future__ import print_function
import sys, re,codecs

def make_ea_2_ascii_table():
 # https://www.w3schools.com/python/ref_string_translate.asp
 x = 'ÜäñöùüĀāīŚśūḍṃṅṇṚṛṢṣṭ…²ÉÑÖÜâäèéñöüĀāĪīŚśŪūḌḍṂṃṄṅṆṇṚṛṢṣṬṭ'
 y = 'uanouuaaussudmnnrrsst  enouaaeenouaaiissuuddmmnnnnrrsstt'
 mytable = str.maketrans(x, y)
 return mytable

ea_2_ascii_table = make_ea_2_ascii_table()

def ea_2_ascii(txt):
 ans = txt.translate(ea_2_ascii_table)
 ans = ans.lower()
 return ans


def find_abbr(lsbody,abbrs):
 """ abbrs assumed sorted by descending length of abbreviation. 
  Find the longest abbreviation that starts lsbody.
  This is the FIRST abbreviation that starts lsbody
 """
 for abbr in abbrs:
  if lsbody.startswith(abbr.abbr):
   return abbr
 #print('find_abbr error. lsbody=',lsbody)
 return None

def write_abbrs(fileout,abbrs):
 outarr = []
 for abbr in abbrs:
  out = "%s %s" %(abbr.abbr,abbr.count)
  outarr.append(out) 
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(outarr),"records written to",fileout)

def write_pwbib(fileout,recs):
 outarr = []
 for rec in recs:
  out = '\t'.join([rec.ident,rec.abbr,rec.lslow,rec.tooltip])
  outarr.append(out) 
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(outarr),"records written to",fileout)


class Abbrev:
 def __init__(self,line):
  line = line.rstrip('\r\n')
  parts = line.split('\t')
  self.ls = parts[0]
  if len(parts) == 2:
   self.tip = parts[1]
  else:
   self.tip = None
  self.ls_ascii = ea_2_ascii(self.ls)
  
def check_dup_abbrevs(recs):
 d = {}
 for irec,rec in enumerate(recs):
  ls = rec.ls
  if ls == '':
   print('check_dup: ls is empty string in record',irec+1)
  if ls in d:
   print('duplicate ls:',ls)
  d[ls] = True

def init_abbrevs(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [Abbrev(line) for line in f if not line.startswith(';')]
 print(len(recs),"ls abbreviations read from",filein)
 check_dup_abbrevs(recs)
 return recs

def write_abbrevs(fileout,abbrevs):
 outarr = []
 for abbrev in abbrevs:
  abbr = abbrev.ls.ljust(15)
  tip = abbrev.tip
  if tip == None:
   tip = '[unknown]'
  out = '%s\t%s' % (abbr,tip)
  outarr.append(out)
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(abbrevs),"written to",fileout)

def write_pwabbrs(fileout,abbrevs):
 outarr = []
 for abbrev in abbrevs:
  abbr = abbrev.abbr.ljust(15)
  tip = abbrev.tooltip
  out = '%s\t%s' % (abbr,tip)
  outarr.append(out)
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(abbrevs),"written to",fileout)
 
if __name__=="__main__":
 filein = sys.argv[1] #  front.txt 
 filebib = sys.argv[2]  # pwbib_input.txt
 fileout = sys.argv[3] # edited and sorted version of front.txt
 fileout1 = sys.argv[4] # sorted version of pwbib_input
 abbrevs = init_abbrevs(filein) # ls abbreviations for sch

 pwabbrs = init_pwbib(filebib)
 # dictionary comprehension technique
 # 
 pwd = {x.abbr.lower():x for x in pwabbrs}
 
 pwabbrs1 = sorted(pwabbrs , key = lambda x : x.abbr_ascii)
 abbrevs1 = sorted(abbrevs , key = lambda x : x.ls_ascii)
 nok = 0
 notok = 0
 for abbrev in abbrevs:
  k = abbrev.ls.lower()
  if abbrev.tip != None:
   # abbreviation is given by Schmidt
   abbrev.tip = '(SCH) %s' %abbrev.tip
  if k in pwd:
   nok = nok + 1
   pwabbr = pwd[k]
   pwtip = '(PW) %s' % pwabbr.tooltip 
   if abbrev.tip != None:
    print('COMPARE: tips for %s' % abbrev.ls)
    print('   '+abbrev.tip )
    print('   '+pwtip)
   abbrev.tip = pwtip
  else:
   notok = notok + 1
 print('sch found in pw = %s, not found = %s' %(nok,notok))
 write_abbrevs(fileout,abbrevs1)
 write_pwabbrs(fileout1,pwabbrs1)
 exit(1)
 #print(len(unknowns),"unknown distinct ls")
 unknowns_sort = sorted(unknowns,key = lambda x : x.abbr)
 write_abbrs(fileother,unknowns_sort)
 if True:
  filename = 'temp_pwbib_input_alpha.txt'
  write_pwbib(filename,abbrs_sort)
 if False:
  filename = 'temp_pwbib_unknown_alpha.txt'
  write_pwbib(filename,unknowns_sort)

 
