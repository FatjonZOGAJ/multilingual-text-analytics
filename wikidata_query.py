import requests

def query(search_term, translated_lang='de'):
    params = dict(
        action='wbsearchentities',
        format='json',
        language='en',
        uselang=translated_lang,
        type='item',
        search=search_term
    )

    # print("Search for item...", end='')
    response = requests.get('https://www.wikidata.org/w/api.php?', params).json()
    return response

def get_translated_entity(search_term, translated_lang='de'):
    res = query(search_term, translated_lang)
    search = res['search']
    if len(search) > 0:
        out = search[0]['label']  
    else:
        out = search_term

    return search_term, out

print(query('ibuprofen'))
languages = ['en', 'de', 'es', 'al']
terms = [
        'ibuprofen', 'diabetes',
        'Atorvastatin', 'Amoxicillin', 'Lisinopril',
        'Levothyroxine', 'Albuterol', 'Metformingc',
        'Lipitor', 'Cholesterol',
        ]

for t in terms:
    tup = []
    for l in languages:
        tup.append(get_translated_entity(t, l))
    print(tup)
    print()

# translate entities from english to german and see if they are also included after summarization and translation