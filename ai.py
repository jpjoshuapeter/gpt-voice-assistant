import os
import openai
import pyttsx3
import speech_recognition as sr

openai.api_key = os.getenv("OPENAI_API_KEY")

def ai_prompt():
    """
    Converts user's prompt to text 
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ask your question:")
        audio_text = r.listen(source)
        print("Thank you")

    prompt = r.recognize_google(audio_text)

    return prompt

def gpt_response(gpt_prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt= gpt_prompt,
        temperature=0.5,
        max_tokens=256,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    gpt_answer = response['choices'][0]['text']
    
    return gpt_answer

def audio_response(answer):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) 
    engine.say(answer)
    engine.runAndWait()

def script():
    prompt = ai_prompt()
    if str("GPT") in prompt:
        gpt_prompt = prompt.replace("ask GPT", "")
        #response = gpt_prompt
        response = gpt_response(gpt_prompt)
    else:
        response = "I can not understand you"
    
    audio_response(response)

    print(prompt)
    print(response)
    return 

script()

