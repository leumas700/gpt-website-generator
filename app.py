from flask import Flask, render_template, request
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI()

def createSite():
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system",
            "content": "Du bist spezialist im Gestalten von HTML, CSS und Javascript websites. Du gibst als antwort nur den reinen code ohne markdown-codeblöcke. Es ist immer alles (html, css und js) in einem html file geschrieben."
            },
            {
            "role": "user",
            "content": "Erstelle eine website mit der p5js library und ein paar animierten beispielen um zu zeigen was mit p5js alles möglich ist. schreibe keine texte, ich will nur wirre formen und animationen sehen."
            }
        ]
    )
    with open("templates/index.html", 'w', encoding='utf-8') as f:
        f.write(completion.choices[0].message.content.strip()) 

@app.route('/', methods=['GET', 'POST'])
def index():
    createSite()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)