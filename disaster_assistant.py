import os
from dotenv import load_dotenv
load_dotenv(override=True)

openai_api_key = os.getenv('OPENAI_API_KEY')
if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set - please head to the troubleshooting guide in the setup folder")

#######################################################
def main():
    question = "What is 2+2?"
    from openai import OpenAI
    openai = OpenAI()  
    messages = [{"role": "user", "content": question}]
    response = openai.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )
    print(response.choices[0].message.content)  

#######################################################
#
if __name__ == "__main__":
    main()