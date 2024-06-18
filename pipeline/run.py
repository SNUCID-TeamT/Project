import ollama

from .device_mapping import google_translate,Device_Mapping
from .SERVICE_DESCRIPTION_FINAL import description
from .fix_code import fix_code2
def generate_code(sentence,needed_services):
    prompt = f"Input: {sentence}\n\n services: {needed_services}"
    response = ollama.chat(model='soplang', messages=[
  {
    'role': 'user',
    'content':prompt
  },
])
    return response['message']['content']
def pipeline(sentence):
    english_sentence = google_translate(sentence)
    print(english_sentence)
    devices = Device_Mapping(english_sentence,str(description),model='soplang')
    print(devices)
    needed_services = dict()
    for device in devices:
        needed_services[device] = description[device]
    code = generate_code(english_sentence,needed_services)
    print(code)
    code = fix_code2(code)
    print(code)

    return code


if __name__ == '__main__':
    dataset = ['1시간마다 TV mute 토글해줘',
    '화요일 목요일 금요일 오후 2시에 눈이오면 에어컨을 heat 모드로 틀어줘']
    for data in dataset:
        pipeline(data)
        