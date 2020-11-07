import requests
import Exceptions
import pprint


class QIWI_API:
    def __init__(self, token, phone):
        self.token = token
        self.phone = phone.replace("+", "")
        print(self.test_connection()["res"].json())
        self.connection = self.test_connection()["s"]

    # TODO Add money withdraw

    def test_connection(self):
        api_access_token = self.token
        my_login = self.phone
        s = requests.Session()
        s.headers['authorization'] = 'Bearer ' + api_access_token
        res = s.get('https://edge.qiwi.com/identification/v1/persons/' + my_login + '/identification')
        try:
            if res.json()["errorCode"] == "auth.forbidden":
                raise Exceptions.InvalidQIWILoginDataError()
        except KeyError:
            pass
        return locals()

    def payment_history_last(self, rows_num):
        """История платежей - последние и следующие n платежей"""
        # TODO ata types (?)
        s = requests.Session()
        s.headers['authorization'] = 'Bearer ' + self.token
        parameters = {'rows': rows_num}
        h = s.get('https://edge.qiwi.com/payment-history/v2/persons/' + self.phone + '/payments', params=parameters)

        result = []
        for pay in h.json()["data"]:
            try:
                # TODO Add sum currency check
                if pay["status"] == "SUCCESS":
                    # TODO Add transaction ID to result
                    result.append({"payer_phone": pay["personId"],
                                   "date": pay["date"],
                                   "sum": pay["sum"]["amount"],
                                   "comment": pay[""]})
            except KeyError:
                pass
                # TODO Add logging
        return result


if __name__ == '__main__':
    from os import getenv

    qiwi = QIWI_API(phone=getenv("phone"), token=getenv("qiwi_token"))

    pprint.PrettyPrinter().pprint(qiwi.payment_history_last(5))
