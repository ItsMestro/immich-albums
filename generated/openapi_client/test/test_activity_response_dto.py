# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.88.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.activity_response_dto import ActivityResponseDto  # noqa: E501

class TestActivityResponseDto(unittest.TestCase):
    """ActivityResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActivityResponseDto:
        """Test ActivityResponseDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActivityResponseDto`
        """
        model = ActivityResponseDto()  # noqa: E501
        if include_optional:
            return ActivityResponseDto(
                asset_id = '',
                comment = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                type = 'comment',
                user = openapi_client.models.user_dto.UserDto(
                    avatar_color = 'primary', 
                    email = '', 
                    id = '', 
                    name = '', 
                    profile_image_path = '', )
            )
        else:
            return ActivityResponseDto(
                asset_id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                type = 'comment',
                user = openapi_client.models.user_dto.UserDto(
                    avatar_color = 'primary', 
                    email = '', 
                    id = '', 
                    name = '', 
                    profile_image_path = '', ),
        )
        """

    def testActivityResponseDto(self):
        """Test ActivityResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
