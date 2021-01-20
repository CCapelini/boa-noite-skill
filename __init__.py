from mycroft import MycroftSkill, intent_file_handler


class BoaNoite(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('noite.boa.intent')
    def handle_noite_boa(self, message):
        self.speak_dialog('noite.boa')


def create_skill():
    return BoaNoite()

