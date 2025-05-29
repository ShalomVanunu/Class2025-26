from google import genai
import Key

client = genai.Client(api_key=Key.Key)
while True:
    contents = input(" prompt :\n")


    response = client.models.generate_content(
    model="gemini-2.0-flash", contents=contents)
    print(response.text)