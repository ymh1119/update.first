from langchain_openai import ChatOpenAI

def init_rag_system(api_key, expert_mode, pdf_name):
    llm = ChatOpenAI(
        api_key=api_key,
        model="gpt-3.5-turbo",
        temperature=0.3
    )

    class SimpleChain:
        def invoke(self, inputs):
            query = inputs["query"]
            history = inputs["chat_history"]
            prompt_text = f"【角色】{expert_mode}\n历史对话:{history}\n用户问题:{query}"
            resp = llm.invoke(prompt_text)
            return {"result": resp.content}

    return SimpleChain()
