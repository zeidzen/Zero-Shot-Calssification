# **Zero Shot Text Classification**

## Inroduction 

This project will create a Python-based zero-shot text classification RESTful web service using FastAPI and Poetry. The web service will leverage the BERT-based pre-trained models available in the Hugging Face's transformers library.

Zero-shot text classification is a type of machine learning approach that allows a model to recognize and classify new classes based on zero-labeled examples of these classes. This is done by using a pre-trained model that has been trained on a large dataset of text and labels.

![image](https://github.com/zeidzen/HR_resume/assets/36964163/5fa8cf5a-9436-4981-ac03-b8cbf1cd0893)


## Overview of Microservices 

The Python microservice is a versatile tool for text classification using BERT-based models. It can efficiently categorize input text into predefined classes or labels. With support for both single sentences and batches of sentences, it offers flexibility for a wide range of text classification tasks. The microservice's core functionality includes tokenization, prediction, and probability scoring, making it a valuable asset for enhancing natural language understanding and classific.

![image](https://github.com/zeidzen/Zero-Shot-Calssification/assets/36964163/378c9be7-b323-49d9-aed4-998fbd26f920)


## Requirements
- Python version above 3.11.0

## How to Install and Run

1. Git clone the repository
2. Open the project in Visual Studio Code
3. Open the Terminal 
4. Install necessary Libraries:
    **pip install poetry uvicorn**

6. Create environment: 
   **poetry shell**

7. If the environment is not activated, Activate the environment by  
   - Windows: **.\zero-shot-env-dYV_COdE-py3.11\Scripts\activate**
   - Linux: **source zero-shot-env-dYV_COdE-py3.11/bin/activate**
8. For install dependencies: **poetry install**
9. . Run the project:
   **uvicorn bert_api:app --reload**

## How to use web service

In the provided links, you'll discover interactive and alternative API documentation. These resources present a comprehensive list of endpoints, along with detailed information on their respective input and output structures, including any associated constraints for making API calls.

Interactive API docs: **localhost:8000/docs**

Alternative API docs: **localhost:8000/redoc**


![image](https://github.com/zeidzen/Zero-Shot-Calssification/assets/36964163/ca123da0-fb8b-410a-94c1-134882c8dc1d)

<br>

![image](https://github.com/zeidzen/Zero-Shot-Calssification/assets/36964163/2120f9c9-a8a8-47a2-9f8d-7047daa6efc0)


## Model Breif and Zero-Short-Classification approach used




Zero-shot classification is a machine learning task in which a model is trained to classify data from known classes but is then able to classify data from unseen classes without being explicitly trained on them. This is done by using auxiliary information about the unseen classes, such as their descriptions or definitions.

There are two main approaches to zero-shot classification:

      - Attribute-based approaches: These approaches use the auxiliary information about the unseen classes to create a vector representation of each class. The model is then trained to predict the class of a new data point by comparing its vector representation to the vector representations of the known classes.

      -Embedding-based approaches: These approaches use the auxiliary information about the unseen classes to create an embedding space for the classes. The model is then trained to predict the class of a new data point by finding the class with the most similar embedding.

      
The zero-shot classification approach is still a relatively new research area, but it has the potential to be used in a wide variety of applications, such as:

   -Text classification: Classifying text documents of topics that the model has never seen before.

   -Speech recognition: Recognizing speech from speakers that the model has never heard before.
   -Machine translation: Translating text from languages that the model has never been trained on.
   
The zero-shot classification approach is a promising new way to improve the performance of machine learning models in a variety of tasks. As research in this area continues, we can expect to see even more applications of zero-shot classification in the future.

