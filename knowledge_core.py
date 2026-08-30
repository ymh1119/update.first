import json

def load_index():
    """读取预先生成好的pdf索引文件 pdf_index.json"""
    with open("pdf_index.json", "r", encoding="utf-8") as f:
        return json.load(f)

def search_knowledge_page(query: str):
    """
    根据用户提问，检索课本索引，返回格式化的页码提示文本
    :param query: 用户输入的问题字符串
    :return: 带格式的课本页码提示，可直接拼接到AI回答后面
    """
    try:
        index = load_index()
    except Exception:
        return "\n\n📖课本参考：索引文件读取失败"
    hits = []
    q = query.lower()
    for item in index:
        txt = item["text"].lower()
        if q in txt:
            hits.append(item)
    if not hits:
        return "\n\n📖课本参考：未检索到该知识点对应课本位置"
    out = "\n\n📖课本参考位置：\n"
    # 最多返回匹配到前3条，避免输出太长
    for h in hits[:3]:
        out += f"- 课本页码：{h['book_page']}\n"
    return out
