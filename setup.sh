mkdir -p data/
cd data/
wget -nc https://gitlab.lip6.fr/scialom/mlsum_data/-/raw/master/MLSUM/de_train.zip
wget -nc https://gitlab.lip6.fr/scialom/mlsum_data/-/raw/master/MLSUM/de_test.zip
wget -nc https://gitlab.lip6.fr/scialom/mlsum_data/-/raw/master/MLSUM/de_val.zip

unzip -n \*.zip

# english doesn't exist?
#wget https://gitlab.lip6.fr/scialom/mlsum_data/-/raw/master/MLSUM/en_train.zip
#wget https://gitlab.lip6.fr/scialom/mlsum_data/-/raw/master/MLSUM/en_test.zip
#wget https://gitlab.lip6.fr/scialom/mlsum_data/-/raw/master/MLSUM/en_val.zip