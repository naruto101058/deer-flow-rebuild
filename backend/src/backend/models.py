class FakeChatModel:
    def invoke(self, messages):
        return {
            "role": "assistant",
            "content": "这是用于测试的固定回复。",
            "tool_calls":[],
        }
