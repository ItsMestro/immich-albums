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

from openapi_client.models.all_job_status_response_dto import AllJobStatusResponseDto  # noqa: E501

class TestAllJobStatusResponseDto(unittest.TestCase):
    """AllJobStatusResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AllJobStatusResponseDto:
        """Test AllJobStatusResponseDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AllJobStatusResponseDto`
        """
        model = AllJobStatusResponseDto()  # noqa: E501
        if include_optional:
            return AllJobStatusResponseDto(
                background_task = openapi_client.models.job_status_dto.JobStatusDto(
                    job_counts = openapi_client.models.job_counts_dto.JobCountsDto(
                        active = 56, 
                        completed = 56, 
                        delayed = 56, 
                        failed = 56, 
                        paused = 56, 
                        waiting = 56, ), 
                    queue_status = openapi_client.models.queue_status_dto.QueueStatusDto(
                        is_active = True, 
                        is_paused = True, ), ),
                clip_encoding = openapi_client.models.job_status_dto.JobStatusDto(
                    job_counts = openapi_client.models.job_counts_dto.JobCountsDto(
                        active = 56, 
                        completed = 56, 
                        delayed = 56, 
                        failed = 56, 
                        paused = 56, 
                        waiting = 56, ), 
                    queue_status = openapi_client.models.queue_status_dto.QueueStatusDto(
                        is_active = True, 
                        is_paused = True, ), ),
                library = openapi_client.models.job_status_dto.JobStatusDto(
                    job_counts = openapi_client.models.job_counts_dto.JobCountsDto(
                        active = 56, 
                        completed = 56, 
                        delayed = 56, 
                        failed = 56, 
                        paused = 56, 
                        waiting = 56, ), 
                    queue_status = openapi_client.models.queue_status_dto.QueueStatusDto(
                        is_active = True, 
                        is_paused = True, ), ),
                metadata_extraction = openapi_client.models.job_status_dto.JobStatusDto(
                    job_counts = openapi_client.models.job_counts_dto.JobCountsDto(
                        active = 56, 
                        completed = 56, 
                        delayed = 56, 
                        failed = 56, 
                        paused = 56, 
                        waiting = 56, ), 
                    queue_status = openapi_client.models.queue_status_dto.QueueStatusDto(
                        is_active = True, 
                        is_paused = True, ), ),
                object_tagging = openapi_client.models.job_status_dto.JobStatusDto(
                    job_counts = openapi_client.models.job_counts_dto.JobCountsDto(
                        active = 56, 
                        completed = 56, 
                        delayed = 56, 
                        failed = 56, 
                        paused = 56, 
                        waiting = 56, ), 
                    queue_status = openapi_client.models.queue_status_dto.QueueStatusDto(
                        is_active = True, 
                        is_paused = True, ), ),
                recognize_faces = openapi_client.models.job_status_dto.JobStatusDto(
                    job_counts = openapi_client.models.job_counts_dto.JobCountsDto(
                        active = 56, 
                        completed = 56, 
                        delayed = 56, 
                        failed = 56, 
                        paused = 56, 
                        waiting = 56, ), 
                    queue_status = openapi_client.models.queue_status_dto.QueueStatusDto(
                        is_active = True, 
                        is_paused = True, ), ),
                search = openapi_client.models.job_status_dto.JobStatusDto(
                    job_counts = openapi_client.models.job_counts_dto.JobCountsDto(
                        active = 56, 
                        completed = 56, 
                        delayed = 56, 
                        failed = 56, 
                        paused = 56, 
                        waiting = 56, ), 
                    queue_status = openapi_client.models.queue_status_dto.QueueStatusDto(
                        is_active = True, 
                        is_paused = True, ), ),
                sidecar = openapi_client.models.job_status_dto.JobStatusDto(
                    job_counts = openapi_client.models.job_counts_dto.JobCountsDto(
                        active = 56, 
                        completed = 56, 
                        delayed = 56, 
                        failed = 56, 
                        paused = 56, 
                        waiting = 56, ), 
                    queue_status = openapi_client.models.queue_status_dto.QueueStatusDto(
                        is_active = True, 
                        is_paused = True, ), ),
                storage_template_migration = openapi_client.models.job_status_dto.JobStatusDto(
                    job_counts = openapi_client.models.job_counts_dto.JobCountsDto(
                        active = 56, 
                        completed = 56, 
                        delayed = 56, 
                        failed = 56, 
                        paused = 56, 
                        waiting = 56, ), 
                    queue_status = openapi_client.models.queue_status_dto.QueueStatusDto(
                        is_active = True, 
                        is_paused = True, ), ),
                thumbnail_generation = openapi_client.models.job_status_dto.JobStatusDto(
                    job_counts = openapi_client.models.job_counts_dto.JobCountsDto(
                        active = 56, 
                        completed = 56, 
                        delayed = 56, 
                        failed = 56, 
                        paused = 56, 
                        waiting = 56, ), 
                    queue_status = openapi_client.models.queue_status_dto.QueueStatusDto(
                        is_active = True, 
                        is_paused = True, ), ),
                video_conversion = openapi_client.models.job_status_dto.JobStatusDto(
                    job_counts = openapi_client.models.job_counts_dto.JobCountsDto(
                        active = 56, 
                        completed = 56, 
                        delayed = 56, 
                        failed = 56, 
                        paused = 56, 
                        waiting = 56, ), 
                    queue_status = openapi_client.models.queue_status_dto.QueueStatusDto(
                        is_active = True, 
                        is_paused = True, ), )
            )
        else:
            return AllJobStatusResponseDto(
                background_task = openapi_client.models.job_status_dto.JobStatusDto(
                    job_counts = openapi_client.models.job_counts_dto.JobCountsDto(
                        active = 56, 
                        completed = 56, 
                        delayed = 56, 
                        failed = 56, 
                        paused = 56, 
                        waiting = 56, ), 
                    queue_status = openapi_client.models.queue_status_dto.QueueStatusDto(
                        is_active = True, 
                        is_paused = True, ), ),
                clip_encoding = openapi_client.models.job_status_dto.JobStatusDto(
                    job_counts = openapi_client.models.job_counts_dto.JobCountsDto(
                        active = 56, 
                        completed = 56, 
                        delayed = 56, 
                        failed = 56, 
                        paused = 56, 
                        waiting = 56, ), 
                    queue_status = openapi_client.models.queue_status_dto.QueueStatusDto(
                        is_active = True, 
                        is_paused = True, ), ),
                library = openapi_client.models.job_status_dto.JobStatusDto(
                    job_counts = openapi_client.models.job_counts_dto.JobCountsDto(
                        active = 56, 
                        completed = 56, 
                        delayed = 56, 
                        failed = 56, 
                        paused = 56, 
                        waiting = 56, ), 
                    queue_status = openapi_client.models.queue_status_dto.QueueStatusDto(
                        is_active = True, 
                        is_paused = True, ), ),
                metadata_extraction = openapi_client.models.job_status_dto.JobStatusDto(
                    job_counts = openapi_client.models.job_counts_dto.JobCountsDto(
                        active = 56, 
                        completed = 56, 
                        delayed = 56, 
                        failed = 56, 
                        paused = 56, 
                        waiting = 56, ), 
                    queue_status = openapi_client.models.queue_status_dto.QueueStatusDto(
                        is_active = True, 
                        is_paused = True, ), ),
                object_tagging = openapi_client.models.job_status_dto.JobStatusDto(
                    job_counts = openapi_client.models.job_counts_dto.JobCountsDto(
                        active = 56, 
                        completed = 56, 
                        delayed = 56, 
                        failed = 56, 
                        paused = 56, 
                        waiting = 56, ), 
                    queue_status = openapi_client.models.queue_status_dto.QueueStatusDto(
                        is_active = True, 
                        is_paused = True, ), ),
                recognize_faces = openapi_client.models.job_status_dto.JobStatusDto(
                    job_counts = openapi_client.models.job_counts_dto.JobCountsDto(
                        active = 56, 
                        completed = 56, 
                        delayed = 56, 
                        failed = 56, 
                        paused = 56, 
                        waiting = 56, ), 
                    queue_status = openapi_client.models.queue_status_dto.QueueStatusDto(
                        is_active = True, 
                        is_paused = True, ), ),
                search = openapi_client.models.job_status_dto.JobStatusDto(
                    job_counts = openapi_client.models.job_counts_dto.JobCountsDto(
                        active = 56, 
                        completed = 56, 
                        delayed = 56, 
                        failed = 56, 
                        paused = 56, 
                        waiting = 56, ), 
                    queue_status = openapi_client.models.queue_status_dto.QueueStatusDto(
                        is_active = True, 
                        is_paused = True, ), ),
                sidecar = openapi_client.models.job_status_dto.JobStatusDto(
                    job_counts = openapi_client.models.job_counts_dto.JobCountsDto(
                        active = 56, 
                        completed = 56, 
                        delayed = 56, 
                        failed = 56, 
                        paused = 56, 
                        waiting = 56, ), 
                    queue_status = openapi_client.models.queue_status_dto.QueueStatusDto(
                        is_active = True, 
                        is_paused = True, ), ),
                storage_template_migration = openapi_client.models.job_status_dto.JobStatusDto(
                    job_counts = openapi_client.models.job_counts_dto.JobCountsDto(
                        active = 56, 
                        completed = 56, 
                        delayed = 56, 
                        failed = 56, 
                        paused = 56, 
                        waiting = 56, ), 
                    queue_status = openapi_client.models.queue_status_dto.QueueStatusDto(
                        is_active = True, 
                        is_paused = True, ), ),
                thumbnail_generation = openapi_client.models.job_status_dto.JobStatusDto(
                    job_counts = openapi_client.models.job_counts_dto.JobCountsDto(
                        active = 56, 
                        completed = 56, 
                        delayed = 56, 
                        failed = 56, 
                        paused = 56, 
                        waiting = 56, ), 
                    queue_status = openapi_client.models.queue_status_dto.QueueStatusDto(
                        is_active = True, 
                        is_paused = True, ), ),
                video_conversion = openapi_client.models.job_status_dto.JobStatusDto(
                    job_counts = openapi_client.models.job_counts_dto.JobCountsDto(
                        active = 56, 
                        completed = 56, 
                        delayed = 56, 
                        failed = 56, 
                        paused = 56, 
                        waiting = 56, ), 
                    queue_status = openapi_client.models.queue_status_dto.QueueStatusDto(
                        is_active = True, 
                        is_paused = True, ), ),
        )
        """

    def testAllJobStatusResponseDto(self):
        """Test AllJobStatusResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
