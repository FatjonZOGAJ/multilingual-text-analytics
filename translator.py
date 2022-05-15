import requests, uuid, json, os

endpoint = os.environ["AZURE_TRANSLATION_ENDPOINT"]
key = os.environ["AZURE_TRANSLATION_KEY"]

def translate_en_to_de(data, key, endpoint):

    path = '/translate'
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': "westeurope",
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    params_to_de = {
        'api-version': '3.0',
        'from': 'en',
        'to': ['de']
    }

    body_to_de = [{
    'text': data
    }]

    request = requests.post(constructed_url, params=params_to_de, headers=headers, json=body_to_de)
    response = request.json()

    # print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
    translated = response[0]['translations'][0]['text']
    return translated

def translate_de_to_en(data, key, endpoint):

    path = '/translate'
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': "westeurope",
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    params_to_en = {
        'api-version': '3.0',
        'from': 'de',
        'to': ['en']
    }

    body_to_en = [{
        'text': data
    }]

    request = requests.post(constructed_url, params=params_to_en, headers=headers, json=body_to_en)
    response = request.json()
    
    # print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
    translated = response[0]['translations'][0]['text']
    return translated

if __name__ == "__main__":
    # To use on a list, call method on every list item
    en_data = 'The extractive summarization feature uses natural language processing techniques to locate key sentences in an unstructured text document.'
    print(translate_en_to_de(en_data, key, endpoint))

    de_data = 'Die extraktive Zusammenfassungsfunktion verwendet Techniken zur Verarbeitung natürlicher Sprache, um Schlüsselsätze in einem unstrukturierten Textdokument zu finden.'
    print(translate_de_to_en(de_data, key, endpoint))

    ## Translate these sentences
    document = [
            "The extractive summarization feature uses natural language processing techniques to locate key sentences in an unstructured text document. "
            "These sentences collectively convey the main idea of the document. This feature is provided as an API for developers. "
            "They can use it to build intelligent solutions based on the relevant information extracted to support various use cases. "
            "In the public preview, extractive summarization supports several languages. It is based on pretrained multilingual transformer models, part of our quest for holistic representations. "
            "It draws its strength from transfer learning across monolingual and harness the shared nature of languages to produce models of improved quality and efficiency. "
        ]

    ## Document for us can be a collection of paragraphs, currently only one entry
    for value in document:
        print(translate_en_to_de(value, key, endpoint))

    ## Tests on medical data:
    data_path = "translation_data/de-en_txt_data/"
    file_de = "german_data.txt"


    file_eng = open(data_path+"english_data.txt", 'r')
    for count, line in enumerate(file_eng.readlines()):
        print(translate_en_to_de(line, key, endpoint))
        if count==2:
            break

    file_de = open(data_path+"german_data.txt", 'r')
    for count, line in enumerate(file_de.readlines()):
        print(line)
        if count==2:
            break



