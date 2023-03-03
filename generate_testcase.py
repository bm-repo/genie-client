# Automated Code Review using the ChatGPT language model

# Import statements
import openai
import os
import requests
import glob
import os

# Authenticating with the OpenAI API
openai.api_key = os.getenv('OPENAPI_KEY')
openai_engine = 'code-cushman-001'
openai_temperature = 1
openai_max_tokens = 1400


def generate_testcases():
    try:
        fl_list = glob.glob('python-files/*.py')
        print('file list ', fl_list)
        for file in fl_list:
            with open(file) as f:
                content = f.read()
                # Sending the code to ChatGPT
                response = openai.Completion.create(
                    engine=openai_engine,
                    prompt=(f"Generate testcases:\n```{content}```"),
                    temperature=openai_temperature,
                    max_tokens=openai_max_tokens
                )
                print(f'test cases generated for "{file}": \n',  {response['choices'][0]['text']})
    except Exception as ex:
        print('exception generated', ex.args)


generate_testcases()
