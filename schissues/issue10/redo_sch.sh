version=$1
echo "version $version"
cp temp_sch_$version.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh sch  ../../sch
sh xmlchk_xampp.sh sch
# ok  No problems noticed
cd /c/xampp/htdocs/sanskrit-lexicon/SCH/schissues/issue10/


