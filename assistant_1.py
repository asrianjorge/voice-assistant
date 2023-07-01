import random
import pyttsx3 as pyt
import speech_recognition as sr
import os
import sys
import wave
import pyaudio

from machine_hearing_3 import MachineHearing

new_user = {
    "new_user": (
        'добавить пользователя', 'добавить голос', 'добавить', 'пользователь', 'polzovatel'
    )
}
cmds = {
    "time_now": (
        'текущее время', 'сейчас времени', 'который час', 'сколько времени', 'какое сейчас время', 'время сейчас'),
    "music": (
        'музыку', 'воспроизведи музыку', 'воспроизведи аудио', 'аудио', 'плеер',
        'плеер'),
    "stupid": (
        'расскажи анекдот', 'расскажи шутку', 'давай посмеёмся', 'хочу посмеяться',
        'ты знаешь какой-нибудь анекдот',
        'ты знаешь какую-нибудь шутку', 'рассмеши меня', 'анекдот', "шутку", "шутка"),
    "hearthstone": (
        'hearthstone', 'хартстоун', 'харстоун', 'херстоун', 'хертстоун'),
    "raid": (
        'рейд', 'рэйд', 'реид', 'рэид', 'raid'),
    "telegram": (
        'телеграм', 'telegram'),
    "chrome": (
        'chrome', 'google', 'google chrome', 'хром', 'гугл', 'гугл хром', 'интернет'),
    "whatsapp": (
        'whatsapp', 'вотсап', 'ватсап'),
    "notes": (
        'заметки', 'записки'),
    "bye": (
        'пока', 'пака', 'пакеда', 'покеда', 'ладно пока', 'прощай', 'до скорых встреч', 'до завтра', 'до вторника',
        'до свидания', 'ещё увидимся'),
    "close": (
        'прощай', 'прощай розовая дама', 'пока', 'exit')
}

questions = {
    'behavior': (
        'как дела', 'как настроение', 'как ты'
    ),
    'creation': (
        'кто тебя создал', 'кто создал', 'кто создал тебя',
    ),
    'who_i_am': (
        'кто ты', 'ты кто', 'кто ты такой', 'что ты', 'что ты такое',
    )
}


class Assistant:

    def answer_message(self, message):
        m = message.lower()
        check = False
        for q, i in new_user.items():
            for j in i:
                if j in m:
                    check = q
                    break
        for q, i in cmds.items():
            for j in i:
                if j in m:
                    check = q
                    break
        if not check:
            for q, i in questions.items():
                for j in i:
                    if j in m:
                        check = q
                        break
        answer = self.just_do_it(check)
        return answer

    def say(self, text):
        speak_engine = pyt.init()
        speak_engine.say(text)
        speak_engine.runAndWait()
        speak_engine.stop()

    def answer_talk(self, message):
        answer = self.answer_message(message)
        a1 = answer
        # self.say(answer)
        return a1

    def analize_user(self, voice):
        mh = MachineHearing()
        name = mh.analize_voice(voice)
        return name

    def processing(self):
        self.say("Я слушаю")
        text = "Я слушаю"
        return text

    def add_user(self):
        mh = MachineHearing()
        self.say("Скажите что-нибудь")
        text, voice = self.voice_down_and_to_text('voice1')
        text_u1 = text
        voice1 = voice
        self.say("Как мне к вам обращаться?")
        text, voice = self.voice_down_and_to_text('voice2')
        text_u2 = text
        voice2 = voice
        train_x = [voice1, voice2]
        train_y = [text_u2, text_u2]
        print(voice1)
        mh.add_voice(train_x, train_y)

        text1 = "Скажите что-нибудь"
        text2 = "Как мне к вам обращаться?"
        text3 = mh.check_tree(text_u2)
        return text1, text_u1, text2, text_u2, text3

    def just_do_it(self, check):
        if check == 'new_user':
            return self.add_user()
        elif check == 'behavior':
            return random.choice(['Всё норм', 'Всё круто!', 'Опечалена я'])
        elif check == 'creation':
            return random.choice(['Я был создан Георгием и Марией',
                                  'Я ничего не скажу!.. АГ БМ, больше ты ничего не узнаешь!',
                                  'Я есть сущность вселенского характера, мне миллиарды лет, я как звезды...'])
        elif check == 'stupid':
            return random.choice(['Колобок повесился', 'Русалка села на шпагат', 'Буратино утонул'])
        elif check == 'close':
            sys.exit()
        elif check == 'whatsapp':
            text = 'Открываю программу WhatsApp'
            os.system("C:\\Users\\George\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
            return text

    def voice_down_and_to_text(self, filename):
        file = None
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            text = r.recognize_google(audio, language="ru-RU").lower()

            p = pyaudio.PyAudio()

            stream = p.open(format=pyaudio.paInt16,
                            channels=2,
                            rate=44100,
                            input=True,
                            frames_per_buffer=1024)

            frames = []
            for i in range(0, int(44100 / 1024 * 5)):
                data = stream.read(1024)
                frames.append(data)

            wf = wave.open(f"{filename}.wav", mode='wb')
            wf.setnchannels(2)
            wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
            wf.setframerate(44100)
            wf.writeframes(b''.join(frames))
            wf.close()

            file = f"{filename}.wav"
            return text, file

        except sr.UnknownValueError:
            text = "Я не смогла распознать вашу команду. Повторите попытку."
            self.say("Я не смогла распознать вашу команду. Повторите попытку.")
            # self.say("Я твой писклявый голосочек чёт не улавливаю. Попробуй-ка ещё раз")
            return text, file

        except sr.RequestError:
            text = "Я не смогла распознать вашу команду. Видимо проблемы с соединением. Повторите попытку."
            self.say("Я не смогла распознать вашу команду. Видимо проблемы с соединением. Повторите попытку.")
            # self.say("Мой батя меня заблокал. Сори, придётся поворковать попозже")
            return text, file