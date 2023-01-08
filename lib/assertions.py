from requests import Response
import json


class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f'Response is not in JSON format. Response text is "{response.text}"'

        assert name in response_as_dict, f'Response JSON doesnot have key "{name}"'
        assert response_as_dict[name]== expected_value, error_message

    @staticmethod
    def assert_id_in_content(response: Response, content):
        try:
            content_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f'Response is not in JSON format. Response text is "{response.text}"'
        assert content in content_as_dict, f'id not in {content}'

    @staticmethod
    def assert_code_status(response: Response, expected_stasus_cod):
        assert response.status_code == expected_stasus_cod, f'Unexpected status cod! Expected: {expected_stasus_cod}. Actual: {response.status_code}'

    @staticmethod
    def assert_not_id_in_content(response: Response, content):
        try:
            content_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f'Response is not in JSON format. Response text is "{response.text}"'
        assert content not in content_as_dict, f'id in {content}'

    @staticmethod
    def assert_not_text_in_response(response: Response, content):
        content_as_text = response.text
        assert content in content_as_text, f'Text {content} not in response'
