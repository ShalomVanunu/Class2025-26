from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='gemma3:12b', messages=[
  {
    'role': 'user',
    'content': 'write about electric car in one sentence',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)