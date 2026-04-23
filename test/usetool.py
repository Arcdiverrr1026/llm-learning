from langchain_community.llms import Tongyi

llm = Tongyi()
llm.model_name = 'qwen-max'

print(llm.invoke('灵积是什么服务'))