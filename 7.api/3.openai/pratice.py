from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# 기본값으로 OpenAI 임베딩 인스턴스 생성
embeddings = OpenAIEmbeddings()

# # 텍스트 문자열들을 임베딩으로 변환
# texts = ["Hello, how are you?", "I love programming."]
# vector_embeddings = embeddings.embed_documents(texts)  # ✅ 변경됨

# 결과 출력
# for text, vector in zip(texts, vector_embeddings):
#     print(f"Text: {text}")
#     print(f"Embedding length: {len(vector)}")  # 벡터 길이 출력
#     print(f"Embedding (first 5 values): {vector[:5]}\n")  # 앞 5개 값만 출력

from langchain_core.runnables import RunnablePassthrough

from langchain_core.runnables import RunnablePassthrough

# 사용자 입력을 받는 함수 정의
# def user_input(input_value):
#     return f"입력된 값: {input_value}"

# # RunnablePassthrough 인스턴스 생성
# passthrough = RunnablePassthrough()

# # 처리 체인 구성
# chain = passthrough | user_input
# print('### chain  : ' , chain)

# # 입력 값 정의
# input_value = "안녕하세요, 이 메시지는 변형되지 않습니다."

# # 사용자 입력을 처리하여 출력
# output = chain.invoke(input_value)
# print("출력:", output)

# 2-튜플 형태의 메시지 목록으로 프롬프트 생성 (type, content)

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# # 1. 프롬프트 정의 (2-튜플 형식)
# chat_prompt = ChatPromptTemplate.from_messages([
#     ("system", "이 시스템은 천문학 질문에 답변할 수 있습니다."),
#     ("user", "{user_input}"),
# ])

# # 2. LLM 초기화
# llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# # 3. 입력된 메시지 구조 확인
# formatted_messages = chat_prompt.format_messages(user_input="태양계에서 가장 큰 행성은 무엇인가요?")
# for msg in formatted_messages:
#     print(f"{msg.__class__.__name__}: {msg.content}")

# print("\n--- LLM 응답 ---")

# # 4. 체인 구성 및 실행
# chain = chat_prompt | llm | StrOutputParser()
# print(chain)
# result = chain.invoke({"user_input": "태양계에서 가장 큰 행성은 무엇인가요?"})


# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# # prompt + model + output parser
# prompt = ChatPromptTemplate.from_template("You are an expert in astronomy. Answer the question. <Question>: {input}")
# llm = ChatOpenAI(model="gpt-4o-mini")
# chain = prompt | llm 
# result = chain.invoke({"input": "지구의 자전 주기는?"})
# print(f'###### Before strOutParser() : {result}, type : {type(result)}')


# output_parser = StrOutputParser()
# chain = prompt | llm | output_parser
# result = chain.invoke({"input": "지구의 자전 주기는?"})
# print(f'###### After strOutParser() : {result}, type : {type(result)}')


# from langchain_core.documents import Document

# document = Document("안녕하세요 공백오입니다.")
# # 메타데이터 추가
# document.metadata["source"] = "0105"
# document.metadata["page"] = 1
# document.metadata["author"] = "공백오"
# print('document.page_content:',document.page_content)
# print('document.metadata :',document.metadata)


from langchain_core.prompts import PromptTemplate

# # 'name'과 'age'라는 두 개의 변수를 사용하는 프롬프트 템플릿을 정의
# template_text = "안녕하세요, 제 이름은 {name}이고, 나이는 {age}살입니다."

# # PromptTemplate 인스턴스를 생성
# prompt_template = PromptTemplate.from_template(template_text)

# # 템플릿에 값을 채워서 프롬프트를 완성
# filled_prompt = prompt_template.format(name="공백오", age=22)

# print(filled_prompt)

from langchain_core.output_parsers import CommaSeparatedListOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# # 1. 출력 파서 초기화 (콤마로 구분된 리스트 형태)
# output_parser = CommaSeparatedListOutputParser()

# # 2. 출력 형식 지침 받기
# format_instructions = output_parser.get_format_instructions()

# # 3. 프롬프트 템플릿 생성 (형식 지침 포함)
# prompt = PromptTemplate(
#     template="List five {subject}.\n{format_instructions}",
#     input_variables=["subject"],
#     partial_variables={"format_instructions": format_instructions},
# )

# # 4. LLM 모델 초기화
# model = ChatOpenAI(temperature=0)

# # 5. 체인 생성: 프롬프트 → 모델 → 출력 파서
# chain = prompt | model | output_parser

# # 6. 실행: 'subject' 변수에 대해 호출
# result = chain.invoke({"subject": "idols"})
# print("결과 리스트:", result)

# import requests
# import os

# API_KEY = os.getenv('OPENAI_API_KEY') # OpenAI API 키 입력
# url = "https://api.openai.com/v1/chat/completions"

# headers = {
#     "Content-Type": "application/json",
#     "Authorization": f"Bearer {API_KEY}"
# }

# data = {
#     "model": "gpt-4o-mini",
#     "messages": [
#         {"role": "user", "content": "너 공백오라고 알아?? 티스토리 하는데 모르면 모른다고해.. 솔직히말해야되고 알고 있으면 어떤 주제의 블로그인지 알려줘"}
#     ]
# }

# response = requests.post(url, headers=headers, json=data)
# result = response.json()

# print("💬 GPT 응답:", result["choices"][0]["message"]["content"])

from openai import OpenAI


# client = OpenAI()

# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "user", "content": "공백오 블로그 구독자 수는? 모르면 모른다고 해!"}
#     ]
# )

# print("💬 GPT 응답:", response.choices[0].message.content)
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage



# OpenAI LLM 객체 생성
llm = ChatOpenAI(model="gpt-4o-mini")

# 대화 메시지 전달
response = llm([HumanMessage(content="올데이 프로젝트 너무 좋아! 너도 그렇니?")])

print("💬 GPT 응답:", response.content)