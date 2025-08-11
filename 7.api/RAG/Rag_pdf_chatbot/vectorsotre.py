import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document
documents_with_id = []
load_dotenv()
os.getcwd()
# 필요한 글로벌 변수 선언
path = os.path.abspath("RAG/Rag_pdf_chatbot")
VECTOR_DB = 'chroma_db'
COLLECTION_NAME = "my-data"
PATH = os.path.join(path, VECTOR_DB)
store = None

def get_store():
    return store

def initialize_vector_db():
    global store
    # 이전 DB가 있었으면? 로딩..
    if os.path.exists(PATH) and os.listdir(PATH):
        store = Chroma(collection_name=COLLECTION_NAME, embedding_function=OpenAIEmbeddings(), persist_directory=PATH)
    else:
        # 없으면? 디렉토리 생성
        os.makedirs(PATH, exist_ok=True)
    return True
    
def create_vector_db(file_path):
    global store
    # 벡터 DB 생성...
    # 1. 파일을 가져온다
    documents = PyPDFLoader(file_path).load()
    
    for doc in documents:
        doc.metadata['source'] = os.path.basename(file_path)
    
    # 2. 문서 분할한다
    texts = CharacterTextSplitter(chunk_size=100, chunk_overlap=20).split_documents(documents)
    print(texts)
    
    for i, doc in enumerate(texts):
        documents_with_id.append(
        Document(
            page_content=doc.page_content,
            metadata={"doc_id": f"doc_{i+1}"}  # 원하는 ID 지정
        )
    )
    
    # 3. 임베딩 한다
    embeddings = OpenAIEmbeddings()
    if store:
        store.add_documents(texts)
    else:
        store = Chroma.from_documents(
            documents_with_id,
            embedding=embeddings, 
            collection_name=COLLECTION_NAME,
            persist_directory=PATH)
    
    print(store._collection_metadata)
    print("벡터 DB가 정상적으로 생성되었습니다.")
    return store

def delete_file_from_vstore(filename):
    #NoSQL rlqksdml db에서 자료 삭제하는 것과 동일하다
    store._collection.delete(where={'source' : filename})

    # vetor db가 persist옵션이 켜져있으면 저장된다
    # 백터DB가 persist 옵션이 켜져 있으면? 저장..
    if hasattr(store, "persist"):
        store.persist()
