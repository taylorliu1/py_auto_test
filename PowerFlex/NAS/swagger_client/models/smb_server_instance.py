# coding: utf-8

"""
    PowerFlex NAS Management REST API

    NAS Storage Management REST API definition.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SmbServerInstance(object):
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
        'id': 'str',
        'nas_server_id': 'str',
        'computer_name': 'str',
        'domain': 'str',
        'netbios_name': 'str',
        'workgroup': 'str',
        'description': 'str',
        'is_standalone': 'bool',
        'is_joined': 'bool',
        'nas_server': 'NasServersInstance'
    }

    attribute_map = {
        'id': 'id',
        'nas_server_id': 'nas_server_id',
        'computer_name': 'computer_name',
        'domain': 'domain',
        'netbios_name': 'netbios_name',
        'workgroup': 'workgroup',
        'description': 'description',
        'is_standalone': 'is_standalone',
        'is_joined': 'is_joined',
        'nas_server': 'nas_server'
    }

    def __init__(self, id=None, nas_server_id=None, computer_name=None, domain=None, netbios_name=None, workgroup=None, description=None, is_standalone=None, is_joined=None, nas_server=None):  # noqa: E501
        """SmbServerInstance - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._nas_server_id = None
        self._computer_name = None
        self._domain = None
        self._netbios_name = None
        self._workgroup = None
        self._description = None
        self._is_standalone = None
        self._is_joined = None
        self._nas_server = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if nas_server_id is not None:
            self.nas_server_id = nas_server_id
        if computer_name is not None:
            self.computer_name = computer_name
        if domain is not None:
            self.domain = domain
        if netbios_name is not None:
            self.netbios_name = netbios_name
        if workgroup is not None:
            self.workgroup = workgroup
        if description is not None:
            self.description = description
        if is_standalone is not None:
            self.is_standalone = is_standalone
        if is_joined is not None:
            self.is_joined = is_joined
        if nas_server is not None:
            self.nas_server = nas_server

    @property
    def id(self):
        """Gets the id of this SmbServerInstance.  # noqa: E501

        Unique identifier of the SMB server.  # noqa: E501

        :return: The id of this SmbServerInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SmbServerInstance.

        Unique identifier of the SMB server.  # noqa: E501

        :param id: The id of this SmbServerInstance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def nas_server_id(self):
        """Gets the nas_server_id of this SmbServerInstance.  # noqa: E501

        Unique identifier of the NAS server.  # noqa: E501

        :return: The nas_server_id of this SmbServerInstance.  # noqa: E501
        :rtype: str
        """
        return self._nas_server_id

    @nas_server_id.setter
    def nas_server_id(self, nas_server_id):
        """Sets the nas_server_id of this SmbServerInstance.

        Unique identifier of the NAS server.  # noqa: E501

        :param nas_server_id: The nas_server_id of this SmbServerInstance.  # noqa: E501
        :type: str
        """

        self._nas_server_id = nas_server_id

    @property
    def computer_name(self):
        """Gets the computer_name of this SmbServerInstance.  # noqa: E501

        DNS name of the associated computer account when the SMB server is joined to an Active Directory domain. This name's minimum length is 2 characters, it is limited to 63 bytes and must not contain the following characters -   - comma (.)   - tilde (~)   - colon (:)   - exclamation point (!)   - at sign (@)   - number sign (#)   - dollar sign ($)   - percent (%)   - caret (^)   - ampersand (&)   - apostrophe (')   - period (.) - note that if you enter string with period only the first word will be kept   - parentheses (())   - braces ({})   - underscore (_)   - white space (blank) as defined by the Microsoft naming convention (see https://support.microsoft.com/en-us/help/909264/)   # noqa: E501

        :return: The computer_name of this SmbServerInstance.  # noqa: E501
        :rtype: str
        """
        return self._computer_name

    @computer_name.setter
    def computer_name(self, computer_name):
        """Sets the computer_name of this SmbServerInstance.

        DNS name of the associated computer account when the SMB server is joined to an Active Directory domain. This name's minimum length is 2 characters, it is limited to 63 bytes and must not contain the following characters -   - comma (.)   - tilde (~)   - colon (:)   - exclamation point (!)   - at sign (@)   - number sign (#)   - dollar sign ($)   - percent (%)   - caret (^)   - ampersand (&)   - apostrophe (')   - period (.) - note that if you enter string with period only the first word will be kept   - parentheses (())   - braces ({})   - underscore (_)   - white space (blank) as defined by the Microsoft naming convention (see https://support.microsoft.com/en-us/help/909264/)   # noqa: E501

        :param computer_name: The computer_name of this SmbServerInstance.  # noqa: E501
        :type: str
        """

        self._computer_name = computer_name

    @property
    def domain(self):
        """Gets the domain of this SmbServerInstance.  # noqa: E501

        Domain name where SMB server is registered in Active Directory, if applicable.  # noqa: E501

        :return: The domain of this SmbServerInstance.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this SmbServerInstance.

        Domain name where SMB server is registered in Active Directory, if applicable.  # noqa: E501

        :param domain: The domain of this SmbServerInstance.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def netbios_name(self):
        """Gets the netbios_name of this SmbServerInstance.  # noqa: E501

        NetBIOS name is the network name of the standalone SMB server. SMB server joined to Active Directory also have NetBIOS Name, defaulted to the 15 first characters of the computerName attribute. Administrators can specify a custom NetBIOS Name for a SMB server using this attribute. NetBIOS Name are limited to 15 characters and cannot contain the following characters -   - backslash (\\)   - slash mark (/)   - colon (:)   - asterisk (*)   - question mark (?)   - quotation mark (\"\")   - less than sign (<)   - greater than sign (>)   - vertical bar (|) as definied by the Microsoft naming convention (see https://support.microsoft.com/en-us/help/909264/)   # noqa: E501

        :return: The netbios_name of this SmbServerInstance.  # noqa: E501
        :rtype: str
        """
        return self._netbios_name

    @netbios_name.setter
    def netbios_name(self, netbios_name):
        """Sets the netbios_name of this SmbServerInstance.

        NetBIOS name is the network name of the standalone SMB server. SMB server joined to Active Directory also have NetBIOS Name, defaulted to the 15 first characters of the computerName attribute. Administrators can specify a custom NetBIOS Name for a SMB server using this attribute. NetBIOS Name are limited to 15 characters and cannot contain the following characters -   - backslash (\\)   - slash mark (/)   - colon (:)   - asterisk (*)   - question mark (?)   - quotation mark (\"\")   - less than sign (<)   - greater than sign (>)   - vertical bar (|) as definied by the Microsoft naming convention (see https://support.microsoft.com/en-us/help/909264/)   # noqa: E501

        :param netbios_name: The netbios_name of this SmbServerInstance.  # noqa: E501
        :type: str
        """

        self._netbios_name = netbios_name

    @property
    def workgroup(self):
        """Gets the workgroup of this SmbServerInstance.  # noqa: E501

        Applies to stand-alone SMB servers only. Windows network workgroup for the SMB server. Workgroup names are limited to 15 alphanumeric ASCII characters.   # noqa: E501

        :return: The workgroup of this SmbServerInstance.  # noqa: E501
        :rtype: str
        """
        return self._workgroup

    @workgroup.setter
    def workgroup(self, workgroup):
        """Sets the workgroup of this SmbServerInstance.

        Applies to stand-alone SMB servers only. Windows network workgroup for the SMB server. Workgroup names are limited to 15 alphanumeric ASCII characters.   # noqa: E501

        :param workgroup: The workgroup of this SmbServerInstance.  # noqa: E501
        :type: str
        """

        self._workgroup = workgroup

    @property
    def description(self):
        """Gets the description of this SmbServerInstance.  # noqa: E501

        Description of the SMB server.  # noqa: E501

        :return: The description of this SmbServerInstance.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SmbServerInstance.

        Description of the SMB server.  # noqa: E501

        :param description: The description of this SmbServerInstance.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def is_standalone(self):
        """Gets the is_standalone of this SmbServerInstance.  # noqa: E501

        Indicates whether the SMB server is standalone. Values are: - true - SMB server is standalone. - false - SMB server is a domain SMB server to be joined to the Active Directory.   # noqa: E501

        :return: The is_standalone of this SmbServerInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_standalone

    @is_standalone.setter
    def is_standalone(self, is_standalone):
        """Sets the is_standalone of this SmbServerInstance.

        Indicates whether the SMB server is standalone. Values are: - true - SMB server is standalone. - false - SMB server is a domain SMB server to be joined to the Active Directory.   # noqa: E501

        :param is_standalone: The is_standalone of this SmbServerInstance.  # noqa: E501
        :type: bool
        """

        self._is_standalone = is_standalone

    @property
    def is_joined(self):
        """Gets the is_joined of this SmbServerInstance.  # noqa: E501

        Indicates whether the SMB server is joined to the Active Directory. Always false for standalone SMB servers.  # noqa: E501

        :return: The is_joined of this SmbServerInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_joined

    @is_joined.setter
    def is_joined(self, is_joined):
        """Sets the is_joined of this SmbServerInstance.

        Indicates whether the SMB server is joined to the Active Directory. Always false for standalone SMB servers.  # noqa: E501

        :param is_joined: The is_joined of this SmbServerInstance.  # noqa: E501
        :type: bool
        """

        self._is_joined = is_joined

    @property
    def nas_server(self):
        """Gets the nas_server of this SmbServerInstance.  # noqa: E501


        :return: The nas_server of this SmbServerInstance.  # noqa: E501
        :rtype: NasServersInstance
        """
        return self._nas_server

    @nas_server.setter
    def nas_server(self, nas_server):
        """Sets the nas_server of this SmbServerInstance.


        :param nas_server: The nas_server of this SmbServerInstance.  # noqa: E501
        :type: NasServersInstance
        """

        self._nas_server = nas_server

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
        if issubclass(SmbServerInstance, dict):
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
        if not isinstance(other, SmbServerInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
