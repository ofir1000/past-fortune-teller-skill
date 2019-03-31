from mycroft import MycroftSkill, intent_file_handler
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft.skills.context import adds_context, removes_context

class PastFortuneTeller(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('teller.fortune.past.intent')
    @adds_context('YesContext')
    def handle_teller_fortune_past(self, message):
        self.answer = false
        self.speak_dialog('teller.fortune.past', expect_response=True)

    @intent_handler(IntentBuilder('AnwerIntent').require("YesKeyword").
                                  require('YesContext').build())
    @remove_context('YesContext')
    @adds_context('NameContext')
    def handle_answer_intent(self, message):
        self.speak('O.K. please tell me your name?', expect_response=True)


def create_skill():
    return PastFortuneTeller()

