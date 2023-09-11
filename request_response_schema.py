
from typing import List
from pydantic import BaseModel, Field, field_validator  

class ReqSentence(BaseModel):
    sentence: str
    candidate_labels:List[str] 
    

class ReqSentences(BaseModel):
    sentences: List[str]
    candidate_labels:List[str]
 
class ResSentence(BaseModel):
    predicted_label:str
    predicted_score:float
    
class ResSentences(BaseModel):
    sentence: str
    result:ResSentence