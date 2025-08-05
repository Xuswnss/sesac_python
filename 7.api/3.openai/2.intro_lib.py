import openai
from dotenv import load_dotenv
import os

load_dotenv()

history = []
openai_api_key = os.getenv('OPEN_API_KEY')

client = openai.OpenAI(api_key = openai_api_key)

#client.chat.completion 
def ask_chatgpt(user_input):
    gpt_question = {'role':'user','content': user_input}
    history.append(gpt_question)
    print(' ########  실제로 우리가 gpt에게 던지는 메세지\n-------- 질문 시작 ---------\n')
    print(history['content'])
    print('---------여기 까지 -----------')

    response = client.chat.completions.create(
    model = 'gpt-3.5-turbo',
    messages = history   )
    gpt_response = {'role' : 'assistant', 'content' : response.choices[0].message.content}
    history.append(gpt_response)

    return gpt_response['content']

# print(f'[chat] : {ask_chatgpt('재미없는 이야기 해줘')}')


while True:
    user_input = input('[YOU] : ')
    if user_input in {'exit', 'quit','종료','그만','끝'}:
        print('[대답을 종료합니다]')
        break
    print('[chat] : ', ask_chatgpt(user_input))
