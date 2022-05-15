import os
from azure.ai.textanalytics import TextAnalyticsClient,ExtractSummaryAction
from azure.core.credentials import AzureKeyCredential

def authenticate_client():
    endpoint = os.environ["AZURE_LANGUAGE_ENDPOINT"]
    key = os.environ["AZURE_LANGUAGE_KEY"]

    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

def summarize(text, max_sentence_count = 4):
    document = [
        text
    ]

    poller = client.begin_analyze_actions(
        document,
        actions=[
            ExtractSummaryAction(max_sentence_count=max_sentence_count)
        ],
    )

    document_results = poller.result()
    for result in document_results:
        extract_summary_result = result[0]
        if extract_summary_result.is_error:
            print("...Is an error with code '{}' and message '{}'".format(
                extract_summary_result.code, extract_summary_result.message
            ))
            raise RuntimeError()
        else:
            return " ".join([sentence.text for sentence in extract_summary_result.sentences])

if __name__ == "__main__":
    print(summarize("The extractive summarization feature uses natural language processing techniques to locate key sentences in an unstructured text document. "
            "These sentences collectively convey the main idea of the document. This feature is provided as an API for developers. "
            "They can use it to build intelligent solutions based on the relevant information extracted to support various use cases. "
            "In the public preview, extractive summarization supports several languages. It is based on pretrained multilingual transformer models, part of our quest for holistic representations. "
            "It draws its strength from transfer learning across monolingual and harness the shared nature of languages to produce models of improved quality and efficiency.", 2))