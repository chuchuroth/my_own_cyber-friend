import requests

# Your API key (replace with real one)
API_KEY = "your_api_key_here"
MEMORY_FILE = "memory.txt"

# Read memory from file
def load_memory():
    try:
        with open(MEMORY_FILE, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "No memory yet."

# Save new info to memory
def save_memory(new_info):
    with open(MEMORY_FILE, "a") as file:
        file.write(new_info + "\n")

# Chat with AI
def chat_with_ai(user_input):
    memory = load_memory()
    prompt = f"Memory: {memory}\nUser: {user_input}"
    response = requests.post(
        "https://api.xai.com/v1/chat",  # Example URL, replace with real one
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={"prompt": prompt, "model": "grok"}
    )
    return response.json()["response"]

# Example use
message = "I’m stressed about work."
response = chat_with_ai(message)
print(response)
save_memory("March 20, 2025: Stressed about work.")
