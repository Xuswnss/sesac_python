# 필요한 글로벌 변수 선언
# import문 작성
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_chroma import Chroma

load_dotenv()
store = None # 백터 db에 저장할 공간
collection_name = 'xuswns'
data_path = os.path.abspath("3.openai/23.reg_chatbot")
VECTOR_DB = './chroma_db'
file_path = os.path.join(data_path ,VECTOR_DB)




# ------------ 변수선언 끝 -------------------------

def initialize_vector_db():
    #디렉 토리 생성
    #이전DB가 있으면 로딩
    # 디렉토리, 파일 존재 여부
    if os.path.exists(VECTOR_DB) and os.listdir(VECTOR_DB):
        global store
        print('이전 데이터 베이스를 로딩중입니다.')
        embeddings = OpenAIEmbeddings()
        store = Chroma( embedding_function=embeddings,collection_name=collection_name ,persist_directory=file_path)
    
    else : 
        print('이전 데이터베이스가 존재하지 않습니다.\n새로 생성합니다. ')
        os.makedirs(VECTOR_DB, exist_ok=True)
        
    return store
 
def create_vector_db(file_path): 
    global store
    document = PyPDFLoader(file_path)
    pages = document.load()
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
        separator="\n\n", # 문서 분할 기준
        chunk_size=2000, # 최대 2000
        chunk_overlap=500, # 중복 500자 포함 (엄밀히는 토큰)
    )
    text = text_splitter.split_documents(pages)
    embeddings = OpenAIEmbeddings()
    
    # store을 존재 여부
    if store:
        store.add_documents(text)
    else:
        store = Chroma.from_documents(
            text, embeddings, collection_name, VECTOR_DB)
    print('##### 백터 DB가 정상적으로 생성되었습니다.')
    return store



prompt = """
주어진 문서 내용을 바탕으로 질문에 답변해주세요

문서내용: {context}

질문: {question}

답변 작성 규칙:
1. 모든 답변은 제공된 문서내용을 기반으로만 답변하고, 정보가 없을경우 없다고 답변하세요.
2. 답변시 참고한 문서의 파일명, 페이지 를 다음 포멧으로 답변하세요.
   예시) 파일명 (페이지: 1)
3. 모든 답변은 번호를 붙여서 3가지 또는 그 이하로만 답변하시오.
4. 보안 취약점 관련된 내용은 대응방안도 함께 답변하시오.
"""
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
prompt = ChatPromptTemplate.from_template(prompt)
outPutParser = StrOutputParser()
chain = prompt | llm |outPutParser

def answer_question(question):
    if store is None:
        return '문서가 로드되지 않았습니다. 먼저 pdf를 업로드 해주세요'
    docs = store.similarity_search(question, k=5)
    context = "\n\n ---- \n ".join([doc.page_context for doc in docs])
    print(f'##### \n [검색한 문서확인] : \n {context}')
    
    result = chain.invoke({
        'context':context , 'question' : question
    })
    
    return result