from google import genai
import Key

client = genai.Client(api_key=Key.Key)



def ask_gemini(contents):
    response = client.models.generate_content(
    model="gemini-2.0-flash", contents=contents)
    return (response.text)


prompt_word ="""
We are playing a game where someone needs to guess a word I’m thinking about.
Suggest a word from Cyber subject like Network Devices as router , IPv4, Web, Encryption like TLS etc.
Respond only with one word I need.
target word:
"""

WORD = ask_gemini(prompt_word)
print(WORD)

prompt_forbidden = f"""
Given a target word, return a list of 4-6 words that identify the target word easily.
Separate the words with a comma.
target word: {WORD} identifying words:
"""

FORBIDDEN_WORDS = ask_gemini(prompt_forbidden)
print(FORBIDDEN_WORDS)

contents = f"""
You are a participant in a game where I need to guess a  
TARGET_WORD you describe in a sentence or two.  
You cannot mention the TARGET_WORD or any of the  
additional forbidden words.  

TARGET_WORD: {WORD}
additional forbidden words: {FORBIDDEN_WORDS}  
description:"""

print(ask_gemini(contents))