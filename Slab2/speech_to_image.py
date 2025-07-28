import requests
import speech_recognition as sr

def recognize_speech():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        audio = rec.listen(source)
        return rec.recognize_google(audio)

def generate_image(prompt):
    headers = {"Authorization": "Bearer YOUR_MONSTER_API_KEY"}  # Replace with your token
    data = {"prompt": prompt}
    res = requests.post("https://api.monsterapi.ai/stable-diffusion", headers=headers, json=data)
    image_url = res.json()["output"][0]
    print("Generated Image URL:", image_url)

if __name__ == "__main__":
    prompt = recognize_speech()
    generate_image(prompt)
