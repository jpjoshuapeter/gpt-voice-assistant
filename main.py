import ctypes
import datetime
import os

import customtkinter as ctk
import openai
import pyttsx3
import requests
import speech_recognition as sr
from cred import govee, phillipshue

openai.api_key = os.getenv("OPENAI_API_KEY")


def audio_response(answer):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 300)
    engine.say(answer)
    engine.runAndWait()


def startup_audio():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        audio_response("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        audio_response("Good Afternoon Sir !")

    else:
        audio_response("Good Evening Sir !")

    assname = ("Artemis 1 point o")
    audio_response("I am your Assistant")
    audio_response(assname)
    audio_response("How can i Help you")


def takeCommand():
    """
    Converts user's prompt to text 
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ask your question:")
        r.pause_threshold = 1
        audio_text = r.listen(source)
        print("Thank you")

    prompt = r.recognize_google(audio_text, show_all=False)

    return prompt


def gpt_response(gpt_prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=gpt_prompt,
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


class Phillipshue_on:

    def __init__(self):

        username = phillipshue.username
        ip = phillipshue.ip
        self.base_url = f'https://{ip}/api/{username}'

    def lights(self):

        def light1(self):

            url = f'{self.base_url}/lights/1/state'
            data = {"on": True, "sat": 11, "bri": 254, "hue": 11013}

            response = requests.put(url, verify=False, json=data)

            return response

        def light2(self):

            url = f'{self.base_url}/lights/2/state'
            data = {"on": True, "sat": 11, "bri": 254, "hue": 11013}

            response = requests.put(url, verify=False, json=data)

            return response

        def light3(self):

            url = f'{self.base_url}/lights/11/state'
            data = {"on": True, "sat": 11, "bri": 254, "hue": 11013}

            response = requests.put(url, verify=False, json=data)

            return response

        return light1(self), light2(self), light3(self)


class Phillipshue_off:

    def __init__(self):

        username = phillipshue.username
        ip = phillipshue.ip
        self.base_url = f'https://{ip}/api/{username}'

    def lights(self):

        def light1(self):

            url = f'{self.base_url}/lights/1/state'
            data = {"on": False, "sat": 11, "bri": 254, "hue": 11013}

            response = requests.put(url, verify=False, json=data)

            return response

        def light2(self):

            url = f'{self.base_url}/lights/2/state'
            data = {"on": False, "sat": 11, "bri": 254, "hue": 11013}

            response = requests.put(url, verify=False, json=data)

            return response

        def light3(self):

            url = f'{self.base_url}/lights/11/state'
            data = {"on": False, "sat": 11, "bri": 254, "hue": 11013}

            response = requests.put(url, verify=False, json=data)

            return response

        return light1(self), light2(self), light3(self)


class GoveeLights:

    def __init__(self):
        self.apikey = govee.API_KEY
        self.url = 'https://developer-api.govee.com/v1'

    def light_on(self):
        apikey = self.apikey

        headers = {
            'Content-Type': 'application/json',
            'Govee-API-Key': apikey
        }

        url = f'{self.url}/devices/control'
        body = {
            'device': '63:CE:D4:AD:FC:49:03:CC',
            'model': 'H61A0',
            "cmd": {
                'name': "brightness",
                'value': 100,
            }
        }

        response1 = requests.put(url, headers=headers, json=body)

        body = {
            'device': '63:CE:D4:AD:FC:49:03:CC',
            'model': 'H61A0',
            "cmd": {
                'name': 'colorTem',
                'value': 7000
            }
        }

        response2 = requests.put(url, headers=headers, json=body)

        return response1, response2

    def light_off(self):
        apikey = govee.API_KEY

        headers = {
            'Content-Type': 'application/json',
            'Govee-API-Key': apikey
        }

        url = f'{self.url}/devices/control'
        body = {
            'device': '63:CE:D4:AD:FC:49:03:CC',
            'model': 'H61A0',
            "cmd": {
                'name': "turn",
                'value': 'off',
            }
        }

        response1 = requests.put(url, headers=headers, json=body)

        return response1


def script():
    """
    Prompt and action
    """
    prompt = takeCommand().lower()

    if str("GPT") in prompt:
        gpt_prompt = prompt.replace("ask GPT", "")
        # response = gpt_prompt
        response = gpt_response(gpt_prompt)

    elif str("work mode") in prompt:
        Phillipshue_on().lights()
        GoveeLights().light_on()
        response = 'I have switched to work mode'

    elif str("lights off") in prompt:
        Phillipshue_off().lights()
        GoveeLights().light_off()
        response = 'I have turned off the lights'

    elif str('how are you') in prompt:
        response = "I am fine, Thank you"

    elif str('lock pc') in prompt:
        audio_response("locking your pc")
        ctypes.windll.user32.LockWorkStation()

    else:
        response = "I can not help you at this time"

    audio_response(response)

    return prompt, response


ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title('GPT Voice Assistant')
        self.geometry('400x600')

        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.frame = ctk.CTkFrame(master=self)
        self.frame.pack(pady=30, padx=30, fill='both', expand=True)

        self.label = ctk.CTkLabel(
            master=self.frame, text='Voice Assistant', font=ctk.CTkFont(size=30, weight="bold"))
        self.label.pack(pady=12, padx=10)

        def ai_button():
            self.text_1 = ctk.CTkTextbox(
                master=self.frame, width=400, height=100)
            self.text_1.pack(pady=15, padx=15, )
            self.text_1.insert("0.0", 'Ask your question:')
            self.text_1.configure(
                state="disabled",
                font=ctk.CTkFont(size=20, weight="normal")
            )

            prompt, response = script()

            self.text_2 = ctk.CTkTextbox(
                master=self.frame, width=400, height=200)
            self.text_2.pack(pady=15, padx=15, )
            self.text_2.insert("0.0", f'Q: {prompt} \n \nR: {response}')
            self.text_2.configure(state="disabled")

        self.button = ctk.CTkButton(
            master=self.frame, text='Speak', command=ai_button)
        self.button.pack(pady=10, padx=8)

        self.after(500, startup_audio)


app = App()

app.mainloop()
