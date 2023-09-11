# **Zero Shot Text Classification**

## Inroduction 
This project will create a Python-based zero-shot text classification RESTful web service using FastAPI and Poetry. The web service will leverage the BERT-based pre-trained models available in the Hugging Face's transformers library.

Zero-shot text classification is a type of machine learning approach that allows a model to recognize and classify new classes based on zero-labeled examples of these classes. This is done by using a pre-trained model that has been trained on a large dataset of text and labels.

![image](https://github.com/zeidzen/HR_resume/assets/36964163/5fa8cf5a-9436-4981-ac03-b8cbf1cd0893)


## Overview of Microservices 
The Python microservice is a versatile tool for text classification using BERT-based models. It can efficiently categorize input text into predefined classes or labels. With support for both single sentences and batches of sentences, it offers flexibility for a wide range of text classification tasks. The microservice's core functionality includes tokenization, prediction, and probability scoring, making it a valuable asset for enhancing natural language understanding and classific

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

7. I the environment is not activated, Activate the environment by  
   - Windows: **.\zero-shot-env-dYV_COdE-py3.11\Scripts\activate**
   - Linux: **source zero-shot-env-dYV_COdE-py3.11/bin/activate**
8. For install dependencies: **poetry install**
9. . Run the project:
   **uvicorn bert_api:app --reload**

## How to use web service


## Model Breif and Zero-Short-Classification approach used



