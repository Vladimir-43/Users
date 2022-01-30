import pytest
import requests
from Lib.base_case import BaseCase
from Lib.base_case import Data
from Lib.payload import GetPayload

class TestWithUsersREST(BaseCase):
    def test_registration_user(self, name, email, password, exp_res):
        payload = GetPayload.get_payload_rest(self, name, email, password)
        response = requests.post(Data.URL_REST+"doregister", data=payload)
        self.get_status_code(response, 200)
        if exp_res == 0:
            self.check_key_is_not_in_json(response, "type")
            self.check_value_by_key_in_json(response, "name", name)
            self.check_value_by_key_in_json(response, "email", email)
        else:
            self.check_value_by_key_in_json(response, "type", "error")
            self.check_key_is_not_in_json(response, "name")
            self.check_key_is_not_in_json(response, "email")

    def test_checking_registration_user(self, name, email, password, exp_res):
        payload = GetPayload.get_payload_rest(self, None, email, password)
        response = requests.post(Data.URL_REST+"dologin", data=payload)
        self.get_status_code(response, 200)
        if exp_res in (0, 2):
            self.check_value_by_key_in_json(response, "result", True)
        else:
            self.check_value_by_key_in_json(response, "result", False)

    @pytest.mark.xfail
    def test_delete_user(self, name, email, password, exp_res):
        payload = GetPayload.get_payload_rest(self, None, email)
        response = requests.post(Data.URL_REST+"deleteuser", data=payload)
        self.get_status_code(response, 200)
        if exp_res == 0:
            # !!!в успешном ответе к json добавляется еще код, распарсить json невозможно!!!
            # плюс, вместо "result" = "ok", всегда "type" = "error"
            # поэтому следующий код не работает, помечен XFAIL
            self.check_key_is_not_in_json(response, "type")
            self.check_value_by_key_in_json(response, "result", "ok")
        else:
            self.check_value_by_key_in_json(response, "type", "error")
            # self.check_value_by_key_in_json(response, "message", "Пользователь с таким email не найден!")
            #  можно добавить обработку сообщений                   "email неправильный!"

@pytest.mark.new
class TestWithUsersSOAP(BaseCase):
    def test_registration_user(self, name, email, password, exp_res):
        payload = GetPayload.get_payload_soap(self, "doRegister", name, email, password)
        response = requests.post(Data.URL_SOAP, data=payload)
        self.get_status_code(response, 200)
        self.check_key_is_not_in_xml(response, "faultstring")
        if exp_res == 0:
            self.check_key_is_not_in_xml(response, "type")
            self.check_value_by_key_in_xml(response, "name", name)
            self.check_value_by_key_in_xml(response, "email", email)
        else:
            self.check_value_by_key_in_xml(response, "type", "error")
            self.check_key_is_not_in_xml(response, "name")
            self.check_key_is_not_in_xml(response, "email")

    def test_checking_registration_user(self, name, email, password, exp_res):
        payload = GetPayload.get_payload_soap(self, "doLogin", None, email, password)
        response = requests.post(Data.URL_SOAP, data=payload)
        self.get_status_code(response, 200)
        self.check_key_is_not_in_xml(response, "faultstring")
        if exp_res in (0, 2):
            self.check_value_by_key_in_xml(response, "return", "true")
        else:
            self.check_value_by_key_in_xml(response, "return", "false")

    def test_delete_user(self, name, email, password, exp_res):
        payload = GetPayload.get_payload_soap(self, "DeleteUser", None, email)
        response = requests.post(Data.URL_SOAP, data=payload)
        self.get_status_code(response, 200)
        self.check_key_is_not_in_xml(response, "faultstring")
        if exp_res == 0:
            self.check_value_by_key_in_xml(response, "return", f"Пользователь с email {email} успешно удален")
        elif exp_res == 3:
            self.check_value_by_key_in_xml(response, "return", "email неправильный!")
        else:
            self.check_value_by_key_in_xml(response, "return", "Пользователь с таким email не найден!")
