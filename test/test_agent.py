# -*- coding: utf-8 -*-
from langchain_community.llms import Tongyi
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import BaseTool
from langchain import hub


# ==========================================
# 第一步：打造你的工具箱 (制作一个假的天气工具)
# ==========================================
class MockWeatherTool(BaseTool):
    name: str = "天气查询工具"
    description: str = "当用户问你某个地方的天气时，使用这个工具。输入参数应该是城市名字，比如'北京'或'杭州'。"

    def _run(self, city: str) -> str:
        # 这里为了测试方便，我们不真去联网，而是直接返回固定结果
        print(f"\n[🔧 工具被触发了！正在查询 {city} 的天气...]")
        if "杭州" in city:
            return "杭州今天大雨，气温 15-20 度，建议穿风衣带伞。"
        else:
            return f"{city} 今天晴空万里，气温 25 度，适合出行。"


# 将工具放进工具箱
tools = [MockWeatherTool()]

# ==========================================
# 第二步：请来大老板 (通义千问大脑) 和 大管家
# ==========================================
# 1. 准备大脑 (温度设为 0.5，让他说话自然点)
model = Tongyi(model_name='qwen-max', model_kwargs={'temperature': 0.5})

# 2. 下载黄金规则说明书
prompt = hub.pull("hwchase17/react")

# 3. 成立外包公司 (创建 Agent)
agent = create_react_agent(model, tools, prompt)

# 4. 请来大管家 (verbose=True 是灵魂！它会把思考过程全打印出来)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# ==========================================
# 第三步：老板，接客了！
# ==========================================
if __name__ == '__main__':
    print("🤖 Agent 已启动，等待提问...\n")

    # 你可以随便改这个测试问题
    test_question = "杭州今天天气怎么样？出门需要带什么？"

    print(f"👤 用户提问：{test_question}")
    print("-" * 50)

    # 让大管家去办这件事
    result = agent_executor.invoke({'input': test_question})

    print("-" * 50)
    print(f"✅ 最终回答：\n{result['output']}")