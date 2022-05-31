#-*- coding:utf-8 -*-
"""make_change_4.py
 
"""
from __future__ import print_function
import sys,re,codecs
import digentry  

class Change(object):
 def __init__(self,lnum,line,newline,metaline):
  self.lnum = lnum
  self.line = line
  self.newline = newline
  self.metaline = metaline
  
def write_changes(fileout,changes):
 outrecs=[]
 prevmeta = None
 for change in changes:
  outarr=[]
  lnum = change.lnum
  line = change.line
  newline = change.newline
  # one correction.
  newline = newline.replace(' </ls>','</ls> ')  # ' H '
  metaline = change.metaline
  metaline = re.sub(r'<k2>.*$','',metaline)
  if prevmeta != metaline:
   outarr.append('; --------------------------------------------------')
   outarr.append('; %s' % metaline)
  else:
   outarr.append(';')
  prevmeta = metaline
  outarr.append('%s old %s' %(lnum,line))
  outarr.append('%s new %s' %(lnum,newline))
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
    for out in outarr:
     f.write(out+'\n')
 print(len(changes),"changes written to",fileout)

drop_periods = {
 'Ko.', 'Abl.', 'Komp.', 'Gen.', 'Nom.', 'Absol.', 'Aufl.', 'Desid.', 'Absol.',
 'Vgl.', 'Beitr.', 'pr.', '.', 'Du.', 'Abl.', 'Bez.', 'best.', 'ff.', 'abstr.', 
 'Adj.', 'Adv.', 'Komm.', 'm.', 'f.', 'n.', 'Lok.', 'vgl.', 'v.u.', 'v.l.', 
 'Partic.', 'Instr.', 'act.', 's.', 'u.', 'Einl.', 'Akk.', 'Dat.', 'Inf.', 'v.a.', 
 'Abstr.', 'st.', 'Bein.', 'adj.', 'Pl.', 'Subst.', 'N.', 'usw.', 'Bez.', 'Bomb.', 'ed.',
 'etc.','Pass.','Bed.','Sg.','Acc.','t.','o.','h.','Mit.','ag.','p.','d.',
 'impers.','Acc.','Art.','No.','Z.','Superl.','a.','Hdschrr.','Konj.','komm.',
 'b.','intrans.','orn.','ist.','i.','v.','l.','trans.','fol.','ist.','Aor.',
 'gedr.','Perf.','von.','ved.','Sch.','].','Vārtt.','dass.','Patron.','Schol.',
 'desgl.','z.','e.','Interj.','Beiw.','Metron.','hinzu.','e.','abst.','Loc.',
 'Intens.','onomat.','Anm.','Hdschr.','Simpl.','Zit.','gedruckt.','Sing.',
 'onomatop.','Calc.','z.B.','Denomin.','S.','B.','Wort.','Festgr.','Ak.',
  'Kl.','Nomin.',
 }
def prelim_helper(x):
 x = re.sub(r'<ls>[^<]*</ls>','',x)
 x = re.sub('{part.*?}','',x)
 x = re.sub('^.*?¦','',x)
 x = re.sub(r'[()]',' ',x)
 x = re.sub(r'[*°]','',x)
 x = re.sub(r'[0-9]+[,.;]','',x)
 x = re.sub(r'{%[^%]*%}','', x)
 x = re.sub(r'<sup>[^<]*</sup>',' ',x)
 x = x.replace('[',' ')
 x = x.replace(']',' ')
 #x = re.sub(r'p\. [0-9]+',' ',x)
 x = re.sub(r'  +',' ',x)
 
 #x = re.sub(r' Adj\.| Adv\.| Komm\.| [mfn]\.','',x)
 parts = re.split(r' +',x)
 periods = [p for p in parts if p.endswith('.')]
 keepsall = [p for p in periods if p not in drop_periods]
 keeps = [p for p in keepsall if not p.lower() == p] # p not all lower-case
 x = ' '.join(keeps)
 return x

def write_changes_prelim(fileout,changes):
 outrecs=[]
 prevmeta = None
 for change in changes:
  outarr=[]
  lnum = change.lnum
  line = change.line
  newline = change.newline
  # one correction.
  newline = newline.replace(' </ls>','</ls> ')  # ' H ' and ' S '
  metaline = change.metaline
  metaline = re.sub(r'<k2>.*$','',metaline)
  if prevmeta != metaline:
   #outarr.append('; --------------------------------------------------')
   #outarr.append('; %s' % metaline)
   pass
  else:
   #outarr.append(';')
   pass
  prevmeta = metaline
  #outarr.append('%s old %s' %(lnum,line))
  newline1 = prelim_helper(newline)
  if newline1.strip() != '':
   outarr.append('%s new %s' %(lnum,newline1))
  if outarr != []:
   outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
    for out in outarr:
     f.write(out+'\n')
 print(len(changes),"changes written to",fileout)

def find_all(a_str, sub):
 """
 https://stackoverflow.com/questions/4664850/how-to-find-all-occurrences-of-a-substring
 """
 start = 0
 while True:
  start = a_str.find(sub, start)
  if start == -1: return
  yield start
  start += len(sub) # use start += 1 to find overlapping matches

def markls_helper(line,old,new):
 # line1 = line.replace(old,new,1)
 parts = re.split(r'(<ls>[^<]*</ls>)',line)
 newparts = []
 for part in parts:
  if part.startswith('<ls>'):
   newpart = part
  else:
   newpart = part.replace(old,new)
  newparts.append(newpart)
 newline = ''.join(newparts)
 if newline != line:
  #a = re.findall(new,newline)
  # If 'new' has '[' or '(', then it is not a 'good' regex.
  # Thus, we use new1 as follows
  m = re.search(r'<ls>[^<]*</ls>',new)
  if m == None:
   print('markls_helper ERROR: line=%s\nnew=%s' %(line,new))
   exit(1)
  new1 = m.group(0)
  # findall can be problematic if there are parentheses, periods, etc in new1.
  #a = re.findall(new1,newline)
  #n = len(a)
  a1 = find_all(newline,new1)
  n = len(list(a1))
 else:
  n = 0
 return newline,n

def markls(line,abbrevs):
 dbg=False
 for abbrev in abbrevs:
  ls = abbrev.ls
  for old,new in abbrev.replacements:
   newline,n = markls_helper(line,old,new)
   if newline != line:
    abbrev.count = abbrev.count + n
    if dbg:
     print("ls='%s'" % ls)
     print("old='%s', new='%s'" %(old,new))
     print('line=%s'%line)
     print('newline=%s'%newline)
    line = newline
 if dbg:
  print('markls quitting')
  exit(1)
 return line
  
def make_changes(entries,abbrevs):
 changes = []
 abbrevs1 = sorted(abbrevs,key = lambda x: len(x.ls), reverse=True)
  
 for ientry,entry in enumerate(entries):
  for iline,line in enumerate(entry.datalines):
   newline = markls(line,abbrevs1)
   if newline != line:
    lnum = entry.linenum1 + iline + 1
    metaline = entry.metaline
    change = Change(lnum,line,newline,metaline)
    changes.append(change)
 return changes

def make_changes_prelim(entries,abbrevs):
 changes = []
 abbrevs1 = sorted(abbrevs,key = lambda x: len(x.ls), reverse=True)
  
 for ientry,entry in enumerate(entries):
  for iline,line in enumerate(entry.datalines):
   newline = markls(line,abbrevs1)
   if True: # newline != line:
    lnum = entry.linenum1 + iline + 1
    metaline = entry.metaline
    change = Change(lnum,line,newline,metaline)
    changes.append(change)
 return changes

class Abbrev:
 def __init__(self,line):
  line = line.rstrip('\r\n')
  parts = line.split('\t')
  self.ls = parts[0]
  self.ls = self.ls.rstrip()
  if self.ls in ['H','S']:
   self.ls = self.ls + ' '
  self.count = 0 # number of instances within xxx.txt
  self.regex = self.ls.replace('.','[.]')
  self.regex = self.regex.replace('(','[(]')
  self.regex = self.regex.replace(')','[)]')
  self.replacements = [
    (' %s' % self.ls,  # old
     ' <ls>%s</ls>' % self.ls),  # new
    ('[%s' % self.ls,  # old
     '[<ls>%s</ls>' % self.ls),  # new
    ('(%s' % self.ls,  # old
     '(<ls>%s</ls>' % self.ls),  # new
   ]

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

def write_lsfreq(fileout,abbrevs0):
 # ascii sort
 abbrevs = sorted(abbrevs0, key = lambda x: ea_2_ascii(x.ls))
 outarr = []
 ntot = 0
 for abbrev in abbrevs:
  n = abbrev.count
  ntot = ntot + n
  ls = abbrev.ls
  nstr = str(n).ljust(5)
  out = '%s %s' %(nstr,ls)
  outarr.append(out)
 with codecs.open(fileout,"w","utf-8") as f:
    for out in outarr:
     f.write(out+'\n')
 print('ls frequencies written to',fileout)
 print(ntot,"total number of ls abbreviations marked")
 
if __name__=="__main__":
 filein = sys.argv[1] # sch.txt
 filein1 = sys.argv[2] # ls abbreviations
 fileout = sys.argv[3] #  
 fileout1 = sys.argv[4] # frequency count
 
 entries = digentry.init(filein)
 abbrevs = init_abbrevs(filein1)
 dbg = False
 if dbg:
  changes = make_changes_prelim(entries,abbrevs)
  write_changes_prelim(fileout,changes)
 else:
  changes = make_changes(entries,abbrevs)
  write_changes(fileout,changes)
 write_lsfreq(fileout1,abbrevs)

 
