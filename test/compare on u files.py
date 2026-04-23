# -*- coding: utf-8 -*-
import os
from langchain_community.llms import Tongyi

# 1. 初始化大模型
llm = Tongyi(model_name='qwen-max')

# 2. 新增的方法：读取本地文本文件
def load_local_doc(file_path):
    """
    读取本地 txt 文件。
    注意：encoding='utf-8' 很重要，不然读取中文可能会乱码报错。
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


# 3. 修改后的主逻辑方法
def diff_local_files(file_path1, file_path2):
    # 将文件路径传给读取方法，拿到纯文本内容
    doc_content_1 = load_local_doc(file_path1)
    doc_content_2 = load_local_doc(file_path2)

    # 剧本（Prompt）几乎没变，只是改了下占位符名字
    prompt = f"""你现在的任务是找出下面两篇文档的不同之处，请不要放过任何细节。
--------
【文档 1】：
{doc_content_1}
--------
【文档 2】：
{doc_content_2}
--------
请给出结论，并用列表形式指出不同之处的具体位置：
"""

    print("正在呼叫通义千问进行对比，请稍候...")
    diff_result = llm.invoke(prompt)
    return diff_result


# --- 运行测试区域 ---
if __name__ == '__main__':
    # 定义你要对比的两个文件的相对路径或绝对路径
    # 请确保这两个 txt 文件和你的 python 脚本放在同一个文件夹里
    file1 = 'doc1.txt'
    file2 = 'doc2.txt'

    # 简单的安全检查：看看文件到底存不存在
    if os.path.exists(file1) and os.path.exists(file2):
        result = diff_local_files(file1, file2)
        print("\n======== 对比结果 ========\n")
        print(result)
    else:
        print(f"报错啦：找不到文件！请检查左侧目录里是不是已经建好了 {file1} 和 {file2}。")