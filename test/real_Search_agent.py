# -*- coding: utf-8 -*-
from langchain_community.llms import Tongyi
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools import DuckDuckGoSearchRun  # 🌟 新来的联网神器！
from langchain import hub

search_tool = DuckDuckGoSearchRun()

search_tool.name = "互联网搜索工具"
search_tool.description = "当用户问你的问题你不知道，或者需要查询最新的实时信息、新闻、天气、股价时，必须使用此工具去互联网上搜索。输入参数应该是精准的搜索关键词。"

tools = [search_tool]

model = Tongyi(model_name='qwen-max', model_kwargs={'temperature': 0.1})

prompt = hub.pull("hwchase17/react")

agent = create_react_agent(model, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

if __name__ == '__main__':
    print("🌐 接入互联网的 Agent 已启动，正在监听世界...\n")

    test_question = input("告诉我你的疑惑：")

    print(f"👤 用户提问：{test_question}")
    print("-" * 50)

    result = agent_executor.invoke({'input': test_question})

    print("-" * 50)
    print(f"✅ 最终回答：\n{result['output']}")