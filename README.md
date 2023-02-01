# GPT-Speech-Assistant

This is a python script that allows you to interact with GPT-3 using speech. You can ask GPT-3 any question and it will respond to you with the answer in speech. The script uses the OpenAI API to access GPT-3, SpeechRecognition to convert speech to text, and pyttsx3 to convert text to speech.

## Requirements

-   Python 3.6 or higher
-   OpenAI API Key
-   SpeechRecognition
-   pyttsx3

## Installation

1.  Clone the repository: `git clone https://github.com/<your-username>/GPT-Speech-Assistant`
2.  Install the required packages: `pip install -r requirements.txt`
3.  Add your OpenAI API Key to your environment variables as `OPENAI_API_KEY`

## Usage

1.  Run the script: `python script.py`
2.  The script will prompt you to ask your question
3.  Speak your question and wait for GPT-3's response

## Customization

You can customize the script by modifying the following parameters in the `gpt_response` function:

-   `engine`: The GPT-3 engine to use. Default is 'text-davinci-002'
-   `prompt`: The question to ask GPT-3. Default is `gpt_prompt`
-   `temperature`: Controls the creativity of the response. Default is 0.5
-   `max_tokens`: The maximum number of tokens in the response. Default is 256
-   `top_p`: The proportion of the mass of the distribution to keep for the top-p filtering. Default is 1.0
-   `frequency_penalty`: The exponent of the frequency penalty. Default is 0.0
-   `presence_penalty`: The exponent of the presence penalty. Default is 0.0

## Note

The script currently only understands the command "ask GPT" before the question, otherwise it will not recognize the speech.

## License

This project is licensed under the MIT License. See the [LICENSE](https://chat.openai.com/LICENSE) file for more details.
