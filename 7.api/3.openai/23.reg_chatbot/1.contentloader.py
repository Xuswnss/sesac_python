from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import TextLoader
from langchain_core.runnables import RunnablePassthrough
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter 
import os
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings

load_dotenv()
# 현재 경로 확인
print("현재 경로:", os.getcwd())

# 상대 경로 → 절대 경로로 변환
file_path = os.path.abspath("3.openai/23.reg_chatbot/nvme.txt")
print("불러올 파일 경로:", file_path)

# 파일 로드
loader = TextLoader(file_path, encoding='utf-8')
documents = loader.load()

# 텍스트 분할기 정의
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)

# 문서 분할
texts = text_splitter.split_documents(documents)

# 결과 출력
# print(texts)

#embading 
embeddings = OpenAIEmbeddings()
store = Chroma.from_documents(texts, embeddings, collection_name='nvme')

llm = ChatOpenAI(model= 'gpt-3.5-turbo', temperature=0.2)

retriever = store.as_retriever()

template = """
다음 내용을 바탕으로 질문에 대답해주세요. 

{context}

질문 : {question}
"""


#체인 구성 : 사용자 질문은 question dp ekadktj rmeofh sjadjrksek.
# context는 retriver로부터 추출해서 {question}라는 공간에 채우 줄 예정
# prompt -> llm -> response
prompt = ChatPromptTemplate.from_template(template)
chain = {'context' : retriever, 'question' : RunnablePassthrough()} | prompt | llm

question = 'MVM와 SATA의 차이점을 100글자 내로 요약해 주세요'
response = chain.invoke(question)
print("############### response.content : \n", response.content)

#6. 확인 작업
context_docs = retriever.invoke(question)
print('------- 검색된 문서는 ? ------- ')
for i, doc in enumerate(context_docs, start=1):
    print(f'######[{i}] : {doc.page_content}\n')
