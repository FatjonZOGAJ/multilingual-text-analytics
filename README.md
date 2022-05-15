# multilingual-text-analytics

## Architecture
### Original Pipeline
Text is translated to English and then back to the original language.
![alt text](img/Datathon_pipeline_original.png)

### Proposed Pipeline
Extends the original pipeline with an additional branch and compares the results to access precision.
![alt text](img/Datathon_pipeline_new.png)

### Tasks
- [x] EN-DE Translation
- [x] DE-EN Translation
- [x] EN Summarization
- [x] DE Summarization
- [x] EN Extractive Summary
- [x] DE Extractive Summary
- [x] EN NLP
- [x] EN-DE Entity translation
- [x] Entity Matching

### Steps to run and reproduce

### For setup, source our setup.sh script. This will create the environment and set the environment variables.

### Please install the dependencies from requirements.txt

### To run our complete pipeline, please run the Pipeline.ipynb file in notebooks/
Our pipeline takes care of all function calls automcatically
