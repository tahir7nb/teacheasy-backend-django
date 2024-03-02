import requests
import os
from dotenv import load_dotenv
load_dotenv()

def get_response_from_openai(prompt, messages):
    URL = "https://api.openai.com/v1/chat/completions"

    # print(''.center(100, '-'))
    # print([initial_message, {"role": "user", "content": prompt}]+messages)
    # print(''.center(100, '-'))

    payload = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": prompt}]+messages,
    "temperature" : 0.7,
    "top_p":1.0,
    "n" : 1,
    "stream": False,
    "presence_penalty":0,
    "frequency_penalty":0,
    }

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}"
    }

    response = requests.post(URL, headers=headers, json=payload, stream=False)
    response = response.json()
    print(response)
    if not response.get('error'):
        response = response['choices'][0]['message']['content']
        follow_on_questions = []
        response = response.replace('Follow-on', 'Follow on').replace('Follow on questions:', 'Follow on questions').replace('Follow on Questions:', 'Follow on questions').replace('Follow on Questions', 'Follow on questions')
        if 'Follow on questions' in response:
            response = response.split('Follow on questions')
            follow_on_questions = [q.replace('1.', '').replace('2.', '').strip() for q in response[1].split('\n') if q]
            response = response[0]
        return response, follow_on_questions
    else:
        return '', ''

# initial_message = {'role': 'system', 'content': 'You are a helpful assistant thats an expert on lesson planning. Answer the last user role question and in a new section and after the answer provide two follow-on questions to that answer in list format with title "Follow on questions".'}
# print(get_response_from_openai(initial_message, "who is zardari?", [{"role": "assistant", "content": "Zardari refers to Asif Ali Zardari, a Pakistani politician who served as the 11th President of Pakistan from 2008 to 2013. He is a prominent figure in the Pakistan People's Party (PPP) and has been involved in politics for several decades.\n\n"}, {"role": "user", "content": "What are some of the key accomplishments or initiatives during Zardari's presidency?"}]))
