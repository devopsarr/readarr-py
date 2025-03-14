# coding: utf-8

# flake8: noqa

"""
    Readarr

    Readarr API docs

    The version of the OpenAPI document: v0.4.10.2734
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.2.0" # x-release-please-version

# import apis into sdk package
from readarr.api.api_info_api import ApiInfoApi
from readarr.api.authentication_api import AuthenticationApi
from readarr.api.author_api import AuthorApi
from readarr.api.author_editor_api import AuthorEditorApi
from readarr.api.author_lookup_api import AuthorLookupApi
from readarr.api.backup_api import BackupApi
from readarr.api.blocklist_api import BlocklistApi
from readarr.api.book_api import BookApi
from readarr.api.book_editor_api import BookEditorApi
from readarr.api.book_file_api import BookFileApi
from readarr.api.book_lookup_api import BookLookupApi
from readarr.api.bookshelf_api import BookshelfApi
from readarr.api.calendar_api import CalendarApi
from readarr.api.calendar_feed_api import CalendarFeedApi
from readarr.api.command_api import CommandApi
from readarr.api.custom_filter_api import CustomFilterApi
from readarr.api.custom_format_api import CustomFormatApi
from readarr.api.cutoff_api import CutoffApi
from readarr.api.delay_profile_api import DelayProfileApi
from readarr.api.development_config_api import DevelopmentConfigApi
from readarr.api.disk_space_api import DiskSpaceApi
from readarr.api.download_client_api import DownloadClientApi
from readarr.api.download_client_config_api import DownloadClientConfigApi
from readarr.api.edition_api import EditionApi
from readarr.api.file_system_api import FileSystemApi
from readarr.api.health_api import HealthApi
from readarr.api.history_api import HistoryApi
from readarr.api.host_config_api import HostConfigApi
from readarr.api.import_list_api import ImportListApi
from readarr.api.import_list_exclusion_api import ImportListExclusionApi
from readarr.api.indexer_api import IndexerApi
from readarr.api.indexer_config_api import IndexerConfigApi
from readarr.api.indexer_flag_api import IndexerFlagApi
from readarr.api.language_api import LanguageApi
from readarr.api.localization_api import LocalizationApi
from readarr.api.log_api import LogApi
from readarr.api.log_file_api import LogFileApi
from readarr.api.manual_import_api import ManualImportApi
from readarr.api.media_cover_api import MediaCoverApi
from readarr.api.media_management_config_api import MediaManagementConfigApi
from readarr.api.metadata_api import MetadataApi
from readarr.api.metadata_profile_api import MetadataProfileApi
from readarr.api.metadata_profile_schema_api import MetadataProfileSchemaApi
from readarr.api.metadata_provider_config_api import MetadataProviderConfigApi
from readarr.api.missing_api import MissingApi
from readarr.api.naming_config_api import NamingConfigApi
from readarr.api.notification_api import NotificationApi
from readarr.api.parse_api import ParseApi
from readarr.api.ping_api import PingApi
from readarr.api.quality_definition_api import QualityDefinitionApi
from readarr.api.quality_profile_api import QualityProfileApi
from readarr.api.quality_profile_schema_api import QualityProfileSchemaApi
from readarr.api.queue_api import QueueApi
from readarr.api.queue_action_api import QueueActionApi
from readarr.api.queue_details_api import QueueDetailsApi
from readarr.api.queue_status_api import QueueStatusApi
from readarr.api.release_api import ReleaseApi
from readarr.api.release_profile_api import ReleaseProfileApi
from readarr.api.release_push_api import ReleasePushApi
from readarr.api.remote_path_mapping_api import RemotePathMappingApi
from readarr.api.rename_book_api import RenameBookApi
from readarr.api.retag_book_api import RetagBookApi
from readarr.api.root_folder_api import RootFolderApi
from readarr.api.search_api import SearchApi
from readarr.api.series_api import SeriesApi
from readarr.api.static_resource_api import StaticResourceApi
from readarr.api.system_api import SystemApi
from readarr.api.tag_api import TagApi
from readarr.api.tag_details_api import TagDetailsApi
from readarr.api.task_api import TaskApi
from readarr.api.ui_config_api import UiConfigApi
from readarr.api.update_api import UpdateApi
from readarr.api.update_log_file_api import UpdateLogFileApi

# import ApiClient
from readarr.api_response import ApiResponse
from readarr.api_client import ApiClient
from readarr.configuration import Configuration
from readarr.exceptions import OpenApiException
from readarr.exceptions import ApiTypeError
from readarr.exceptions import ApiValueError
from readarr.exceptions import ApiKeyError
from readarr.exceptions import ApiAttributeError
from readarr.exceptions import ApiException

# import models into sdk package
from readarr.models.add_author_options import AddAuthorOptions
from readarr.models.add_book_options import AddBookOptions
from readarr.models.allow_fingerprinting import AllowFingerprinting
from readarr.models.api_info_resource import ApiInfoResource
from readarr.models.apply_tags import ApplyTags
from readarr.models.authentication_required_type import AuthenticationRequiredType
from readarr.models.authentication_type import AuthenticationType
from readarr.models.author import Author
from readarr.models.author_editor_resource import AuthorEditorResource
from readarr.models.author_lazy_loaded import AuthorLazyLoaded
from readarr.models.author_metadata import AuthorMetadata
from readarr.models.author_metadata_lazy_loaded import AuthorMetadataLazyLoaded
from readarr.models.author_resource import AuthorResource
from readarr.models.author_statistics_resource import AuthorStatisticsResource
from readarr.models.author_status_type import AuthorStatusType
from readarr.models.author_title_info import AuthorTitleInfo
from readarr.models.backup_resource import BackupResource
from readarr.models.backup_type import BackupType
from readarr.models.blocklist_bulk_resource import BlocklistBulkResource
from readarr.models.blocklist_resource import BlocklistResource
from readarr.models.blocklist_resource_paging_resource import BlocklistResourcePagingResource
from readarr.models.book import Book
from readarr.models.book_add_type import BookAddType
from readarr.models.book_editor_resource import BookEditorResource
from readarr.models.book_file import BookFile
from readarr.models.book_file_list_lazy_loaded import BookFileListLazyLoaded
from readarr.models.book_file_list_resource import BookFileListResource
from readarr.models.book_file_resource import BookFileResource
from readarr.models.book_lazy_loaded import BookLazyLoaded
from readarr.models.book_list_lazy_loaded import BookListLazyLoaded
from readarr.models.book_resource import BookResource
from readarr.models.book_resource_paging_resource import BookResourcePagingResource
from readarr.models.book_statistics_resource import BookStatisticsResource
from readarr.models.books_monitored_resource import BooksMonitoredResource
from readarr.models.bookshelf_author_resource import BookshelfAuthorResource
from readarr.models.bookshelf_resource import BookshelfResource
from readarr.models.certificate_validation_type import CertificateValidationType
from readarr.models.command import Command
from readarr.models.command_priority import CommandPriority
from readarr.models.command_resource import CommandResource
from readarr.models.command_result import CommandResult
from readarr.models.command_status import CommandStatus
from readarr.models.command_trigger import CommandTrigger
from readarr.models.contract_field import ContractField
from readarr.models.custom_filter_resource import CustomFilterResource
from readarr.models.custom_format import CustomFormat
from readarr.models.custom_format_resource import CustomFormatResource
from readarr.models.custom_format_specification_schema import CustomFormatSpecificationSchema
from readarr.models.database_type import DatabaseType
from readarr.models.delay_profile_resource import DelayProfileResource
from readarr.models.development_config_resource import DevelopmentConfigResource
from readarr.models.disk_space_resource import DiskSpaceResource
from readarr.models.download_client_bulk_resource import DownloadClientBulkResource
from readarr.models.download_client_config_resource import DownloadClientConfigResource
from readarr.models.download_client_resource import DownloadClientResource
from readarr.models.download_protocol import DownloadProtocol
from readarr.models.edition import Edition
from readarr.models.edition_lazy_loaded import EditionLazyLoaded
from readarr.models.edition_list_lazy_loaded import EditionListLazyLoaded
from readarr.models.edition_resource import EditionResource
from readarr.models.entity_history_event_type import EntityHistoryEventType
from readarr.models.file_date_type import FileDateType
from readarr.models.health_check_result import HealthCheckResult
from readarr.models.health_resource import HealthResource
from readarr.models.history_resource import HistoryResource
from readarr.models.history_resource_paging_resource import HistoryResourcePagingResource
from readarr.models.host_config_resource import HostConfigResource
from readarr.models.i_custom_format_specification import ICustomFormatSpecification
from readarr.models.import_list_bulk_resource import ImportListBulkResource
from readarr.models.import_list_exclusion_resource import ImportListExclusionResource
from readarr.models.import_list_monitor_type import ImportListMonitorType
from readarr.models.import_list_resource import ImportListResource
from readarr.models.import_list_type import ImportListType
from readarr.models.indexer_bulk_resource import IndexerBulkResource
from readarr.models.indexer_config_resource import IndexerConfigResource
from readarr.models.indexer_flag_resource import IndexerFlagResource
from readarr.models.indexer_flags import IndexerFlags
from readarr.models.indexer_resource import IndexerResource
from readarr.models.iso_country import IsoCountry
from readarr.models.language_resource import LanguageResource
from readarr.models.links import Links
from readarr.models.log_file_resource import LogFileResource
from readarr.models.log_resource import LogResource
from readarr.models.log_resource_paging_resource import LogResourcePagingResource
from readarr.models.manual_import_resource import ManualImportResource
from readarr.models.manual_import_update_resource import ManualImportUpdateResource
from readarr.models.media_cover import MediaCover
from readarr.models.media_cover_types import MediaCoverTypes
from readarr.models.media_info_model import MediaInfoModel
from readarr.models.media_info_resource import MediaInfoResource
from readarr.models.media_management_config_resource import MediaManagementConfigResource
from readarr.models.metadata_profile import MetadataProfile
from readarr.models.metadata_profile_lazy_loaded import MetadataProfileLazyLoaded
from readarr.models.metadata_profile_resource import MetadataProfileResource
from readarr.models.metadata_provider_config_resource import MetadataProviderConfigResource
from readarr.models.metadata_resource import MetadataResource
from readarr.models.monitor_types import MonitorTypes
from readarr.models.monitoring_options import MonitoringOptions
from readarr.models.naming_config_resource import NamingConfigResource
from readarr.models.new_item_monitor_types import NewItemMonitorTypes
from readarr.models.notification_resource import NotificationResource
from readarr.models.parse_resource import ParseResource
from readarr.models.parsed_book_info import ParsedBookInfo
from readarr.models.parsed_track_info import ParsedTrackInfo
from readarr.models.ping_resource import PingResource
from readarr.models.profile_format_item import ProfileFormatItem
from readarr.models.profile_format_item_resource import ProfileFormatItemResource
from readarr.models.proper_download_types import ProperDownloadTypes
from readarr.models.provider_message import ProviderMessage
from readarr.models.provider_message_type import ProviderMessageType
from readarr.models.proxy_type import ProxyType
from readarr.models.quality import Quality
from readarr.models.quality_definition_resource import QualityDefinitionResource
from readarr.models.quality_model import QualityModel
from readarr.models.quality_profile import QualityProfile
from readarr.models.quality_profile_lazy_loaded import QualityProfileLazyLoaded
from readarr.models.quality_profile_quality_item import QualityProfileQualityItem
from readarr.models.quality_profile_quality_item_resource import QualityProfileQualityItemResource
from readarr.models.quality_profile_resource import QualityProfileResource
from readarr.models.queue_bulk_resource import QueueBulkResource
from readarr.models.queue_resource import QueueResource
from readarr.models.queue_resource_paging_resource import QueueResourcePagingResource
from readarr.models.queue_status_resource import QueueStatusResource
from readarr.models.ratings import Ratings
from readarr.models.rejection import Rejection
from readarr.models.rejection_type import RejectionType
from readarr.models.release_profile_resource import ReleaseProfileResource
from readarr.models.release_resource import ReleaseResource
from readarr.models.remote_path_mapping_resource import RemotePathMappingResource
from readarr.models.rename_book_resource import RenameBookResource
from readarr.models.rescan_after_refresh_type import RescanAfterRefreshType
from readarr.models.retag_book_resource import RetagBookResource
from readarr.models.revision import Revision
from readarr.models.root_folder_resource import RootFolderResource
from readarr.models.runtime_mode import RuntimeMode
from readarr.models.select_option import SelectOption
from readarr.models.series import Series
from readarr.models.series_book_link import SeriesBookLink
from readarr.models.series_book_link_list_lazy_loaded import SeriesBookLinkListLazyLoaded
from readarr.models.series_book_link_resource import SeriesBookLinkResource
from readarr.models.series_lazy_loaded import SeriesLazyLoaded
from readarr.models.series_list_lazy_loaded import SeriesListLazyLoaded
from readarr.models.series_resource import SeriesResource
from readarr.models.sort_direction import SortDirection
from readarr.models.system_resource import SystemResource
from readarr.models.tag_details_resource import TagDetailsResource
from readarr.models.tag_difference import TagDifference
from readarr.models.tag_resource import TagResource
from readarr.models.task_resource import TaskResource
from readarr.models.tracked_download_state import TrackedDownloadState
from readarr.models.tracked_download_status import TrackedDownloadStatus
from readarr.models.tracked_download_status_message import TrackedDownloadStatusMessage
from readarr.models.ui_config_resource import UiConfigResource
from readarr.models.update_changes import UpdateChanges
from readarr.models.update_mechanism import UpdateMechanism
from readarr.models.update_resource import UpdateResource
from readarr.models.write_audio_tags_type import WriteAudioTagsType
from readarr.models.write_book_tags_type import WriteBookTagsType
