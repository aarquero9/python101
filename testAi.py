import torch
from transformers import BertForQuestionAnswering, BertTokenizer

# Load pre-trained model and tokenizer
model_name = "bert-large-uncased-whole-word-masking-finetuned-squad"
model = BertForQuestionAnswering.from_pretrained(model_name)
tokenizer = BertTokenizer.from_pretrained(model_name)

# Define a function to answer questions
def answer_question(question, context):
    # Tokenize input question and context
    input_text = "[CLS] " + question + " [SEP] " + context + " [SEP]"
    input_ids = tokenizer.encode(input_text, add_special_tokens=False, return_tensors="pt")  

    # Perform inference
    start_scores, end_scores = model(input_ids)
    print("Start Scores Shape:", start_scores.shape)
    print("End Scores Shape:", end_scores.shape)

    start_index = torch.argmax(start_scores)
    end_index = torch.argmax(end_scores)

    # Convert token indices to actual tokens
    tokens = tokenizer.convert_ids_to_tokens(input_ids[0])
    answer = tokens[start_index:end_index+1]
    answer = tokenizer.convert_tokens_to_string(answer)

    return answer

# Example question and context
question = "What is the capital of France?"
context = "France, officially the French Republic, is a country primarily located in Western Europe, consisting of metropolitan France and several overseas regions and territories."

# Get the answer
answer = answer_question(question, context)
print("Question:", question)
print("Answer:", answer)
