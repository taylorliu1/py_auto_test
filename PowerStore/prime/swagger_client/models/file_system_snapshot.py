# coding: utf-8

"""
    PowerStore REST API

    Storage cluster REST API definition. ( For \"Try It Out\", use the cluster management IP address to load this swaggerui interface. )  # noqa: E501

    OpenAPI spec version: 3.0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from prime.swagger_client.configuration import Configuration


class FileSystemSnapshot(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'description': 'str',
        'expiration_timestamp': 'datetime',
        'is_auto_delete_enabled': 'bool',
        'access_type': 'FileSystemSnapshotAccessTypeEnum',
        'access_policy': 'FileSystemAccessPolicyEnum',
        'locking_policy': 'FileSystemLockingPolicyEnum',
        'folder_rename_policy': 'FileSystemFolderRenamePolicyEnum',
        'is_smb_sync_writes_enabled': 'bool',
        'is_smb_no_notify_enabled': 'bool',
        'is_smb_op_locks_enabled': 'bool',
        'is_smb_notify_on_access_enabled': 'bool',
        'is_smb_notify_on_write_enabled': 'bool',
        'smb_notify_on_change_dir_depth': 'int',
        'is_async_m_time_enabled': 'bool',
        'file_events_publishing_mode': 'FileEventsPublishingModeEnum'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'expiration_timestamp': 'expiration_timestamp',
        'is_auto_delete_enabled': 'is_auto_delete_enabled',
        'access_type': 'access_type',
        'access_policy': 'access_policy',
        'locking_policy': 'locking_policy',
        'folder_rename_policy': 'folder_rename_policy',
        'is_smb_sync_writes_enabled': 'is_smb_sync_writes_enabled',
        'is_smb_no_notify_enabled': 'is_smb_no_notify_enabled',
        'is_smb_op_locks_enabled': 'is_smb_op_locks_enabled',
        'is_smb_notify_on_access_enabled': 'is_smb_notify_on_access_enabled',
        'is_smb_notify_on_write_enabled': 'is_smb_notify_on_write_enabled',
        'smb_notify_on_change_dir_depth': 'smb_notify_on_change_dir_depth',
        'is_async_m_time_enabled': 'is_async_MTime_enabled',
        'file_events_publishing_mode': 'file_events_publishing_mode'
    }

    def __init__(self, name=None, description=None, expiration_timestamp=None, is_auto_delete_enabled=None, access_type=None, access_policy=None, locking_policy=None, folder_rename_policy=None, is_smb_sync_writes_enabled=None, is_smb_no_notify_enabled=None, is_smb_op_locks_enabled=None, is_smb_notify_on_access_enabled=None, is_smb_notify_on_write_enabled=None, smb_notify_on_change_dir_depth=None, is_async_m_time_enabled=None, file_events_publishing_mode=None, _configuration=None):  # noqa: E501
        """FileSystemSnapshot - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._description = None
        self._expiration_timestamp = None
        self._is_auto_delete_enabled = None
        self._access_type = None
        self._access_policy = None
        self._locking_policy = None
        self._folder_rename_policy = None
        self._is_smb_sync_writes_enabled = None
        self._is_smb_no_notify_enabled = None
        self._is_smb_op_locks_enabled = None
        self._is_smb_notify_on_access_enabled = None
        self._is_smb_notify_on_write_enabled = None
        self._smb_notify_on_change_dir_depth = None
        self._is_async_m_time_enabled = None
        self._file_events_publishing_mode = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if expiration_timestamp is not None:
            self.expiration_timestamp = expiration_timestamp
        if is_auto_delete_enabled is not None:
            self.is_auto_delete_enabled = is_auto_delete_enabled
        if access_type is not None:
            self.access_type = access_type
        if access_policy is not None:
            self.access_policy = access_policy
        if locking_policy is not None:
            self.locking_policy = locking_policy
        if folder_rename_policy is not None:
            self.folder_rename_policy = folder_rename_policy
        if is_smb_sync_writes_enabled is not None:
            self.is_smb_sync_writes_enabled = is_smb_sync_writes_enabled
        if is_smb_no_notify_enabled is not None:
            self.is_smb_no_notify_enabled = is_smb_no_notify_enabled
        if is_smb_op_locks_enabled is not None:
            self.is_smb_op_locks_enabled = is_smb_op_locks_enabled
        if is_smb_notify_on_access_enabled is not None:
            self.is_smb_notify_on_access_enabled = is_smb_notify_on_access_enabled
        if is_smb_notify_on_write_enabled is not None:
            self.is_smb_notify_on_write_enabled = is_smb_notify_on_write_enabled
        if smb_notify_on_change_dir_depth is not None:
            self.smb_notify_on_change_dir_depth = smb_notify_on_change_dir_depth
        if is_async_m_time_enabled is not None:
            self.is_async_m_time_enabled = is_async_m_time_enabled
        if file_events_publishing_mode is not None:
            self.file_events_publishing_mode = file_events_publishing_mode

    @property
    def name(self):
        """Gets the name of this FileSystemSnapshot.  # noqa: E501

        Name of the snapshot. The default name of the snapshot is the date and time when the snapshot is taken.  # noqa: E501

        :return: The name of this FileSystemSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FileSystemSnapshot.

        Name of the snapshot. The default name of the snapshot is the date and time when the snapshot is taken.  # noqa: E501

        :param name: The name of this FileSystemSnapshot.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this FileSystemSnapshot.  # noqa: E501

        Description of the snapshot.  # noqa: E501

        :return: The description of this FileSystemSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FileSystemSnapshot.

        Description of the snapshot.  # noqa: E501

        :param description: The description of this FileSystemSnapshot.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                description is not None and len(description) > 255):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def expiration_timestamp(self):
        """Gets the expiration_timestamp of this FileSystemSnapshot.  # noqa: E501

        Time, when the snapshot will expire.  # noqa: E501

        :return: The expiration_timestamp of this FileSystemSnapshot.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_timestamp

    @expiration_timestamp.setter
    def expiration_timestamp(self, expiration_timestamp):
        """Sets the expiration_timestamp of this FileSystemSnapshot.

        Time, when the snapshot will expire.  # noqa: E501

        :param expiration_timestamp: The expiration_timestamp of this FileSystemSnapshot.  # noqa: E501
        :type: datetime
        """

        self._expiration_timestamp = expiration_timestamp

    @property
    def is_auto_delete_enabled(self):
        """Gets the is_auto_delete_enabled of this FileSystemSnapshot.  # noqa: E501

        Indicates whether the snapshot can be automatically deleted per threshold settings. Values are: * true - Snapshot can be automatically deleted per threshold settings. * false - Snapshot cannot be automatically deleted.   # noqa: E501

        :return: The is_auto_delete_enabled of this FileSystemSnapshot.  # noqa: E501
        :rtype: bool
        """
        return self._is_auto_delete_enabled

    @is_auto_delete_enabled.setter
    def is_auto_delete_enabled(self, is_auto_delete_enabled):
        """Sets the is_auto_delete_enabled of this FileSystemSnapshot.

        Indicates whether the snapshot can be automatically deleted per threshold settings. Values are: * true - Snapshot can be automatically deleted per threshold settings. * false - Snapshot cannot be automatically deleted.   # noqa: E501

        :param is_auto_delete_enabled: The is_auto_delete_enabled of this FileSystemSnapshot.  # noqa: E501
        :type: bool
        """

        self._is_auto_delete_enabled = is_auto_delete_enabled

    @property
    def access_type(self):
        """Gets the access_type of this FileSystemSnapshot.  # noqa: E501


        :return: The access_type of this FileSystemSnapshot.  # noqa: E501
        :rtype: FileSystemSnapshotAccessTypeEnum
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        """Sets the access_type of this FileSystemSnapshot.


        :param access_type: The access_type of this FileSystemSnapshot.  # noqa: E501
        :type: FileSystemSnapshotAccessTypeEnum
        """

        self._access_type = access_type

    @property
    def access_policy(self):
        """Gets the access_policy of this FileSystemSnapshot.  # noqa: E501


        :return: The access_policy of this FileSystemSnapshot.  # noqa: E501
        :rtype: FileSystemAccessPolicyEnum
        """
        return self._access_policy

    @access_policy.setter
    def access_policy(self, access_policy):
        """Sets the access_policy of this FileSystemSnapshot.


        :param access_policy: The access_policy of this FileSystemSnapshot.  # noqa: E501
        :type: FileSystemAccessPolicyEnum
        """

        self._access_policy = access_policy

    @property
    def locking_policy(self):
        """Gets the locking_policy of this FileSystemSnapshot.  # noqa: E501


        :return: The locking_policy of this FileSystemSnapshot.  # noqa: E501
        :rtype: FileSystemLockingPolicyEnum
        """
        return self._locking_policy

    @locking_policy.setter
    def locking_policy(self, locking_policy):
        """Sets the locking_policy of this FileSystemSnapshot.


        :param locking_policy: The locking_policy of this FileSystemSnapshot.  # noqa: E501
        :type: FileSystemLockingPolicyEnum
        """

        self._locking_policy = locking_policy

    @property
    def folder_rename_policy(self):
        """Gets the folder_rename_policy of this FileSystemSnapshot.  # noqa: E501


        :return: The folder_rename_policy of this FileSystemSnapshot.  # noqa: E501
        :rtype: FileSystemFolderRenamePolicyEnum
        """
        return self._folder_rename_policy

    @folder_rename_policy.setter
    def folder_rename_policy(self, folder_rename_policy):
        """Sets the folder_rename_policy of this FileSystemSnapshot.


        :param folder_rename_policy: The folder_rename_policy of this FileSystemSnapshot.  # noqa: E501
        :type: FileSystemFolderRenamePolicyEnum
        """

        self._folder_rename_policy = folder_rename_policy

    @property
    def is_smb_sync_writes_enabled(self):
        """Gets the is_smb_sync_writes_enabled of this FileSystemSnapshot.  # noqa: E501

        Indicates whether the synchronous writes option is enabled on the file system. Values are: * true - Synchronous writes option is enabled on the file system. * false - Synchronous writes option is disabled on the file system.   # noqa: E501

        :return: The is_smb_sync_writes_enabled of this FileSystemSnapshot.  # noqa: E501
        :rtype: bool
        """
        return self._is_smb_sync_writes_enabled

    @is_smb_sync_writes_enabled.setter
    def is_smb_sync_writes_enabled(self, is_smb_sync_writes_enabled):
        """Sets the is_smb_sync_writes_enabled of this FileSystemSnapshot.

        Indicates whether the synchronous writes option is enabled on the file system. Values are: * true - Synchronous writes option is enabled on the file system. * false - Synchronous writes option is disabled on the file system.   # noqa: E501

        :param is_smb_sync_writes_enabled: The is_smb_sync_writes_enabled of this FileSystemSnapshot.  # noqa: E501
        :type: bool
        """

        self._is_smb_sync_writes_enabled = is_smb_sync_writes_enabled

    @property
    def is_smb_no_notify_enabled(self):
        """Gets the is_smb_no_notify_enabled of this FileSystemSnapshot.  # noqa: E501

        Indicates whether notifications of changes to a directory file structure are enabled. * true - Change directory notifications are disabled. * false - Change directory notifications are enabled.   # noqa: E501

        :return: The is_smb_no_notify_enabled of this FileSystemSnapshot.  # noqa: E501
        :rtype: bool
        """
        return self._is_smb_no_notify_enabled

    @is_smb_no_notify_enabled.setter
    def is_smb_no_notify_enabled(self, is_smb_no_notify_enabled):
        """Sets the is_smb_no_notify_enabled of this FileSystemSnapshot.

        Indicates whether notifications of changes to a directory file structure are enabled. * true - Change directory notifications are disabled. * false - Change directory notifications are enabled.   # noqa: E501

        :param is_smb_no_notify_enabled: The is_smb_no_notify_enabled of this FileSystemSnapshot.  # noqa: E501
        :type: bool
        """

        self._is_smb_no_notify_enabled = is_smb_no_notify_enabled

    @property
    def is_smb_op_locks_enabled(self):
        """Gets the is_smb_op_locks_enabled of this FileSystemSnapshot.  # noqa: E501

        Indicates whether opportunistic file locking is enabled on the file system. Values are: * true - Opportunistic file locking is enabled on the file system. * false - Opportunistic file locking is disabled on the file system.   # noqa: E501

        :return: The is_smb_op_locks_enabled of this FileSystemSnapshot.  # noqa: E501
        :rtype: bool
        """
        return self._is_smb_op_locks_enabled

    @is_smb_op_locks_enabled.setter
    def is_smb_op_locks_enabled(self, is_smb_op_locks_enabled):
        """Sets the is_smb_op_locks_enabled of this FileSystemSnapshot.

        Indicates whether opportunistic file locking is enabled on the file system. Values are: * true - Opportunistic file locking is enabled on the file system. * false - Opportunistic file locking is disabled on the file system.   # noqa: E501

        :param is_smb_op_locks_enabled: The is_smb_op_locks_enabled of this FileSystemSnapshot.  # noqa: E501
        :type: bool
        """

        self._is_smb_op_locks_enabled = is_smb_op_locks_enabled

    @property
    def is_smb_notify_on_access_enabled(self):
        """Gets the is_smb_notify_on_access_enabled of this FileSystemSnapshot.  # noqa: E501

        Indicates whether file access notifications are enabled on the file system. Values are: * true - File access notifications are enabled on the file system. * false - File access notifications are disabled on the file system.   # noqa: E501

        :return: The is_smb_notify_on_access_enabled of this FileSystemSnapshot.  # noqa: E501
        :rtype: bool
        """
        return self._is_smb_notify_on_access_enabled

    @is_smb_notify_on_access_enabled.setter
    def is_smb_notify_on_access_enabled(self, is_smb_notify_on_access_enabled):
        """Sets the is_smb_notify_on_access_enabled of this FileSystemSnapshot.

        Indicates whether file access notifications are enabled on the file system. Values are: * true - File access notifications are enabled on the file system. * false - File access notifications are disabled on the file system.   # noqa: E501

        :param is_smb_notify_on_access_enabled: The is_smb_notify_on_access_enabled of this FileSystemSnapshot.  # noqa: E501
        :type: bool
        """

        self._is_smb_notify_on_access_enabled = is_smb_notify_on_access_enabled

    @property
    def is_smb_notify_on_write_enabled(self):
        """Gets the is_smb_notify_on_write_enabled of this FileSystemSnapshot.  # noqa: E501

        Indicates whether file writes notifications are enabled on the file system. Values are: * true - File writes notifications are enabled on the file system. * false - File writes notifications are disabled on the file system.   # noqa: E501

        :return: The is_smb_notify_on_write_enabled of this FileSystemSnapshot.  # noqa: E501
        :rtype: bool
        """
        return self._is_smb_notify_on_write_enabled

    @is_smb_notify_on_write_enabled.setter
    def is_smb_notify_on_write_enabled(self, is_smb_notify_on_write_enabled):
        """Sets the is_smb_notify_on_write_enabled of this FileSystemSnapshot.

        Indicates whether file writes notifications are enabled on the file system. Values are: * true - File writes notifications are enabled on the file system. * false - File writes notifications are disabled on the file system.   # noqa: E501

        :param is_smb_notify_on_write_enabled: The is_smb_notify_on_write_enabled of this FileSystemSnapshot.  # noqa: E501
        :type: bool
        """

        self._is_smb_notify_on_write_enabled = is_smb_notify_on_write_enabled

    @property
    def smb_notify_on_change_dir_depth(self):
        """Gets the smb_notify_on_change_dir_depth of this FileSystemSnapshot.  # noqa: E501

        Lowest directory level to which the enabled notifications apply, if any.  # noqa: E501

        :return: The smb_notify_on_change_dir_depth of this FileSystemSnapshot.  # noqa: E501
        :rtype: int
        """
        return self._smb_notify_on_change_dir_depth

    @smb_notify_on_change_dir_depth.setter
    def smb_notify_on_change_dir_depth(self, smb_notify_on_change_dir_depth):
        """Sets the smb_notify_on_change_dir_depth of this FileSystemSnapshot.

        Lowest directory level to which the enabled notifications apply, if any.  # noqa: E501

        :param smb_notify_on_change_dir_depth: The smb_notify_on_change_dir_depth of this FileSystemSnapshot.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                smb_notify_on_change_dir_depth is not None and smb_notify_on_change_dir_depth > 512):  # noqa: E501
            raise ValueError("Invalid value for `smb_notify_on_change_dir_depth`, must be a value less than or equal to `512`")  # noqa: E501
        if (self._configuration.client_side_validation and
                smb_notify_on_change_dir_depth is not None and smb_notify_on_change_dir_depth < 1):  # noqa: E501
            raise ValueError("Invalid value for `smb_notify_on_change_dir_depth`, must be a value greater than or equal to `1`")  # noqa: E501

        self._smb_notify_on_change_dir_depth = smb_notify_on_change_dir_depth

    @property
    def is_async_m_time_enabled(self):
        """Gets the is_async_m_time_enabled of this FileSystemSnapshot.  # noqa: E501

        Indicates whether asynchronous MTIME is enabled on the protocol snaps that are mounted writeable. Values are: * true - Asynchronous MTIME is enabled on the file system. * false - Asynchronous MTIME is disabled on the file system.           # noqa: E501

        :return: The is_async_m_time_enabled of this FileSystemSnapshot.  # noqa: E501
        :rtype: bool
        """
        return self._is_async_m_time_enabled

    @is_async_m_time_enabled.setter
    def is_async_m_time_enabled(self, is_async_m_time_enabled):
        """Sets the is_async_m_time_enabled of this FileSystemSnapshot.

        Indicates whether asynchronous MTIME is enabled on the protocol snaps that are mounted writeable. Values are: * true - Asynchronous MTIME is enabled on the file system. * false - Asynchronous MTIME is disabled on the file system.           # noqa: E501

        :param is_async_m_time_enabled: The is_async_m_time_enabled of this FileSystemSnapshot.  # noqa: E501
        :type: bool
        """

        self._is_async_m_time_enabled = is_async_m_time_enabled

    @property
    def file_events_publishing_mode(self):
        """Gets the file_events_publishing_mode of this FileSystemSnapshot.  # noqa: E501

         Was added in version 3.0.0.0.  # noqa: E501

        :return: The file_events_publishing_mode of this FileSystemSnapshot.  # noqa: E501
        :rtype: FileEventsPublishingModeEnum
        """
        return self._file_events_publishing_mode

    @file_events_publishing_mode.setter
    def file_events_publishing_mode(self, file_events_publishing_mode):
        """Sets the file_events_publishing_mode of this FileSystemSnapshot.

         Was added in version 3.0.0.0.  # noqa: E501

        :param file_events_publishing_mode: The file_events_publishing_mode of this FileSystemSnapshot.  # noqa: E501
        :type: FileEventsPublishingModeEnum
        """

        self._file_events_publishing_mode = file_events_publishing_mode

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(FileSystemSnapshot, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FileSystemSnapshot):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileSystemSnapshot):
            return True

        return self.to_dict() != other.to_dict()
