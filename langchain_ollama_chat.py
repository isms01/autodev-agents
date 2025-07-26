from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "{question}"),
    ]
)
llm = ChatOllama(model="phi3:3.8b")

# LCEL(Runnable): pipe
chain = prompt | llm

res = chain.invoke(
    {"question": "What are the benefits of using LangChain with Ollama?"}
)
print(res.content)
