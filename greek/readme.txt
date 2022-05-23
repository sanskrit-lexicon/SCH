
small number of Greek text fragments in schmidt.

cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch_0.txt
 at csl-orig commit 1be2bd4db20263f9ec52406140be0c199edfbaae


cd /c/xampp/htdocs/sanskrit-lexicon/sch/greek

refer https://github.com/sanskrit-lexicon/GreekInSanskrit/issues/36

temp_sch_1.txt  manually edited per this issue36
5 cases  of form '[greek]X[greek]'

python diff_to_changes.py temp_sch_0.txt temp_sch_1.txt change_1.txt

==============================================================
install into csl-orig and check validity
cp temp_sch_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh sch  ../../sch
sh xmlchk_xampp.sh sch
  OK as hoped!

cd /c/xampp/htdocs/sanskrit-lexicon/sch/greek
