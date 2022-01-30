import json
from lxml import etree
from requests import Response

class Data():
    URL_REST = "http://users.bugred.ru/tasks/rest/"
    URL_SOAP = "http://users.bugred.ru/tasks/soap/WrapperSoapServer.php"
    EMAIL = "bvv_01@mail.ru"
    NAME = "bvv_01"
    PASSWORD = "1234"
    def avatar(self):
        return open("Data/avatar.jpg", "rb")

class BaseCase:
    def check_json_format(self, response: Response):
        try:
            response_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON Format. Response text is '{response.text}'"
        return response_dict

    def check_xml_format(self, response: Response):
        try:
            response_xml = etree.XML(response.content)
        except etree.XMLSyntaxError:
            assert False, f"Response is not in XML Format. Response content is '{response.content}'"
        return response_xml

    def check_value_by_key_in_json(self, response: Response, key_name, value):
        response_dict = self.check_json_format(response)
        self.check_key_is_in_json(response_dict, key_name)
        assert response_dict[key_name] == value, f"Response key '{key_name}' is not '{value}', is " \
                                                 f"'{response_dict[key_name]}'"

    def check_value_by_key_in_xml(self, response: Response, key_name, value):
        response_xml = self.check_xml_format(response)
        self.check_key_is_in_xml(response_xml, key_name)
        resp = etree.XML(response.content).iter(key_name)
        res = False
        for i in resp:
            if i.text == value:
                res = True
            else:
                val = i.text
        assert res, f"Response key '{key_name}' is not '{value}, is '{val}'"

    def check_key_is_in_json(self, response_dict, key_name):
        assert key_name in response_dict, f"Response JSON doesn't have key '{key_name}'"

    def check_key_is_in_xml(self, response_xml, key_name):
        resp = response_xml.iter(key_name)
        sum = len(list(resp))
        assert sum > 0, f"Response XML doesn't have key '{key_name}'"

    def check_key_is_not_in_json(self, response: Response, key_name):
        response_dict = self.check_json_format(response)
        assert key_name not in response_dict, f"Response with '{key_name}'='{response_dict[key_name]}'" \
                                              f"-->{response_dict['message']}"

    def check_key_is_not_in_xml(self, response, key_name):
        resp = etree.XML(response.content).iter(key_name)
        sum = len(list(resp))
        assert sum == 0, f"Response XML does have key '{key_name}'"

    def get_value_by_key_in_json(self, response: Response, key_name):
        response_dict = self.check_json_format(response)
        self.check_key_is_in_json(response_dict, key_name)
        return response_dict[key_name]

    def get_status_code(self, response: Response, code):
        assert response.status_code == code, f"Status code is not {code}, is {response.status_code}"
