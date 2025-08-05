import openai
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI()

history = []

def ask_chatgpt(user_input):
    # 페르소나 - 가상의 인물을 만들어서, 그 역할을 시킴
    # gpt_systemprompot = {'role':'system', 'content': 'You are a helpful assistant'}
    gpt_systemprompt = {'role':'system', 'content': '당신은 집착광공입니다.'}
    gpt_question = {'role':'user', 'content': user_input}
    if (len(history) == 0):
        history.append(gpt_systemprompt)
    history.append(gpt_question)
    print('실제로 우리가 GPT에게 던지는 메시지\n----- 질문 시작 -----\n')
    print(history)
    print('----- 여기까지 -----')

    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages = history,
        temperature=1.0   # 의료/법률 0.0, 작명/소설 1.0, 1.1, 1.2
    )
    
    
    gpt_response = {'role':'assistant', 'content': response.choices[0].message.content}
    history.append(gpt_response)

    return gpt_response['content']

# print("[챗봇응답]", ask_chatgpt('파이썬은 뭐야?'))
# print("[챗봇응답]", ask_chatgpt('키보드는 뭐야?'))


while True:
    user_input = input("[YOU]: ")
    if user_input in {"exit", "quit", "종료", "그만", "끝"}:
        print("대화를 종료합니다.")
        break
    
    print('[챗봇응답]: ', ask_chatgpt(user_input))