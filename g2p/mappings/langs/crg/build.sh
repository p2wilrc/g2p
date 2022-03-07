python fix_case.py

cat crg-tmd-to-dv-words.csv.new crg-tmd-to-dv-morphs.csv.new \
  crg-tmd-to-dv.csv.new crg-equiv.csv > crg-tmd-to-dv-full.csv
#cat crg-tmd-to-dv-words.csv.new crg-tmd-to-dv.csv.new > crg-tmd-to-dv-full.csv

g2p update

python ../../../tests/run.py langs
