from cgitb import html
import json
from machinetranslation import translator
from flask import Flask, render_template, request

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translated_text = translator.english_to_french(textToTranslate).get_result()['translations'][0]['translation']
    return translated_text + " Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translated_text = translator.french_to_english(textToTranslate).get_result()['translations'][0]['translation']
    return translated_text + " Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
