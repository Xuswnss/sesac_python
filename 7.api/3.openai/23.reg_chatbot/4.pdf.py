from dotenv import load_dotenv

# 채팅하기 위한 기본 라이브러리들
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# 임베딩 추가 라이브러리
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_chroma import Chroma

# pip install pypdf

load_dotenv()

pdf_filename = "./DATA/Python_시큐어코딩_가이드(2023년_개정본).pdf"
PERSIST_DIR = "chroma_db"
COLLECTION_NAME = "secure_coding_python"

def create_vector_db():
    loader = PyPDFLoader(pdf_filename)
    pages = loader.load()

    # print(pages)
    # print(f"총 페이지 수: {len(pages)}")
    # print(f"2페이지 내용 샘플:\n{pages[1].page_content}")
    # print(f"2페이지 메타데이터:\n{pages[1].metadata}")

    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
        separator="\n\n", # 문서 분할 기준
        chunk_size=2000, # 최대 2000
        chunk_overlap=500, # 중복 500자 포함 (엄밀히는 토큰)
    )
    texts = text_splitter.split_documents(pages)
    # print(texts[10])

    embeddings = OpenAIEmbeddings()
    store = Chroma.from_documents(texts, embeddings, collection_name=COLLECTION_NAME, persist_directory=PERSIST_DIR)
    
    return store

def load_vector_db():
    embeddings = OpenAIEmbeddings()
    store = Chroma(collection_name=COLLECTION_NAME, embedding_function=embeddings, persist_directory=PERSIST_DIR)
    return store

def check_collection_exists(persist_dir, collection_name):
    embeddings = OpenAIEmbeddings()
    store = Chroma(collection_name=collection_name, embedding_function=embeddings, persist_directory=persist_dir)
    
    # 문서를 아무거나 달라고 해서, 1개 이상의 문서가 있는지 확인한다.
    results = store.get(limit=1)
    print(f"결과의길이 {len(results['ids'])}")
    return bool(results["ids"])

if check_collection_exists(PERSIST_DIR, COLLECTION_NAME):
    print("기존 데이터베이스를 로딩합니다.")
    store = load_vector_db()
else:
    print("새로운 데이터베이스를 생성합니다.")
    store = create_vector_db()


llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2)

template = """
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

prompt = ChatPromptTemplate.from_template(template)
retriever = store.as_retriever(search_kwargs={'k':5}) # 유사 문서 5개를 바탕으로...
chain = ({"context": retriever, "question": RunnablePassthrough()}) | prompt | llm | StrOutputParser()

def answer_question(question):
    # 디버깅용
    # 질문과 관련된 문서를 조회
    docs = retriever.invoke(question)
    sources = []
    context = ""
    for doc in docs:
        source = doc.metadata.get("source") # 파일명
        page = doc.metadata.get("page") # 페이지
        sources.append(f"{source} (page {page})")
        context += f"[출처: {source}, 페이지: {page}]\n{doc.page_content.strip()}\n\n"
        
    print(context)
    print('-'* 50)
    
    response = chain.invoke(question)
    print('----- 시작 -----')
    print("Q: ", question)
    print("A: ", response)
    print('----- 끝 -----')

# answer_question("시큐어코딩의 주요 기법들에 대해서 리스트 형태로 요약해서 설명해줘")
# answer_question("입력데이터 검증 및 오류 기법에 대해서 상세히 설명해줘")
answer_question("입력데이터 취약점 예시는?")
# answer_question("오늘 저녁에 먹을 메뉴는?")