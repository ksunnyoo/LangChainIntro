# 🦜 LangChain + Google Gemini API 연동 테스트

> **LangChain**과 **Google Gemini API**가 정상 연동되는지 검증하는 입문용 프로젝트입니다.  
> LCEL(LangChain Expression Language) 파이프 체인 구조로 Gemini 모델을 호출합니다.

---

## 📁 프로젝트 구조

```
LANGCHAIN_INTRO_20260708_S/
├── test_gemini.py   # LangChain + Gemini 연동 테스트 스크립트
├── .env             # API 키 환경변수 (⚠️ .gitignore에 의해 공유 차단됨)
├── .gitignore       # 민감 정보 파일 제외 설정
└── README.md        # 프로젝트 안내 문서
```

---

## 🛠️ 기술 스택

| 항목 | 내용 |
|------|------|
| **언어** | Python 3.14 |
| **LLM 프레임워크** | LangChain |
| **AI 모델** | Google Gemini 2.5 Flash |
| **체인 방식** | LCEL (LangChain Expression Language) |
| **API 키 관리** | python-dotenv (.env 파일) |

---

## ⚡ 빠른 시작

### 1. 패키지 설치

```bash
python -m pip install langchain langchain-google-genai langchain-core python-dotenv
```

### 2. API 키 설정

프로젝트 루트에 `.env` 파일을 생성하고 아래 내용을 입력하세요:

```
GOOGLE_API_KEY=여기에_본인의_API_키_입력
```

> 🔑 API 키는 [Google AI Studio](https://aistudio.google.com/app/apikey)에서 발급받을 수 있습니다.

### 3. 실행

```bash
python test_gemini.py
```

### 4. 예상 출력

```
=== LangChain + Gemini 연동 테스트 시작 ===

=== Gemini 응답 ===
네, 저도 반갑습니다!

=== 테스트 성공! ===
```

---

## 🔗 체인 구조 (LCEL)

```python
# 파이프 연산자(|)를 사용한 LCEL 체인
chain = prompt | llm | StrOutputParser()

# 실행
result = chain.invoke({"input": "안녕? 반가워. 한 문장으로 인사해줘."})
```

```
[ChatPromptTemplate]
        |
        ↓
[ChatGoogleGenerativeAI]  ← Gemini 2.5 Flash
        |
        ↓
[StrOutputParser]
        |
        ↓
     응답 문자열
```

---

## 🔒 보안 주의사항

- `.env` 파일은 **절대 GitHub에 업로드하지 마세요**.
- `.gitignore`에 `.env`가 등록되어 있어 자동으로 제외됩니다.
- API 키가 노출된 경우 즉시 [Google AI Studio](https://aistudio.google.com/app/apikey)에서 키를 재발급하세요.

---

## 📚 참고 자료

- [LangChain 공식 문서](https://python.langchain.com/)
- [LangChain Google Generative AI](https://python.langchain.com/docs/integrations/chat/google_generative_ai/)
- [Google AI Studio](https://aistudio.google.com/)
- [LCEL 가이드](https://python.langchain.com/docs/concepts/lcel/)
