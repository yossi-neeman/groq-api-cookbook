#set GROQ_API_KEY in the secrets

import os
import httpx
from groq import Groq

# WARNING: This disables SSL verification for local development only
# DO NOT use this in production! This is a workaround for SSL certificate
# issues on some macOS Python installations.
# 
# For production, ensure Python's SSL certificates are properly configured.
http_client = httpx.Client(
    verify=False  # Disable SSL verification (local dev only!)
)

# Create the Groq client with the custom http_client
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
    http_client=http_client
)

# Set the system prompt
system_prompt = {
    "role": "system",
    "content":
    "You are a helpful assistant. You reply with very short answers."
}

# Initialize the chat history
chat_history = [system_prompt]

while True:
  # Get user input from the console
  user_input = input("You: ")

  # Append the user input to the chat history
  chat_history.append({"role": "user", "content": user_input})

  response = client.chat.completions.create(model="llama-3.1-8b-instant",
                                            messages=chat_history,
                                            max_tokens=100,
                                            temperature=1.2)
  # Append the response to the chat history
  chat_history.append({
      "role": "assistant",
      "content": response.choices[0].message.content
  })
  # Print the response
  print("Assistant:", response.choices[0].message.content)
