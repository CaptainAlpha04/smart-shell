import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def neo(args):
    # Load the API key from the .env file
    genai.configure(api_key = os.getenv('GEMINI_API_KEY'))
    model = genai.GenerativeModel('gemini-1.5-flash', 
            system_instruction= "Give answer without any formatting and styling, in a helpful and friendly tone."
            )
    
    chat = model.start_chat()
    try:
        if len(args) == 0:
            while True:
                prompt = input("\033[32m@Neo#\033[0m \033[33m")  # Prompt for user input
                if prompt == ':exit':  # Check if user wants to exit
                    break
                else:
                    response = chat.send_message(prompt, stream=True)  # Send user input to chat model
                    for chunk in response:
                        print("\033[0m" + chunk.text)  # Print the response from the chat model
        else:
            prompt = ' '.join(args)  # Combine command line arguments into a single string
            response = model.generate_content(prompt, stream=True)  # Generate content based on the prompt
            for chunk in response:
                print("\033[0m" + chunk.text)  # Print the generated content
    except: 
        print("An error occurred. Please try again later.")
