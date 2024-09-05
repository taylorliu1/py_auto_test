# LdapDomainModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ldap_servers** | **list[str]** | List of IP addresses of the LDAP servers for the domain. IP addesses are in IPv4 or IPv6 format. | [optional] 
**port** | **int** | Port number used to connect to the LDAP Server. Default values are LDAP(389), LDAPs(636), GlobalCatalog LDAP(3268), Global Catalog LDAPs(3269). | [optional] 
**ldap_server_type** | [**LDAPServerTypeEnum**](LDAPServerTypeEnum.md) |  | [optional] 
**protocol** | [**LDAPProtocolEnum**](LDAPProtocolEnum.md) |  | [optional] 
**bind_user** | **str** | Distinguished Name (DN) of the user to be used when binding; that is, authenticating and setting up the connection to the LDAP Server. | [optional] 
**bind_password** | **str** | Password to use when binding a new LDAP session. | [optional] 
**ldap_timeout** | **int** | Timeout for establishing a connection to an LDAP server in milliseconds. If the system does not receive a reply from the LDAP server after the specified timeout, it stops sending requests. Default value is 30000 (30 seconds). | [optional] 
**is_global_catalog** | **bool** | Whether or not the catalog is global. Default value is false. | [optional] 
**user_id_attribute** | **str** | Name of the LDAP attribute whose value indicates the unique identifier of the user. Default value is sAMAccountName. | [optional] 
**user_object_class** | **str** | LDAP object class for users. Default value is user. | [optional] 
**user_search_path** | **str** | Path used to search for users on the directory server. Search path is empty, if global catalog is enabled. | [optional] 
**group_name_attribute** | **str** | Name of the LDAP attribute whose value indicates the group name. Default value is cn. | [optional] 
**group_member_attribute** | **str** | Name of the LDAP attribute whose value contains the names of group members within a group. Default value is member. | [optional] 
**group_object_class** | **str** | LDAP object class for groups. Default value is group. In Active Directory, groups and users are stored in the same directory path, and are in a class called group. Default value is group. | [optional] 
**group_search_path** | **str** | Path used to search for groups on the directory server. Search path is empty, if global catalog is enabled. | [optional] 
**group_search_level** | **int** | Nested search level for performing group search. Default value is 0 (no nested search level limitation) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


