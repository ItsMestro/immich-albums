# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.79.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.auth_device_response_dto import AuthDeviceResponseDto  # noqa: E501

class TestAuthDeviceResponseDto(unittest.TestCase):
    """AuthDeviceResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuthDeviceResponseDto:
        """Test AuthDeviceResponseDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthDeviceResponseDto`
        """
        model = AuthDeviceResponseDto()  # noqa: E501
        if include_optional:
            return AuthDeviceResponseDto(
                created_at = '',
                current = True,
                device_os = '',
                device_type = '',
                id = '',
                updated_at = ''
            )
        else:
            return AuthDeviceResponseDto(
                created_at = '',
                current = True,
                device_os = '',
                device_type = '',
                id = '',
                updated_at = '',
        )
        """

    def testAuthDeviceResponseDto(self):
        """Test AuthDeviceResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()