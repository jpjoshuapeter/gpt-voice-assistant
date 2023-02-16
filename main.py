import ctypes
import datetime
import os
import subprocess
import time

import customtkinter as ctk
import openai
import pyttsx3
import requests
import services.Phillipshue as ph
import speech_recognition as sr
from credentials import Files, Weather, govee

openai.api_key = os.getenv("OPENAI_API_KEY")

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')


def audio_response(answer):
    """
    TTS for response
    """
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 200)
    engine.say(answer)
    engine.runAndWait()


def startup_audio():
    """
    Audio to be played when starting the application
    """
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        audio_response("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        audio_response("Good Afternoon Sir !")

    else:
        audio_response("Good Evening Sir !")

    assname = "Artemis"
    audio_response("I am your Assistant" +
                   f"{assname} 1 point o, How can I help you today?")


def takeCommand():
    """
    Converts user's prompt to text
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print("Ask your question:")
        r.pause_threshold = 1
        audio_text = r.listen(source)
        # print("Thank you")

    try:
        prompt = r.recognize_google(audio_text, show_all=False)

    except Exception as e:
        print(e)
        print("Say that again please")
        return "None"

    return prompt


def gpt_response(gpt_prompt):
    """
    Uses OpenAI api to get response from GPT3
    """
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


class GoveeLights:
    """
    Turn on and off Govee lights
    """

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


def shutdown():
    """
    Shutdown process of the device and lights
    """
    audio_response('intializing shutdown')
    ph.Phillipshue_off().lights()
    GoveeLights().light_off()
    ph.bedroomLightsON().lights()
    time.sleep(15)
    subprocess.call('shutdown /p /f')


class WeatherApi:

    def __init__(self):
        self.apikey = Weather.API_KEY
        self.url = 'https://api.tomorrow.io/v4/weather'

    def realTimeWeather(self, city='bartlesville'):
        """
        Gets real time weather
        """

        apikey = self.apikey
        headers = {
            "accept": "application/json"
        }

        data = {
            'location': city,
            'units': 'imperial',
            'apikey': apikey
        }

        url = f'{self.url}/realtime'

        r = requests.get(
            url, params=data, headers=headers
        )

        response = r.json()

        temperature = response['data']['values']['temperature']

        precipitation = response['data']['values']['precipitationProbability']

        return temperature, precipitation

    def morningWeather(self, city='bartlesville'):
        """
        Get weather data for 7 am central time the following day
        """
        apikey = self.apikey
        headers = {
            "accept": "application/json"
        }

        data = {
            'location': city,
            'units': 'imperial',
            'timesteps': '1h',
            'apikey': apikey

        }

        url = f'{self.url}/forecast'

        r = requests.get(
            url, params=data, headers=headers
        )

        response = r.json()
        tomorrow = (datetime.datetime.now() +
                    datetime.timedelta(1)).strftime("%Y-%m-%d")
        for hour in response["timelines"]["hourly"]:
            if hour["time"] == f"{tomorrow}T13:00:00Z":
                temperature = hour["values"]["temperature"]
                break

        # print(r.url)

        return temperature

    def dailyWeather(self, city='bartlesville'):
        """
        Getting the forecast for the current day
        """
        apikey = self.apikey
        headers = {
            "accept": "application/json"
        }

        data = {
            'location': city,
            'units': 'imperial',
            'timesteps': '1d',
            'apikey': apikey

        }

        url = f'{self.url}/forecast'

        r = requests.get(
            url, params=data, headers=headers
        )

        response = r.json()

        today = (datetime.datetime.now()).strftime("%Y-%m-%d")

        for day in response["timelines"]["daily"]:
            if day["time"] == f"{today}T00:00:00Z":
                temperatureMax = day["values"]["temperatureMax"]
                percentageRain = day["values"]["precipitationProbabilityMax"]
                totalRain = day["values"]["rainAccumulationSum"]
                break

        return temperatureMax, percentageRain, totalRain


def weatherReport():
    high_temp, rain_chance, rain_amount = WeatherApi().dailyWeather()

    response = "Good Morning Sir, The weather forecast for today is looking "
    if high_temp >= 85:
        response += "hot and sunny with a high of " + \
            str(high_temp) + "°F. "
    elif high_temp >= 70:
        response += "pleasant with a high of " + str(high_temp) + "°F. "
    else:
        response += "chilly with a high of " + str(high_temp) + "°F. "

    if rain_chance >= 50:
        response += "There's a " + \
            str(rain_chance) + "% chance of rain and "
        response += "a total of " + str(rain_amount) + " inches expected. "
        response += "Don't forget your umbrella!"
    elif rain_chance >= 20:
        response += "There's a slight chance of rain with a " + \
            str(rain_chance) + "% chance, "
        response += "and a total of " + \
            str(rain_amount) + " inches expected. "
        response += "It might be a good idea to pack a light jacket just in case."
    else:
        response += "It looks like it will stay dry with only a " + \
            str(rain_chance) + "% chance of rain. "
        response += "Enjoy the sunshine!"
    return response


def script():
    """
    Prompt and action
    """
    prompt = takeCommand().lower()

    if str("GPT") in prompt:
        gpt_prompt = prompt.replace("ask GPT", "")
        # response = gpt_prompt
        response = gpt_response(gpt_prompt)
        audio_response(response)

    elif str("work mode") in prompt or str("lights on") in prompt:
        ph.Phillipshue_on().lights()
        GoveeLights().light_on()
        response = 'I have switched to work mode'
        audio_response(response)

    elif str("lights off") in prompt:
        ph.Phillipshue_off().lights()
        GoveeLights().light_off()
        response = 'I have turned off the lights'
        audio_response(response)

    elif str('how are you') in prompt:
        response = "I am fine, Thank you"
        audio_response(response)

    elif str('discord') in prompt:
        os.startfile(
            Files.discord)
        response = 'I have opened discord'
        audio_response(response)

    elif str('lock pc') in prompt:
        audio_response("locking your pc")
        ctypes.windll.user32.LockWorkStation()

    elif str('current weather') in prompt:
        temperature, precipitation = WeatherApi().realTimeWeather()
        response = f'It is currently {temperature} degrees with a {precipitation} percent chance of rain.'
        audio_response(response)

    elif str('tomorrow morning') in prompt:
        temperature = WeatherApi().morningWeather()
        response = f'It will be {temperature} degrees at 7 tomorrow morning.'
        audio_response(response)

    elif str('shutdown') in prompt or str('shut down') in prompt:
        shutdown()
        response = 'Initiating shutdown'

    elif str('morning') in prompt:
        ph.bedroomLightsOff().lights()
        ph.Phillipshue_on().lights()
        GoveeLights().light_on()
        response = weatherReport()
        audio_response(response)

    elif "make a note" in prompt:
        """
        ! currently not working
        """
        audio_response("What should i write, sir")
        note = takeCommand()
        file = open('artemis.txt', 'w')
        audio_response("Sir, Should i include date and time")
        snfm = takeCommand()
        if 'yes' in snfm or 'sure' in snfm:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")
            file.write(strTime)
            file.write(" :- ")
            file.write(note)
        else:
            file.write(note)
        response = 'I have finished the note'
        audio_response(response)

    elif 'exit' in prompt:
        exit()

    else:
        response = "I can not help you at this time"
        audio_response(response)

    with open("conversation_history.txt", "a") as history_file:
        # Keeps track of the current conversation and
        # adds it to the conversation history txt file
        now = datetime.datetime.now()
        history_file.write(
            "\n" + f'{now}' + "\n" + f'Q: {prompt}' + "\n" + f'R: {response}' + "\n")

    return prompt, response


class App(ctk.CTk):
    """
    Builds GUI with Speak Button and shows response
    """

    def __init__(self):
        super().__init__()

        self.title('GPT Voice Assistant')
        self.geometry('400x600')

        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.frame = ctk.CTkScrollableFrame(master=self)
        self.frame.pack(pady=30, padx=30, fill='both', expand=True)

        self.label = ctk.CTkLabel(
            master=self.frame, text='Voice Assistant', font=ctk.CTkFont(size=30, weight="bold"))
        self.label.pack(pady=12, padx=10)

        def ai_button():
            prompt, response = script()

            self.text_2 = ctk.CTkTextbox(
                master=self.frame, width=400, height=200)
            self.text_2.pack(pady=15, padx=15, )
            self.text_2.insert("0.0", f'Q: {prompt} \n \nR: {response}')
            self.text_2.configure(state="disabled")

        self.button = ctk.CTkButton(
            master=self.frame, text='Speak', command=ai_button)
        self.button.pack(pady=10, padx=8)

        # self.after(500, startup_audio)


app = App()
app.mainloop()
