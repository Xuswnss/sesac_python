# pip install langchain langchain_openai
# openai 사 모델과 연동하려면 langchain_openai
# claude 사 모델과 연동하려면 langchain_claude
# gemini 사 모델과 연동하려면 langchain_gemini
import os
from dotenv import load_dotenv

# from langchain.llms import OpenAI  # 구버전 API임..
from langchain_openai import OpenAI  # 신버전 API

load_dotenv()

# llm = OpenAI(api_key=api_key)
llm = OpenAI(max_tokens=1000)  # gpt-3.5-turbo-instruct 가 기본값임. 2024.01
                # text-davinci-003 (deprecated 된 모델 2024.01)
                
# gpt-3.5-turbo-instruct    # 시키는 모델, 문장 완성형 모델
# gpt-3.5-turbo             # 채팅, 사용자와 인터렉션, QA 모델...
# 두개 모델의 차이를...
print(llm)

prompt = "인공지능이란"

result = llm.invoke(prompt)
print(result)