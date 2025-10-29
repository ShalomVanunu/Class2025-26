from google import genai
import Key

client = genai.Client(api_key=Key.Key)

def ask_gemini(contents):
    response = client.models.generate_content(
    model="gemini-2.0-flash", contents=contents)
    return (response.text)

DATA = """
A network sniffer captured a TCP packet originating from Source IP: 192.168.1.100, destined for Destination IP: 10.0.0.5, with a Source Port of 54321 and a Destination Port of 80 associated with the Application Name: HTTP, observed at the Physical Layer via Ethernet
"""

prompt = f"""
Extract the IP V4 details of TCP/IP Layers of the user STATEMENT in one line.
Extract the Physical Layer ,Source and Destination IP, Source and Destination PORT,  Application Layer for each TCP/IP Layer. If nothing was mentioned, return NONE. STATEMENT: {DATA}
TCP/IP:"""

print(ask_gemini(prompt))

