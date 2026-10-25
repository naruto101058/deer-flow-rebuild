from backend.models import FakeChatModel
from copy import deepcopy
def test_fake_model_returns_assistant_message():
    model = FakeChatModel()
    messages = [{'role':'user','content':'你好'}]
    result = model.invoke(messages)
    assert result == {'role': 'assistant', 'content': '这是用于测试的固定回复。', 'tool_calls': []}
    

def test_fake_model_does_not_modify_input():
    model = FakeChatModel()
    messages = [{"role": "user", "content": "你好"}]
    # 保存调用前的独立快照
    before = deepcopy(messages)
    # 调用模型
    model.invoke(messages)
    # 检查调用后的输入是否与快照一致
    assert messages == before