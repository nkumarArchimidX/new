import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
 
def sample_classify_document_single_label(text):
   
    endpoint = "https://textclassificationlangaugemodel.cognitiveservices.azure.com/"  
    key = "85fb707c375147baae5206eb5cdbfa1c"  
    project_name = "archimidx"  
    deployment_name = "classification"  
     
    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
    )
 
    while True:
       
        document_text = text
 
        # if document_text.lower() == 'exit':
        #     print("Exiting the classifier.")
        #     break
 
        document = [document_text]
 
        poller = text_analytics_client.begin_single_label_classify(
            document,
            project_name=project_name,
            deployment_name=deployment_name
        )
 
        document_results = poller.result()
        for doc, classification_result in zip(document, document_results):
            if classification_result.kind == "CustomDocumentClassification":
                classification = classification_result.classifications[0]
                
                return {(classification.category,):classification.confidence_score}
            #     print("The document text '{}' was classified as '{}' with confidence score {}.".format(
            #         doc, classification.category, classification.confidence_score)
            #     )
            # elif classification_result.is_error is True:
            #     print("Document text '{}' has an error with code '{}' and message '{}'".format(
            #         doc, classification_result.error.code, classification_result.error.message
            #     ))
 
# if __name__ == "__main__":
#     print(sample_classify_document_single_label("exam"))