import torch
from transformers import BertTokenizer, BertForSequenceClassification, BertConfig
import torch.nn.functional as F

class uncase_classification:
    
    def __init__(self, candidate_labels) -> None:
        
        self.model_name = "bert-base-uncased"
        self.candidate_labels = candidate_labels
        self.tokenizer = BertTokenizer.from_pretrained(self.model_name)
        self.model= self.create_model()
        
    
    def create_model(self):
        
        config = BertConfig.from_pretrained(self.model_name, num_labels=len(self.candidate_labels))
        model = BertForSequenceClassification.from_pretrained(self.model_name, config=config)
        model.config.id2label = {i: label for i, label in enumerate(self.candidate_labels)}
        model.config.label2id = {label: i for i, label in enumerate(self.candidate_labels)}
        return model
        
    def single_sentence (self, sentence:str) -> dict:
        
        inputs = self.tokenizer(sentence, return_tensors="pt", padding=True, truncation=True)
        outputs = self.model(**inputs)
        logits = outputs.logits
        predicted_label = torch.argmax(logits, dim=1).item()
        probs = F.softmax(logits, dim=-1)
        predicted_score = probs[0][predicted_label].item()
        predicted_label_name = self.candidate_labels[predicted_label]
        result={"predicted_label": predicted_label_name, "predicted_score": predicted_score}
        return result 

    def multi_sentence (self, sentences:list) -> list:
        
        results= list()
        for sentence in sentences:
            result_single_sentence = self.single_sentence(sentence)
            result_single_sentence = {"sentence":sentence, "result":result_single_sentence}
            results.append(result_single_sentence)
        return results