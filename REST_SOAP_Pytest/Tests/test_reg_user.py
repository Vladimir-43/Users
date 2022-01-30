import pytest
import requests
from Lib.base_case import BaseCase
from Lib.base_case import Data
from Lib.payload import GetPayload

@pytest.mark.smoke
class TestWithUserREST(BaseCase):
    def test_registration_user(self):
        payload = GetPayload.get_payload_rest(self, Data.NAME, Data.EMAIL, Data.PASSWORD)
        response = requests.post(Data.URL_REST+"doregister", data=payload)
        self.get_status_code(response, 200)
        self.check_key_is_not_in_json(response, "type")
        self.check_value_by_key_in_json(response, "name", Data.NAME)
        self.check_value_by_key_in_json(response, "email", Data.EMAIL)

    def test_checking_registration_user(self):
        payload = GetPayload.get_payload_rest(self, None, Data.EMAIL, Data.PASSWORD)
        response = requests.post(Data.URL_REST+"dologin", data=payload)
        self.get_status_code(response, 200)
        self.check_value_by_key_in_json(response, "result", True)
        
    def test_add_avatar_1(self):  # 1 способ: Email в теле запроса
        payload = GetPayload.get_payload_rest(self, None, Data.EMAIL)
        files = {'avatar': Data.avatar(self)}
        response = requests.post(Data.URL_REST+"addavatar", files=files, data=payload)
        self.get_status_code(response, 200)
        self.check_key_is_not_in_json(response, "type")
        self.check_value_by_key_in_json(response, "status", "ok")

    def test_add_avatar_2(self):  # 2 способ: Email в URL
        payload = GetPayload.get_payload_rest(self, None, Data.EMAIL)
        files = {'avatar': Data.avatar(self)}
        response = requests.post(Data.URL_REST+"addavatar", files=files, params=payload)
        self.get_status_code(response, 200)
        self.check_key_is_not_in_json(response, "type")
        self.check_value_by_key_in_json(response, "status", "ok")

    def test_delete_avatar_1(self):  # 1 способ: Email в теле запроса
        payload = GetPayload.get_payload_rest(self, None, Data.EMAIL)
        response = requests.post(Data.URL_REST+"deleteavatar", data=payload)
        self.check_key_is_not_in_json(response, "type")
        self.check_value_by_key_in_json(response, "status", "ok")

    def test_delete_avatar_2(self):  # 2 способ: Email в URL
        payload = GetPayload.get_payload_rest(self, None, Data.EMAIL)
        response = requests.post(Data.URL_REST+"deleteavatar", params=payload)
        self.check_key_is_not_in_json(response, "type")
        self.check_value_by_key_in_json(response, "status", "ok")

    @pytest.mark.xfail
    def test_delete_user(self):
        payload = GetPayload.get_payload_rest(self, None, Data.EMAIL)
        response = requests.post(Data.URL_REST+"deleteuser", data=payload)
        self.get_status_code(response, 200)
        # !!!в ответе к json добавляется еще код, распарсить json невозможно!!!
        # плюс, вместо "result" = "ok", всегда "type" = "error"
        # поэтому следующий код не работает
        self.check_key_is_not_in_json(response, "type")
        self.check_value_by_key_in_json(response, "result", "ok")

@pytest.mark.smoke
class TestWithUserSOAP(BaseCase):
    def test_registration_user(self):
        payload = GetPayload.get_payload_soap(self, "doRegister", Data.NAME, Data.EMAIL, Data.PASSWORD)
        response = requests.post(Data.URL_SOAP, data=payload)
        self.get_status_code(response, 200)
        self.check_key_is_not_in_xml(response, "faultstring")
        self.check_key_is_not_in_xml(response, "type")
        self.check_value_by_key_in_xml(response, "name", Data.NAME)
        self.check_value_by_key_in_xml(response, "email", Data.EMAIL)

    def test_checking_registration_user(self):
        payload = GetPayload.get_payload_soap(self, "doLogin", None, Data.EMAIL, Data.PASSWORD)
        response = requests.post(Data.URL_SOAP, data=payload)
        self.get_status_code(response, 200)
        self.check_key_is_not_in_xml(response, "faultstring")
        self.check_value_by_key_in_xml(response, "return", "true")

    def test_delete_user(self):
        payload = GetPayload.get_payload_soap(self, "DeleteUser", None, Data.EMAIL)
        response = requests.post(Data.URL_SOAP, data=payload)
        self.get_status_code(response, 200)
        self.check_key_is_not_in_xml(response, "faultstring")
        self.check_value_by_key_in_xml(response, "return", f"Пользователь с email {Data.EMAIL} успешно удален")
