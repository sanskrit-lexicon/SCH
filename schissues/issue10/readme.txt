12-07-2024. 

Ref: https://github.com/sanskrit-lexicon/SCH/issues/10
   BHĀGAVATAPURĀṆA link target

   standardization of sch links for 'Bhāg. P.'
BHĀG. P. akarAla

this directory:
cd /c/xampp/htdocs/sanskrit-lexicon/SCH/schissues/issue10

----
Start with sch.txt from csl-orig at latest commit
  f87f373f9dc250108a8d8f781c1f7bf0afa86da9

cd /c/xampp/htdocs/cologne/csl-orig
git show f87f373f9:v02/sch/sch.txt > /c/xampp/htdocs/sanskrit-lexicon/SCH/schissues/issue10/temp_sch_0.txt

-----------------------------------------------
baseline: all links
196 matches in 192 lines for "Bhāg\. P\." in buffer: temp_sch_0.txt

There are numerous non-standard aspects of <ls>
 e.g. '<ls>Suśr.</ls> 1, 27, 14.' -> '<ls>Suśr. 1,27,14.</ls>'
This applies to all ls with parameters, not only "Bhāg\. P\."

python link_prepare.py temp_sch_0.txt temp_sch_1.txt
88721 read from temp_sch_0.txt
88721 lines written to temp_sch_1.txt


-----------------------------------------------
-----------------------------------------------
-----------------------------------------------

python link_prelim2.py temp_sch_1.txt link_prelim2_1.txt
  196 <ls>Bhāg. P..*?</ls>
    0 <ls n="Bhāg. P..*?</ls>
  196 Total

python link_expand.py link_prelim2_1.txt link_expand_1.txt link_change_1_todo.txt
00196 ALL
00176 STANDARD
00018 CANTDO
00002 OK
00196 TOTAL
all cases accounted for
2 lines written to link_expand_1.txt
18 lines written to link_change_1_todo.txt

Note: there are NO links to expand!

python check_bur.py link_prelim2_1.txt Burnouf.BhP.index.txt temp_check_bur.txt
0 links incompatible with index
-----------------------------------------------
python summary.py 1 temp_sch_1.txt bhagp_standard_1.txt bhagp_nonstandard_1.txt
88721 lines read from temp_sch_1.txt
29123 entries found
196 instances of ls
176 cases written to bhagp_standard_1.txt
20 cases written to bhagp_nonstandard_1.txt

------
cp bhagp_nonstandard_1.txt prechange_2.txt
# Manual edit prechange_2.txt
# Construct change_2.txt
python make_change1.py temp_sch_1.txt prechange_2.txt change_2.txt
14 cases written to change_2.txt

# construct temp_sch_2.txt
python updateByLine.py temp_sch_1.txt change_2.txt temp_sch_2.txt
14 change transactions from change_2.txt
------

sh redo_sch.sh 2
# ok
------
python summary.py 1 temp_sch_2.txt bhagp_standard_2.txt bhagp_nonstandard_2.txt
208 instances of ls
findall_ls_entries: number of lines with duplicates= 0
202 cases written to bhagp_standard_2.txt
6 cases written to bhagp_nonstandard_2.txt
   These 6 are all of form <ls>Bhāg. P. ed. Bomb. x,y,z</ls>

python link_prelim2.py temp_sch_2.txt temp_link_prelim2_2.txt

python check_bur.py temp_link_prelim2_2.txt Burnouf.BhP.index.txt temp_check_bur.txt
0 links incompatible with index.

sh redo_sch.sh 2

++++++++++++++++++++++++++++++

# make change_1.txt
python diff_to_changes_dict.py temp_sch_0.txt temp_sch_1.txt change_1.txt
2 changes written to change_1.txt

python link_prelim2.py temp_sch_1.txt link_prelim2_1.txt
  198 <ls>Bhāg. P..*?</ls>
   13 <ls n="Bhāg. P..*?</ls>
  211 Total

python check_bur.py link_prelim2_1.txt Burnouf.BhP.index.txt temp_check_bur.txt
0 links incompatible with index  # good!

-----------------------------------------
# summary by book order
python summary.py 1 temp_sch_2.txt bhagp_standard_2.txt bhagp_nonstandard_2.txt
208 instances of ls
202 cases written to bhagp_standard_2.txt
6 cases written to bhagp_nonstandard_2.txt

# summary by skandha, adhyaya, verse  # only standard
python summary.py 2 temp_sch_2.txt bhagp_verse_2.txt
208 instances of ls
195 cases written to bhagp_verse_2.txt

--------------------------------------------
Installation version 2
--------------------------------------------
# local installation
sh redo_sch.sh 2
# ok
-----------------------------------
sync csl-orig to Github
cd /c/xampp/htdocs/cologne/csl-orig

git add . # sch.txt
git commit -m "SCH: standardization of links for 'Bhāg. P.'
Ref: https://github.com/sanskrit-lexicon/SCH/issues/110"
#  26170  lines changed.  (So many due to global changes in temp_sch_1.txt
git push

-----------------------------------
sync csl-websanlexicon to Github
cd /c/xampp/htdocs/cologne/csl-websanlexicon

git add . # basicadjust.php
git commit -m "SCH, etc. links for 'Bhāg. P.'
Ref: https://github.com/sanskrit-lexicon/SCH/issues/110"
git push

-----------------------------------
sync csl-apidev to Github
cd /c/xampp/htdocs/cologne/csl-apidev

git add . # basicadjust.php
git commit -m "SCH, etc. links for 'Bhāg. P.'
Ref: https://github.com/sanskrit-lexicon/SCH/issues/110"
git push

-----------------------------------
Sync Cologne server to github
1. csl-orig repo pull
2. csl-websanlexicon pull
3. csl-apidev pull
4. csl-pywork/v02  remake displays for sch, pw, pwg

-----------------------------------
sync this SCH repo to github.
cd /c/xampp/htdocs/sanskrit-lexicon/SCH/schissues/issue10
git add .
git commit -m "standardize links for 'Bhāg. P.' #10"


============================================================
