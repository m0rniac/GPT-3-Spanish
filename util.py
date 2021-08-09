#[Util; Herramienta de traducción].
import requests

#[Corpus; Función principal].
def esp_trans(topic, target, text):
	p = {'sl': topic, 'tl': target, 'q': text}

	c = {"Charset":"UTF-8","User-Agent":"AndroidTranslate/5.3.0.RC02.130475354-53000263 5.1 phone TRANSLATE_OPM5_TEST_1"}
	link = "https://translate.google.com/translate_a/single?client=at&dt=t&dt=ld&dt=qca&dt=rm&dt=bd&dj=1&hl=es-ES&ie=UTF-8&oe=UTF-8&inputm=2&otf=2&iid=1dd3b944-fa62-4b55-b330-74909a99969e"

	response = requests.post(link, data = p, headers = c)

	if response.status_code == 200:
		for x in response.json()['sentences']:
			return x['trans']
	else:
		print("[Error; Ocurrió un error en la traducción].\n")
		err_eng = "[Error; An error occurred in the translation]."