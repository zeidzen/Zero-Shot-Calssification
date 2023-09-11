from fastapi import FastAPI, HTTPException, Request, status
from core import uncase_classification
from request_response_schema import ReqSentence, ReqSentences, ResSentence, ResSentences
from typing import List

description="""This project will create a Python-based zero-shot text classification RESTful web service using FastAPI and Poetry. The web service will leverage the BERT-based pre-trained models available in the Hugging Face's transformers library.""" 
title='Zero Short Text Classification'
app = FastAPI( title=title, description=description)
    
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/classify_sentence/")
async def classify_sentence(data:ReqSentence) -> ResSentence:
    try:
        set_obj = uncase_classification(data.candidate_labels)
        results = set_obj.single_sentence(sentence=data.sentence)
        return results
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("/classify_multi_sentences/")
async def classify_multi_sentences(data:ReqSentences) -> List[ResSentences]:
    try:
        set_obj = uncase_classification(data.candidate_labels)
        results = set_obj.multi_sentence(data.sentences)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))    
    
        
# To run the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)