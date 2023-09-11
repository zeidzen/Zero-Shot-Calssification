from fastapi import FastAPI, HTTPException, Request, status
from core import SentimentAnalysis
from request_response_schema import ReqSentence, ReqSentences, ResSentence, ResSentences
from typing import List

     
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/classify_sentence/")
async def classify_sentence(data:ReqSentence) -> ResSentence:
    try:
        set_obj = SentimentAnalysis(data.candidate_labels)
        results = set_obj.single_sentence(sentence=data.sentence)
        return results
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("/classify_multi_sentences/")
async def classify_multi_sentences(data:ReqSentences) -> List[ResSentences]:
    try:
        set_obj = SentimentAnalysis(data.candidate_labels)
        results = set_obj.multi_sentence(data.sentences)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))    
    
        
# To run the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)