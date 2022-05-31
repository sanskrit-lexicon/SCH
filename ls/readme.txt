Add ls markup to sch.txt

temp_sch_0.txt   latest from csl-orig:
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch_0.txt
  At csl-orig commit 55c39114b89340f4c99a7c57a143c0663a3259c1
  
front.txt  Extracted from
https://www.sanskrit-lexicon.uni-koeln.de/scans/csldev/csldoc/build/_static/SCH-Nachtraege.htm

==============================================================
temp_sch_1.txt  manual changes while applying change_ls1.py
==============================================================
temp_change_2.txt

python change_ls1.py temp_sch_1.txt front.txt temp_change_2.txt freq_ls1.txt

This was run repeatedly with 'dbg=True' (in main).  This listed
  unmatched words to change_2 which were examined looking for missed
  ls words.  Such words, when found, were added to front.txt.
  Also, several changes were made to temp_sch_1.txt to correct likely errors.
  Ultimately, almost 500 additional words were identified as ls.
Then, once this tedious revision to front.txt was deemed complete,
 the program was run with 'dbg=False'.
 Change records are  written to change_2.txt.  Almost 30,000 lines changed!
 This program also generates frequency of occurrence of the abbreviations.
 
python change_ls1.py temp_sch_1.txt front.txt change_2a.txt freq_ls1.txt
88721 lines read from temp_sch_1.txt
29123 entries found
550 ls abbreviations read from front.txt
26082 changes written to temp_change_2.txt
ls frequencies written to freq_ls1.txt
30739 total number of ls abbreviations marked

==============================================================
Next, we will create front1a.txt by editing front1.txt in light
of pwbib_input.txt, and then we will create change_2.txt


==============================================================
Get list of extended ascii codes, to help with sorting the
abbreviations.
python ea.py front.txt temp_front_ea.txt
22 extended ascii counts written to temp_front_ea.txt
eachars:ÜäñöùüĀāīŚśūḍṃṅṇṚṛṢṣṭ…

cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pw/pywork/pwauth/pwbib_input.txt temp_pwbib_input.txt

python ea.py temp_pwbib_input.txt temp_pwbib_input_ea.txt
34 extended ascii counts written to temp_pwbib_input_ea.txt
eachars:²ÉÑÖÜâäèéñöüĀāĪīŚśŪūḌḍṂṃṄṅṆṇṚṛṢṣṬṭ

x = 'ÜäñöùüĀāīŚśūḍṃṅṇṚṛṢṣṭ…²ÉÑÖÜâäèéñöüĀāĪīŚśŪūḌḍṂṃṄṅṆṇṚṛṢṣṬṭ'
y = 'uanouuaaussudmnnrrsst  enouaaeenouaaiissuuddmmnnnnrrsstt'

==============================================================
pwgbib ls abbreviations may also be useful

cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pwg/pywork/pwgauth/pwgbib_input.txt temp_pwgbib_input.txt

==============================================================
Finding tooltips
Only about 60 of the ls abbreviations have tooltips derived
 from the Schmidt front matter.
 The rest need to be filled in.
 First locus is from the ls abbreviations for PW(K)
cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pw/pywork/pwauth/pwbib_input.txt temp_pwbib_input.txt

parsing pwbib_input is adapted from listls1.py in
 /c/xampp/htdocs/sanskrit-lexicon/PWK/pw_ls/pw_ls_AB/
 front1 and pwbib_input1 are sorted 
python front1.py front.txt temp_pwbib_input.txt front1.txt temp_pwbib_input1.txt
550 ls abbreviations read from front.txt
844 pwbib read from temp_pwbib_input.txt


==============================================================
open questions:
front
front1a:  manual editing of front1
1. (6) Alaṃkāras. typo?  = ?  Alaṃkāraś. (PW) ALAṂKĀRAŚEKHARA,
3. (1) Anarghar. S.  Is 'S.' print error for '5,' ?
4. (3) Antyeṣṭik. not ls?  "antyezwi-kriyA f. funeral ceremonies"
5. 
==============================================================
change_2.txt created from front1a.

python change_ls1.py temp_sch_1.txt front1a.txt change_2.txt freq_ls1a.txt

==============================================================
# generate change_1.txt
python diff_to_changes.py temp_sch_0.txt temp_sch_1.txt change_1.txt
154 changes written to change_1.txt

# generate next version of sch
python updateByLine.py temp_sch_1.txt change_2.txt temp_sch_2.txt
26081 change transactions from change_2.txt


==============================================================
install into csl-orig and check validity
cp temp_sch_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh sch  ../../sch
sh xmlchk_xampp.sh sch
  OK as hoped!

cd /c/xampp/htdocs/sanskrit-lexicon/sch/greek


==============================================================
creation of tooltip file for ls abbreviations
Start with front1a.txt
Change format slightly
python make_scha

cd /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/sch/pywork
cp -r ../../ben/pywork/benauth/ schauth
Manually edit schauth directory

cp /c/xampp/htdocs/sanskrit-lexicon/sch/ls/front1a.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/sch/pywork/schauth/tooltip.txt

manually edit tooltip.txt
  ' +\t' -> '\t'  (removing trailing spaces in ls abbreviations

Re-install sch
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh sch  ../../sch


cd /c/xampp/htdocs/sanskrit-lexicon/sch/ls

==============================================================
Modify basicdisplay.php in csl-websanlexicon
modify /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php

Re-install sch

cd /c/xampp/htdocs/cologne/csl-pywork/v02
in 'inventory.txt', add 'sch' under 'literary sources: ap90, ben,
in makotemplates/redo_postxml.sh,  and 'sch' under '# literary source'
sh generate_dict.sh sch  ../../sch
sh xmlchk_xampp.sh sch

View basic display on localhost to be sure installation looks ok.

modify basicadjust.php in csl-apidev
cp /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php /c/xampp/htdocs/cologne/csl-apidev/basicadjust.php

Test local version of simple search

==============================================================
push to Github:
csl-orig, csl-pywork, csl-websanlexicon, csl-apidev

==============================================================
install at Cologne
pull 
csl-orig, csl-pywork, csl-websanlexicon, csl-apidev

update sch in csl-pywork/v02.

==============================================================
