# coding: utf-8

# flake8: noqa
"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.79.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from openapi_client.models.api_key_create_dto import APIKeyCreateDto
from openapi_client.models.api_key_create_response_dto import APIKeyCreateResponseDto
from openapi_client.models.api_key_response_dto import APIKeyResponseDto
from openapi_client.models.api_key_update_dto import APIKeyUpdateDto
from openapi_client.models.add_users_dto import AddUsersDto
from openapi_client.models.admin_signup_response_dto import AdminSignupResponseDto
from openapi_client.models.album_count_response_dto import AlbumCountResponseDto
from openapi_client.models.album_response_dto import AlbumResponseDto
from openapi_client.models.all_job_status_response_dto import AllJobStatusResponseDto
from openapi_client.models.asset_bulk_update_dto import AssetBulkUpdateDto
from openapi_client.models.asset_bulk_upload_check_dto import AssetBulkUploadCheckDto
from openapi_client.models.asset_bulk_upload_check_item import AssetBulkUploadCheckItem
from openapi_client.models.asset_bulk_upload_check_response_dto import AssetBulkUploadCheckResponseDto
from openapi_client.models.asset_bulk_upload_check_result import AssetBulkUploadCheckResult
from openapi_client.models.asset_file_upload_response_dto import AssetFileUploadResponseDto
from openapi_client.models.asset_ids_dto import AssetIdsDto
from openapi_client.models.asset_ids_response_dto import AssetIdsResponseDto
from openapi_client.models.asset_job_name import AssetJobName
from openapi_client.models.asset_jobs_dto import AssetJobsDto
from openapi_client.models.asset_response_dto import AssetResponseDto
from openapi_client.models.asset_stats_response_dto import AssetStatsResponseDto
from openapi_client.models.asset_type_enum import AssetTypeEnum
from openapi_client.models.audio_codec import AudioCodec
from openapi_client.models.audit_deletes_response_dto import AuditDeletesResponseDto
from openapi_client.models.auth_device_response_dto import AuthDeviceResponseDto
from openapi_client.models.bulk_id_response_dto import BulkIdResponseDto
from openapi_client.models.bulk_ids_dto import BulkIdsDto
from openapi_client.models.clip_config import CLIPConfig
from openapi_client.models.clip_mode import CLIPMode
from openapi_client.models.cq_mode import CQMode
from openapi_client.models.change_password_dto import ChangePasswordDto
from openapi_client.models.check_duplicate_asset_dto import CheckDuplicateAssetDto
from openapi_client.models.check_duplicate_asset_response_dto import CheckDuplicateAssetResponseDto
from openapi_client.models.check_existing_assets_dto import CheckExistingAssetsDto
from openapi_client.models.check_existing_assets_response_dto import CheckExistingAssetsResponseDto
from openapi_client.models.classification_config import ClassificationConfig
from openapi_client.models.colorspace import Colorspace
from openapi_client.models.create_album_dto import CreateAlbumDto
from openapi_client.models.create_library_dto import CreateLibraryDto
from openapi_client.models.create_profile_image_response_dto import CreateProfileImageResponseDto
from openapi_client.models.create_tag_dto import CreateTagDto
from openapi_client.models.create_user_dto import CreateUserDto
from openapi_client.models.curated_locations_response_dto import CuratedLocationsResponseDto
from openapi_client.models.curated_objects_response_dto import CuratedObjectsResponseDto
from openapi_client.models.delete_asset_dto import DeleteAssetDto
from openapi_client.models.delete_asset_response_dto import DeleteAssetResponseDto
from openapi_client.models.delete_asset_status import DeleteAssetStatus
from openapi_client.models.download_archive_info import DownloadArchiveInfo
from openapi_client.models.download_info_dto import DownloadInfoDto
from openapi_client.models.download_response_dto import DownloadResponseDto
from openapi_client.models.entity_type import EntityType
from openapi_client.models.exif_response_dto import ExifResponseDto
from openapi_client.models.import_asset_dto import ImportAssetDto
from openapi_client.models.job_command import JobCommand
from openapi_client.models.job_command_dto import JobCommandDto
from openapi_client.models.job_counts_dto import JobCountsDto
from openapi_client.models.job_name import JobName
from openapi_client.models.job_settings_dto import JobSettingsDto
from openapi_client.models.job_status_dto import JobStatusDto
from openapi_client.models.library_response_dto import LibraryResponseDto
from openapi_client.models.library_stats_response_dto import LibraryStatsResponseDto
from openapi_client.models.library_type import LibraryType
from openapi_client.models.login_credential_dto import LoginCredentialDto
from openapi_client.models.login_response_dto import LoginResponseDto
from openapi_client.models.logout_response_dto import LogoutResponseDto
from openapi_client.models.map_marker_response_dto import MapMarkerResponseDto
from openapi_client.models.memory_lane_response_dto import MemoryLaneResponseDto
from openapi_client.models.merge_person_dto import MergePersonDto
from openapi_client.models.model_type import ModelType
from openapi_client.models.o_auth_authorize_response_dto import OAuthAuthorizeResponseDto
from openapi_client.models.o_auth_callback_dto import OAuthCallbackDto
from openapi_client.models.o_auth_config_dto import OAuthConfigDto
from openapi_client.models.o_auth_config_response_dto import OAuthConfigResponseDto
from openapi_client.models.people_response_dto import PeopleResponseDto
from openapi_client.models.people_update_dto import PeopleUpdateDto
from openapi_client.models.people_update_item import PeopleUpdateItem
from openapi_client.models.person_response_dto import PersonResponseDto
from openapi_client.models.person_update_dto import PersonUpdateDto
from openapi_client.models.queue_status_dto import QueueStatusDto
from openapi_client.models.recognition_config import RecognitionConfig
from openapi_client.models.scan_library_dto import ScanLibraryDto
from openapi_client.models.search_album_response_dto import SearchAlbumResponseDto
from openapi_client.models.search_asset_dto import SearchAssetDto
from openapi_client.models.search_asset_response_dto import SearchAssetResponseDto
from openapi_client.models.search_explore_item import SearchExploreItem
from openapi_client.models.search_explore_response_dto import SearchExploreResponseDto
from openapi_client.models.search_facet_count_response_dto import SearchFacetCountResponseDto
from openapi_client.models.search_facet_response_dto import SearchFacetResponseDto
from openapi_client.models.search_response_dto import SearchResponseDto
from openapi_client.models.server_config_dto import ServerConfigDto
from openapi_client.models.server_features_dto import ServerFeaturesDto
from openapi_client.models.server_info_response_dto import ServerInfoResponseDto
from openapi_client.models.server_media_types_response_dto import ServerMediaTypesResponseDto
from openapi_client.models.server_ping_response import ServerPingResponse
from openapi_client.models.server_stats_response_dto import ServerStatsResponseDto
from openapi_client.models.server_version_response_dto import ServerVersionResponseDto
from openapi_client.models.shared_link_create_dto import SharedLinkCreateDto
from openapi_client.models.shared_link_edit_dto import SharedLinkEditDto
from openapi_client.models.shared_link_response_dto import SharedLinkResponseDto
from openapi_client.models.shared_link_type import SharedLinkType
from openapi_client.models.sign_up_dto import SignUpDto
from openapi_client.models.smart_info_response_dto import SmartInfoResponseDto
from openapi_client.models.system_config_dto import SystemConfigDto
from openapi_client.models.system_config_f_fmpeg_dto import SystemConfigFFmpegDto
from openapi_client.models.system_config_job_dto import SystemConfigJobDto
from openapi_client.models.system_config_machine_learning_dto import SystemConfigMachineLearningDto
from openapi_client.models.system_config_map_dto import SystemConfigMapDto
from openapi_client.models.system_config_o_auth_dto import SystemConfigOAuthDto
from openapi_client.models.system_config_password_login_dto import SystemConfigPasswordLoginDto
from openapi_client.models.system_config_storage_template_dto import SystemConfigStorageTemplateDto
from openapi_client.models.system_config_template_storage_option_dto import SystemConfigTemplateStorageOptionDto
from openapi_client.models.system_config_thumbnail_dto import SystemConfigThumbnailDto
from openapi_client.models.tag_response_dto import TagResponseDto
from openapi_client.models.tag_type_enum import TagTypeEnum
from openapi_client.models.thumbnail_format import ThumbnailFormat
from openapi_client.models.time_bucket_response_dto import TimeBucketResponseDto
from openapi_client.models.time_bucket_size import TimeBucketSize
from openapi_client.models.tone_mapping import ToneMapping
from openapi_client.models.transcode_hw_accel import TranscodeHWAccel
from openapi_client.models.transcode_policy import TranscodePolicy
from openapi_client.models.update_album_dto import UpdateAlbumDto
from openapi_client.models.update_asset_dto import UpdateAssetDto
from openapi_client.models.update_library_dto import UpdateLibraryDto
from openapi_client.models.update_tag_dto import UpdateTagDto
from openapi_client.models.update_user_dto import UpdateUserDto
from openapi_client.models.usage_by_user_dto import UsageByUserDto
from openapi_client.models.user_count_response_dto import UserCountResponseDto
from openapi_client.models.user_response_dto import UserResponseDto
from openapi_client.models.validate_access_token_response_dto import ValidateAccessTokenResponseDto
from openapi_client.models.video_codec import VideoCodec
