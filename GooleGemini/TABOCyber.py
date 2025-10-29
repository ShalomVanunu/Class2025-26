from google import genai
import Key

client = genai.Client(api_key=Key.Key)

contents = """
You are a participant in a game where I need to guess a  
TARGET_WORD you describe in a sentence or two.  
You cannot mention the TARGET_WORD or any of the  
additional forbidden words.  

TARGET_WORD: 'router'  
additional forbidden words: internet, wifi, device, traffic  
description:"""


response = client.models.generate_content(
model="gemini-2.0-flash", contents=contents)
print(response.text)