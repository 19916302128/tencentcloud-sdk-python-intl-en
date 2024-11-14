# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AddUserContactRequest(AbstractModel):
    """AddUserContact request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Contact name, which needs to be unique and can contain 2-60 characters, supporting uppercase and lowercase letters, numbers, and underline “_”. It cannot start with “_”.
        :type Name: str
        :param _ContactInfo: Email address, which can contain uppercase and lowercase letters, numbers, and underline “_”, and cannot start with “_”.
        :type ContactInfo: str
        :param _Product: Service type, which is fixed to “mysql”.
        :type Product: str
        """
        self._Name = None
        self._ContactInfo = None
        self._Product = None

    @property
    def Name(self):
        """Contact name, which needs to be unique and can contain 2-60 characters, supporting uppercase and lowercase letters, numbers, and underline “_”. It cannot start with “_”.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ContactInfo(self):
        """Email address, which can contain uppercase and lowercase letters, numbers, and underline “_”, and cannot start with “_”.
        :rtype: str
        """
        return self._ContactInfo

    @ContactInfo.setter
    def ContactInfo(self, ContactInfo):
        self._ContactInfo = ContactInfo

    @property
    def Product(self):
        """Service type, which is fixed to “mysql”.
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ContactInfo = params.get("ContactInfo")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUserContactResponse(AbstractModel):
    """AddUserContact response structure.

    """

    def __init__(self):
        r"""
        :param _Id: The successfully added contact ID
        :type Id: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        """The successfully added contact ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class ContactItem(AbstractModel):
    """Contact description.

    """

    def __init__(self):
        r"""
        :param _Id: Contact ID.
        :type Id: int
        :param _Name: Contact name.
        :type Name: str
        :param _Mail: The email address of the contact.
        :type Mail: str
        """
        self._Id = None
        self._Name = None
        self._Mail = None

    @property
    def Id(self):
        """Contact ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """Contact name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Mail(self):
        """The email address of the contact.
        :rtype: str
        """
        return self._Mail

    @Mail.setter
    def Mail(self, Mail):
        self._Mail = Mail


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Mail = params.get("Mail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBDiagReportTaskRequest(AbstractModel):
    """CreateDBDiagReportTask request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _StartTime: Start time, such as `2020-11-08T14:00:00+08:00`.
        :type StartTime: str
        :param _EndTime: End time, such as `2020-11-09T14:00:00+08:00`.
        :type EndTime: str
        :param _SendMailFlag: Whether to send an email. Valid values: 0 - Yes, 1 - No.
        :type SendMailFlag: int
        :param _ContactPerson: An array of contact IDs to receive the email.
        :type ContactPerson: list of int
        :param _ContactGroup: An array of contact group IDs to receive the email.
        :type ContactGroup: list of int
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)). Default value: `mysql`.
        :type Product: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._SendMailFlag = None
        self._ContactPerson = None
        self._ContactGroup = None
        self._Product = None

    @property
    def InstanceId(self):
        """Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        """Start time, such as `2020-11-08T14:00:00+08:00`.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time, such as `2020-11-09T14:00:00+08:00`.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SendMailFlag(self):
        """Whether to send an email. Valid values: 0 - Yes, 1 - No.
        :rtype: int
        """
        return self._SendMailFlag

    @SendMailFlag.setter
    def SendMailFlag(self, SendMailFlag):
        self._SendMailFlag = SendMailFlag

    @property
    def ContactPerson(self):
        """An array of contact IDs to receive the email.
        :rtype: list of int
        """
        return self._ContactPerson

    @ContactPerson.setter
    def ContactPerson(self, ContactPerson):
        self._ContactPerson = ContactPerson

    @property
    def ContactGroup(self):
        """An array of contact group IDs to receive the email.
        :rtype: list of int
        """
        return self._ContactGroup

    @ContactGroup.setter
    def ContactGroup(self, ContactGroup):
        self._ContactGroup = ContactGroup

    @property
    def Product(self):
        """Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)). Default value: `mysql`.
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SendMailFlag = params.get("SendMailFlag")
        self._ContactPerson = params.get("ContactPerson")
        self._ContactGroup = params.get("ContactGroup")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBDiagReportTaskResponse(AbstractModel):
    """CreateDBDiagReportTask response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: ID of an async task request, which can be used to query the execution result of an async task.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type AsyncRequestId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        """ID of an async task request, which can be used to query the execution result of an async task.
Note: this field may return `null`, indicating that no valid value is obtained.
        :rtype: int
        """
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class CreateDBDiagReportUrlRequest(AbstractModel):
    """CreateDBDiagReportUrl request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _AsyncRequestId: The health report task ID, which can be queried through `DescribeDBDiagReportTasks`.
        :type AsyncRequestId: int
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL). Default value: `mysql`.
        :type Product: str
        """
        self._InstanceId = None
        self._AsyncRequestId = None
        self._Product = None

    @property
    def InstanceId(self):
        """Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AsyncRequestId(self):
        """The health report task ID, which can be queried through `DescribeDBDiagReportTasks`.
        :rtype: int
        """
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def Product(self):
        """Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL). Default value: `mysql`.
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBDiagReportUrlResponse(AbstractModel):
    """CreateDBDiagReportUrl response structure.

    """

    def __init__(self):
        r"""
        :param _ReportUrl: The URL of the health report.
        :type ReportUrl: str
        :param _ExpireTime: The expiration timestamp of the health report URL (in seconds).
        :type ExpireTime: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ReportUrl = None
        self._ExpireTime = None
        self._RequestId = None

    @property
    def ReportUrl(self):
        """The URL of the health report.
        :rtype: str
        """
        return self._ReportUrl

    @ReportUrl.setter
    def ReportUrl(self, ReportUrl):
        self._ReportUrl = ReportUrl

    @property
    def ExpireTime(self):
        """The expiration timestamp of the health report URL (in seconds).
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReportUrl = params.get("ReportUrl")
        self._ExpireTime = params.get("ExpireTime")
        self._RequestId = params.get("RequestId")


class CreateMailProfileRequest(AbstractModel):
    """CreateMailProfile request structure.

    """

    def __init__(self):
        r"""
        :param _ProfileInfo: Email configurations
        :type ProfileInfo: :class:`tencentcloud.dbbrain.v20191016.models.ProfileInfo`
        :param _ProfileLevel: Configuration level. Valid values: "User" (user-level), "Instance" (instance-level). For database inspection report, it should be `User`; and for scheduled task reports, it should be `Instance`.
        :type ProfileLevel: str
        :param _ProfileName: Configuration name, which needs to be unique. For database inspection reports, this name can be customize as needed. For scheduled task reports, the name should be in the format of "scheduler_" + {instanceId}, such as "schduler_cdb-test".
        :type ProfileName: str
        :param _ProfileType: Configuration type. Valid values: "dbScan_mail_configuration" (email configuration of database inspection report), "scheduler_mail_configuration" (email configuration of scheduled task report).
        :type ProfileType: str
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)).
        :type Product: str
        :param _BindInstanceIds: Instance ID bound with the configuration, which is set when the configuration level is "Instance". Only one instance can be bound at a time. When the configuration level is “User”, leave this parameter empty.
        :type BindInstanceIds: list of str
        """
        self._ProfileInfo = None
        self._ProfileLevel = None
        self._ProfileName = None
        self._ProfileType = None
        self._Product = None
        self._BindInstanceIds = None

    @property
    def ProfileInfo(self):
        """Email configurations
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.ProfileInfo`
        """
        return self._ProfileInfo

    @ProfileInfo.setter
    def ProfileInfo(self, ProfileInfo):
        self._ProfileInfo = ProfileInfo

    @property
    def ProfileLevel(self):
        """Configuration level. Valid values: "User" (user-level), "Instance" (instance-level). For database inspection report, it should be `User`; and for scheduled task reports, it should be `Instance`.
        :rtype: str
        """
        return self._ProfileLevel

    @ProfileLevel.setter
    def ProfileLevel(self, ProfileLevel):
        self._ProfileLevel = ProfileLevel

    @property
    def ProfileName(self):
        """Configuration name, which needs to be unique. For database inspection reports, this name can be customize as needed. For scheduled task reports, the name should be in the format of "scheduler_" + {instanceId}, such as "schduler_cdb-test".
        :rtype: str
        """
        return self._ProfileName

    @ProfileName.setter
    def ProfileName(self, ProfileName):
        self._ProfileName = ProfileName

    @property
    def ProfileType(self):
        """Configuration type. Valid values: "dbScan_mail_configuration" (email configuration of database inspection report), "scheduler_mail_configuration" (email configuration of scheduled task report).
        :rtype: str
        """
        return self._ProfileType

    @ProfileType.setter
    def ProfileType(self, ProfileType):
        self._ProfileType = ProfileType

    @property
    def Product(self):
        """Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)).
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def BindInstanceIds(self):
        """Instance ID bound with the configuration, which is set when the configuration level is "Instance". Only one instance can be bound at a time. When the configuration level is “User”, leave this parameter empty.
        :rtype: list of str
        """
        return self._BindInstanceIds

    @BindInstanceIds.setter
    def BindInstanceIds(self, BindInstanceIds):
        self._BindInstanceIds = BindInstanceIds


    def _deserialize(self, params):
        if params.get("ProfileInfo") is not None:
            self._ProfileInfo = ProfileInfo()
            self._ProfileInfo._deserialize(params.get("ProfileInfo"))
        self._ProfileLevel = params.get("ProfileLevel")
        self._ProfileName = params.get("ProfileName")
        self._ProfileType = params.get("ProfileType")
        self._Product = params.get("Product")
        self._BindInstanceIds = params.get("BindInstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMailProfileResponse(AbstractModel):
    """CreateMailProfile response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateSchedulerMailProfileRequest(AbstractModel):
    """CreateSchedulerMailProfile request structure.

    """

    def __init__(self):
        r"""
        :param _WeekConfiguration: Value range: 1-7, representing Monday to Sunday respectively.
        :type WeekConfiguration: list of int
        :param _ProfileInfo: Email configurations
        :type ProfileInfo: :class:`tencentcloud.dbbrain.v20191016.models.ProfileInfo`
        :param _ProfileName: Configuration name, which needs to be unique. For scheduled task reports, the name should be in the format of "scheduler_" + {instanceId}, such as "schduler_cdb-test".
        :type ProfileName: str
        :param _BindInstanceId: Configure the instance ID that you need to generate the health report.
        :type BindInstanceId: str
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL). Default value: `mysql`.
        :type Product: str
        """
        self._WeekConfiguration = None
        self._ProfileInfo = None
        self._ProfileName = None
        self._BindInstanceId = None
        self._Product = None

    @property
    def WeekConfiguration(self):
        """Value range: 1-7, representing Monday to Sunday respectively.
        :rtype: list of int
        """
        return self._WeekConfiguration

    @WeekConfiguration.setter
    def WeekConfiguration(self, WeekConfiguration):
        self._WeekConfiguration = WeekConfiguration

    @property
    def ProfileInfo(self):
        """Email configurations
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.ProfileInfo`
        """
        return self._ProfileInfo

    @ProfileInfo.setter
    def ProfileInfo(self, ProfileInfo):
        self._ProfileInfo = ProfileInfo

    @property
    def ProfileName(self):
        """Configuration name, which needs to be unique. For scheduled task reports, the name should be in the format of "scheduler_" + {instanceId}, such as "schduler_cdb-test".
        :rtype: str
        """
        return self._ProfileName

    @ProfileName.setter
    def ProfileName(self, ProfileName):
        self._ProfileName = ProfileName

    @property
    def BindInstanceId(self):
        """Configure the instance ID that you need to generate the health report.
        :rtype: str
        """
        return self._BindInstanceId

    @BindInstanceId.setter
    def BindInstanceId(self, BindInstanceId):
        self._BindInstanceId = BindInstanceId

    @property
    def Product(self):
        """Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL). Default value: `mysql`.
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._WeekConfiguration = params.get("WeekConfiguration")
        if params.get("ProfileInfo") is not None:
            self._ProfileInfo = ProfileInfo()
            self._ProfileInfo._deserialize(params.get("ProfileInfo"))
        self._ProfileName = params.get("ProfileName")
        self._BindInstanceId = params.get("BindInstanceId")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSchedulerMailProfileResponse(AbstractModel):
    """CreateSchedulerMailProfile response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAllUserContactRequest(AbstractModel):
    """DescribeAllUserContact request structure.

    """

    def __init__(self):
        r"""
        :param _Product: Service type, which is fixed to “mysql”.
        :type Product: str
        :param _Names: An array of contact name. Fuzzy search is supported.
        :type Names: list of str
        """
        self._Product = None
        self._Names = None

    @property
    def Product(self):
        """Service type, which is fixed to “mysql”.
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Names(self):
        """An array of contact name. Fuzzy search is supported.
        :rtype: list of str
        """
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllUserContactResponse(AbstractModel):
    """DescribeAllUserContact response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of contacts.
        :type TotalCount: int
        :param _Contacts: Contact information.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Contacts: list of ContactItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Contacts = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of contacts.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Contacts(self):
        """Contact information.
Note: this field may return `null`, indicating that no valid value is obtained.
        :rtype: list of ContactItem
        """
        return self._Contacts

    @Contacts.setter
    def Contacts(self, Contacts):
        self._Contacts = Contacts

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Contacts") is not None:
            self._Contacts = []
            for item in params.get("Contacts"):
                obj = ContactItem()
                obj._deserialize(item)
                self._Contacts.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAllUserGroupRequest(AbstractModel):
    """DescribeAllUserGroup request structure.

    """

    def __init__(self):
        r"""
        :param _Product: Service type, which is fixed to “mysql”.
        :type Product: str
        :param _Names: An array of contact group name. Fuzzy search is supported.
        :type Names: list of str
        """
        self._Product = None
        self._Names = None

    @property
    def Product(self):
        """Service type, which is fixed to “mysql”.
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Names(self):
        """An array of contact group name. Fuzzy search is supported.
        :rtype: list of str
        """
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllUserGroupResponse(AbstractModel):
    """DescribeAllUserGroup response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of contact groups.
        :type TotalCount: int
        :param _Groups: Contact group information.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Groups: list of GroupItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Groups = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of contact groups.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Groups(self):
        """Contact group information.
Note: this field may return `null`, indicating that no valid value is obtained.
        :rtype: list of GroupItem
        """
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = GroupItem()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBDiagEventRequest(AbstractModel):
    """DescribeDBDiagEvent request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _EventId: Event ID, which can be obtained through the `DescribeDBDiagHistory` API.
        :type EventId: int
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)). Default value: `mysql`.
        :type Product: str
        """
        self._InstanceId = None
        self._EventId = None
        self._Product = None

    @property
    def InstanceId(self):
        """Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EventId(self):
        """Event ID, which can be obtained through the `DescribeDBDiagHistory` API.
        :rtype: int
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def Product(self):
        """Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)). Default value: `mysql`.
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._EventId = params.get("EventId")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBDiagEventResponse(AbstractModel):
    """DescribeDBDiagEvent response structure.

    """

    def __init__(self):
        r"""
        :param _DiagItem: Diagnosis item.
        :type DiagItem: str
        :param _DiagType: Diagnosis type.
        :type DiagType: str
        :param _EventId: Event ID.
        :type EventId: int
        :param _Explanation: Event details.
        :type Explanation: str
        :param _Outline: Summary.
        :type Outline: str
        :param _Problem: Problem found.
        :type Problem: str
        :param _Severity: Severity, which can be divided into 5 levels: 1: fatal, 2: severe, 3: warning, 4: notice, 5: healthy.
        :type Severity: int
        :param _StartTime: Start time
        :type StartTime: str
        :param _Suggestions: Suggestion.
        :type Suggestions: str
        :param _Metric: Reserved field.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Metric: str
        :param _EndTime: End time.
        :type EndTime: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DiagItem = None
        self._DiagType = None
        self._EventId = None
        self._Explanation = None
        self._Outline = None
        self._Problem = None
        self._Severity = None
        self._StartTime = None
        self._Suggestions = None
        self._Metric = None
        self._EndTime = None
        self._RequestId = None

    @property
    def DiagItem(self):
        """Diagnosis item.
        :rtype: str
        """
        return self._DiagItem

    @DiagItem.setter
    def DiagItem(self, DiagItem):
        self._DiagItem = DiagItem

    @property
    def DiagType(self):
        """Diagnosis type.
        :rtype: str
        """
        return self._DiagType

    @DiagType.setter
    def DiagType(self, DiagType):
        self._DiagType = DiagType

    @property
    def EventId(self):
        """Event ID.
        :rtype: int
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def Explanation(self):
        """Event details.
        :rtype: str
        """
        return self._Explanation

    @Explanation.setter
    def Explanation(self, Explanation):
        self._Explanation = Explanation

    @property
    def Outline(self):
        """Summary.
        :rtype: str
        """
        return self._Outline

    @Outline.setter
    def Outline(self, Outline):
        self._Outline = Outline

    @property
    def Problem(self):
        """Problem found.
        :rtype: str
        """
        return self._Problem

    @Problem.setter
    def Problem(self, Problem):
        self._Problem = Problem

    @property
    def Severity(self):
        """Severity, which can be divided into 5 levels: 1: fatal, 2: severe, 3: warning, 4: notice, 5: healthy.
        :rtype: int
        """
        return self._Severity

    @Severity.setter
    def Severity(self, Severity):
        self._Severity = Severity

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Suggestions(self):
        """Suggestion.
        :rtype: str
        """
        return self._Suggestions

    @Suggestions.setter
    def Suggestions(self, Suggestions):
        self._Suggestions = Suggestions

    @property
    def Metric(self):
        """Reserved field.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def EndTime(self):
        """End time.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DiagItem = params.get("DiagItem")
        self._DiagType = params.get("DiagType")
        self._EventId = params.get("EventId")
        self._Explanation = params.get("Explanation")
        self._Outline = params.get("Outline")
        self._Problem = params.get("Problem")
        self._Severity = params.get("Severity")
        self._StartTime = params.get("StartTime")
        self._Suggestions = params.get("Suggestions")
        self._Metric = params.get("Metric")
        self._EndTime = params.get("EndTime")
        self._RequestId = params.get("RequestId")


class DescribeDBDiagHistoryRequest(AbstractModel):
    """DescribeDBDiagHistory request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _StartTime: Start time, such as "2019-09-10 12:13:14".
        :type StartTime: str
        :param _EndTime: End time, such as "2019-09-11 12:13:14". The interval between the end time and the start time can be up to 2 days.
        :type EndTime: str
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)). Default value: `mysql`.
        :type Product: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Product = None

    @property
    def InstanceId(self):
        """Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        """Start time, such as "2019-09-10 12:13:14".
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time, such as "2019-09-11 12:13:14". The interval between the end time and the start time can be up to 2 days.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Product(self):
        """Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)). Default value: `mysql`.
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBDiagHistoryResponse(AbstractModel):
    """DescribeDBDiagHistory response structure.

    """

    def __init__(self):
        r"""
        :param _Events: Event description.
        :type Events: list of DiagHistoryEventItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Events = None
        self._RequestId = None

    @property
    def Events(self):
        """Event description.
        :rtype: list of DiagHistoryEventItem
        """
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Events") is not None:
            self._Events = []
            for item in params.get("Events"):
                obj = DiagHistoryEventItem()
                obj._deserialize(item)
                self._Events.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBDiagReportTasksRequest(AbstractModel):
    """DescribeDBDiagReportTasks request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time of the first task in the format of yyyy-MM-dd HH:mm:ss, such as 2019-09-10 12:13:14. It is used for queries by time range.
        :type StartTime: str
        :param _EndTime: End time of the last task in the format of yyyy-MM-dd HH:mm:ss, such as 2019-09-10 12:13:14. It is used for queries by time range.
        :type EndTime: str
        :param _InstanceIds: Instance ID array, which is used to filter the task list of a specified instance.
        :type InstanceIds: list of str
        :param _Sources: Source that triggers the task. Valid values: `DAILY_INSPECTION` (instance inspection), `SCHEDULED` (timed generation), and `MANUAL` (manual trigger).
        :type Sources: list of str
        :param _HealthLevels: Health level. Valid values: `HEALTH` (healthy), `SUB_HEALTH` (suboptimal), `RISK` (risky), and `HIGH_RISK` (critical).
        :type HealthLevels: str
        :param _TaskStatuses: The task status. Valid values: `created` (create), `chosen` (to be executed), `running` (being executed), `failed` (failed), and `finished` (completed).
        :type TaskStatuses: str
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20.
        :type Limit: int
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL). Default value: `mysql`.
        :type Product: str
        """
        self._StartTime = None
        self._EndTime = None
        self._InstanceIds = None
        self._Sources = None
        self._HealthLevels = None
        self._TaskStatuses = None
        self._Offset = None
        self._Limit = None
        self._Product = None

    @property
    def StartTime(self):
        """Start time of the first task in the format of yyyy-MM-dd HH:mm:ss, such as 2019-09-10 12:13:14. It is used for queries by time range.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time of the last task in the format of yyyy-MM-dd HH:mm:ss, such as 2019-09-10 12:13:14. It is used for queries by time range.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def InstanceIds(self):
        """Instance ID array, which is used to filter the task list of a specified instance.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Sources(self):
        """Source that triggers the task. Valid values: `DAILY_INSPECTION` (instance inspection), `SCHEDULED` (timed generation), and `MANUAL` (manual trigger).
        :rtype: list of str
        """
        return self._Sources

    @Sources.setter
    def Sources(self, Sources):
        self._Sources = Sources

    @property
    def HealthLevels(self):
        """Health level. Valid values: `HEALTH` (healthy), `SUB_HEALTH` (suboptimal), `RISK` (risky), and `HIGH_RISK` (critical).
        :rtype: str
        """
        return self._HealthLevels

    @HealthLevels.setter
    def HealthLevels(self, HealthLevels):
        self._HealthLevels = HealthLevels

    @property
    def TaskStatuses(self):
        """The task status. Valid values: `created` (create), `chosen` (to be executed), `running` (being executed), `failed` (failed), and `finished` (completed).
        :rtype: str
        """
        return self._TaskStatuses

    @TaskStatuses.setter
    def TaskStatuses(self, TaskStatuses):
        self._TaskStatuses = TaskStatuses

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of returned results. Default value: 20.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Product(self):
        """Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL). Default value: `mysql`.
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._InstanceIds = params.get("InstanceIds")
        self._Sources = params.get("Sources")
        self._HealthLevels = params.get("HealthLevels")
        self._TaskStatuses = params.get("TaskStatuses")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBDiagReportTasksResponse(AbstractModel):
    """DescribeDBDiagReportTasks response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of tasks.
        :type TotalCount: int
        :param _Tasks: Task list.
        :type Tasks: list of HealthReportTask
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tasks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of tasks.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tasks(self):
        """Task list.
        :rtype: list of HealthReportTask
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = HealthReportTask()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBSpaceStatusRequest(AbstractModel):
    """DescribeDBSpaceStatus request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _RangeDays: Query period in days. The end date is the current date and the query period is 7 days by default.
        :type RangeDays: int
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)). Default value: `mysql`.
        :type Product: str
        """
        self._InstanceId = None
        self._RangeDays = None
        self._Product = None

    @property
    def InstanceId(self):
        """Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RangeDays(self):
        """Query period in days. The end date is the current date and the query period is 7 days by default.
        :rtype: int
        """
        return self._RangeDays

    @RangeDays.setter
    def RangeDays(self, RangeDays):
        self._RangeDays = RangeDays

    @property
    def Product(self):
        """Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)). Default value: `mysql`.
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RangeDays = params.get("RangeDays")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSpaceStatusResponse(AbstractModel):
    """DescribeDBSpaceStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Growth: Disk usage growth in MB.
        :type Growth: int
        :param _Remain: Available disk space in MB.
        :type Remain: int
        :param _Total: Total disk space in MB.
        :type Total: int
        :param _AvailableDays: Estimated number of available days.
        :type AvailableDays: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Growth = None
        self._Remain = None
        self._Total = None
        self._AvailableDays = None
        self._RequestId = None

    @property
    def Growth(self):
        """Disk usage growth in MB.
        :rtype: int
        """
        return self._Growth

    @Growth.setter
    def Growth(self, Growth):
        self._Growth = Growth

    @property
    def Remain(self):
        """Available disk space in MB.
        :rtype: int
        """
        return self._Remain

    @Remain.setter
    def Remain(self, Remain):
        self._Remain = Remain

    @property
    def Total(self):
        """Total disk space in MB.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def AvailableDays(self):
        """Estimated number of available days.
        :rtype: int
        """
        return self._AvailableDays

    @AvailableDays.setter
    def AvailableDays(self, AvailableDays):
        self._AvailableDays = AvailableDays

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Growth = params.get("Growth")
        self._Remain = params.get("Remain")
        self._Total = params.get("Total")
        self._AvailableDays = params.get("AvailableDays")
        self._RequestId = params.get("RequestId")


class DescribeDiagDBInstancesRequest(AbstractModel):
    """DescribeDiagDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _IsSupported: Whether it is an instance supported by DBbrain. It is fixed to “true”.
        :type IsSupported: bool
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL). Default value: `mysql`.
        :type Product: str
        :param _Offset: Pagination parameter indicating the offset.
        :type Offset: int
        :param _Limit: Pagination parameter indicating the number of entries for each page.
        :type Limit: int
        :param _InstanceNames: Query by instance name.
        :type InstanceNames: list of str
        :param _InstanceIds: Query by instance ID.
        :type InstanceIds: list of str
        :param _Regions: Query by region.
        :type Regions: list of str
        """
        self._IsSupported = None
        self._Product = None
        self._Offset = None
        self._Limit = None
        self._InstanceNames = None
        self._InstanceIds = None
        self._Regions = None

    @property
    def IsSupported(self):
        """Whether it is an instance supported by DBbrain. It is fixed to “true”.
        :rtype: bool
        """
        return self._IsSupported

    @IsSupported.setter
    def IsSupported(self, IsSupported):
        self._IsSupported = IsSupported

    @property
    def Product(self):
        """Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL). Default value: `mysql`.
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Offset(self):
        """Pagination parameter indicating the offset.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Pagination parameter indicating the number of entries for each page.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def InstanceNames(self):
        """Query by instance name.
        :rtype: list of str
        """
        return self._InstanceNames

    @InstanceNames.setter
    def InstanceNames(self, InstanceNames):
        self._InstanceNames = InstanceNames

    @property
    def InstanceIds(self):
        """Query by instance ID.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Regions(self):
        """Query by region.
        :rtype: list of str
        """
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions


    def _deserialize(self, params):
        self._IsSupported = params.get("IsSupported")
        self._Product = params.get("Product")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstanceNames = params.get("InstanceNames")
        self._InstanceIds = params.get("InstanceIds")
        self._Regions = params.get("Regions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiagDBInstancesResponse(AbstractModel):
    """DescribeDiagDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total Number of Instances
        :type TotalCount: int
        :param _DbScanStatus: Status of all instance inspection. 0: all instance inspection enabled, 1: all instance inspection disabled
        :type DbScanStatus: int
        :param _Items: Instance related information
        :type Items: list of InstanceInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._DbScanStatus = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total Number of Instances
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DbScanStatus(self):
        """Status of all instance inspection. 0: all instance inspection enabled, 1: all instance inspection disabled
        :rtype: int
        """
        return self._DbScanStatus

    @DbScanStatus.setter
    def DbScanStatus(self, DbScanStatus):
        self._DbScanStatus = DbScanStatus

    @property
    def Items(self):
        """Instance related information
        :rtype: list of InstanceInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._DbScanStatus = params.get("DbScanStatus")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHealthScoreRequest(AbstractModel):
    """DescribeHealthScore request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The instance ID that needs to obtain the health score
        :type InstanceId: str
        :param _Time: Time to obtain the health score
        :type Time: str
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL (compatible with MySQL)). Default value: `mysql`.
        :type Product: str
        """
        self._InstanceId = None
        self._Time = None
        self._Product = None

    @property
    def InstanceId(self):
        """The instance ID that needs to obtain the health score
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Time(self):
        """Time to obtain the health score
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Product(self):
        """Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL (compatible with MySQL)). Default value: `mysql`.
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Time = params.get("Time")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHealthScoreResponse(AbstractModel):
    """DescribeHealthScore response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Health score and deduction for exceptions
        :type Data: :class:`tencentcloud.dbbrain.v20191016.models.HealthScoreInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """Health score and deduction for exceptions
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.HealthScoreInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = HealthScoreInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeMailProfileRequest(AbstractModel):
    """DescribeMailProfile request structure.

    """

    def __init__(self):
        r"""
        :param _ProfileType: Configuration type. Valid values: "dbScan_mail_configuration" (email configuration of database inspection report), "scheduler_mail_configuration" (email configuration of scheduled task report).
        :type ProfileType: str
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL). Default value: `mysql`.
        :type Product: str
        :param _Offset: Pagination offset
        :type Offset: int
        :param _Limit: The number of results per page in paginated queries. Maximum value: 50
        :type Limit: int
        :param _ProfileName: Query by the name of email configuration. The name of the regularly sent email configuration should be in the format of "scheduler_"+{instanceId}.
        :type ProfileName: str
        """
        self._ProfileType = None
        self._Product = None
        self._Offset = None
        self._Limit = None
        self._ProfileName = None

    @property
    def ProfileType(self):
        """Configuration type. Valid values: "dbScan_mail_configuration" (email configuration of database inspection report), "scheduler_mail_configuration" (email configuration of scheduled task report).
        :rtype: str
        """
        return self._ProfileType

    @ProfileType.setter
    def ProfileType(self, ProfileType):
        self._ProfileType = ProfileType

    @property
    def Product(self):
        """Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL). Default value: `mysql`.
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Offset(self):
        """Pagination offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """The number of results per page in paginated queries. Maximum value: 50
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ProfileName(self):
        """Query by the name of email configuration. The name of the regularly sent email configuration should be in the format of "scheduler_"+{instanceId}.
        :rtype: str
        """
        return self._ProfileName

    @ProfileName.setter
    def ProfileName(self, ProfileName):
        self._ProfileName = ProfileName


    def _deserialize(self, params):
        self._ProfileType = params.get("ProfileType")
        self._Product = params.get("Product")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ProfileName = params.get("ProfileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMailProfileResponse(AbstractModel):
    """DescribeMailProfile response structure.

    """

    def __init__(self):
        r"""
        :param _ProfileList: Email configuration details
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ProfileList: list of UserProfile
        :param _TotalCount: Total number of email templates
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProfileList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ProfileList(self):
        """Email configuration details
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: list of UserProfile
        """
        return self._ProfileList

    @ProfileList.setter
    def ProfileList(self, ProfileList):
        self._ProfileList = ProfileList

    @property
    def TotalCount(self):
        """Total number of email templates
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ProfileList") is not None:
            self._ProfileList = []
            for item in params.get("ProfileList"):
                obj = UserProfile()
                obj._deserialize(item)
                self._ProfileList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSlowLogTimeSeriesStatsRequest(AbstractModel):
    """DescribeSlowLogTimeSeriesStats request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _StartTime: Start time, such as "2019-09-10 12:13:14".
        :type StartTime: str
        :param _EndTime: End time, such as "2019-09-10 12:13:14". The interval between the end time and the start time can be up to 7 days.
        :type EndTime: str
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)). Default value: `mysql`.
        :type Product: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Product = None

    @property
    def InstanceId(self):
        """Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        """Start time, such as "2019-09-10 12:13:14".
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time, such as "2019-09-10 12:13:14". The interval between the end time and the start time can be up to 7 days.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Product(self):
        """Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)). Default value: `mysql`.
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogTimeSeriesStatsResponse(AbstractModel):
    """DescribeSlowLogTimeSeriesStats response structure.

    """

    def __init__(self):
        r"""
        :param _Period: Time range in seconds in histogram.
        :type Period: int
        :param _TimeSeries: Number of slow logs in specified time range.
        :type TimeSeries: list of TimeSlice
        :param _SeriesData: Instance CPU utilization monitoring data in specified time range.
        :type SeriesData: :class:`tencentcloud.dbbrain.v20191016.models.MonitorMetricSeriesData`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Period = None
        self._TimeSeries = None
        self._SeriesData = None
        self._RequestId = None

    @property
    def Period(self):
        """Time range in seconds in histogram.
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def TimeSeries(self):
        """Number of slow logs in specified time range.
        :rtype: list of TimeSlice
        """
        return self._TimeSeries

    @TimeSeries.setter
    def TimeSeries(self, TimeSeries):
        self._TimeSeries = TimeSeries

    @property
    def SeriesData(self):
        """Instance CPU utilization monitoring data in specified time range.
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.MonitorMetricSeriesData`
        """
        return self._SeriesData

    @SeriesData.setter
    def SeriesData(self, SeriesData):
        self._SeriesData = SeriesData

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Period = params.get("Period")
        if params.get("TimeSeries") is not None:
            self._TimeSeries = []
            for item in params.get("TimeSeries"):
                obj = TimeSlice()
                obj._deserialize(item)
                self._TimeSeries.append(obj)
        if params.get("SeriesData") is not None:
            self._SeriesData = MonitorMetricSeriesData()
            self._SeriesData._deserialize(params.get("SeriesData"))
        self._RequestId = params.get("RequestId")


class DescribeSlowLogTopSqlsRequest(AbstractModel):
    """DescribeSlowLogTopSqls request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _StartTime: Start time, such as "2019-09-10 12:13:14".
        :type StartTime: str
        :param _EndTime: End time, such as "2019-09-10 12:13:14". The interval between the end time and the start time can be up to 7 days.
        :type EndTime: str
        :param _SortBy: Sorting key. Valid values: QueryTime, ExecTimes, RowsSent, LockTime, RowsExamined.
        :type SortBy: str
        :param _OrderBy: Sorting order. Valid values: ASC (ascending), DESC (descending).
        :type OrderBy: str
        :param _Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _SchemaList: Database name array.
        :type SchemaList: list of SchemaItem
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)). Default value: `mysql`.
        :type Product: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._SortBy = None
        self._OrderBy = None
        self._Limit = None
        self._Offset = None
        self._SchemaList = None
        self._Product = None

    @property
    def InstanceId(self):
        """Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        """Start time, such as "2019-09-10 12:13:14".
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time, such as "2019-09-10 12:13:14". The interval between the end time and the start time can be up to 7 days.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SortBy(self):
        """Sorting key. Valid values: QueryTime, ExecTimes, RowsSent, LockTime, RowsExamined.
        :rtype: str
        """
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def OrderBy(self):
        """Sorting order. Valid values: ASC (ascending), DESC (descending).
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Limit(self):
        """Number of results to be returned. Default value: 20. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def SchemaList(self):
        """Database name array.
        :rtype: list of SchemaItem
        """
        return self._SchemaList

    @SchemaList.setter
    def SchemaList(self, SchemaList):
        self._SchemaList = SchemaList

    @property
    def Product(self):
        """Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)). Default value: `mysql`.
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SortBy = params.get("SortBy")
        self._OrderBy = params.get("OrderBy")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("SchemaList") is not None:
            self._SchemaList = []
            for item in params.get("SchemaList"):
                obj = SchemaItem()
                obj._deserialize(item)
                self._SchemaList.append(obj)
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogTopSqlsResponse(AbstractModel):
    """DescribeSlowLogTopSqls response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible entries.
        :type TotalCount: int
        :param _Rows: List of top slow SQL statements
        :type Rows: list of SlowLogTopSqlItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Rows = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of eligible entries.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Rows(self):
        """List of top slow SQL statements
        :rtype: list of SlowLogTopSqlItem
        """
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = SlowLogTopSqlItem()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSlowLogUserHostStatsRequest(AbstractModel):
    """DescribeSlowLogUserHostStats request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _StartTime: Start time of the time range in the format of yyyy-MM-dd HH:mm:ss, such as 2019-09-10 12:13:14.
        :type StartTime: str
        :param _EndTime: End time of the time range in the format of yyyy-MM-dd HH:mm:ss, such as 2019-09-10 12:13:14.
        :type EndTime: str
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL). Default value: `mysql`.
        :type Product: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Product = None

    @property
    def InstanceId(self):
        """Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        """Start time of the time range in the format of yyyy-MM-dd HH:mm:ss, such as 2019-09-10 12:13:14.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time of the time range in the format of yyyy-MM-dd HH:mm:ss, such as 2019-09-10 12:13:14.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Product(self):
        """Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL). Default value: `mysql`.
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogUserHostStatsResponse(AbstractModel):
    """DescribeSlowLogUserHostStats response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of source addresses.
        :type TotalCount: int
        :param _Items: Detailed list of the proportion of slow logs from each source address.
        :type Items: list of SlowLogHost
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of source addresses.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """Detailed list of the proportion of slow logs from each source address.
        :rtype: list of SlowLogHost
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = SlowLogHost()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTopSpaceSchemaTimeSeriesRequest(AbstractModel):
    """DescribeTopSpaceSchemaTimeSeries request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _Limit: Number of returned top databases. Maximum value: 100. Default value: 20.
        :type Limit: int
        :param _SortBy: Field used to sort top tables. Valid values: `DataLength`, `IndexLength`, `TotalLength`, `DataFree`, `FragRatio`, `TableRows`, and `PhysicalFileSize` (supported only by TencentDB for MySQL instances). For TencentDB for MySQL instances, the default value is `PhysicalFileSize`; for other database instances, the default value is `TotalLength`.
        :type SortBy: str
        :param _StartDate: Start date. It can be as early as 29 days before the current date, and defaults to 6 days before the end date.
        :type StartDate: str
        :param _EndDate: End date. It can be as early as 29 days before the current date, and defaults to the current date.
        :type EndDate: str
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)). Default value: `mysql`.
        :type Product: str
        """
        self._InstanceId = None
        self._Limit = None
        self._SortBy = None
        self._StartDate = None
        self._EndDate = None
        self._Product = None

    @property
    def InstanceId(self):
        """Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        """Number of returned top databases. Maximum value: 100. Default value: 20.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SortBy(self):
        """Field used to sort top tables. Valid values: `DataLength`, `IndexLength`, `TotalLength`, `DataFree`, `FragRatio`, `TableRows`, and `PhysicalFileSize` (supported only by TencentDB for MySQL instances). For TencentDB for MySQL instances, the default value is `PhysicalFileSize`; for other database instances, the default value is `TotalLength`.
        :rtype: str
        """
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def StartDate(self):
        """Start date. It can be as early as 29 days before the current date, and defaults to 6 days before the end date.
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """End date. It can be as early as 29 days before the current date, and defaults to the current date.
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Product(self):
        """Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)). Default value: `mysql`.
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._SortBy = params.get("SortBy")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopSpaceSchemaTimeSeriesResponse(AbstractModel):
    """DescribeTopSpaceSchemaTimeSeries response structure.

    """

    def __init__(self):
        r"""
        :param _TopSpaceSchemaTimeSeries: Time series list of the returned space statistics of top databases.
        :type TopSpaceSchemaTimeSeries: list of SchemaSpaceTimeSeries
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TopSpaceSchemaTimeSeries = None
        self._RequestId = None

    @property
    def TopSpaceSchemaTimeSeries(self):
        """Time series list of the returned space statistics of top databases.
        :rtype: list of SchemaSpaceTimeSeries
        """
        return self._TopSpaceSchemaTimeSeries

    @TopSpaceSchemaTimeSeries.setter
    def TopSpaceSchemaTimeSeries(self, TopSpaceSchemaTimeSeries):
        self._TopSpaceSchemaTimeSeries = TopSpaceSchemaTimeSeries

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TopSpaceSchemaTimeSeries") is not None:
            self._TopSpaceSchemaTimeSeries = []
            for item in params.get("TopSpaceSchemaTimeSeries"):
                obj = SchemaSpaceTimeSeries()
                obj._deserialize(item)
                self._TopSpaceSchemaTimeSeries.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTopSpaceSchemasRequest(AbstractModel):
    """DescribeTopSpaceSchemas request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _Limit: Number of returned top databases. Maximum value: 100. Default value: 20.
        :type Limit: int
        :param _SortBy: Field used to sort top tables. Valid values: `DataLength`, `IndexLength`, `TotalLength`, `DataFree`, `FragRatio`, `TableRows`, and `PhysicalFileSize` (supported only by TencentDB for MySQL instances). For TencentDB for MySQL instances, the default value is `PhysicalFileSize`; for other database instances, the default value is `TotalLength`.
        :type SortBy: str
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)). Default value: `mysql`.
        :type Product: str
        """
        self._InstanceId = None
        self._Limit = None
        self._SortBy = None
        self._Product = None

    @property
    def InstanceId(self):
        """Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        """Number of returned top databases. Maximum value: 100. Default value: 20.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SortBy(self):
        """Field used to sort top tables. Valid values: `DataLength`, `IndexLength`, `TotalLength`, `DataFree`, `FragRatio`, `TableRows`, and `PhysicalFileSize` (supported only by TencentDB for MySQL instances). For TencentDB for MySQL instances, the default value is `PhysicalFileSize`; for other database instances, the default value is `TotalLength`.
        :rtype: str
        """
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def Product(self):
        """Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)). Default value: `mysql`.
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._SortBy = params.get("SortBy")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopSpaceSchemasResponse(AbstractModel):
    """DescribeTopSpaceSchemas response structure.

    """

    def __init__(self):
        r"""
        :param _TopSpaceSchemas: List of the returned space statistics of top databases.
        :type TopSpaceSchemas: list of SchemaSpaceData
        :param _Timestamp: Timestamp (in seconds) of database space data collect points
        :type Timestamp: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TopSpaceSchemas = None
        self._Timestamp = None
        self._RequestId = None

    @property
    def TopSpaceSchemas(self):
        """List of the returned space statistics of top databases.
        :rtype: list of SchemaSpaceData
        """
        return self._TopSpaceSchemas

    @TopSpaceSchemas.setter
    def TopSpaceSchemas(self, TopSpaceSchemas):
        self._TopSpaceSchemas = TopSpaceSchemas

    @property
    def Timestamp(self):
        """Timestamp (in seconds) of database space data collect points
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TopSpaceSchemas") is not None:
            self._TopSpaceSchemas = []
            for item in params.get("TopSpaceSchemas"):
                obj = SchemaSpaceData()
                obj._deserialize(item)
                self._TopSpaceSchemas.append(obj)
        self._Timestamp = params.get("Timestamp")
        self._RequestId = params.get("RequestId")


class DescribeTopSpaceTableTimeSeriesRequest(AbstractModel):
    """DescribeTopSpaceTableTimeSeries request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _Limit: Number of returned top tables. Maximum value: 100. Default value: 20.
        :type Limit: int
        :param _SortBy: Field used to sort top tables. Valid values: DataLength, IndexLength, TotalLength, DataFree, FragRatio, TableRows, PhysicalFileSize. Default value: PhysicalFileSize.
        :type SortBy: str
        :param _StartDate: Start date. It can be as early as 29 days before the current date, and defaults to 6 days before the end date.
        :type StartDate: str
        :param _EndDate: End date. It can be as early as 29 days before the current date, and defaults to the current date.
        :type EndDate: str
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)). Default value: `mysql`.
        :type Product: str
        """
        self._InstanceId = None
        self._Limit = None
        self._SortBy = None
        self._StartDate = None
        self._EndDate = None
        self._Product = None

    @property
    def InstanceId(self):
        """Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        """Number of returned top tables. Maximum value: 100. Default value: 20.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SortBy(self):
        """Field used to sort top tables. Valid values: DataLength, IndexLength, TotalLength, DataFree, FragRatio, TableRows, PhysicalFileSize. Default value: PhysicalFileSize.
        :rtype: str
        """
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def StartDate(self):
        """Start date. It can be as early as 29 days before the current date, and defaults to 6 days before the end date.
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """End date. It can be as early as 29 days before the current date, and defaults to the current date.
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Product(self):
        """Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)). Default value: `mysql`.
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._SortBy = params.get("SortBy")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopSpaceTableTimeSeriesResponse(AbstractModel):
    """DescribeTopSpaceTableTimeSeries response structure.

    """

    def __init__(self):
        r"""
        :param _TopSpaceTableTimeSeries: Time series list of the returned space statistics of top tables.
        :type TopSpaceTableTimeSeries: list of TableSpaceTimeSeries
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TopSpaceTableTimeSeries = None
        self._RequestId = None

    @property
    def TopSpaceTableTimeSeries(self):
        """Time series list of the returned space statistics of top tables.
        :rtype: list of TableSpaceTimeSeries
        """
        return self._TopSpaceTableTimeSeries

    @TopSpaceTableTimeSeries.setter
    def TopSpaceTableTimeSeries(self, TopSpaceTableTimeSeries):
        self._TopSpaceTableTimeSeries = TopSpaceTableTimeSeries

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TopSpaceTableTimeSeries") is not None:
            self._TopSpaceTableTimeSeries = []
            for item in params.get("TopSpaceTableTimeSeries"):
                obj = TableSpaceTimeSeries()
                obj._deserialize(item)
                self._TopSpaceTableTimeSeries.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTopSpaceTablesRequest(AbstractModel):
    """DescribeTopSpaceTables request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _Limit: Number of returned top tables. Maximum value: 100. Default value: 20.
        :type Limit: int
        :param _SortBy: Field used to sort top tables. Valid values: `DataLength`, `IndexLength`, `TotalLength`, `DataFree`, `FragRatio`, `TableRows`, and `PhysicalFileSize` (only supported by TencentDB for MySQL instances). For TencentDB for MySQL instances, the default value is PhysicalFileSize; for other database instances, the default value is `TotalLength`.
        :type SortBy: str
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)). Default value: `mysql`.
        :type Product: str
        """
        self._InstanceId = None
        self._Limit = None
        self._SortBy = None
        self._Product = None

    @property
    def InstanceId(self):
        """Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        """Number of returned top tables. Maximum value: 100. Default value: 20.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SortBy(self):
        """Field used to sort top tables. Valid values: `DataLength`, `IndexLength`, `TotalLength`, `DataFree`, `FragRatio`, `TableRows`, and `PhysicalFileSize` (only supported by TencentDB for MySQL instances). For TencentDB for MySQL instances, the default value is PhysicalFileSize; for other database instances, the default value is `TotalLength`.
        :rtype: str
        """
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def Product(self):
        """Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)). Default value: `mysql`.
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._SortBy = params.get("SortBy")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopSpaceTablesResponse(AbstractModel):
    """DescribeTopSpaceTables response structure.

    """

    def __init__(self):
        r"""
        :param _TopSpaceTables: List of the returned space statistics of top tables.
        :type TopSpaceTables: list of TableSpaceData
        :param _Timestamp: Timestamp (in seconds) of tablespace data collect points
        :type Timestamp: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TopSpaceTables = None
        self._Timestamp = None
        self._RequestId = None

    @property
    def TopSpaceTables(self):
        """List of the returned space statistics of top tables.
        :rtype: list of TableSpaceData
        """
        return self._TopSpaceTables

    @TopSpaceTables.setter
    def TopSpaceTables(self, TopSpaceTables):
        self._TopSpaceTables = TopSpaceTables

    @property
    def Timestamp(self):
        """Timestamp (in seconds) of tablespace data collect points
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TopSpaceTables") is not None:
            self._TopSpaceTables = []
            for item in params.get("TopSpaceTables"):
                obj = TableSpaceData()
                obj._deserialize(item)
                self._TopSpaceTables.append(obj)
        self._Timestamp = params.get("Timestamp")
        self._RequestId = params.get("RequestId")


class DescribeUserSqlAdviceRequest(AbstractModel):
    """DescribeUserSqlAdvice request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _SqlText: SQL statement.
        :type SqlText: str
        :param _Schema: Database name.
        :type Schema: str
        """
        self._InstanceId = None
        self._SqlText = None
        self._Schema = None

    @property
    def InstanceId(self):
        """Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SqlText(self):
        """SQL statement.
        :rtype: str
        """
        return self._SqlText

    @SqlText.setter
    def SqlText(self, SqlText):
        self._SqlText = SqlText

    @property
    def Schema(self):
        """Database name.
        :rtype: str
        """
        return self._Schema

    @Schema.setter
    def Schema(self, Schema):
        self._Schema = Schema


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SqlText = params.get("SqlText")
        self._Schema = params.get("Schema")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserSqlAdviceResponse(AbstractModel):
    """DescribeUserSqlAdvice response structure.

    """

    def __init__(self):
        r"""
        :param _Advices: SQL statement optimization suggestions, which can be parsed into JSON arrays.
        :type Advices: str
        :param _Comments: Notes of SQL statement optimization suggestions, which can be parsed into String arrays.
        :type Comments: str
        :param _SqlText: SQL statement.
        :type SqlText: str
        :param _Schema: Database name.
        :type Schema: str
        :param _Tables: DDL information of related tables, which can be parsed into JSON arrays.
        :type Tables: str
        :param _SqlPlan: SQL execution plan, which can be parsed into JSON.
        :type SqlPlan: str
        :param _Cost: Cost saving details after SQL statement optimization, which can be parsed into JSON.
        :type Cost: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Advices = None
        self._Comments = None
        self._SqlText = None
        self._Schema = None
        self._Tables = None
        self._SqlPlan = None
        self._Cost = None
        self._RequestId = None

    @property
    def Advices(self):
        """SQL statement optimization suggestions, which can be parsed into JSON arrays.
        :rtype: str
        """
        return self._Advices

    @Advices.setter
    def Advices(self, Advices):
        self._Advices = Advices

    @property
    def Comments(self):
        """Notes of SQL statement optimization suggestions, which can be parsed into String arrays.
        :rtype: str
        """
        return self._Comments

    @Comments.setter
    def Comments(self, Comments):
        self._Comments = Comments

    @property
    def SqlText(self):
        """SQL statement.
        :rtype: str
        """
        return self._SqlText

    @SqlText.setter
    def SqlText(self, SqlText):
        self._SqlText = SqlText

    @property
    def Schema(self):
        """Database name.
        :rtype: str
        """
        return self._Schema

    @Schema.setter
    def Schema(self, Schema):
        self._Schema = Schema

    @property
    def Tables(self):
        """DDL information of related tables, which can be parsed into JSON arrays.
        :rtype: str
        """
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables

    @property
    def SqlPlan(self):
        """SQL execution plan, which can be parsed into JSON.
        :rtype: str
        """
        return self._SqlPlan

    @SqlPlan.setter
    def SqlPlan(self, SqlPlan):
        self._SqlPlan = SqlPlan

    @property
    def Cost(self):
        """Cost saving details after SQL statement optimization, which can be parsed into JSON.
        :rtype: str
        """
        return self._Cost

    @Cost.setter
    def Cost(self, Cost):
        self._Cost = Cost

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Advices = params.get("Advices")
        self._Comments = params.get("Comments")
        self._SqlText = params.get("SqlText")
        self._Schema = params.get("Schema")
        self._Tables = params.get("Tables")
        self._SqlPlan = params.get("SqlPlan")
        self._Cost = params.get("Cost")
        self._RequestId = params.get("RequestId")


class DiagHistoryEventItem(AbstractModel):
    """Instance diagnosis event

    """

    def __init__(self):
        r"""
        :param _DiagType: Diagnosis type.
        :type DiagType: str
        :param _EndTime: End time.
        :type EndTime: str
        :param _StartTime: Start time.
        :type StartTime: str
        :param _EventId: Event ID.
        :type EventId: int
        :param _Severity: Severity, which can be divided into 5 levels: 1: fatal, 2: severe, 3: warning, 4: notice, 5: healthy.
        :type Severity: int
        :param _Outline: Summary.
        :type Outline: str
        :param _DiagItem: Diagnosis item.
        :type DiagItem: str
        :param _InstanceId: Instance ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _Metric: Reserved field
Note: this field may return null, indicating that no valid values can be obtained.
        :type Metric: str
        :param _Region: Region
Note: this field may return null, indicating that no valid values can be obtained.
        :type Region: str
        """
        self._DiagType = None
        self._EndTime = None
        self._StartTime = None
        self._EventId = None
        self._Severity = None
        self._Outline = None
        self._DiagItem = None
        self._InstanceId = None
        self._Metric = None
        self._Region = None

    @property
    def DiagType(self):
        """Diagnosis type.
        :rtype: str
        """
        return self._DiagType

    @DiagType.setter
    def DiagType(self, DiagType):
        self._DiagType = DiagType

    @property
    def EndTime(self):
        """End time.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StartTime(self):
        """Start time.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EventId(self):
        """Event ID.
        :rtype: int
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def Severity(self):
        """Severity, which can be divided into 5 levels: 1: fatal, 2: severe, 3: warning, 4: notice, 5: healthy.
        :rtype: int
        """
        return self._Severity

    @Severity.setter
    def Severity(self, Severity):
        self._Severity = Severity

    @property
    def Outline(self):
        """Summary.
        :rtype: str
        """
        return self._Outline

    @Outline.setter
    def Outline(self, Outline):
        self._Outline = Outline

    @property
    def DiagItem(self):
        """Diagnosis item.
        :rtype: str
        """
        return self._DiagItem

    @DiagItem.setter
    def DiagItem(self, DiagItem):
        self._DiagItem = DiagItem

    @property
    def InstanceId(self):
        """Instance ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Metric(self):
        """Reserved field
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Region(self):
        """Region
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._DiagType = params.get("DiagType")
        self._EndTime = params.get("EndTime")
        self._StartTime = params.get("StartTime")
        self._EventId = params.get("EventId")
        self._Severity = params.get("Severity")
        self._Outline = params.get("Outline")
        self._DiagItem = params.get("DiagItem")
        self._InstanceId = params.get("InstanceId")
        self._Metric = params.get("Metric")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventInfo(AbstractModel):
    """Exception information

    """

    def __init__(self):
        r"""
        :param _EventId: Event ID
        :type EventId: int
        :param _DiagType: Diagnosis type
        :type DiagType: str
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _Outline: Summary
        :type Outline: str
        :param _Severity: Severity, which can be divided into 5 levels: 1: fatal, 2: severe, 3: warning, 4: notice, 5: healthy.
        :type Severity: int
        :param _ScoreLost: Deduction
        :type ScoreLost: int
        :param _Metric: Reserved field
        :type Metric: str
        :param _Count: The number of alarms
        :type Count: int
        """
        self._EventId = None
        self._DiagType = None
        self._StartTime = None
        self._EndTime = None
        self._Outline = None
        self._Severity = None
        self._ScoreLost = None
        self._Metric = None
        self._Count = None

    @property
    def EventId(self):
        """Event ID
        :rtype: int
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def DiagType(self):
        """Diagnosis type
        :rtype: str
        """
        return self._DiagType

    @DiagType.setter
    def DiagType(self, DiagType):
        self._DiagType = DiagType

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Outline(self):
        """Summary
        :rtype: str
        """
        return self._Outline

    @Outline.setter
    def Outline(self, Outline):
        self._Outline = Outline

    @property
    def Severity(self):
        """Severity, which can be divided into 5 levels: 1: fatal, 2: severe, 3: warning, 4: notice, 5: healthy.
        :rtype: int
        """
        return self._Severity

    @Severity.setter
    def Severity(self, Severity):
        self._Severity = Severity

    @property
    def ScoreLost(self):
        """Deduction
        :rtype: int
        """
        return self._ScoreLost

    @ScoreLost.setter
    def ScoreLost(self, ScoreLost):
        self._ScoreLost = ScoreLost

    @property
    def Metric(self):
        """Reserved field
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Count(self):
        """The number of alarms
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        self._DiagType = params.get("DiagType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Outline = params.get("Outline")
        self._Severity = params.get("Severity")
        self._ScoreLost = params.get("ScoreLost")
        self._Metric = params.get("Metric")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupItem(AbstractModel):
    """Describe the group information.

    """

    def __init__(self):
        r"""
        :param _Id: Group ID.
        :type Id: int
        :param _Name: Group name.
        :type Name: str
        :param _MemberCount: Number of group members.
        :type MemberCount: int
        """
        self._Id = None
        self._Name = None
        self._MemberCount = None

    @property
    def Id(self):
        """Group ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """Group name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def MemberCount(self):
        """Number of group members.
        :rtype: int
        """
        return self._MemberCount

    @MemberCount.setter
    def MemberCount(self, MemberCount):
        self._MemberCount = MemberCount


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._MemberCount = params.get("MemberCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthReportTask(AbstractModel):
    """Details of health report tasks.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task request ID.
        :type AsyncRequestId: int
        :param _Source: Source that triggers the task. Valid values: `DAILY_INSPECTION` (instance inspection), `SCHEDULED` (timed generation), and `MANUAL` (manual trigger).
        :type Source: str
        :param _Progress: Task progress in %.
        :type Progress: int
        :param _CreateTime: Task creation time.
        :type CreateTime: str
        :param _StartTime: Task start time.
        :type StartTime: str
        :param _EndTime: Task end time.
        :type EndTime: str
        :param _InstanceInfo: Basic information about the instance to which the task belongs.
        :type InstanceInfo: :class:`tencentcloud.dbbrain.v20191016.models.InstanceBasicInfo`
        :param _HealthStatus: Health information in a health report.
        :type HealthStatus: :class:`tencentcloud.dbbrain.v20191016.models.HealthStatus`
        """
        self._AsyncRequestId = None
        self._Source = None
        self._Progress = None
        self._CreateTime = None
        self._StartTime = None
        self._EndTime = None
        self._InstanceInfo = None
        self._HealthStatus = None

    @property
    def AsyncRequestId(self):
        """Async task request ID.
        :rtype: int
        """
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def Source(self):
        """Source that triggers the task. Valid values: `DAILY_INSPECTION` (instance inspection), `SCHEDULED` (timed generation), and `MANUAL` (manual trigger).
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Progress(self):
        """Task progress in %.
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def CreateTime(self):
        """Task creation time.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        """Task start time.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Task end time.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def InstanceInfo(self):
        """Basic information about the instance to which the task belongs.
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.InstanceBasicInfo`
        """
        return self._InstanceInfo

    @InstanceInfo.setter
    def InstanceInfo(self, InstanceInfo):
        self._InstanceInfo = InstanceInfo

    @property
    def HealthStatus(self):
        """Health information in a health report.
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.HealthStatus`
        """
        return self._HealthStatus

    @HealthStatus.setter
    def HealthStatus(self, HealthStatus):
        self._HealthStatus = HealthStatus


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._Source = params.get("Source")
        self._Progress = params.get("Progress")
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("InstanceInfo") is not None:
            self._InstanceInfo = InstanceBasicInfo()
            self._InstanceInfo._deserialize(params.get("InstanceInfo"))
        if params.get("HealthStatus") is not None:
            self._HealthStatus = HealthStatus()
            self._HealthStatus._deserialize(params.get("HealthStatus"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthScoreInfo(AbstractModel):
    """Obtain the details of the health score and deduction.

    """

    def __init__(self):
        r"""
        :param _IssueTypes: Exception details
        :type IssueTypes: list of IssueTypeInfo
        :param _EventsTotalCount: Total number of the exceptions
        :type EventsTotalCount: int
        :param _HealthScore: Health score
        :type HealthScore: int
        :param _HealthLevel: Health level, such as "HEALTH", "SUB_HEALTH", "RISK", "HIGH_RISK".
        :type HealthLevel: str
        """
        self._IssueTypes = None
        self._EventsTotalCount = None
        self._HealthScore = None
        self._HealthLevel = None

    @property
    def IssueTypes(self):
        """Exception details
        :rtype: list of IssueTypeInfo
        """
        return self._IssueTypes

    @IssueTypes.setter
    def IssueTypes(self, IssueTypes):
        self._IssueTypes = IssueTypes

    @property
    def EventsTotalCount(self):
        """Total number of the exceptions
        :rtype: int
        """
        return self._EventsTotalCount

    @EventsTotalCount.setter
    def EventsTotalCount(self, EventsTotalCount):
        self._EventsTotalCount = EventsTotalCount

    @property
    def HealthScore(self):
        """Health score
        :rtype: int
        """
        return self._HealthScore

    @HealthScore.setter
    def HealthScore(self, HealthScore):
        self._HealthScore = HealthScore

    @property
    def HealthLevel(self):
        """Health level, such as "HEALTH", "SUB_HEALTH", "RISK", "HIGH_RISK".
        :rtype: str
        """
        return self._HealthLevel

    @HealthLevel.setter
    def HealthLevel(self, HealthLevel):
        self._HealthLevel = HealthLevel


    def _deserialize(self, params):
        if params.get("IssueTypes") is not None:
            self._IssueTypes = []
            for item in params.get("IssueTypes"):
                obj = IssueTypeInfo()
                obj._deserialize(item)
                self._IssueTypes.append(obj)
        self._EventsTotalCount = params.get("EventsTotalCount")
        self._HealthScore = params.get("HealthScore")
        self._HealthLevel = params.get("HealthLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthStatus(AbstractModel):
    """Instance health status.

    """

    def __init__(self):
        r"""
        :param _HealthScore: Health score out of 100 points.
        :type HealthScore: int
        :param _HealthLevel: Health level. Valid values: `HEALTH` (healthy), `SUB_HEALTH` (suboptimal), `RISK` (risky), and `HIGH_RISK` (critical).
        :type HealthLevel: str
        :param _ScoreLost: Total scores deducted.
        :type ScoreLost: int
        :param _ScoreDetails: Deduction details.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type ScoreDetails: list of ScoreDetail
        """
        self._HealthScore = None
        self._HealthLevel = None
        self._ScoreLost = None
        self._ScoreDetails = None

    @property
    def HealthScore(self):
        """Health score out of 100 points.
        :rtype: int
        """
        return self._HealthScore

    @HealthScore.setter
    def HealthScore(self, HealthScore):
        self._HealthScore = HealthScore

    @property
    def HealthLevel(self):
        """Health level. Valid values: `HEALTH` (healthy), `SUB_HEALTH` (suboptimal), `RISK` (risky), and `HIGH_RISK` (critical).
        :rtype: str
        """
        return self._HealthLevel

    @HealthLevel.setter
    def HealthLevel(self, HealthLevel):
        self._HealthLevel = HealthLevel

    @property
    def ScoreLost(self):
        """Total scores deducted.
        :rtype: int
        """
        return self._ScoreLost

    @ScoreLost.setter
    def ScoreLost(self, ScoreLost):
        self._ScoreLost = ScoreLost

    @property
    def ScoreDetails(self):
        """Deduction details.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: list of ScoreDetail
        """
        return self._ScoreDetails

    @ScoreDetails.setter
    def ScoreDetails(self, ScoreDetails):
        self._ScoreDetails = ScoreDetails


    def _deserialize(self, params):
        self._HealthScore = params.get("HealthScore")
        self._HealthLevel = params.get("HealthLevel")
        self._ScoreLost = params.get("ScoreLost")
        if params.get("ScoreDetails") is not None:
            self._ScoreDetails = []
            for item in params.get("ScoreDetails"):
                obj = ScoreDetail()
                obj._deserialize(item)
                self._ScoreDetails.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceBasicInfo(AbstractModel):
    """Basic information of instance.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _InstanceName: Instance name.
        :type InstanceName: str
        :param _Vip: Private IP of the instance.
        :type Vip: str
        :param _Vport: Private network port of the instance.
        :type Vport: int
        :param _Product: Instance product.
        :type Product: str
        :param _EngineVersion: Instance engine version.
        :type EngineVersion: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Vip = None
        self._Vport = None
        self._Product = None
        self._EngineVersion = None

    @property
    def InstanceId(self):
        """Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """Instance name.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Vip(self):
        """Private IP of the instance.
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """Private network port of the instance.
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Product(self):
        """Instance product.
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def EngineVersion(self):
        """Instance engine version.
        :rtype: str
        """
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._Product = params.get("Product")
        self._EngineVersion = params.get("EngineVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceConfs(AbstractModel):
    """Instance configuration.

    """

    def __init__(self):
        r"""
        :param _DailyInspection: Whether to enable database inspection. Valid values: Yes/No.
        :type DailyInspection: str
        :param _OverviewDisplay: Whether to enable instance overview. Valid values: Yes/No.
        :type OverviewDisplay: str
        """
        self._DailyInspection = None
        self._OverviewDisplay = None

    @property
    def DailyInspection(self):
        """Whether to enable database inspection. Valid values: Yes/No.
        :rtype: str
        """
        return self._DailyInspection

    @DailyInspection.setter
    def DailyInspection(self, DailyInspection):
        self._DailyInspection = DailyInspection

    @property
    def OverviewDisplay(self):
        """Whether to enable instance overview. Valid values: Yes/No.
        :rtype: str
        """
        return self._OverviewDisplay

    @OverviewDisplay.setter
    def OverviewDisplay(self, OverviewDisplay):
        self._OverviewDisplay = OverviewDisplay


    def _deserialize(self, params):
        self._DailyInspection = params.get("DailyInspection")
        self._OverviewDisplay = params.get("OverviewDisplay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInfo(AbstractModel):
    """Query the list of instances and return information about the instances.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _Region: The region where the instance belongs
        :type Region: str
        :param _HealthScore: Health score
        :type HealthScore: int
        :param _Product: Service
        :type Product: str
        :param _EventCount: Number of exceptions
        :type EventCount: int
        :param _InstanceType: Instance type. Valid values: 1: MASTER, 2: DR, 3: RO, 4: SDR
        :type InstanceType: int
        :param _Cpu: Number of cores
        :type Cpu: int
        :param _Memory: Memory in MB
        :type Memory: int
        :param _Volume: Disk storage in GB
        :type Volume: int
        :param _EngineVersion: Database version
        :type EngineVersion: str
        :param _Vip: Private network address
        :type Vip: str
        :param _Vport: Private network port
        :type Vport: int
        :param _Source: Access source
        :type Source: str
        :param _GroupId: Group ID
        :type GroupId: str
        :param _GroupName: Group name
        :type GroupName: str
        :param _Status: Instance status. Valid values: 0: Delivering, 1: Running, 4: Terminating, 5: Isolated
        :type Status: int
        :param _UniqSubnetId: Subnet unified ID
        :type UniqSubnetId: str
        :param _DeployMode: cdb (TencentDB instance) type
        :type DeployMode: str
        :param _InitFlag: cdb (TencentDB instance) initialization flag. Valid values: 0: not initialized, 1: initialized
        :type InitFlag: int
        :param _TaskStatus: Task status
        :type TaskStatus: int
        :param _UniqVpcId: Unified VPC ID
        :type UniqVpcId: str
        :param _InstanceConf: Instance inspection/overview status
        :type InstanceConf: :class:`tencentcloud.dbbrain.v20191016.models.InstanceConfs`
        :param _DeadlineTime: Resource expiration time
        :type DeadlineTime: str
        :param _IsSupported: Whether it is an instance supported by DBbrain.
        :type IsSupported: bool
        :param _SecAuditStatus: The status of instance security audit log. ON: enabled, OFF: disabled.
        :type SecAuditStatus: str
        :param _AuditPolicyStatus: The status of instance audit log. ALL_AUDIT: full audit is enabled, RULE_AUDIT: rule audit is enabled, UNBOUND: audit is disabled.
        :type AuditPolicyStatus: str
        :param _AuditRunningStatus: The running status of instance audit log. normal: running, paused: suspension due to arrears
        :type AuditRunningStatus: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Region = None
        self._HealthScore = None
        self._Product = None
        self._EventCount = None
        self._InstanceType = None
        self._Cpu = None
        self._Memory = None
        self._Volume = None
        self._EngineVersion = None
        self._Vip = None
        self._Vport = None
        self._Source = None
        self._GroupId = None
        self._GroupName = None
        self._Status = None
        self._UniqSubnetId = None
        self._DeployMode = None
        self._InitFlag = None
        self._TaskStatus = None
        self._UniqVpcId = None
        self._InstanceConf = None
        self._DeadlineTime = None
        self._IsSupported = None
        self._SecAuditStatus = None
        self._AuditPolicyStatus = None
        self._AuditRunningStatus = None

    @property
    def InstanceId(self):
        """Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """Instance name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Region(self):
        """The region where the instance belongs
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def HealthScore(self):
        """Health score
        :rtype: int
        """
        return self._HealthScore

    @HealthScore.setter
    def HealthScore(self, HealthScore):
        self._HealthScore = HealthScore

    @property
    def Product(self):
        """Service
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def EventCount(self):
        """Number of exceptions
        :rtype: int
        """
        return self._EventCount

    @EventCount.setter
    def EventCount(self, EventCount):
        self._EventCount = EventCount

    @property
    def InstanceType(self):
        """Instance type. Valid values: 1: MASTER, 2: DR, 3: RO, 4: SDR
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Cpu(self):
        """Number of cores
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """Memory in MB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        """Disk storage in GB
        :rtype: int
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def EngineVersion(self):
        """Database version
        :rtype: str
        """
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def Vip(self):
        """Private network address
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """Private network port
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Source(self):
        """Access source
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def GroupId(self):
        """Group ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        """Group name
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Status(self):
        """Instance status. Valid values: 0: Delivering, 1: Running, 4: Terminating, 5: Isolated
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UniqSubnetId(self):
        """Subnet unified ID
        :rtype: str
        """
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def DeployMode(self):
        """cdb (TencentDB instance) type
        :rtype: str
        """
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def InitFlag(self):
        """cdb (TencentDB instance) initialization flag. Valid values: 0: not initialized, 1: initialized
        :rtype: int
        """
        return self._InitFlag

    @InitFlag.setter
    def InitFlag(self, InitFlag):
        self._InitFlag = InitFlag

    @property
    def TaskStatus(self):
        """Task status
        :rtype: int
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def UniqVpcId(self):
        """Unified VPC ID
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def InstanceConf(self):
        """Instance inspection/overview status
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.InstanceConfs`
        """
        return self._InstanceConf

    @InstanceConf.setter
    def InstanceConf(self, InstanceConf):
        self._InstanceConf = InstanceConf

    @property
    def DeadlineTime(self):
        """Resource expiration time
        :rtype: str
        """
        return self._DeadlineTime

    @DeadlineTime.setter
    def DeadlineTime(self, DeadlineTime):
        self._DeadlineTime = DeadlineTime

    @property
    def IsSupported(self):
        """Whether it is an instance supported by DBbrain.
        :rtype: bool
        """
        return self._IsSupported

    @IsSupported.setter
    def IsSupported(self, IsSupported):
        self._IsSupported = IsSupported

    @property
    def SecAuditStatus(self):
        """The status of instance security audit log. ON: enabled, OFF: disabled.
        :rtype: str
        """
        return self._SecAuditStatus

    @SecAuditStatus.setter
    def SecAuditStatus(self, SecAuditStatus):
        self._SecAuditStatus = SecAuditStatus

    @property
    def AuditPolicyStatus(self):
        """The status of instance audit log. ALL_AUDIT: full audit is enabled, RULE_AUDIT: rule audit is enabled, UNBOUND: audit is disabled.
        :rtype: str
        """
        return self._AuditPolicyStatus

    @AuditPolicyStatus.setter
    def AuditPolicyStatus(self, AuditPolicyStatus):
        self._AuditPolicyStatus = AuditPolicyStatus

    @property
    def AuditRunningStatus(self):
        """The running status of instance audit log. normal: running, paused: suspension due to arrears
        :rtype: str
        """
        return self._AuditRunningStatus

    @AuditRunningStatus.setter
    def AuditRunningStatus(self, AuditRunningStatus):
        self._AuditRunningStatus = AuditRunningStatus


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Region = params.get("Region")
        self._HealthScore = params.get("HealthScore")
        self._Product = params.get("Product")
        self._EventCount = params.get("EventCount")
        self._InstanceType = params.get("InstanceType")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._EngineVersion = params.get("EngineVersion")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._Source = params.get("Source")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._Status = params.get("Status")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._DeployMode = params.get("DeployMode")
        self._InitFlag = params.get("InitFlag")
        self._TaskStatus = params.get("TaskStatus")
        self._UniqVpcId = params.get("UniqVpcId")
        if params.get("InstanceConf") is not None:
            self._InstanceConf = InstanceConfs()
            self._InstanceConf._deserialize(params.get("InstanceConf"))
        self._DeadlineTime = params.get("DeadlineTime")
        self._IsSupported = params.get("IsSupported")
        self._SecAuditStatus = params.get("SecAuditStatus")
        self._AuditPolicyStatus = params.get("AuditPolicyStatus")
        self._AuditRunningStatus = params.get("AuditRunningStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IssueTypeInfo(AbstractModel):
    """Metric information

    """

    def __init__(self):
        r"""
        :param _IssueType: Metric categories: AVAILABILITY, MAINTAINABILITY, PERFORMANCE, and RELIABILITY
        :type IssueType: str
        :param _Events: Exception
        :type Events: list of EventInfo
        :param _TotalCount: Total number of the exceptions
        :type TotalCount: int
        """
        self._IssueType = None
        self._Events = None
        self._TotalCount = None

    @property
    def IssueType(self):
        """Metric categories: AVAILABILITY, MAINTAINABILITY, PERFORMANCE, and RELIABILITY
        :rtype: str
        """
        return self._IssueType

    @IssueType.setter
    def IssueType(self, IssueType):
        self._IssueType = IssueType

    @property
    def Events(self):
        """Exception
        :rtype: list of EventInfo
        """
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def TotalCount(self):
        """Total number of the exceptions
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        self._IssueType = params.get("IssueType")
        if params.get("Events") is not None:
            self._Events = []
            for item in params.get("Events"):
                obj = EventInfo()
                obj._deserialize(item)
                self._Events.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MailConfiguration(AbstractModel):
    """Email sending configuration.

    """

    def __init__(self):
        r"""
        :param _SendMail: Whether to enable email sending. Valid values: 0 (No), 1 (Yes).
        :type SendMail: int
        :param _Region: Region configuration, such as "ap-guangzhou", "ap-shanghai". For the inspection email sending template, configure the region where you need to send the inspection email. For the subscription email sending template, configure the region to which the current subscribed instance belongs.
        :type Region: list of str
        :param _HealthStatus: Sending a report with the specified health level, such as "HEALTH", "SUB_HEALTH", "RISK", "HIGH_RISK".
        :type HealthStatus: list of str
        :param _ContactPerson: Contact ID. Either `ContactGroup` or `ContactID` should be passed in.
        :type ContactPerson: list of int
        :param _ContactGroup: Contact group ID. Either `ContactGroup` or `ContactID` should be passed in.
        :type ContactGroup: list of int
        """
        self._SendMail = None
        self._Region = None
        self._HealthStatus = None
        self._ContactPerson = None
        self._ContactGroup = None

    @property
    def SendMail(self):
        """Whether to enable email sending. Valid values: 0 (No), 1 (Yes).
        :rtype: int
        """
        return self._SendMail

    @SendMail.setter
    def SendMail(self, SendMail):
        self._SendMail = SendMail

    @property
    def Region(self):
        """Region configuration, such as "ap-guangzhou", "ap-shanghai". For the inspection email sending template, configure the region where you need to send the inspection email. For the subscription email sending template, configure the region to which the current subscribed instance belongs.
        :rtype: list of str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def HealthStatus(self):
        """Sending a report with the specified health level, such as "HEALTH", "SUB_HEALTH", "RISK", "HIGH_RISK".
        :rtype: list of str
        """
        return self._HealthStatus

    @HealthStatus.setter
    def HealthStatus(self, HealthStatus):
        self._HealthStatus = HealthStatus

    @property
    def ContactPerson(self):
        """Contact ID. Either `ContactGroup` or `ContactID` should be passed in.
        :rtype: list of int
        """
        return self._ContactPerson

    @ContactPerson.setter
    def ContactPerson(self, ContactPerson):
        self._ContactPerson = ContactPerson

    @property
    def ContactGroup(self):
        """Contact group ID. Either `ContactGroup` or `ContactID` should be passed in.
        :rtype: list of int
        """
        return self._ContactGroup

    @ContactGroup.setter
    def ContactGroup(self, ContactGroup):
        self._ContactGroup = ContactGroup


    def _deserialize(self, params):
        self._SendMail = params.get("SendMail")
        self._Region = params.get("Region")
        self._HealthStatus = params.get("HealthStatus")
        self._ContactPerson = params.get("ContactPerson")
        self._ContactGroup = params.get("ContactGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDiagDBInstanceConfRequest(AbstractModel):
    """ModifyDiagDBInstanceConf request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceConfs: Whether to enable inspection
        :type InstanceConfs: :class:`tencentcloud.dbbrain.v20191016.models.InstanceConfs`
        :param _Regions: Target regions of the request. If the value is `All`, it is applied to all regions.
        :type Regions: str
        :param _Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)).
        :type Product: str
        :param _InstanceIds: ID of the instance to modify.
        :type InstanceIds: list of str
        """
        self._InstanceConfs = None
        self._Regions = None
        self._Product = None
        self._InstanceIds = None

    @property
    def InstanceConfs(self):
        """Whether to enable inspection
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.InstanceConfs`
        """
        return self._InstanceConfs

    @InstanceConfs.setter
    def InstanceConfs(self, InstanceConfs):
        self._InstanceConfs = InstanceConfs

    @property
    def Regions(self):
        """Target regions of the request. If the value is `All`, it is applied to all regions.
        :rtype: str
        """
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions

    @property
    def Product(self):
        """Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TencentDB for CynosDB (compatible with MySQL)).
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceIds(self):
        """ID of the instance to modify.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        if params.get("InstanceConfs") is not None:
            self._InstanceConfs = InstanceConfs()
            self._InstanceConfs._deserialize(params.get("InstanceConfs"))
        self._Regions = params.get("Regions")
        self._Product = params.get("Product")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDiagDBInstanceConfResponse(AbstractModel):
    """ModifyDiagDBInstanceConf response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class MonitorFloatMetric(AbstractModel):
    """Monitoring data in float type

    """

    def __init__(self):
        r"""
        :param _Metric: Metric name.
        :type Metric: str
        :param _Unit: Metric unit.
        :type Unit: str
        :param _Values: Metric value.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Values: list of float
        """
        self._Metric = None
        self._Unit = None
        self._Values = None

    @property
    def Metric(self):
        """Metric name.
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Unit(self):
        """Metric unit.
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Values(self):
        """Metric value.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of float
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Metric = params.get("Metric")
        self._Unit = params.get("Unit")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonitorFloatMetricSeriesData(AbstractModel):
    """Monitoring metric value in float type in a unit of time interval

    """

    def __init__(self):
        r"""
        :param _Series: Monitoring metric.
        :type Series: list of MonitorFloatMetric
        :param _Timestamp: Timestamp corresponding to monitoring metric.
        :type Timestamp: list of int
        """
        self._Series = None
        self._Timestamp = None

    @property
    def Series(self):
        """Monitoring metric.
        :rtype: list of MonitorFloatMetric
        """
        return self._Series

    @Series.setter
    def Series(self, Series):
        self._Series = Series

    @property
    def Timestamp(self):
        """Timestamp corresponding to monitoring metric.
        :rtype: list of int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp


    def _deserialize(self, params):
        if params.get("Series") is not None:
            self._Series = []
            for item in params.get("Series"):
                obj = MonitorFloatMetric()
                obj._deserialize(item)
                self._Series.append(obj)
        self._Timestamp = params.get("Timestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonitorMetric(AbstractModel):
    """Monitoring data

    """

    def __init__(self):
        r"""
        :param _Metric: Metric name.
        :type Metric: str
        :param _Unit: Metric unit.
        :type Unit: str
        :param _Values: Metric value.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Values: list of int
        """
        self._Metric = None
        self._Unit = None
        self._Values = None

    @property
    def Metric(self):
        """Metric name.
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Unit(self):
        """Metric unit.
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Values(self):
        """Metric value.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of int
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Metric = params.get("Metric")
        self._Unit = params.get("Unit")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonitorMetricSeriesData(AbstractModel):
    """Monitoring metric data in specified time range

    """

    def __init__(self):
        r"""
        :param _Series: Monitoring metric.
        :type Series: list of MonitorMetric
        :param _Timestamp: Timestamp corresponding to monitoring metric.
        :type Timestamp: list of int
        """
        self._Series = None
        self._Timestamp = None

    @property
    def Series(self):
        """Monitoring metric.
        :rtype: list of MonitorMetric
        """
        return self._Series

    @Series.setter
    def Series(self, Series):
        self._Series = Series

    @property
    def Timestamp(self):
        """Timestamp corresponding to monitoring metric.
        :rtype: list of int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp


    def _deserialize(self, params):
        if params.get("Series") is not None:
            self._Series = []
            for item in params.get("Series"):
                obj = MonitorMetric()
                obj._deserialize(item)
                self._Series.append(obj)
        self._Timestamp = params.get("Timestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProfileInfo(AbstractModel):
    """Information configured by user.

    """

    def __init__(self):
        r"""
        :param _Language: Language of the email, such as `en`.
        :type Language: str
        :param _MailConfiguration: The content of email template.
        :type MailConfiguration: :class:`tencentcloud.dbbrain.v20191016.models.MailConfiguration`
        """
        self._Language = None
        self._MailConfiguration = None

    @property
    def Language(self):
        """Language of the email, such as `en`.
        :rtype: str
        """
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language

    @property
    def MailConfiguration(self):
        """The content of email template.
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.MailConfiguration`
        """
        return self._MailConfiguration

    @MailConfiguration.setter
    def MailConfiguration(self, MailConfiguration):
        self._MailConfiguration = MailConfiguration


    def _deserialize(self, params):
        self._Language = params.get("Language")
        if params.get("MailConfiguration") is not None:
            self._MailConfiguration = MailConfiguration()
            self._MailConfiguration._deserialize(params.get("MailConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchemaItem(AbstractModel):
    """`SchemaItem` array

    """

    def __init__(self):
        r"""
        :param _Schema: Database name
        :type Schema: str
        """
        self._Schema = None

    @property
    def Schema(self):
        """Database name
        :rtype: str
        """
        return self._Schema

    @Schema.setter
    def Schema(self, Schema):
        self._Schema = Schema


    def _deserialize(self, params):
        self._Schema = params.get("Schema")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchemaSpaceData(AbstractModel):
    """Database space statistics.

    """

    def __init__(self):
        r"""
        :param _TableSchema: Database name.
        :type TableSchema: str
        :param _DataLength: Data space in MB.
        :type DataLength: float
        :param _IndexLength: Index space in MB.
        :type IndexLength: float
        :param _DataFree: Fragmented space in MB.
        :type DataFree: float
        :param _TotalLength: Total space usage in MB.
        :type TotalLength: float
        :param _FragRatio: Fragmented rate (%).
        :type FragRatio: float
        :param _TableRows: Number of rows.
        :type TableRows: int
        :param _PhysicalFileSize: The total size of the independent physical files corresponding to all the database tables (MB).
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type PhysicalFileSize: float
        """
        self._TableSchema = None
        self._DataLength = None
        self._IndexLength = None
        self._DataFree = None
        self._TotalLength = None
        self._FragRatio = None
        self._TableRows = None
        self._PhysicalFileSize = None

    @property
    def TableSchema(self):
        """Database name.
        :rtype: str
        """
        return self._TableSchema

    @TableSchema.setter
    def TableSchema(self, TableSchema):
        self._TableSchema = TableSchema

    @property
    def DataLength(self):
        """Data space in MB.
        :rtype: float
        """
        return self._DataLength

    @DataLength.setter
    def DataLength(self, DataLength):
        self._DataLength = DataLength

    @property
    def IndexLength(self):
        """Index space in MB.
        :rtype: float
        """
        return self._IndexLength

    @IndexLength.setter
    def IndexLength(self, IndexLength):
        self._IndexLength = IndexLength

    @property
    def DataFree(self):
        """Fragmented space in MB.
        :rtype: float
        """
        return self._DataFree

    @DataFree.setter
    def DataFree(self, DataFree):
        self._DataFree = DataFree

    @property
    def TotalLength(self):
        """Total space usage in MB.
        :rtype: float
        """
        return self._TotalLength

    @TotalLength.setter
    def TotalLength(self, TotalLength):
        self._TotalLength = TotalLength

    @property
    def FragRatio(self):
        """Fragmented rate (%).
        :rtype: float
        """
        return self._FragRatio

    @FragRatio.setter
    def FragRatio(self, FragRatio):
        self._FragRatio = FragRatio

    @property
    def TableRows(self):
        """Number of rows.
        :rtype: int
        """
        return self._TableRows

    @TableRows.setter
    def TableRows(self, TableRows):
        self._TableRows = TableRows

    @property
    def PhysicalFileSize(self):
        """The total size of the independent physical files corresponding to all the database tables (MB).
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._PhysicalFileSize

    @PhysicalFileSize.setter
    def PhysicalFileSize(self, PhysicalFileSize):
        self._PhysicalFileSize = PhysicalFileSize


    def _deserialize(self, params):
        self._TableSchema = params.get("TableSchema")
        self._DataLength = params.get("DataLength")
        self._IndexLength = params.get("IndexLength")
        self._DataFree = params.get("DataFree")
        self._TotalLength = params.get("TotalLength")
        self._FragRatio = params.get("FragRatio")
        self._TableRows = params.get("TableRows")
        self._PhysicalFileSize = params.get("PhysicalFileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchemaSpaceTimeSeries(AbstractModel):
    """Time series of database space data

    """

    def __init__(self):
        r"""
        :param _TableSchema: Database name
        :type TableSchema: str
        :param _SeriesData: Monitoring metric data in a unit of time interval.
        :type SeriesData: :class:`tencentcloud.dbbrain.v20191016.models.MonitorMetricSeriesData`
        """
        self._TableSchema = None
        self._SeriesData = None

    @property
    def TableSchema(self):
        """Database name
        :rtype: str
        """
        return self._TableSchema

    @TableSchema.setter
    def TableSchema(self, TableSchema):
        self._TableSchema = TableSchema

    @property
    def SeriesData(self):
        """Monitoring metric data in a unit of time interval.
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.MonitorMetricSeriesData`
        """
        return self._SeriesData

    @SeriesData.setter
    def SeriesData(self, SeriesData):
        self._SeriesData = SeriesData


    def _deserialize(self, params):
        self._TableSchema = params.get("TableSchema")
        if params.get("SeriesData") is not None:
            self._SeriesData = MonitorMetricSeriesData()
            self._SeriesData._deserialize(params.get("SeriesData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScoreDetail(AbstractModel):
    """Deduction details.

    """

    def __init__(self):
        r"""
        :param _IssueType: Deduction item types. Valid values: availability, maintainability, performance, and reliability.
        :type IssueType: str
        :param _ScoreLost: Total scores deducted.
        :type ScoreLost: int
        :param _ScoreLostMax: Upper limit of the deducted scores.
        :type ScoreLostMax: int
        :param _Items: Deduction item list.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type Items: list of ScoreItem
        """
        self._IssueType = None
        self._ScoreLost = None
        self._ScoreLostMax = None
        self._Items = None

    @property
    def IssueType(self):
        """Deduction item types. Valid values: availability, maintainability, performance, and reliability.
        :rtype: str
        """
        return self._IssueType

    @IssueType.setter
    def IssueType(self, IssueType):
        self._IssueType = IssueType

    @property
    def ScoreLost(self):
        """Total scores deducted.
        :rtype: int
        """
        return self._ScoreLost

    @ScoreLost.setter
    def ScoreLost(self, ScoreLost):
        self._ScoreLost = ScoreLost

    @property
    def ScoreLostMax(self):
        """Upper limit of the deducted scores.
        :rtype: int
        """
        return self._ScoreLostMax

    @ScoreLostMax.setter
    def ScoreLostMax(self, ScoreLostMax):
        self._ScoreLostMax = ScoreLostMax

    @property
    def Items(self):
        """Deduction item list.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :rtype: list of ScoreItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._IssueType = params.get("IssueType")
        self._ScoreLost = params.get("ScoreLost")
        self._ScoreLostMax = params.get("ScoreLostMax")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ScoreItem()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScoreItem(AbstractModel):
    """Diagnosis deduction item.

    """

    def __init__(self):
        r"""
        :param _DiagItem: Exception diagnosis item name.
        :type DiagItem: str
        :param _IssueType: Diagnosis item types. Valid values: availability, maintainability, performance, and reliability.
        :type IssueType: str
        :param _TopSeverity: Health level. Valid values: information, reminder, alarm, serious, fatal.
        :type TopSeverity: str
        :param _Count: Number of occurrences of this exception diagnosis item.
        :type Count: int
        :param _ScoreLost: Scores deducted.
        :type ScoreLost: int
        """
        self._DiagItem = None
        self._IssueType = None
        self._TopSeverity = None
        self._Count = None
        self._ScoreLost = None

    @property
    def DiagItem(self):
        """Exception diagnosis item name.
        :rtype: str
        """
        return self._DiagItem

    @DiagItem.setter
    def DiagItem(self, DiagItem):
        self._DiagItem = DiagItem

    @property
    def IssueType(self):
        """Diagnosis item types. Valid values: availability, maintainability, performance, and reliability.
        :rtype: str
        """
        return self._IssueType

    @IssueType.setter
    def IssueType(self, IssueType):
        self._IssueType = IssueType

    @property
    def TopSeverity(self):
        """Health level. Valid values: information, reminder, alarm, serious, fatal.
        :rtype: str
        """
        return self._TopSeverity

    @TopSeverity.setter
    def TopSeverity(self, TopSeverity):
        self._TopSeverity = TopSeverity

    @property
    def Count(self):
        """Number of occurrences of this exception diagnosis item.
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def ScoreLost(self):
        """Scores deducted.
        :rtype: int
        """
        return self._ScoreLost

    @ScoreLost.setter
    def ScoreLost(self, ScoreLost):
        self._ScoreLost = ScoreLost


    def _deserialize(self, params):
        self._DiagItem = params.get("DiagItem")
        self._IssueType = params.get("IssueType")
        self._TopSeverity = params.get("TopSeverity")
        self._Count = params.get("Count")
        self._ScoreLost = params.get("ScoreLost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogHost(AbstractModel):
    """Details of slow log source addresses.

    """

    def __init__(self):
        r"""
        :param _UserHost: Source addresses.
        :type UserHost: str
        :param _Ratio: The proportion (in %) of slow logs from this source address to the total number of slow logs
        :type Ratio: float
        :param _Count: Number of slow logs from this source address.
        :type Count: int
        """
        self._UserHost = None
        self._Ratio = None
        self._Count = None

    @property
    def UserHost(self):
        """Source addresses.
        :rtype: str
        """
        return self._UserHost

    @UserHost.setter
    def UserHost(self, UserHost):
        self._UserHost = UserHost

    @property
    def Ratio(self):
        """The proportion (in %) of slow logs from this source address to the total number of slow logs
        :rtype: float
        """
        return self._Ratio

    @Ratio.setter
    def Ratio(self, Ratio):
        self._Ratio = Ratio

    @property
    def Count(self):
        """Number of slow logs from this source address.
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._UserHost = params.get("UserHost")
        self._Ratio = params.get("Ratio")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogTopSqlItem(AbstractModel):
    """Top slow SQL statements

    """

    def __init__(self):
        r"""
        :param _LockTime: Total SQL lock wait time
        :type LockTime: float
        :param _LockTimeMax: Maximum lock wait time
        :type LockTimeMax: float
        :param _LockTimeMin: Minimum lock wait time
        :type LockTimeMin: float
        :param _RowsExamined: Total number of scanned rows
        :type RowsExamined: int
        :param _RowsExaminedMax: Maximum number of scanned rows
        :type RowsExaminedMax: int
        :param _RowsExaminedMin: Minimum number of scanned rows
        :type RowsExaminedMin: int
        :param _QueryTime: Total duration
        :type QueryTime: float
        :param _QueryTimeMax: Maximum execution time
        :type QueryTimeMax: float
        :param _QueryTimeMin: Minimum execution time
        :type QueryTimeMin: float
        :param _RowsSent: Total number of returned rows
        :type RowsSent: int
        :param _RowsSentMax: Maximum number of returned rows
        :type RowsSentMax: int
        :param _RowsSentMin: Minimum number of returned rows
        :type RowsSentMin: int
        :param _ExecTimes: Number of executions
        :type ExecTimes: int
        :param _SqlTemplate: SQL template
        :type SqlTemplate: str
        :param _SqlText: SQL with parameter (random)
        :type SqlText: str
        :param _Schema: Database name
        :type Schema: str
        :param _QueryTimeRatio: Ratio of total duration
        :type QueryTimeRatio: float
        :param _LockTimeRatio: Ratio of total SQL lock wait time
        :type LockTimeRatio: float
        :param _RowsExaminedRatio: Ratio of total number of scanned rows
        :type RowsExaminedRatio: float
        :param _RowsSentRatio: Ratio of total number of returned rows
        :type RowsSentRatio: float
        :param _QueryTimeAvg: Average execution time
        :type QueryTimeAvg: float
        :param _RowsSentAvg: Average number of rows returned
        :type RowsSentAvg: float
        :param _LockTimeAvg: Average lock wait time
        :type LockTimeAvg: float
        :param _RowsExaminedAvg: Average number of rows scanned
        :type RowsExaminedAvg: float
        """
        self._LockTime = None
        self._LockTimeMax = None
        self._LockTimeMin = None
        self._RowsExamined = None
        self._RowsExaminedMax = None
        self._RowsExaminedMin = None
        self._QueryTime = None
        self._QueryTimeMax = None
        self._QueryTimeMin = None
        self._RowsSent = None
        self._RowsSentMax = None
        self._RowsSentMin = None
        self._ExecTimes = None
        self._SqlTemplate = None
        self._SqlText = None
        self._Schema = None
        self._QueryTimeRatio = None
        self._LockTimeRatio = None
        self._RowsExaminedRatio = None
        self._RowsSentRatio = None
        self._QueryTimeAvg = None
        self._RowsSentAvg = None
        self._LockTimeAvg = None
        self._RowsExaminedAvg = None

    @property
    def LockTime(self):
        """Total SQL lock wait time
        :rtype: float
        """
        return self._LockTime

    @LockTime.setter
    def LockTime(self, LockTime):
        self._LockTime = LockTime

    @property
    def LockTimeMax(self):
        """Maximum lock wait time
        :rtype: float
        """
        return self._LockTimeMax

    @LockTimeMax.setter
    def LockTimeMax(self, LockTimeMax):
        self._LockTimeMax = LockTimeMax

    @property
    def LockTimeMin(self):
        """Minimum lock wait time
        :rtype: float
        """
        return self._LockTimeMin

    @LockTimeMin.setter
    def LockTimeMin(self, LockTimeMin):
        self._LockTimeMin = LockTimeMin

    @property
    def RowsExamined(self):
        """Total number of scanned rows
        :rtype: int
        """
        return self._RowsExamined

    @RowsExamined.setter
    def RowsExamined(self, RowsExamined):
        self._RowsExamined = RowsExamined

    @property
    def RowsExaminedMax(self):
        """Maximum number of scanned rows
        :rtype: int
        """
        return self._RowsExaminedMax

    @RowsExaminedMax.setter
    def RowsExaminedMax(self, RowsExaminedMax):
        self._RowsExaminedMax = RowsExaminedMax

    @property
    def RowsExaminedMin(self):
        """Minimum number of scanned rows
        :rtype: int
        """
        return self._RowsExaminedMin

    @RowsExaminedMin.setter
    def RowsExaminedMin(self, RowsExaminedMin):
        self._RowsExaminedMin = RowsExaminedMin

    @property
    def QueryTime(self):
        """Total duration
        :rtype: float
        """
        return self._QueryTime

    @QueryTime.setter
    def QueryTime(self, QueryTime):
        self._QueryTime = QueryTime

    @property
    def QueryTimeMax(self):
        """Maximum execution time
        :rtype: float
        """
        return self._QueryTimeMax

    @QueryTimeMax.setter
    def QueryTimeMax(self, QueryTimeMax):
        self._QueryTimeMax = QueryTimeMax

    @property
    def QueryTimeMin(self):
        """Minimum execution time
        :rtype: float
        """
        return self._QueryTimeMin

    @QueryTimeMin.setter
    def QueryTimeMin(self, QueryTimeMin):
        self._QueryTimeMin = QueryTimeMin

    @property
    def RowsSent(self):
        """Total number of returned rows
        :rtype: int
        """
        return self._RowsSent

    @RowsSent.setter
    def RowsSent(self, RowsSent):
        self._RowsSent = RowsSent

    @property
    def RowsSentMax(self):
        """Maximum number of returned rows
        :rtype: int
        """
        return self._RowsSentMax

    @RowsSentMax.setter
    def RowsSentMax(self, RowsSentMax):
        self._RowsSentMax = RowsSentMax

    @property
    def RowsSentMin(self):
        """Minimum number of returned rows
        :rtype: int
        """
        return self._RowsSentMin

    @RowsSentMin.setter
    def RowsSentMin(self, RowsSentMin):
        self._RowsSentMin = RowsSentMin

    @property
    def ExecTimes(self):
        """Number of executions
        :rtype: int
        """
        return self._ExecTimes

    @ExecTimes.setter
    def ExecTimes(self, ExecTimes):
        self._ExecTimes = ExecTimes

    @property
    def SqlTemplate(self):
        """SQL template
        :rtype: str
        """
        return self._SqlTemplate

    @SqlTemplate.setter
    def SqlTemplate(self, SqlTemplate):
        self._SqlTemplate = SqlTemplate

    @property
    def SqlText(self):
        """SQL with parameter (random)
        :rtype: str
        """
        return self._SqlText

    @SqlText.setter
    def SqlText(self, SqlText):
        self._SqlText = SqlText

    @property
    def Schema(self):
        """Database name
        :rtype: str
        """
        return self._Schema

    @Schema.setter
    def Schema(self, Schema):
        self._Schema = Schema

    @property
    def QueryTimeRatio(self):
        """Ratio of total duration
        :rtype: float
        """
        return self._QueryTimeRatio

    @QueryTimeRatio.setter
    def QueryTimeRatio(self, QueryTimeRatio):
        self._QueryTimeRatio = QueryTimeRatio

    @property
    def LockTimeRatio(self):
        """Ratio of total SQL lock wait time
        :rtype: float
        """
        return self._LockTimeRatio

    @LockTimeRatio.setter
    def LockTimeRatio(self, LockTimeRatio):
        self._LockTimeRatio = LockTimeRatio

    @property
    def RowsExaminedRatio(self):
        """Ratio of total number of scanned rows
        :rtype: float
        """
        return self._RowsExaminedRatio

    @RowsExaminedRatio.setter
    def RowsExaminedRatio(self, RowsExaminedRatio):
        self._RowsExaminedRatio = RowsExaminedRatio

    @property
    def RowsSentRatio(self):
        """Ratio of total number of returned rows
        :rtype: float
        """
        return self._RowsSentRatio

    @RowsSentRatio.setter
    def RowsSentRatio(self, RowsSentRatio):
        self._RowsSentRatio = RowsSentRatio

    @property
    def QueryTimeAvg(self):
        """Average execution time
        :rtype: float
        """
        return self._QueryTimeAvg

    @QueryTimeAvg.setter
    def QueryTimeAvg(self, QueryTimeAvg):
        self._QueryTimeAvg = QueryTimeAvg

    @property
    def RowsSentAvg(self):
        """Average number of rows returned
        :rtype: float
        """
        return self._RowsSentAvg

    @RowsSentAvg.setter
    def RowsSentAvg(self, RowsSentAvg):
        self._RowsSentAvg = RowsSentAvg

    @property
    def LockTimeAvg(self):
        """Average lock wait time
        :rtype: float
        """
        return self._LockTimeAvg

    @LockTimeAvg.setter
    def LockTimeAvg(self, LockTimeAvg):
        self._LockTimeAvg = LockTimeAvg

    @property
    def RowsExaminedAvg(self):
        """Average number of rows scanned
        :rtype: float
        """
        return self._RowsExaminedAvg

    @RowsExaminedAvg.setter
    def RowsExaminedAvg(self, RowsExaminedAvg):
        self._RowsExaminedAvg = RowsExaminedAvg


    def _deserialize(self, params):
        self._LockTime = params.get("LockTime")
        self._LockTimeMax = params.get("LockTimeMax")
        self._LockTimeMin = params.get("LockTimeMin")
        self._RowsExamined = params.get("RowsExamined")
        self._RowsExaminedMax = params.get("RowsExaminedMax")
        self._RowsExaminedMin = params.get("RowsExaminedMin")
        self._QueryTime = params.get("QueryTime")
        self._QueryTimeMax = params.get("QueryTimeMax")
        self._QueryTimeMin = params.get("QueryTimeMin")
        self._RowsSent = params.get("RowsSent")
        self._RowsSentMax = params.get("RowsSentMax")
        self._RowsSentMin = params.get("RowsSentMin")
        self._ExecTimes = params.get("ExecTimes")
        self._SqlTemplate = params.get("SqlTemplate")
        self._SqlText = params.get("SqlText")
        self._Schema = params.get("Schema")
        self._QueryTimeRatio = params.get("QueryTimeRatio")
        self._LockTimeRatio = params.get("LockTimeRatio")
        self._RowsExaminedRatio = params.get("RowsExaminedRatio")
        self._RowsSentRatio = params.get("RowsSentRatio")
        self._QueryTimeAvg = params.get("QueryTimeAvg")
        self._RowsSentAvg = params.get("RowsSentAvg")
        self._LockTimeAvg = params.get("LockTimeAvg")
        self._RowsExaminedAvg = params.get("RowsExaminedAvg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableSpaceData(AbstractModel):
    """Database table space statistics.

    """

    def __init__(self):
        r"""
        :param _TableName: Table name.
        :type TableName: str
        :param _TableSchema: Database name.
        :type TableSchema: str
        :param _Engine: Database table storage engine.
        :type Engine: str
        :param _DataLength: Data space in MB.
        :type DataLength: float
        :param _IndexLength: Index space in MB.
        :type IndexLength: float
        :param _DataFree: Fragmented space in MB.
        :type DataFree: float
        :param _TotalLength: Total space usage in MB.
        :type TotalLength: float
        :param _FragRatio: Fragmented rate (%).
        :type FragRatio: float
        :param _TableRows: Number of rows.
        :type TableRows: int
        :param _PhysicalFileSize: Size in MB of the physical file exclusive to a table.
        :type PhysicalFileSize: float
        """
        self._TableName = None
        self._TableSchema = None
        self._Engine = None
        self._DataLength = None
        self._IndexLength = None
        self._DataFree = None
        self._TotalLength = None
        self._FragRatio = None
        self._TableRows = None
        self._PhysicalFileSize = None

    @property
    def TableName(self):
        """Table name.
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def TableSchema(self):
        """Database name.
        :rtype: str
        """
        return self._TableSchema

    @TableSchema.setter
    def TableSchema(self, TableSchema):
        self._TableSchema = TableSchema

    @property
    def Engine(self):
        """Database table storage engine.
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def DataLength(self):
        """Data space in MB.
        :rtype: float
        """
        return self._DataLength

    @DataLength.setter
    def DataLength(self, DataLength):
        self._DataLength = DataLength

    @property
    def IndexLength(self):
        """Index space in MB.
        :rtype: float
        """
        return self._IndexLength

    @IndexLength.setter
    def IndexLength(self, IndexLength):
        self._IndexLength = IndexLength

    @property
    def DataFree(self):
        """Fragmented space in MB.
        :rtype: float
        """
        return self._DataFree

    @DataFree.setter
    def DataFree(self, DataFree):
        self._DataFree = DataFree

    @property
    def TotalLength(self):
        """Total space usage in MB.
        :rtype: float
        """
        return self._TotalLength

    @TotalLength.setter
    def TotalLength(self, TotalLength):
        self._TotalLength = TotalLength

    @property
    def FragRatio(self):
        """Fragmented rate (%).
        :rtype: float
        """
        return self._FragRatio

    @FragRatio.setter
    def FragRatio(self, FragRatio):
        self._FragRatio = FragRatio

    @property
    def TableRows(self):
        """Number of rows.
        :rtype: int
        """
        return self._TableRows

    @TableRows.setter
    def TableRows(self, TableRows):
        self._TableRows = TableRows

    @property
    def PhysicalFileSize(self):
        """Size in MB of the physical file exclusive to a table.
        :rtype: float
        """
        return self._PhysicalFileSize

    @PhysicalFileSize.setter
    def PhysicalFileSize(self, PhysicalFileSize):
        self._PhysicalFileSize = PhysicalFileSize


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        self._TableSchema = params.get("TableSchema")
        self._Engine = params.get("Engine")
        self._DataLength = params.get("DataLength")
        self._IndexLength = params.get("IndexLength")
        self._DataFree = params.get("DataFree")
        self._TotalLength = params.get("TotalLength")
        self._FragRatio = params.get("FragRatio")
        self._TableRows = params.get("TableRows")
        self._PhysicalFileSize = params.get("PhysicalFileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableSpaceTimeSeries(AbstractModel):
    """Time series of database table space data

    """

    def __init__(self):
        r"""
        :param _TableName: Table name.
        :type TableName: str
        :param _TableSchema: Database name.
        :type TableSchema: str
        :param _Engine: Database table storage engine.
        :type Engine: str
        :param _SeriesData: Monitoring metric data in a unit of time interval.
        :type SeriesData: :class:`tencentcloud.dbbrain.v20191016.models.MonitorFloatMetricSeriesData`
        """
        self._TableName = None
        self._TableSchema = None
        self._Engine = None
        self._SeriesData = None

    @property
    def TableName(self):
        """Table name.
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def TableSchema(self):
        """Database name.
        :rtype: str
        """
        return self._TableSchema

    @TableSchema.setter
    def TableSchema(self, TableSchema):
        self._TableSchema = TableSchema

    @property
    def Engine(self):
        """Database table storage engine.
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def SeriesData(self):
        """Monitoring metric data in a unit of time interval.
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.MonitorFloatMetricSeriesData`
        """
        return self._SeriesData

    @SeriesData.setter
    def SeriesData(self, SeriesData):
        self._SeriesData = SeriesData


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        self._TableSchema = params.get("TableSchema")
        self._Engine = params.get("Engine")
        if params.get("SeriesData") is not None:
            self._SeriesData = MonitorFloatMetricSeriesData()
            self._SeriesData._deserialize(params.get("SeriesData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeSlice(AbstractModel):
    """Slow log statistics in specified time range

    """

    def __init__(self):
        r"""
        :param _Count: Total number
        :type Count: int
        :param _Timestamp: Statistics start time
        :type Timestamp: int
        """
        self._Count = None
        self._Timestamp = None

    @property
    def Count(self):
        """Total number
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Timestamp(self):
        """Statistics start time
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._Timestamp = params.get("Timestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserProfile(AbstractModel):
    """Information configured by user, including email configuration.

    """

    def __init__(self):
        r"""
        :param _ProfileId: Configured ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ProfileId: str
        :param _ProfileType: Configuration type
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ProfileType: str
        :param _ProfileLevel: Configuration level. Valid values: “User” or “Instance”
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ProfileLevel: str
        :param _ProfileName: Configuration name
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ProfileName: str
        :param _ProfileInfo: Configuration details
        :type ProfileInfo: :class:`tencentcloud.dbbrain.v20191016.models.ProfileInfo`
        """
        self._ProfileId = None
        self._ProfileType = None
        self._ProfileLevel = None
        self._ProfileName = None
        self._ProfileInfo = None

    @property
    def ProfileId(self):
        """Configured ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProfileId

    @ProfileId.setter
    def ProfileId(self, ProfileId):
        self._ProfileId = ProfileId

    @property
    def ProfileType(self):
        """Configuration type
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProfileType

    @ProfileType.setter
    def ProfileType(self, ProfileType):
        self._ProfileType = ProfileType

    @property
    def ProfileLevel(self):
        """Configuration level. Valid values: “User” or “Instance”
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProfileLevel

    @ProfileLevel.setter
    def ProfileLevel(self, ProfileLevel):
        self._ProfileLevel = ProfileLevel

    @property
    def ProfileName(self):
        """Configuration name
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProfileName

    @ProfileName.setter
    def ProfileName(self, ProfileName):
        self._ProfileName = ProfileName

    @property
    def ProfileInfo(self):
        """Configuration details
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.ProfileInfo`
        """
        return self._ProfileInfo

    @ProfileInfo.setter
    def ProfileInfo(self, ProfileInfo):
        self._ProfileInfo = ProfileInfo


    def _deserialize(self, params):
        self._ProfileId = params.get("ProfileId")
        self._ProfileType = params.get("ProfileType")
        self._ProfileLevel = params.get("ProfileLevel")
        self._ProfileName = params.get("ProfileName")
        if params.get("ProfileInfo") is not None:
            self._ProfileInfo = ProfileInfo()
            self._ProfileInfo._deserialize(params.get("ProfileInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        