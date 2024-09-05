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


class VsphereHostInstance(object):
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
        'name': 'str',
        'vsphere_object_id': 'str',
        'vcenter_id': 'str',
        'version': 'str',
        'build': 'str',
        'vcenter': 'VcenterInstance',
        'license_assignments': 'list[VsphereHostLicenseAssignmentInstance]',
        'virtual_machines': 'list[VirtualMachineInstance]',
        'datastores': 'list[DatastoreInstance]',
        'hosts': 'list[HostInstance]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'vsphere_object_id': 'vsphere_object_id',
        'vcenter_id': 'vcenter_id',
        'version': 'version',
        'build': 'build',
        'vcenter': 'vcenter',
        'license_assignments': 'license_assignments',
        'virtual_machines': 'virtual_machines',
        'datastores': 'datastores',
        'hosts': 'hosts'
    }

    def __init__(self, id=None, name=None, vsphere_object_id=None, vcenter_id=None, version=None, build=None, vcenter=None, license_assignments=None, virtual_machines=None, datastores=None, hosts=None, _configuration=None):  # noqa: E501
        """VsphereHostInstance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._vsphere_object_id = None
        self._vcenter_id = None
        self._version = None
        self._build = None
        self._vcenter = None
        self._license_assignments = None
        self._virtual_machines = None
        self._datastores = None
        self._hosts = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if vsphere_object_id is not None:
            self.vsphere_object_id = vsphere_object_id
        if vcenter_id is not None:
            self.vcenter_id = vcenter_id
        if version is not None:
            self.version = version
        if build is not None:
            self.build = build
        if vcenter is not None:
            self.vcenter = vcenter
        if license_assignments is not None:
            self.license_assignments = license_assignments
        if virtual_machines is not None:
            self.virtual_machines = virtual_machines
        if datastores is not None:
            self.datastores = datastores
        if hosts is not None:
            self.hosts = hosts

    @property
    def id(self):
        """Gets the id of this VsphereHostInstance.  # noqa: E501

        Unique identifier of the vsphere_host instance.  # noqa: E501

        :return: The id of this VsphereHostInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VsphereHostInstance.

        Unique identifier of the vsphere_host instance.  # noqa: E501

        :param id: The id of this VsphereHostInstance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this VsphereHostInstance.  # noqa: E501

        User-assigned name of the ESXi host in vCenter.  This property supports case-insensitive filtering.  # noqa: E501

        :return: The name of this VsphereHostInstance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VsphereHostInstance.

        User-assigned name of the ESXi host in vCenter.  This property supports case-insensitive filtering.  # noqa: E501

        :param name: The name of this VsphereHostInstance.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def vsphere_object_id(self):
        """Gets the vsphere_object_id of this VsphereHostInstance.  # noqa: E501

        Unique identifier of the vsphere_host in vCenter.  # noqa: E501

        :return: The vsphere_object_id of this VsphereHostInstance.  # noqa: E501
        :rtype: str
        """
        return self._vsphere_object_id

    @vsphere_object_id.setter
    def vsphere_object_id(self, vsphere_object_id):
        """Sets the vsphere_object_id of this VsphereHostInstance.

        Unique identifier of the vsphere_host in vCenter.  # noqa: E501

        :param vsphere_object_id: The vsphere_object_id of this VsphereHostInstance.  # noqa: E501
        :type: str
        """

        self._vsphere_object_id = vsphere_object_id

    @property
    def vcenter_id(self):
        """Gets the vcenter_id of this VsphereHostInstance.  # noqa: E501

        Unique identifier of a vCenter instance.  # noqa: E501

        :return: The vcenter_id of this VsphereHostInstance.  # noqa: E501
        :rtype: str
        """
        return self._vcenter_id

    @vcenter_id.setter
    def vcenter_id(self, vcenter_id):
        """Sets the vcenter_id of this VsphereHostInstance.

        Unique identifier of a vCenter instance.  # noqa: E501

        :param vcenter_id: The vcenter_id of this VsphereHostInstance.  # noqa: E501
        :type: str
        """

        self._vcenter_id = vcenter_id

    @property
    def version(self):
        """Gets the version of this VsphereHostInstance.  # noqa: E501

        ESXi host version.  # noqa: E501

        :return: The version of this VsphereHostInstance.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this VsphereHostInstance.

        ESXi host version.  # noqa: E501

        :param version: The version of this VsphereHostInstance.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def build(self):
        """Gets the build of this VsphereHostInstance.  # noqa: E501

        ESXi host build.  # noqa: E501

        :return: The build of this VsphereHostInstance.  # noqa: E501
        :rtype: str
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this VsphereHostInstance.

        ESXi host build.  # noqa: E501

        :param build: The build of this VsphereHostInstance.  # noqa: E501
        :type: str
        """

        self._build = build

    @property
    def vcenter(self):
        """Gets the vcenter of this VsphereHostInstance.  # noqa: E501

        This is the embeddable reference form of vcenter_id attribute.  # noqa: E501

        :return: The vcenter of this VsphereHostInstance.  # noqa: E501
        :rtype: VcenterInstance
        """
        return self._vcenter

    @vcenter.setter
    def vcenter(self, vcenter):
        """Sets the vcenter of this VsphereHostInstance.

        This is the embeddable reference form of vcenter_id attribute.  # noqa: E501

        :param vcenter: The vcenter of this VsphereHostInstance.  # noqa: E501
        :type: VcenterInstance
        """

        self._vcenter = vcenter

    @property
    def license_assignments(self):
        """Gets the license_assignments of this VsphereHostInstance.  # noqa: E501

        This is the inverse of the resource type vsphere_host_license_assignment association.  # noqa: E501

        :return: The license_assignments of this VsphereHostInstance.  # noqa: E501
        :rtype: list[VsphereHostLicenseAssignmentInstance]
        """
        return self._license_assignments

    @license_assignments.setter
    def license_assignments(self, license_assignments):
        """Sets the license_assignments of this VsphereHostInstance.

        This is the inverse of the resource type vsphere_host_license_assignment association.  # noqa: E501

        :param license_assignments: The license_assignments of this VsphereHostInstance.  # noqa: E501
        :type: list[VsphereHostLicenseAssignmentInstance]
        """

        self._license_assignments = license_assignments

    @property
    def virtual_machines(self):
        """Gets the virtual_machines of this VsphereHostInstance.  # noqa: E501

        List of the virtual_machines that are associated with this vsphere_host.  # noqa: E501

        :return: The virtual_machines of this VsphereHostInstance.  # noqa: E501
        :rtype: list[VirtualMachineInstance]
        """
        return self._virtual_machines

    @virtual_machines.setter
    def virtual_machines(self, virtual_machines):
        """Sets the virtual_machines of this VsphereHostInstance.

        List of the virtual_machines that are associated with this vsphere_host.  # noqa: E501

        :param virtual_machines: The virtual_machines of this VsphereHostInstance.  # noqa: E501
        :type: list[VirtualMachineInstance]
        """

        self._virtual_machines = virtual_machines

    @property
    def datastores(self):
        """Gets the datastores of this VsphereHostInstance.  # noqa: E501

        List of the datastores that are associated with this vsphere_host.  # noqa: E501

        :return: The datastores of this VsphereHostInstance.  # noqa: E501
        :rtype: list[DatastoreInstance]
        """
        return self._datastores

    @datastores.setter
    def datastores(self, datastores):
        """Sets the datastores of this VsphereHostInstance.

        List of the datastores that are associated with this vsphere_host.  # noqa: E501

        :param datastores: The datastores of this VsphereHostInstance.  # noqa: E501
        :type: list[DatastoreInstance]
        """

        self._datastores = datastores

    @property
    def hosts(self):
        """Gets the hosts of this VsphereHostInstance.  # noqa: E501

        List of the hosts that are associated with this vsphere_host.  # noqa: E501

        :return: The hosts of this VsphereHostInstance.  # noqa: E501
        :rtype: list[HostInstance]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this VsphereHostInstance.

        List of the hosts that are associated with this vsphere_host.  # noqa: E501

        :param hosts: The hosts of this VsphereHostInstance.  # noqa: E501
        :type: list[HostInstance]
        """

        self._hosts = hosts

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
        if issubclass(VsphereHostInstance, dict):
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
        if not isinstance(other, VsphereHostInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VsphereHostInstance):
            return True

        return self.to_dict() != other.to_dict()
