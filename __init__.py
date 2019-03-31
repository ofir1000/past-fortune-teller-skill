from mycroft import MycroftSkill, intent_file_handler


class PastFortuneTeller(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('teller.fortune.past.intent')
    def handle_teller_fortune_past(self, message):
        self.speak_dialog('teller.fortune.past')


def create_skill():
    return PastFortuneTeller()

