from langchain_core.prompts import PromptTemplate

template = "You are a naming consultant. Suggest a name for a company that makes {product}"

prompt = PromptTemplate(
    input_variables=['product'],
    template=template
)

filled_prompt = prompt.format(product="icecream")
print(filled_prompt)

filled_prompt = prompt.format(product="cookie")
print(filled_prompt)

filled_prompt = prompt.format(product="smartphone")
print(filled_prompt)

test_products = [
    "mobile games",
    "robot toys",
    "electrical bike",
    "camping goods",
    "programming language education"
]

from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI() # 필요시 모델, 키, 온도 등을 설정한다

for product in test_products:
    result = prompt.format(product=product)
    print(f"[{product}] : {result}")

    # 미션. 이렇게 만들어진 프롬푸트를... 다시 llm.invoke로 호출하시오.
    response = llm.invoke(result)
    print("생성된 이름: ", response.strip())
