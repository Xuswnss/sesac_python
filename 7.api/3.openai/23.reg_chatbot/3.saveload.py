from dotenv import load_dotenv

# 채팅하기 위한 기본 라이브러리들
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# 임베딩 추가 라이브러리
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

# pip install langchain-chroma
from langchain_chroma import Chroma

load_dotenv()

PERSIST_DIR = "./chroma_db"  # 쓸대없이 DB 커밋하지 않도록 .gitignore에 추가할것

def create_vector_db():
    loader = TextLoader('./nvme.txt', encoding='utf-8')
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200) # 1000/200, 2000/500
    texts = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    store = Chroma.from_documents(texts, embeddings, collection_name="nvme", persist_directory=PERSIST_DIR)
    return store

def load_vector_db():
    embeddings = OpenAIEmbeddings()
    store = Chroma(collection_name="nvme", embedding_function=embeddings, persist_directory=PERSIST_DIR)
    return store

# 시작시에, 해당 디렉토리가 있으면?? 로딩... 없으면?? 생성...
import os
if os.path.exists(PERSIST_DIR):
    print('이전 데이터베이스를 로딩 중입니다...')
    store = load_vector_db()
else:
    print('이전 데이터베이스가 없어서, 새로 생성 중입니다...')
    store = create_vector_db()

print('데이터베이스 준비가 완료되었습니다.')

# 4. 실제로 질문할 준비..
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2) # RAG모델 에서는 온도를 낮추는게 일반적..
retriever = store.as_retriever()
template = """
다음 내용을 바탕으로 질문에 답변해주세요.
{context}

질문: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = {"context": retriever, "question": RunnablePassthrough()} | prompt | llm

question = "NVME와 SATA의 차이점을 100글자로 요약해 주세요."
response = chain.invoke(question)
print(response.content)