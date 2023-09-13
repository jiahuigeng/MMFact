import re
import pandas as pd
from chatgpt_predict import chatgpt
from sklearn.metrics import precision_score, recall_score, f1_score

file_path = "D:\\Mocheg-main\\Mocheg-main\\data\\test\\Corpus2_for_verification.csv"
df = pd.read_csv(file_path, usecols=['claim_id','Claim', 'Evidence', 'cleaned_truthfulness'], nrows=10)

def clean_pre(pre):
    pre = pre.lower() 
    if 'supported'in pre:
        pre = 'supported'
    if 'nei'in pre:
        pre = 'NEI'
    if 'refuted'in pre:
        pre = 'refuted'
    return pre

#to save prediction
predictions = []

for index, row in df.iterrows():
   claim = row['Claim']
   evidence = row['Evidence']
   message = "claim:" + claim + "/n" + " evidence:" + evidence
   pre = clean_pre(chatgpt(message))
   predictions.append(pre)  

# Assuming 'predictions' and 'cleaned_truthfulness' are lists
precision = precision_score(df['cleaned_truthfulness'], predictions, average='weighted')
recall = recall_score(df['cleaned_truthfulness'], predictions, average='weighted')
f1 = f1_score(df['cleaned_truthfulness'], predictions, average='weighted')

print(df['cleaned_truthfulness'].tolist())
print(predictions)
print("Precision:", precision)
print("Recall:", recall)
print("F1:", f1)