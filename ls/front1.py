#-*- coding:utf-8 -*-
"""front1.py
"""
from __future__ import print_function
import sys, re,codecs

def get_ls_pw(text):
 "All <ls>X</ls>"
 lsarr = re.findall(r'<ls>.*?</ls>',text)
 return lsarr

def generate_ab_ls(lsarr):
 """ combine <ls> and following <ln>
 """
 val = None # previous <ls>x</ls>
 for idx,item in enumerate(lsarr):
  if idx == 0:
   if item.startswith('<ln>'):
    yield item
   else:  # it is <ls>
    val = item
  elif item.startswith('<ls>'):
   if val != None:
    yield val
   val = item
  else: # item = '<ln>'
   if val != None:
    newval = val + item
    yield newval
    val = None
   else:
    yield item
    val = None
 if val != None:
  yield val  # last one

def lsab1_merge(lsarr):
 """ assume each item x in the lsarr list has one of three forms:
  <ls>X</ls><ln>Y</ln>  -> <ls>ZY</ls>
  <ls>X</ls> or -> <ls>Z</ls>
  <ln>Y</ln> or -> <ls>Y</ls>
  where Z is X with the spaces removed
  for ab
 """
 ans = []
 if False:
  n = len(lsarr)
  if n != 0:
   print('lsab1_merge',n)
   for a in lsarr:
    print(a)
   print('quitting') 
   #exit(1)
 for a in lsarr:
  #if a.startswith('<ls>VĀMANA</ls>'): print('a=',a)
  m = re.search(r'^<ls>VĀMANA</ls><ln>(.*?)</ln>$',a)
  if m != None:
   ln = m.group(1)
   d = '<ls>VĀMANA %s</ls>' %ln
   if False:
    print("ab1_merge: '%s' -> '%s'" %(a,d))
   ans.append(d)
   continue
  # 'Usual' case
  b = a.replace(' ','')
  c = b.replace('ln>','ls>')
  # is VĀMANA handled right?  It should have no period in PW.
  d = c.replace('</ls><ls>','')
  ans.append(d)
 return ans

def get_ls_ab(text,option):
 """ remove a lot of stuff that is in the way of ls identification
 """
 text = re.sub(r'<ab>.*?</ab>',' ',text)
 text = re.sub(r'<lex>.*?</lex>',' ',text)
 text = re.sub(r'<bot>.*?</bot>',' ',text)
 text = re.sub(r'<is>.*?</is>',' ',text)
 text = re.sub(r'{%.*?%}',' ',text)
 text = re.sub(r'{#.*?#}',' ',text)
 # replace <x> with <ln>x</ln> when x starts with  a digit
 # 10-26-2021 This change made in temp_pw_AB_02.txt
 #text = re.sub(r'<([1-9].*?)>',r'<ln>\1</ln>',text)
 lsarr0 = re.findall(r'<l[sn]>.*?</l[sn]>',text)
 lsarr1 = list(generate_ab_ls(lsarr0))
 if option == 'ab':
  lsarr = lsarr1
 else:  # ab1
  lsarr = lsab1_merge(lsarr1)
 return lsarr

def markls(entry,option):
 text = ' '.join(entry.datalines)
 if option == 'pw':
  lsarr = get_ls_pw(text)
 else:
  lsarr = get_ls_ab(text,option)
 if False: # dbg
  L = entry.metad['L']
  if L == '2':
   print('chk',L,'\n'.join(lsarr))
 entry.lsarr = lsarr

def write_ls(fileout,entries):
 with codecs.open(fileout,"w","utf-8") as f:
  nentry = 0 # number of entries with an ls
  nls = 0 # total number of ls entries
  for entry in entries:
   lsarr = entry.lsarr
   n = len(lsarr)
   if n == 0:
    continue
   nentry = nentry + 1
   nls = nls + n
   outarr = []
   L = entry.metad['L']
   k1 = entry.metad['k1']
   outarr.append('; %s %s (%s)' % (L,k1,n))
   for ls in lsarr:
    outarr.append(ls)
   outarr.append('; --------------------')
   for out in outarr:
    f.write(out+'\n')
 print(nentry,'entries have ls markup')
 print(nls,'Total ls markup instances')

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

class PWBIB(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  p = line.split('\t')
  assert len(p)== 4
  self.ident,self.abbr,self.lslow,self.tooltip = p
  self.count = 0
  self.abbr_ascii = ea_2_ascii(self.abbr)

def init_pwbib(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  recs = [PWBIB(line) for line in f]
 print(len(recs),"pwbib read from",filein)
 # check for duplicate idents
 d = {}
 for irec,rec in enumerate(recs):
  if rec.ident in d:
   print("ERROR: duplicate ident",rec.ident)
  d[rec.ident] = True
 # check for duplicate lower-case abbr
 d = {}
 for irec,rec in enumerate(recs):
  x = rec.abbr_ascii.lower()
  if x in d:
   print("ERROR: duplicate abbr lowered",x,d[x])
  d[x] = rec.abbr

 return recs

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

def update_abbrs(line,abbrs1,unknowns):
 for m in re.finditer(r'<ls>([^0-9].*?)</ls>',line):
  ls = m.group(1)
  if ls.startswith('II,'): #Similar to numeric
   continue
  if ls.startswith('S. '): #Similar to numeric (Seite = page)
   if not ls.startswith('S. S. S.'):
    continue
  pwbibrec = find_abbr(ls,abbrs1)
  if pwbibrec != None:
   pwbibrec.count = pwbibrec.count + 1
   continue
  # Use pwbibrec to generate a new PWBIB record
  # Assume unknowns is, like abbrs1, a list of PWBIB records,
  # sorted like abbrs1
  pwbibrec = find_abbr(ls,unknowns)
  if pwbibrec != None:
   pwbibrec.count = pwbibrec.count + 1
   continue
  # ls is a new unknown
  templine = '\t'.join(['_','_','_','_'])
  rec = PWBIB(templine)
  # now fill in values for rec
  n = len(unknowns)
  rec.ident = 'Z%s' % (n+1,)
  rec.abbr = ls
  rec.lslow = ls.capitalize()
  rec.tooltip = '[unknown literary source]'
  rec.count = rec.count + 1
  # add rec to unknowns
  unknowns.append(rec)
  unknowns.sort(key = lambda x : len(x.abbr),reverse=True)
   
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

def test_make_ls():
 lsarr = [
  "AIT.", "CHR.", "GOP. BR.", "Gött. Nachr. 1880", "KAIYY.", 
  
  "MADHYAM.", "SCHLEGEL", "ĀJAN.", "ŚR.", "ŚRĪPATI", # Friedrich Schlegel
  "ŚĀŚVATA", "", "", "", "", 
  "", "", "", "", "", 
  "", "", "", "", "", 
  "", "", "", "", "", 
 ]
 
 n = 1
 for ls in lsarr:
  if ls == '':
   continue
  ident = 'Y%03d'%n
  n = n + 1
  line = '\t'.join([ident,ls,ls.capitalize(),'[unknown literary source]'])
  print(line)
 print('finished with test routine')
 exit(1)

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

 
