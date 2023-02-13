# Voice Assistant with GPT 

This is a voice-based AI assistant that can answer your questions and interact with connected devices. The script is developed using Python libraries like OpenAI, speech_recognition, pyttsx3, requests, and customtkinter.

## Features

1.  The script starts by greeting the user based on the time of the day.
2.  The user can ask the AI any question through voice and get a response.
3.  The script has integration with the Phillips Hue smart lights, and the user can turn on or off the lights through voice commands.
4.  The script also has integration with the Govee smart device, but it's not currently in use.

## Requirements

-   Python 3.6 or higher
-   OpenAI API Key
-   Required libraries listed in the import section.
-   Philips Hue smart lights and a Hue bridge for light integration.
-   Govee smart device for integration, but it's not currently in use.

## Installation

1.  Clone the repository: `git clone https://github.com/jpjoshuapeter/GPT-Speech-Assistant`
2.  Install the required packages: `pip install -r requirements.txt`
3.  Add your OpenAI API Key to your environment variables as `OPENAI_API_KEY`

## Usage

1.  Create a new file called "cred.py" in the same directory as the script and define the required credentials for the Phillips Hue bridge and the Govee device.
2.  Run the script by executing `python script.py`.
3.  The script will start by greeting the user, then ask for a voice prompt.
4.  The user can ask the AI anything, and the response will be played through the speakers.
5.  The user can also turn on or off the Phillips Hue lights and Govee by saying "Turn on the lights" or "Turn off the lights".
	1. This needs to be customized with the Phillips Hue API and Govee to work with your lights


## Customization

You can customize the script by modifying the following parameters in the `gpt_response` function:

-   `engine`: The GPT-3 engine to use. Default is 'text-davinci-002'
-   `prompt`: The question to ask GPT-3. Default is `gpt_prompt`
-   `temperature`: Controls the creativity of the response. Default is 0.5
-   `max_tokens`: The maximum number of tokens in the response. Default is 256
-   `top_p`: The proportion of the mass of the distribution to keep for the top-p filtering. Default is 1.0
-   `frequency_penalty`: The exponent of the frequency penalty. Default is 0.0
-   `presence_penalty`: The exponent of the presence penalty. Default is 0.0

# Note

1.  The script requires an active internet connection for OpenAI API and Philips Hue API calls.
2.  The speech recognition may not work correctly in a noisy environment.
3.  The script currently only understands the command "ask GPT" before the question, to activate OpenAi otherwise it will not recognize the speech.

## License

This project is licensed under the MIT License. See the [LICENSE](https://chat.openai.com/LICENSE) file for more details.
