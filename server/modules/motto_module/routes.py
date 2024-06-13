import server.utils.openaiUtils as utils
import json
import server.modules.module.module as modules

motto_schema_json = '''
 "motto": "string"
'''
query_for_who = "Napisz motto dla"
query_doing_what = "tworzacego aplikacje do"
query_expectations = "Wynik przedstaw w postaci tablicy json zgodnie ze schematem " + motto_schema_json + ", wartości pól uzupełnij w języku polskim."

class MottoModule(modules.Module):
    def __init__(self, model):
        self.Model = model

    def make_ai_call(self, message, type):
        messages = [{"role": "system", "content": message}]
        response = utils.sendAIRequest(self.Model, messages, "json", 4000)
        return response

    def get_content(self, forWho, doingWhat, isMock, **kwargs):
        text_response_for_motto = self.make_ai_call(query_for_who + " " + forWho + " " + query_doing_what + " " + doingWhat + " " + query_expectations, {"type": "json_object"});
        return text_response_for_motto
