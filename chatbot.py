import google.generativeai as genai

#Using Google API key
GENAI_API_KEY = "AIzaSyB9_bXCGsZMFiAwokza8uEwWxZDXTIwr0Q"
genai.configure(api_key=GENAI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash-latest")  

def get_response(user_input):
    try:
        response = model.generate_content(user_input)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("🤖 Chatbot Ready! Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye! 👋")
            break
        response = get_response(user_input)
        print("Chatbot:", response)
