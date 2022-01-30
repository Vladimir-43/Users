from Lib.base_case import BaseCase

class GetPayload(BaseCase):
    def get_payload_rest(self, name=None, email=None, password=None):
        payload = {}
        if name != None: payload.update({"name": name})
        if email != None: payload.update({"email": email})
        if password != None: payload.update({"password": password})
        return payload

    def get_payload_soap(self, method, name=None, email=None, password=None):
        payload = f'<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" \
                                    xmlns:wrap="http://foo.bar/wrappersoapserver"> \
                    <soapenv:Header/> \
                    <soapenv:Body> \
                        <wrap:{method}>'
        if email != None: payload = payload + f'<email>{email}</email>'
        if name != None: payload = payload + f'<name>{name}</name>'
        if password != None: payload = payload + f'<password>{password}</password>'
        payload = payload + f'</wrap:{method}> \
                            </soapenv:Body> \
                            </soapenv:Envelope>'
        return payload

