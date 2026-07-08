"""
LangChain + Google Gemini API 연동 테스트
- LCEL(LangChain Expression Language) 파이프 체인 사용
- gemini-1.5-flash 모델 호출
"""

from dotenv import load_dotenv
load_dotenv()  # .env 파일에서 GOOGLE_API_KEY 로드

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. 모델 초기화
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# 2. 프롬프트 템플릿 정의
prompt = ChatPromptTemplate.from_messages([
    ("human", "{input}")
])

# 3. LCEL 체인 구성 (파이프 연산자 | 사용)
chain = prompt | llm | StrOutputParser()

# 4. 체인 실행
print("=== LangChain + Gemini 연동 테스트 시작 ===")
result = chain.invoke({"input": "안녕? 반가워. 한 문장으로 인사해줘."})
print("\n=== Gemini 응답 ===")
print(result)
print("\n=== 테스트 성공! ===")
