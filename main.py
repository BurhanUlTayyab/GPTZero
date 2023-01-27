"""
This code a slight modification of perplexity by hugging face
https://huggingface.co/docs/transformers/perplexity

Both this code and the orignal code are published under the MIT license.

by Burhan Ul tayyab and Nicholas Chua
"""

from torch import equal
from model import GPT2PPL
from fastapi import FastAPI, Form
from fastapi import Request
import gradio as gr
import uvicorn
from database import DB
from HTML_MD_Components import noticeBoardMarkDown, footerHTML, bannerHTML, emailHTML, googleAnalytics

CUSTOM_PATH = "/"

app = FastAPI()

# initialize the model
model = GPT2PPL()
database  = DB()

@app.post("/postdb")
def uploadDataBase(email: str = Form(), request: Request = None):
    database.set(request.client.host, email)
    return "Email Sent"

def inference(sentence: str):
    return model(sentence=sentence)

@app.get("/infer")
def infer(sentence: str):
    return model(sentence=sentence)


with gr.Blocks(title="SG-GPTZero", css="#submit {background-color: #FF8C00} #advertisment {text-align: center;} #email {height:120%; background-color: LightSeaGreen} #blank {margin:150px} #code_feedback { margin-left:-0.3em;color:gray;text-align: center;margin-bottom:-100%;padding-bottom:-100%}") as io:
    gr.HTML(bannerHTML, visible=True)
    with gr.Row():
        gr.HTML(googleAnalytics, visible=True)
    with gr.Row():
        gr.Markdown('<h1 style="text-align: center;">SG-GPTZero</h1>')
    with gr.Row():
        gr.Markdown("Use SG-GPTZero to determine if the text is written by AI or Human.")
    with gr.Row(elem_id="row1"):
        with gr.Column(scale=1):
            InputTextBox = gr.Textbox(lines=7, placeholder="Please Insert your text(s) here", label="Texts")
            sumbit_btn = gr.Button("Submit", elem_id="submit")
        with gr.Column(scale=1):
            OutputLabels = gr.JSON(label="Output")
            OutputTextBox = gr.Textbox(show_label=False)
        sumbit_btn.click(inference, inputs=InputTextBox, outputs=[OutputLabels, OutputTextBox], api_name="infer")
    with gr.Row():
        with gr.Box():
            gr.Markdown(noticeBoardMarkDown(), visible=True)
    with gr.Row():
        gr.Markdown('# <span style="color:#006400">Register</span> here for updates.')
    with gr.Row():
        with gr.Column(scale=0.5):
            emailTextBox = gr.HTML(emailHTML)
        with gr.Column(scale=0.5):
            pass
    with gr.Row():
        gr.Markdown('<span style="color:red">Do you want to train Computer vision models faster. Visit [Ailiverse](https://ailiverse.com)</span> <br> <span style="color:gray"><p>Powered by Ailiverse </p></span>', elem_id="advertisment")
    with gr.Row():
        gr.Markdown('<a style="text-decoration:none;color:gray" href="https://github.com/BurhanUlTayyab/GPTZero">Code</a> . <a style="text-decoration:none;color:gray" href="https://mail.google.com/mail/?view=cm&fs=1&tf=1&to=gptzero@ailiverse.com" target="_blank">Feedback</a>', elem_id="code_feedback")

app = gr.mount_gradio_app(app, io, path=CUSTOM_PATH)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True, forwarded_allow_ips="*", proxy_headers=True)
