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

from openapi_client.models.album_count_response_dto import AlbumCountResponseDto  # noqa: E501

class TestAlbumCountResponseDto(unittest.TestCase):
    """AlbumCountResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlbumCountResponseDto:
        """Test AlbumCountResponseDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlbumCountResponseDto`
        """
        model = AlbumCountResponseDto()  # noqa: E501
        if include_optional:
            return AlbumCountResponseDto(
                not_shared = 56,
                owned = 56,
                shared = 56
            )
        else:
            return AlbumCountResponseDto(
                not_shared = 56,
                owned = 56,
                shared = 56,
        )
        """

    def testAlbumCountResponseDto(self):
        """Test AlbumCountResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()