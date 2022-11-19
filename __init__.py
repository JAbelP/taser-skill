from mycroft import MycroftSkill, intent_file_handler


class Taser(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('taser.intent')
    def handle_taser(self, message):
        self.speak_dialog('taser')


def create_skill():
    return Taser()

