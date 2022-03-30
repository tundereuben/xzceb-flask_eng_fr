from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = 'mpyy3-E4DoYeXLnlWQqy0GR3Awb3GTYyqeh80Viko2G5'
URL = 'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/2643cf54-2956-4a3a-ab9d-1f1e0de2218b'

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(URL)

def englishToFrench(english_text):
    """convert english text to french"""
    result = language_translator.translate(text=english_text ,model_id='en-fr').get_result()
    french_ext = result['translations'][0]['translation']
    return french_ext

def frenchToEnglish(french_ext):
    """convert French text to English"""
    result = language_translator.translate(text=french_ext ,model_id='fr-en').get_result()
    english_text = result['translations'][0]['translation']
    return english_text

print(englishToFrench('Hello'))
# print(frenchToEnglish('Bonjour'))