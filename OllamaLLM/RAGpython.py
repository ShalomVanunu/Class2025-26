import time
from google import genai
from google.genai import types

import Key

client = genai.Client(api_key=Key.key)
store = client.file_search_stores.create()

upload_op = client.file_search_stores.upload_to_file_search_store(
    file_search_store_name=store.name,
    file='Takanon.pdf'
)

while not upload_op.done:
  time.sleep(5)
  upload_op = client.operations.get(upload_op)

# Use the file search store as a tool in your generation call
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='האם מותר לשרוג בזמן שיעור',
    config=types.GenerateContentConfig(
        tools=[types.Tool(
            file_search=types.FileSearch(
                file_search_store_names=[store.name]
            )
        )]
    )
)
print(response.text)

# Support your response with links to the grounding sources.
grounding = response.candidates[0].grounding_metadata
if not grounding:
 print('No grounding sources found')
else:
 sources = {c.retrieved_context.title for c in grounding.grounding_chunks}
 print('Sources:', *sources)