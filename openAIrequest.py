import os
import json
import openai
import gc_createEvent

# "key" api_key
# user "promt"
# "storeReponse" path to store openaiReponse
def sendPrompt(openAIKEY, prompt):
    #print(prompt)

    openai.api_key = openAIKEY
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "you are a scheduler for a person."},
      {"role": "user", "content": prompt}
    ]
    )
    return completion.choices[0].message["content"]

  

