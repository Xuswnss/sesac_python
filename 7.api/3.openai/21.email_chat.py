from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda

load_dotenv()

# 1. 템플릿 정의
template = "다음 문장을 영어로 번역하시오.\n\n{article}"
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template([
    'You are an expert corporate communication specialist. '
    'Write in a formal, professional tone and Please write this in Korean.'
    
]),

    HumanMessagePromptTemplate.from_template(template)
])

# 2. 모델 정의
llm = ChatOpenAI(temperature=0.5) # 번역할꺼니깐, 창의력 줄이고, 펙트 위주로...

# 3. 체인 생성
chain = prompt | llm | RunnableLambda(lambda x: {"email": x.content.strip()})

# 4. 입력 및 호출
input_text = {
    "article": """
- 애플, 아이폰17 프로 라인업 출시 예정
- 고성능 이미지 센서, AI 최적화 업그레이드
- 자 사 설계 커스텀 이미지 센서 도입, 최대 20스톱 다이내믹레인지 구현
    """
}

result = chain.invoke(input_text)
print("최종결과: ", result)