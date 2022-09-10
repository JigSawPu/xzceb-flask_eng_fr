'''Translation program'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey=apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def english_to_french(english_text):
    '''Translates english to french'''
    french_text = language_translator.translate(text=english_text,
    model_id="en-fr", source="en", target="fr")
    return french_text

def french_to_english(french_text):
    '''Translates french to english'''
    english_text = language_translator.translate(text=french_text,
    model_id="fr-en", source="fr", target="en")
    return english_text
# model = language_translator.list_models().get_result()
# print(json.dumps(model, indent=2))
# print(frenchToEnglish('Bonjour').get_result()['translations'][0]['translation'])
