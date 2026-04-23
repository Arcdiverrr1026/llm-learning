from langchain_community.llms import Tongyi
llm = Tongyi(streaming=True)
for chunk in llm.stream(input("你想问啥：")):
    print(chunk, end="", flush=True)#flush使内容流式输出
