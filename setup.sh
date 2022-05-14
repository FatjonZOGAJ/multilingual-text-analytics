#!/bin/bash
# call source ./setup.sh

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

cd ..
python3 -m venv mta
deactivate
source mta/bin/activate
pip install azure-ai-textanalytics --pre

export AZURE_LANGUAGE_ENDPOINT=https://datathon.cognitiveservices.azure.com/
export AZURE_LANGUAGE_KEY=abdeac0882324fb59b2cf327e84f783a

export AZURE_TRANSLATION_ENDPOINT=https://api.cognitive.microsofttranslator.com/
export AZURE_TRANSLATION_KEY=ed4486cc91334c13863a64530126be25