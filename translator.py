import requests, uuid, json, os

endpoint = os.environ["AZURE_TRANSLATION_ENDPOINT"]
key = os.environ["AZURE_TRANSLATION_KEY"]

path = '/translate'
constructed_url = endpoint + path

headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Ocp-Apim-Subscription-Region': "westeurope",
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

def translate_en_to_de(data):

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
    # print(response[0]['translations'])
    for value in response[0]['translations']:
        print(value['text'])

def translate_de_to_en(data):

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
    for value in response[0]['translations']:
        print(value['text'])


# To use on a list, call method on every list item
en_data = 'The extractive summarization feature uses natural language processing techniques to locate key sentences in an unstructured text document.'
# translate_en_to_de(en_data)

de_data = 'Die extraktive Zusammenfassungsfunktion verwendet Techniken zur Verarbeitung natürlicher Sprache, um Schlüsselsätze in einem unstrukturierten Textdokument zu finden.'
# translate_de_to_en(de_data)

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
    translate_en_to_de(value)