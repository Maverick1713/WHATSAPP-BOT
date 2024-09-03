import os


from bardapi import Bard
from dotenv import load_dotenv
load_dotenv()

os.environ['_BARD_API_KEY']='dQgwF2BbsvqHbMT2z1wQugaj0VDnZqJSKmt5c0madTuYq2RDanCx5MLhzXT7ZMEuy98ffg.'

def text_generate(prompt:str):
    x= Bard().get_answer(prompt)['content']
    print(x)
    return (x)