from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def send_prompt(prompt, system_message="You are a helpful AI assistant.", model="gpt-4o-mini"):
    """
    Gửi một prompt đến OpenAI API và trả về phản hồi
    
    Tham số:
        prompt (str): Nội dung prompt
        system_message (str): Thông điệp hệ thống (mặc định: "You are a helpful AI assistant.")
        model (str): Mô hình AI sử dụng (mặc định: "gpt-4o-mini")
        
    Trả về:
        str: Phản hồi từ AI
    """
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    test_prompt = "Giải thích prompt engineering bằng 1 câu."
    result = send_prompt(test_prompt)
    print(result)
