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


class Account(AbstractModel):
    """TencentDB account information

    """

    def __init__(self):
        r"""
        :param _User: Account name
        :type User: str
        :param _Host: Host address
        :type Host: str
        """
        self._User = None
        self._Host = None

    @property
    def User(self):
        """Account name
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Host(self):
        """Host address
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host


    def _deserialize(self, params):
        self._User = params.get("User")
        self._Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _Product: Database engine name. Valid value: `mariadb`.
        :type Product: str
        :param _SecurityGroupId: ID of the security group to be associated in the format of sg-efil73jd.
        :type SecurityGroupId: str
        :param _InstanceIds: ID(s) of the instance(s) to be associated in the format of tdsql-lesecurk. You can specify multiple instances.
        :type InstanceIds: list of str
        """
        self._Product = None
        self._SecurityGroupId = None
        self._InstanceIds = None

    @property
    def Product(self):
        """Database engine name. Valid value: `mariadb`.
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def SecurityGroupId(self):
        """ID of the security group to be associated in the format of sg-efil73jd.
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def InstanceIds(self):
        """ID(s) of the instance(s) to be associated in the format of tdsql-lesecurk. You can specify multiple instances.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsResponse(AbstractModel):
    """AssociateSecurityGroups response structure.

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


class CancelDcnJobRequest(AbstractModel):
    """CancelDcnJob request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Disaster recovery instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Disaster recovery instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelDcnJobResponse(AbstractModel):
    """CancelDcnJob response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task ID
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Task ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CloneAccountRequest(AbstractModel):
    """CloneAccount request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _SrcUser: Source user account name
        :type SrcUser: str
        :param _SrcHost: Source user host
        :type SrcHost: str
        :param _DstUser: Target user account name
        :type DstUser: str
        :param _DstHost: Target user host
        :type DstHost: str
        :param _DstDesc: Target account description
        :type DstDesc: str
        """
        self._InstanceId = None
        self._SrcUser = None
        self._SrcHost = None
        self._DstUser = None
        self._DstHost = None
        self._DstDesc = None

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
    def SrcUser(self):
        """Source user account name
        :rtype: str
        """
        return self._SrcUser

    @SrcUser.setter
    def SrcUser(self, SrcUser):
        self._SrcUser = SrcUser

    @property
    def SrcHost(self):
        """Source user host
        :rtype: str
        """
        return self._SrcHost

    @SrcHost.setter
    def SrcHost(self, SrcHost):
        self._SrcHost = SrcHost

    @property
    def DstUser(self):
        """Target user account name
        :rtype: str
        """
        return self._DstUser

    @DstUser.setter
    def DstUser(self, DstUser):
        self._DstUser = DstUser

    @property
    def DstHost(self):
        """Target user host
        :rtype: str
        """
        return self._DstHost

    @DstHost.setter
    def DstHost(self, DstHost):
        self._DstHost = DstHost

    @property
    def DstDesc(self):
        """Target account description
        :rtype: str
        """
        return self._DstDesc

    @DstDesc.setter
    def DstDesc(self, DstDesc):
        self._DstDesc = DstDesc


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SrcUser = params.get("SrcUser")
        self._SrcHost = params.get("SrcHost")
        self._DstUser = params.get("DstUser")
        self._DstHost = params.get("DstHost")
        self._DstDesc = params.get("DstDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneAccountResponse(AbstractModel):
    """CloneAccount response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task flow ID.
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Async task flow ID.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CloseDBExtranetAccessRequest(AbstractModel):
    """CloseDBExtranetAccess request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of instance for which to disable public network access. The ID is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :type InstanceId: str
        :param _Ipv6Flag: Whether IPv6 is used. Default value: 0
        :type Ipv6Flag: int
        """
        self._InstanceId = None
        self._Ipv6Flag = None

    @property
    def InstanceId(self):
        """ID of instance for which to disable public network access. The ID is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ipv6Flag(self):
        """Whether IPv6 is used. Default value: 0
        :rtype: int
        """
        return self._Ipv6Flag

    @Ipv6Flag.setter
    def Ipv6Flag(self, Ipv6Flag):
        self._Ipv6Flag = Ipv6Flag


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Ipv6Flag = params.get("Ipv6Flag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseDBExtranetAccessResponse(AbstractModel):
    """CloseDBExtranetAccess response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task ID. The task status can be queried through the `DescribeFlow` API.
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Async task ID. The task status can be queried through the `DescribeFlow` API.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ColumnPrivilege(AbstractModel):
    """Column permission information

    """

    def __init__(self):
        r"""
        :param _Database: Database name
        :type Database: str
        :param _Table: Table name
        :type Table: str
        :param _Column: Column name
        :type Column: str
        :param _Privileges: Permission information
        :type Privileges: list of str
        """
        self._Database = None
        self._Table = None
        self._Column = None
        self._Privileges = None

    @property
    def Database(self):
        """Database name
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        """Table name
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Column(self):
        """Column name
        :rtype: str
        """
        return self._Column

    @Column.setter
    def Column(self, Column):
        self._Column = Column

    @property
    def Privileges(self):
        """Permission information
        :rtype: list of str
        """
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Table = params.get("Table")
        self._Column = params.get("Column")
        self._Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConstraintRange(AbstractModel):
    """Range of constraint type values

    """

    def __init__(self):
        r"""
        :param _Min: Minimum value when the constraint type is `section`
        :type Min: str
        :param _Max: Maximum value when the constraint type is `section`
        :type Max: str
        """
        self._Min = None
        self._Max = None

    @property
    def Min(self):
        """Minimum value when the constraint type is `section`
        :rtype: str
        """
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def Max(self):
        """Maximum value when the constraint type is `section`
        :rtype: str
        """
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max


    def _deserialize(self, params):
        self._Min = params.get("Min")
        self._Max = params.get("Max")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyAccountPrivilegesRequest(AbstractModel):
    """CopyAccountPrivileges request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :type InstanceId: str
        :param _SrcUserName: Source username
        :type SrcUserName: str
        :param _SrcHost: Access host allowed for source user
        :type SrcHost: str
        :param _DstUserName: Target username
        :type DstUserName: str
        :param _DstHost: Access host allowed for target user
        :type DstHost: str
        :param _SrcReadOnly: `ReadOnly` attribute of source account
        :type SrcReadOnly: str
        :param _DstReadOnly: `ReadOnly` attribute of target account
        :type DstReadOnly: str
        """
        self._InstanceId = None
        self._SrcUserName = None
        self._SrcHost = None
        self._DstUserName = None
        self._DstHost = None
        self._SrcReadOnly = None
        self._DstReadOnly = None

    @property
    def InstanceId(self):
        """Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SrcUserName(self):
        """Source username
        :rtype: str
        """
        return self._SrcUserName

    @SrcUserName.setter
    def SrcUserName(self, SrcUserName):
        self._SrcUserName = SrcUserName

    @property
    def SrcHost(self):
        """Access host allowed for source user
        :rtype: str
        """
        return self._SrcHost

    @SrcHost.setter
    def SrcHost(self, SrcHost):
        self._SrcHost = SrcHost

    @property
    def DstUserName(self):
        """Target username
        :rtype: str
        """
        return self._DstUserName

    @DstUserName.setter
    def DstUserName(self, DstUserName):
        self._DstUserName = DstUserName

    @property
    def DstHost(self):
        """Access host allowed for target user
        :rtype: str
        """
        return self._DstHost

    @DstHost.setter
    def DstHost(self, DstHost):
        self._DstHost = DstHost

    @property
    def SrcReadOnly(self):
        """`ReadOnly` attribute of source account
        :rtype: str
        """
        return self._SrcReadOnly

    @SrcReadOnly.setter
    def SrcReadOnly(self, SrcReadOnly):
        self._SrcReadOnly = SrcReadOnly

    @property
    def DstReadOnly(self):
        """`ReadOnly` attribute of target account
        :rtype: str
        """
        return self._DstReadOnly

    @DstReadOnly.setter
    def DstReadOnly(self, DstReadOnly):
        self._DstReadOnly = DstReadOnly


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SrcUserName = params.get("SrcUserName")
        self._SrcHost = params.get("SrcHost")
        self._DstUserName = params.get("DstUserName")
        self._DstHost = params.get("DstHost")
        self._SrcReadOnly = params.get("SrcReadOnly")
        self._DstReadOnly = params.get("DstReadOnly")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyAccountPrivilegesResponse(AbstractModel):
    """CopyAccountPrivileges response structure.

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


class CreateAccountRequest(AbstractModel):
    """CreateAccount request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :type InstanceId: str
        :param _UserName: Login username, which can contain 1-32 letters, digits, underscores, and hyphens.
        :type UserName: str
        :param _Host: Host that can be logged in to, which is in the same format as the host of the MySQL account and supports wildcards, such as %, 10.%, and 10.20.%.
        :type Host: str
        :param _Password: Account password. It must contain 8-32 characters in all of the following four types: lowercase letters, uppercase letters, digits, and symbols (()~!@#$%^&*-+=_|{}[]:<>,.?/), and cannot start with a slash (/).
        :type Password: str
        :param _ReadOnly: Whether to create a read-only account. 0: no; 1: for the account's SQL requests, the secondary will be used first, and if it is unavailable, the primary will be used; 2: the secondary will be used first, and if it is unavailable, the operation will fail.
        :type ReadOnly: int
        :param _Description: Account remarks, which can contain 0-256 letters, digits, and common symbols.
        :type Description: str
        :param _DelayThresh: Determines whether the secondary is unavailable based on the passed-in time
        :type DelayThresh: int
        :param _SlaveConst: Whether to specify a replica server for read-only account. Valid values: `0` (No replica server is specified, which means that the proxy will select another available replica server to keep connection with the client if the current replica server doesn’t meet the requirement). `1` (The replica server is specified, which means that the connection will be disconnected if the specified replica server doesn’t meet the requirement.)
        :type SlaveConst: int
        :param _MaxUserConnections: Maximum number of connections. If left empty or `0` is passed in, the connections will be unlimited. This parameter configuration is not supported for kernel version 10.1.
        :type MaxUserConnections: int
        """
        self._InstanceId = None
        self._UserName = None
        self._Host = None
        self._Password = None
        self._ReadOnly = None
        self._Description = None
        self._DelayThresh = None
        self._SlaveConst = None
        self._MaxUserConnections = None

    @property
    def InstanceId(self):
        """Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        """Login username, which can contain 1-32 letters, digits, underscores, and hyphens.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        """Host that can be logged in to, which is in the same format as the host of the MySQL account and supports wildcards, such as %, 10.%, and 10.20.%.
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Password(self):
        """Account password. It must contain 8-32 characters in all of the following four types: lowercase letters, uppercase letters, digits, and symbols (()~!@#$%^&*-+=_|{}[]:<>,.?/), and cannot start with a slash (/).
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ReadOnly(self):
        """Whether to create a read-only account. 0: no; 1: for the account's SQL requests, the secondary will be used first, and if it is unavailable, the primary will be used; 2: the secondary will be used first, and if it is unavailable, the operation will fail.
        :rtype: int
        """
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly

    @property
    def Description(self):
        """Account remarks, which can contain 0-256 letters, digits, and common symbols.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DelayThresh(self):
        """Determines whether the secondary is unavailable based on the passed-in time
        :rtype: int
        """
        return self._DelayThresh

    @DelayThresh.setter
    def DelayThresh(self, DelayThresh):
        self._DelayThresh = DelayThresh

    @property
    def SlaveConst(self):
        """Whether to specify a replica server for read-only account. Valid values: `0` (No replica server is specified, which means that the proxy will select another available replica server to keep connection with the client if the current replica server doesn’t meet the requirement). `1` (The replica server is specified, which means that the connection will be disconnected if the specified replica server doesn’t meet the requirement.)
        :rtype: int
        """
        return self._SlaveConst

    @SlaveConst.setter
    def SlaveConst(self, SlaveConst):
        self._SlaveConst = SlaveConst

    @property
    def MaxUserConnections(self):
        """Maximum number of connections. If left empty or `0` is passed in, the connections will be unlimited. This parameter configuration is not supported for kernel version 10.1.
        :rtype: int
        """
        return self._MaxUserConnections

    @MaxUserConnections.setter
    def MaxUserConnections(self, MaxUserConnections):
        self._MaxUserConnections = MaxUserConnections


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        self._Password = params.get("Password")
        self._ReadOnly = params.get("ReadOnly")
        self._Description = params.get("Description")
        self._DelayThresh = params.get("DelayThresh")
        self._SlaveConst = params.get("SlaveConst")
        self._MaxUserConnections = params.get("MaxUserConnections")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountResponse(AbstractModel):
    """CreateAccount response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, which is passed through from the input parameters.
        :type InstanceId: str
        :param _UserName: Username, which is passed through from the input parameters.
        :type UserName: str
        :param _Host: Host allowed for access, which is passed through from the input parameters.
        :type Host: str
        :param _ReadOnly: Passed through from the input parameters.
        :type ReadOnly: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._UserName = None
        self._Host = None
        self._ReadOnly = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """Instance ID, which is passed through from the input parameters.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        """Username, which is passed through from the input parameters.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        """Host allowed for access, which is passed through from the input parameters.
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def ReadOnly(self):
        """Passed through from the input parameters.
        :rtype: int
        """
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly

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
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        self._ReadOnly = params.get("ReadOnly")
        self._RequestId = params.get("RequestId")


class CreateDBInstanceRequest(AbstractModel):
    """CreateDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _Zones: AZs to deploy instance nodes. You can specify up to two AZs (one as primary AZ and another as replica AZ). When the shard specification is 1-primary-2-replica, the primary and one of the replicas are deployed in the primary AZ.
        :type Zones: list of str
        :param _NodeCount: Number of nodes, which can be obtained 
 by querying the instance specification through the `DescribeDBInstanceSpecs` API.
        :type NodeCount: int
        :param _Memory: Memory size in GB, which can be obtained 
 by querying the instance specification through the `DescribeDBInstanceSpecs` API.
        :type Memory: int
        :param _Storage: Storage capacity in GB. The maximum and minimum storage space can be obtained 
 by querying instance specification through the `DescribeDBInstanceSpecs` API.
        :type Storage: int
        :param _Period: Validity period in months
        :type Period: int
        :param _Count: The number of instances to be purchased. Only one instance is queried for price by default.
        :type Count: int
        :param _AutoVoucher: Whether to automatically use vouchers. This option is disabled by default.
        :type AutoVoucher: bool
        :param _VoucherIds: Voucher ID list. Currently, you can specify only one voucher.
        :type VoucherIds: list of str
        :param _VpcId: VPC ID. If this parameter is not passed in, the instance will be created on the classic network.
        :type VpcId: str
        :param _SubnetId: VPC subnet ID, which is required when `VpcId` is specified.
        :type SubnetId: str
        :param _ProjectId: Project ID, which can be obtained through the `DescribeProjects` API. If this parameter is not passed in, the instance will be associated with the default project.
        :type ProjectId: int
        :param _DbVersionId: Database engine version. Valid values: `5.7`, `8.0`, `10.0`, `10.1`.
        :type DbVersionId: str
        :param _InstanceName: Name of the instance, which can be customized.
        :type InstanceName: str
        :param _SecurityGroupIds: List of security group IDs
        :type SecurityGroupIds: list of str
        :param _AutoRenewFlag: Auto-renewal flag. Valid values: `1` (auto-renewal), `2` (no renewal upon expiration).
        :type AutoRenewFlag: int
        :param _Ipv6Flag: Whether IPv6 is supported. Valid values: `0` (unsupported), `1` (supported).
        :type Ipv6Flag: int
        :param _ResourceTags: Array of tag key-value pairs
        :type ResourceTags: list of ResourceTag
        :param _InitParams: List of parameters. Valid values: `character_set_server` (character set; required); `lower_case_table_names` (table name case sensitivity; required; `0`: case-sensitive; `1`: case-insensitive); `innodb_page_size` (InnoDB data page size; default size: 16 KB); `sync_mode` (sync mode; `0`: async; `1`: strong sync; `2`: downgradable strong sync; default value: `2`).
        :type InitParams: list of DBParamValue
        :param _DcnRegion: DCN source region
        :type DcnRegion: str
        :param _DcnInstanceId: DCN source instance ID
        :type DcnInstanceId: str
        """
        self._Zones = None
        self._NodeCount = None
        self._Memory = None
        self._Storage = None
        self._Period = None
        self._Count = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._VpcId = None
        self._SubnetId = None
        self._ProjectId = None
        self._DbVersionId = None
        self._InstanceName = None
        self._SecurityGroupIds = None
        self._AutoRenewFlag = None
        self._Ipv6Flag = None
        self._ResourceTags = None
        self._InitParams = None
        self._DcnRegion = None
        self._DcnInstanceId = None

    @property
    def Zones(self):
        """AZs to deploy instance nodes. You can specify up to two AZs (one as primary AZ and another as replica AZ). When the shard specification is 1-primary-2-replica, the primary and one of the replicas are deployed in the primary AZ.
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def NodeCount(self):
        """Number of nodes, which can be obtained 
 by querying the instance specification through the `DescribeDBInstanceSpecs` API.
        :rtype: int
        """
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def Memory(self):
        """Memory size in GB, which can be obtained 
 by querying the instance specification through the `DescribeDBInstanceSpecs` API.
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        """Storage capacity in GB. The maximum and minimum storage space can be obtained 
 by querying instance specification through the `DescribeDBInstanceSpecs` API.
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def Period(self):
        """Validity period in months
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Count(self):
        """The number of instances to be purchased. Only one instance is queried for price by default.
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def AutoVoucher(self):
        """Whether to automatically use vouchers. This option is disabled by default.
        :rtype: bool
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        """Voucher ID list. Currently, you can specify only one voucher.
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def VpcId(self):
        """VPC ID. If this parameter is not passed in, the instance will be created on the classic network.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """VPC subnet ID, which is required when `VpcId` is specified.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ProjectId(self):
        """Project ID, which can be obtained through the `DescribeProjects` API. If this parameter is not passed in, the instance will be associated with the default project.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DbVersionId(self):
        """Database engine version. Valid values: `5.7`, `8.0`, `10.0`, `10.1`.
        :rtype: str
        """
        return self._DbVersionId

    @DbVersionId.setter
    def DbVersionId(self, DbVersionId):
        self._DbVersionId = DbVersionId

    @property
    def InstanceName(self):
        """Name of the instance, which can be customized.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def SecurityGroupIds(self):
        """List of security group IDs
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def AutoRenewFlag(self):
        """Auto-renewal flag. Valid values: `1` (auto-renewal), `2` (no renewal upon expiration).
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def Ipv6Flag(self):
        """Whether IPv6 is supported. Valid values: `0` (unsupported), `1` (supported).
        :rtype: int
        """
        return self._Ipv6Flag

    @Ipv6Flag.setter
    def Ipv6Flag(self, Ipv6Flag):
        self._Ipv6Flag = Ipv6Flag

    @property
    def ResourceTags(self):
        """Array of tag key-value pairs
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def InitParams(self):
        """List of parameters. Valid values: `character_set_server` (character set; required); `lower_case_table_names` (table name case sensitivity; required; `0`: case-sensitive; `1`: case-insensitive); `innodb_page_size` (InnoDB data page size; default size: 16 KB); `sync_mode` (sync mode; `0`: async; `1`: strong sync; `2`: downgradable strong sync; default value: `2`).
        :rtype: list of DBParamValue
        """
        return self._InitParams

    @InitParams.setter
    def InitParams(self, InitParams):
        self._InitParams = InitParams

    @property
    def DcnRegion(self):
        """DCN source region
        :rtype: str
        """
        return self._DcnRegion

    @DcnRegion.setter
    def DcnRegion(self, DcnRegion):
        self._DcnRegion = DcnRegion

    @property
    def DcnInstanceId(self):
        """DCN source instance ID
        :rtype: str
        """
        return self._DcnInstanceId

    @DcnInstanceId.setter
    def DcnInstanceId(self, DcnInstanceId):
        self._DcnInstanceId = DcnInstanceId


    def _deserialize(self, params):
        self._Zones = params.get("Zones")
        self._NodeCount = params.get("NodeCount")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._Period = params.get("Period")
        self._Count = params.get("Count")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._ProjectId = params.get("ProjectId")
        self._DbVersionId = params.get("DbVersionId")
        self._InstanceName = params.get("InstanceName")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._Ipv6Flag = params.get("Ipv6Flag")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        if params.get("InitParams") is not None:
            self._InitParams = []
            for item in params.get("InitParams"):
                obj = DBParamValue()
                obj._deserialize(item)
                self._InitParams.append(obj)
        self._DcnRegion = params.get("DcnRegion")
        self._DcnInstanceId = params.get("DcnInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBInstanceResponse(AbstractModel):
    """CreateDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _DealName: Order ID, which is used for calling the `DescribeOrders` API.
 The parameter can be used to either query order details or call the user account APIs to make another payment when this payment fails.
        :type DealName: str
        :param _InstanceIds: IDs of the instances you have purchased in this order. If no instance IDs are returned, you can query them with the `DescribeOrders` API. You can also use the `DescribeDBInstances` API to check whether an instance has been created successfully.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealName = None
        self._InstanceIds = None
        self._RequestId = None

    @property
    def DealName(self):
        """Order ID, which is used for calling the `DescribeOrders` API.
 The parameter can be used to either query order details or call the user account APIs to make another payment when this payment fails.
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def InstanceIds(self):
        """IDs of the instances you have purchased in this order. If no instance IDs are returned, you can query them with the `DescribeOrders` API. You can also use the `DescribeDBInstances` API to check whether an instance has been created successfully.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

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
        self._DealName = params.get("DealName")
        self._InstanceIds = params.get("InstanceIds")
        self._RequestId = params.get("RequestId")


class CreateHourDBInstanceRequest(AbstractModel):
    """CreateHourDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _Zones: AZs to deploy instance nodes. You can specify up to two AZs.
        :type Zones: list of str
        :param _NodeCount: Number of nodes.
        :type NodeCount: int
        :param _Memory: Memory size in GB.
        :type Memory: int
        :param _Storage: Storage size in GB.
        :type Storage: int
        :param _Count: Number of instances to purchase.
        :type Count: int
        :param _ProjectId: Project ID. If this parameter is not passed in, the default project will be used.
        :type ProjectId: int
        :param _VpcId: Unique ID of the network. If this parameter is not passed in, the classic network will be used.
        :type VpcId: str
        :param _SubnetId: Unique ID of the subnet. If `VpcId` is specified, this parameter is required.
        :type SubnetId: str
        :param _DbVersionId: Database engine version. Valid values: `5.7`, `8.0`, `10.0`, `10.1`.
        :type DbVersionId: str
        :param _InstanceName: Custom name of the instance.
        :type InstanceName: str
        :param _SecurityGroupIds: Security group ID. If this parameter is not passed in, no security groups will be associated when the instance is created.
        :type SecurityGroupIds: list of str
        :param _Ipv6Flag: Whether IPv6 is supported. Valid values: `0` (unsupported), `1` (supported).
        :type Ipv6Flag: int
        :param _ResourceTags: Array of tag key-value pairs.
        :type ResourceTags: list of ResourceTag
        :param _DcnRegion: If you create a disaster recovery instance, you need to use this parameter to specify the region of the associated primary instance so that the disaster recovery instance can sync data with the primary instance over the Data Communication Network (DCN).
        :type DcnRegion: str
        :param _DcnInstanceId: If you create a disaster recovery instance, you need to use this parameter to specify the ID of the associated primary instance so that the disaster recovery instance can sync data with the primary instance over the Data Communication Network (DCN).
        :type DcnInstanceId: str
        :param _InitParams: List of parameters. Valid values: 
`character_set_server` (character set; required); `lower_case_table_names` (table name case sensitivity; required; 0: case-sensitive; 1: case-insensitive);
`innodb_page_size` (innoDB data page size; default size: 16 KB); `sync_mode` (sync mode; 0: async; 1: strong sync; 2: downgradable strong sync; default value: 2).
        :type InitParams: list of DBParamValue
        :param _RollbackInstanceId: ID of the instance to be rolled back, such as “2021-11-22 00:00:00”.
        :type RollbackInstanceId: str
        :param _RollbackTime: Rollback time.
        :type RollbackTime: str
        """
        self._Zones = None
        self._NodeCount = None
        self._Memory = None
        self._Storage = None
        self._Count = None
        self._ProjectId = None
        self._VpcId = None
        self._SubnetId = None
        self._DbVersionId = None
        self._InstanceName = None
        self._SecurityGroupIds = None
        self._Ipv6Flag = None
        self._ResourceTags = None
        self._DcnRegion = None
        self._DcnInstanceId = None
        self._InitParams = None
        self._RollbackInstanceId = None
        self._RollbackTime = None

    @property
    def Zones(self):
        """AZs to deploy instance nodes. You can specify up to two AZs.
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def NodeCount(self):
        """Number of nodes.
        :rtype: int
        """
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def Memory(self):
        """Memory size in GB.
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        """Storage size in GB.
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def Count(self):
        """Number of instances to purchase.
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def ProjectId(self):
        """Project ID. If this parameter is not passed in, the default project will be used.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def VpcId(self):
        """Unique ID of the network. If this parameter is not passed in, the classic network will be used.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Unique ID of the subnet. If `VpcId` is specified, this parameter is required.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def DbVersionId(self):
        """Database engine version. Valid values: `5.7`, `8.0`, `10.0`, `10.1`.
        :rtype: str
        """
        return self._DbVersionId

    @DbVersionId.setter
    def DbVersionId(self, DbVersionId):
        self._DbVersionId = DbVersionId

    @property
    def InstanceName(self):
        """Custom name of the instance.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def SecurityGroupIds(self):
        """Security group ID. If this parameter is not passed in, no security groups will be associated when the instance is created.
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def Ipv6Flag(self):
        """Whether IPv6 is supported. Valid values: `0` (unsupported), `1` (supported).
        :rtype: int
        """
        return self._Ipv6Flag

    @Ipv6Flag.setter
    def Ipv6Flag(self, Ipv6Flag):
        self._Ipv6Flag = Ipv6Flag

    @property
    def ResourceTags(self):
        """Array of tag key-value pairs.
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def DcnRegion(self):
        """If you create a disaster recovery instance, you need to use this parameter to specify the region of the associated primary instance so that the disaster recovery instance can sync data with the primary instance over the Data Communication Network (DCN).
        :rtype: str
        """
        return self._DcnRegion

    @DcnRegion.setter
    def DcnRegion(self, DcnRegion):
        self._DcnRegion = DcnRegion

    @property
    def DcnInstanceId(self):
        """If you create a disaster recovery instance, you need to use this parameter to specify the ID of the associated primary instance so that the disaster recovery instance can sync data with the primary instance over the Data Communication Network (DCN).
        :rtype: str
        """
        return self._DcnInstanceId

    @DcnInstanceId.setter
    def DcnInstanceId(self, DcnInstanceId):
        self._DcnInstanceId = DcnInstanceId

    @property
    def InitParams(self):
        """List of parameters. Valid values: 
`character_set_server` (character set; required); `lower_case_table_names` (table name case sensitivity; required; 0: case-sensitive; 1: case-insensitive);
`innodb_page_size` (innoDB data page size; default size: 16 KB); `sync_mode` (sync mode; 0: async; 1: strong sync; 2: downgradable strong sync; default value: 2).
        :rtype: list of DBParamValue
        """
        return self._InitParams

    @InitParams.setter
    def InitParams(self, InitParams):
        self._InitParams = InitParams

    @property
    def RollbackInstanceId(self):
        """ID of the instance to be rolled back, such as “2021-11-22 00:00:00”.
        :rtype: str
        """
        return self._RollbackInstanceId

    @RollbackInstanceId.setter
    def RollbackInstanceId(self, RollbackInstanceId):
        self._RollbackInstanceId = RollbackInstanceId

    @property
    def RollbackTime(self):
        """Rollback time.
        :rtype: str
        """
        return self._RollbackTime

    @RollbackTime.setter
    def RollbackTime(self, RollbackTime):
        self._RollbackTime = RollbackTime


    def _deserialize(self, params):
        self._Zones = params.get("Zones")
        self._NodeCount = params.get("NodeCount")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._Count = params.get("Count")
        self._ProjectId = params.get("ProjectId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._DbVersionId = params.get("DbVersionId")
        self._InstanceName = params.get("InstanceName")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._Ipv6Flag = params.get("Ipv6Flag")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._DcnRegion = params.get("DcnRegion")
        self._DcnInstanceId = params.get("DcnInstanceId")
        if params.get("InitParams") is not None:
            self._InitParams = []
            for item in params.get("InitParams"):
                obj = DBParamValue()
                obj._deserialize(item)
                self._InitParams.append(obj)
        self._RollbackInstanceId = params.get("RollbackInstanceId")
        self._RollbackTime = params.get("RollbackTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHourDBInstanceResponse(AbstractModel):
    """CreateHourDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _DealName: Order ID, which is used for calling the `DescribeOrders` API.
 The parameter can be used to either query order details or call the user account APIs to make another payment when this payment fails.
        :type DealName: str
        :param _InstanceIds: IDs of the instances you have purchased in this order. If no instance IDs are returned, you can query them with the `DescribeOrders` API. You can also use the `DescribeDBInstances` API to check whether an instance has been created successfully.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type InstanceIds: list of str
        :param _FlowId: Async task ID, which can be used in the [DescribeFlow](https://www.tencentcloud.com/document/product/237/16177) API to query the async task result.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealName = None
        self._InstanceIds = None
        self._FlowId = None
        self._RequestId = None

    @property
    def DealName(self):
        """Order ID, which is used for calling the `DescribeOrders` API.
 The parameter can be used to either query order details or call the user account APIs to make another payment when this payment fails.
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def InstanceIds(self):
        """IDs of the instances you have purchased in this order. If no instance IDs are returned, you can query them with the `DescribeOrders` API. You can also use the `DescribeDBInstances` API to check whether an instance has been created successfully.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def FlowId(self):
        """Async task ID, which can be used in the [DescribeFlow](https://www.tencentcloud.com/document/product/237/16177) API to query the async task result.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._DealName = params.get("DealName")
        self._InstanceIds = params.get("InstanceIds")
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class DBAccount(AbstractModel):
    """TencentDB account information

    """

    def __init__(self):
        r"""
        :param _UserName: Username
        :type UserName: str
        :param _Host: Host from which a user can log in (corresponding to the `host` field for a MySQL user; a user is uniquely identified by username and host; this parameter is in IP format and ends with % for IP range; % can be entered; if this parameter is left empty, % will be used by default).
        :type Host: str
        :param _Description: User remarks
        :type Description: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _UpdateTime: Last updated time
        :type UpdateTime: str
        :param _ReadOnly: Read-only flag. 0: no; 1: for the account's SQL requests, the replica will be used first, and if it is unavailable, the primary will be used; 2: the replica will be used first, and if it is unavailable, the operation will fail.
        :type ReadOnly: int
        :param _DelayThresh: This field is meaningful for read-only accounts, indicating that a replica should be selected if its delay from the primary is less than this value.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DelayThresh: int
        :param _SlaveConst: Whether to specify a replica server for read-only account. Valid values: `0` (No replica server is specified, which means that the proxy will select another available replica server to keep connection with the client if the current replica server doesn’t meet the requirement). `1` (The replica server is specified, which means that the connection will be disconnected if the specified replica server doesn’t meet the requirement.)
        :type SlaveConst: int
        :param _MaxUserConnections: Maximum number of connections. `0` indicates no limit.
        :type MaxUserConnections: int
        """
        self._UserName = None
        self._Host = None
        self._Description = None
        self._CreateTime = None
        self._UpdateTime = None
        self._ReadOnly = None
        self._DelayThresh = None
        self._SlaveConst = None
        self._MaxUserConnections = None

    @property
    def UserName(self):
        """Username
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        """Host from which a user can log in (corresponding to the `host` field for a MySQL user; a user is uniquely identified by username and host; this parameter is in IP format and ends with % for IP range; % can be entered; if this parameter is left empty, % will be used by default).
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Description(self):
        """User remarks
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        """Creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """Last updated time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ReadOnly(self):
        """Read-only flag. 0: no; 1: for the account's SQL requests, the replica will be used first, and if it is unavailable, the primary will be used; 2: the replica will be used first, and if it is unavailable, the operation will fail.
        :rtype: int
        """
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly

    @property
    def DelayThresh(self):
        """This field is meaningful for read-only accounts, indicating that a replica should be selected if its delay from the primary is less than this value.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DelayThresh

    @DelayThresh.setter
    def DelayThresh(self, DelayThresh):
        self._DelayThresh = DelayThresh

    @property
    def SlaveConst(self):
        """Whether to specify a replica server for read-only account. Valid values: `0` (No replica server is specified, which means that the proxy will select another available replica server to keep connection with the client if the current replica server doesn’t meet the requirement). `1` (The replica server is specified, which means that the connection will be disconnected if the specified replica server doesn’t meet the requirement.)
        :rtype: int
        """
        return self._SlaveConst

    @SlaveConst.setter
    def SlaveConst(self, SlaveConst):
        self._SlaveConst = SlaveConst

    @property
    def MaxUserConnections(self):
        """Maximum number of connections. `0` indicates no limit.
        :rtype: int
        """
        return self._MaxUserConnections

    @MaxUserConnections.setter
    def MaxUserConnections(self, MaxUserConnections):
        self._MaxUserConnections = MaxUserConnections


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._ReadOnly = params.get("ReadOnly")
        self._DelayThresh = params.get("DelayThresh")
        self._SlaveConst = params.get("SlaveConst")
        self._MaxUserConnections = params.get("MaxUserConnections")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBInstance(AbstractModel):
    """TencentDB instance details.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, which uniquely identifies a TDSQL instance
        :type InstanceId: str
        :param _InstanceName: Customizable instance name
        :type InstanceName: str
        :param _AppId: Application ID of instance
        :type AppId: int
        :param _ProjectId: Project ID of instance
        :type ProjectId: int
        :param _Region: Instance region name, such as ap-shanghai
        :type Region: str
        :param _Zone: Instance AZ name, such as ap-guangzhou-1
        :type Zone: str
        :param _VpcId: VPC ID, which is 0 if the basic network is used
        :type VpcId: int
        :param _SubnetId: Subnet ID, which is 0 if the basic network is used
        :type SubnetId: int
        :param _Status: Instance status. Valid values: `0` (creating), `1` (running task), `2` (running), `3` (uninitialized), `-1` (isolated), `4` (initializing), `5` (eliminating), `6` (restarting), `7` (migrating data)
        :type Status: int
        :param _Vip: Private IP address
        :type Vip: str
        :param _Vport: Private network port
        :type Vport: int
        :param _WanDomain: Domain name for public network access, which can be resolved by the public network
        :type WanDomain: str
        :param _WanVip: Public IP address, which can be accessed over the public network
        :type WanVip: str
        :param _WanPort: Public network port
        :type WanPort: int
        :param _CreateTime: Instance creation time in the format of `2006-01-02 15:04:05`
        :type CreateTime: str
        :param _UpdateTime: Last updated time of instance in the format of `2006-01-02 15:04:05`
        :type UpdateTime: str
        :param _AutoRenewFlag: Auto-renewal flag. 0: no, 1: yes
        :type AutoRenewFlag: int
        :param _PeriodEndTime: Instance expiration time in the format of `2006-01-02 15:04:05`
        :type PeriodEndTime: str
        :param _Uin: Instance account
        :type Uin: str
        :param _TdsqlVersion: TDSQL version information
        :type TdsqlVersion: str
        :param _Memory: Instance memory size in GB
        :type Memory: int
        :param _Storage: Instance storage capacity in GB
        :type Storage: int
        :param _UniqueVpcId: VPC ID in string type
        :type UniqueVpcId: str
        :param _UniqueSubnetId: VPC subnet ID in string type
        :type UniqueSubnetId: str
        :param _OriginSerialId: Original ID of instance (this field is obsolete and should not be depended on)
        :type OriginSerialId: str
        :param _NodeCount: Number of nodes. 2: one master and one slave, 3: one master and two slaves
        :type NodeCount: int
        :param _IsTmp: Whether it is a temp instance. 0: no, non-zero value: yes
        :type IsTmp: int
        :param _ExclusterId: Dedicated cluster ID. If this parameter is empty, the instance is a general instance
        :type ExclusterId: str
        :param _Id: Numeric ID of instance (this field is obsolete and should not be depended on)
        :type Id: int
        :param _Pid: Product type ID
        :type Pid: int
        :param _Qps: Maximum QPS value
        :type Qps: int
        :param _Paymode: Billing mode
Note: this field may return null, indicating that no valid values can be obtained.
        :type Paymode: str
        :param _Locker: Async task flow ID when an async task is in progress on an instance
Note: this field may return null, indicating that no valid values can be obtained.
        :type Locker: int
        :param _StatusDesc: Current instance running status description
Note: this field may return null, indicating that no valid values can be obtained.
        :type StatusDesc: str
        :param _WanStatus: Public network access status. 0: not enabled, 1: enabled, 2: disabled, 3: enabling
        :type WanStatus: int
        :param _IsAuditSupported: Whether the instance supports audit. 1: yes, 0: no
        :type IsAuditSupported: int
        :param _Machine: Model
        :type Machine: str
        :param _IsEncryptSupported: Whether data encryption is supported. 1: yes, 0: no
        :type IsEncryptSupported: int
        :param _Cpu: Number of CPU cores of instance
        :type Cpu: int
        :param _Ipv6Flag: Indicates whether the instance uses IPv6
Note: this field may return null, indicating that no valid values can be obtained.
        :type Ipv6Flag: int
        :param _Vipv6: Private network IPv6 address
Note: this field may return null, indicating that no valid values can be obtained.
        :type Vipv6: str
        :param _WanVipv6: Public network IPv6 address
Note: this field may return null, indicating that no valid values can be obtained.
        :type WanVipv6: str
        :param _WanPortIpv6: Public network IPv6 port
Note: this field may return null, indicating that no valid values can be obtained.
        :type WanPortIpv6: int
        :param _WanStatusIpv6: Public network IPv6 status
Note: this field may return null, indicating that no valid values can be obtained.
        :type WanStatusIpv6: int
        :param _DbEngine: Database engine
Note: this field may return null, indicating that no valid values can be obtained.
        :type DbEngine: str
        :param _DbVersion: Database version
Note: this field may return null, indicating that no valid values can be obtained.
        :type DbVersion: str
        :param _DcnFlag: DCN type. Valid values: 0 (null), 1 (primary instance), 2 (disaster recovery instance)
Note: this field may return null, indicating that no valid values can be obtained.
        :type DcnFlag: int
        :param _DcnStatus: DCN status. Valid values: 0 (null), 1 (creating), 2 (syncing), 3 (disconnected)
Note: this field may return null, indicating that no valid values can be obtained.
        :type DcnStatus: int
        :param _DcnDstNum: The number of DCN disaster recovery instances
Note: this field may return null, indicating that no valid values can be obtained.
        :type DcnDstNum: int
        :param _InstanceType: Instance type. Valid values: `1` (dedicated primary instance), `2` (primary instance), `3` (disaster recovery instance), and `4` (dedicated disaster recovery instance).
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceType: int
        :param _ResourceTags: Instance tag information
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ResourceTags: list of ResourceTag
        :param _DbVersionId: Database version
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbVersionId: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._AppId = None
        self._ProjectId = None
        self._Region = None
        self._Zone = None
        self._VpcId = None
        self._SubnetId = None
        self._Status = None
        self._Vip = None
        self._Vport = None
        self._WanDomain = None
        self._WanVip = None
        self._WanPort = None
        self._CreateTime = None
        self._UpdateTime = None
        self._AutoRenewFlag = None
        self._PeriodEndTime = None
        self._Uin = None
        self._TdsqlVersion = None
        self._Memory = None
        self._Storage = None
        self._UniqueVpcId = None
        self._UniqueSubnetId = None
        self._OriginSerialId = None
        self._NodeCount = None
        self._IsTmp = None
        self._ExclusterId = None
        self._Id = None
        self._Pid = None
        self._Qps = None
        self._Paymode = None
        self._Locker = None
        self._StatusDesc = None
        self._WanStatus = None
        self._IsAuditSupported = None
        self._Machine = None
        self._IsEncryptSupported = None
        self._Cpu = None
        self._Ipv6Flag = None
        self._Vipv6 = None
        self._WanVipv6 = None
        self._WanPortIpv6 = None
        self._WanStatusIpv6 = None
        self._DbEngine = None
        self._DbVersion = None
        self._DcnFlag = None
        self._DcnStatus = None
        self._DcnDstNum = None
        self._InstanceType = None
        self._ResourceTags = None
        self._DbVersionId = None

    @property
    def InstanceId(self):
        """Instance ID, which uniquely identifies a TDSQL instance
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """Customizable instance name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AppId(self):
        """Application ID of instance
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ProjectId(self):
        """Project ID of instance
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Region(self):
        """Instance region name, such as ap-shanghai
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        """Instance AZ name, such as ap-guangzhou-1
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcId(self):
        """VPC ID, which is 0 if the basic network is used
        :rtype: int
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Subnet ID, which is 0 if the basic network is used
        :rtype: int
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Status(self):
        """Instance status. Valid values: `0` (creating), `1` (running task), `2` (running), `3` (uninitialized), `-1` (isolated), `4` (initializing), `5` (eliminating), `6` (restarting), `7` (migrating data)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Vip(self):
        """Private IP address
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
    def WanDomain(self):
        """Domain name for public network access, which can be resolved by the public network
        :rtype: str
        """
        return self._WanDomain

    @WanDomain.setter
    def WanDomain(self, WanDomain):
        self._WanDomain = WanDomain

    @property
    def WanVip(self):
        """Public IP address, which can be accessed over the public network
        :rtype: str
        """
        return self._WanVip

    @WanVip.setter
    def WanVip(self, WanVip):
        self._WanVip = WanVip

    @property
    def WanPort(self):
        """Public network port
        :rtype: int
        """
        return self._WanPort

    @WanPort.setter
    def WanPort(self, WanPort):
        self._WanPort = WanPort

    @property
    def CreateTime(self):
        """Instance creation time in the format of `2006-01-02 15:04:05`
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """Last updated time of instance in the format of `2006-01-02 15:04:05`
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def AutoRenewFlag(self):
        """Auto-renewal flag. 0: no, 1: yes
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def PeriodEndTime(self):
        """Instance expiration time in the format of `2006-01-02 15:04:05`
        :rtype: str
        """
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

    @property
    def Uin(self):
        """Instance account
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def TdsqlVersion(self):
        """TDSQL version information
        :rtype: str
        """
        return self._TdsqlVersion

    @TdsqlVersion.setter
    def TdsqlVersion(self, TdsqlVersion):
        self._TdsqlVersion = TdsqlVersion

    @property
    def Memory(self):
        """Instance memory size in GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        """Instance storage capacity in GB
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def UniqueVpcId(self):
        """VPC ID in string type
        :rtype: str
        """
        return self._UniqueVpcId

    @UniqueVpcId.setter
    def UniqueVpcId(self, UniqueVpcId):
        self._UniqueVpcId = UniqueVpcId

    @property
    def UniqueSubnetId(self):
        """VPC subnet ID in string type
        :rtype: str
        """
        return self._UniqueSubnetId

    @UniqueSubnetId.setter
    def UniqueSubnetId(self, UniqueSubnetId):
        self._UniqueSubnetId = UniqueSubnetId

    @property
    def OriginSerialId(self):
        """Original ID of instance (this field is obsolete and should not be depended on)
        :rtype: str
        """
        return self._OriginSerialId

    @OriginSerialId.setter
    def OriginSerialId(self, OriginSerialId):
        self._OriginSerialId = OriginSerialId

    @property
    def NodeCount(self):
        """Number of nodes. 2: one master and one slave, 3: one master and two slaves
        :rtype: int
        """
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def IsTmp(self):
        """Whether it is a temp instance. 0: no, non-zero value: yes
        :rtype: int
        """
        return self._IsTmp

    @IsTmp.setter
    def IsTmp(self, IsTmp):
        self._IsTmp = IsTmp

    @property
    def ExclusterId(self):
        """Dedicated cluster ID. If this parameter is empty, the instance is a general instance
        :rtype: str
        """
        return self._ExclusterId

    @ExclusterId.setter
    def ExclusterId(self, ExclusterId):
        self._ExclusterId = ExclusterId

    @property
    def Id(self):
        """Numeric ID of instance (this field is obsolete and should not be depended on)
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Pid(self):
        """Product type ID
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def Qps(self):
        """Maximum QPS value
        :rtype: int
        """
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def Paymode(self):
        """Billing mode
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Paymode

    @Paymode.setter
    def Paymode(self, Paymode):
        self._Paymode = Paymode

    @property
    def Locker(self):
        """Async task flow ID when an async task is in progress on an instance
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Locker

    @Locker.setter
    def Locker(self, Locker):
        self._Locker = Locker

    @property
    def StatusDesc(self):
        """Current instance running status description
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def WanStatus(self):
        """Public network access status. 0: not enabled, 1: enabled, 2: disabled, 3: enabling
        :rtype: int
        """
        return self._WanStatus

    @WanStatus.setter
    def WanStatus(self, WanStatus):
        self._WanStatus = WanStatus

    @property
    def IsAuditSupported(self):
        """Whether the instance supports audit. 1: yes, 0: no
        :rtype: int
        """
        return self._IsAuditSupported

    @IsAuditSupported.setter
    def IsAuditSupported(self, IsAuditSupported):
        self._IsAuditSupported = IsAuditSupported

    @property
    def Machine(self):
        """Model
        :rtype: str
        """
        return self._Machine

    @Machine.setter
    def Machine(self, Machine):
        self._Machine = Machine

    @property
    def IsEncryptSupported(self):
        """Whether data encryption is supported. 1: yes, 0: no
        :rtype: int
        """
        return self._IsEncryptSupported

    @IsEncryptSupported.setter
    def IsEncryptSupported(self, IsEncryptSupported):
        self._IsEncryptSupported = IsEncryptSupported

    @property
    def Cpu(self):
        """Number of CPU cores of instance
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Ipv6Flag(self):
        """Indicates whether the instance uses IPv6
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Ipv6Flag

    @Ipv6Flag.setter
    def Ipv6Flag(self, Ipv6Flag):
        self._Ipv6Flag = Ipv6Flag

    @property
    def Vipv6(self):
        """Private network IPv6 address
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Vipv6

    @Vipv6.setter
    def Vipv6(self, Vipv6):
        self._Vipv6 = Vipv6

    @property
    def WanVipv6(self):
        """Public network IPv6 address
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._WanVipv6

    @WanVipv6.setter
    def WanVipv6(self, WanVipv6):
        self._WanVipv6 = WanVipv6

    @property
    def WanPortIpv6(self):
        """Public network IPv6 port
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._WanPortIpv6

    @WanPortIpv6.setter
    def WanPortIpv6(self, WanPortIpv6):
        self._WanPortIpv6 = WanPortIpv6

    @property
    def WanStatusIpv6(self):
        """Public network IPv6 status
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._WanStatusIpv6

    @WanStatusIpv6.setter
    def WanStatusIpv6(self, WanStatusIpv6):
        self._WanStatusIpv6 = WanStatusIpv6

    @property
    def DbEngine(self):
        """Database engine
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DbEngine

    @DbEngine.setter
    def DbEngine(self, DbEngine):
        self._DbEngine = DbEngine

    @property
    def DbVersion(self):
        """Database version
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DbVersion

    @DbVersion.setter
    def DbVersion(self, DbVersion):
        self._DbVersion = DbVersion

    @property
    def DcnFlag(self):
        """DCN type. Valid values: 0 (null), 1 (primary instance), 2 (disaster recovery instance)
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DcnFlag

    @DcnFlag.setter
    def DcnFlag(self, DcnFlag):
        self._DcnFlag = DcnFlag

    @property
    def DcnStatus(self):
        """DCN status. Valid values: 0 (null), 1 (creating), 2 (syncing), 3 (disconnected)
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DcnStatus

    @DcnStatus.setter
    def DcnStatus(self, DcnStatus):
        self._DcnStatus = DcnStatus

    @property
    def DcnDstNum(self):
        """The number of DCN disaster recovery instances
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DcnDstNum

    @DcnDstNum.setter
    def DcnDstNum(self, DcnDstNum):
        self._DcnDstNum = DcnDstNum

    @property
    def InstanceType(self):
        """Instance type. Valid values: `1` (dedicated primary instance), `2` (primary instance), `3` (disaster recovery instance), and `4` (dedicated disaster recovery instance).
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def ResourceTags(self):
        """Instance tag information
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def DbVersionId(self):
        """Database version
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DbVersionId

    @DbVersionId.setter
    def DbVersionId(self, DbVersionId):
        self._DbVersionId = DbVersionId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._AppId = params.get("AppId")
        self._ProjectId = params.get("ProjectId")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Status = params.get("Status")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._WanDomain = params.get("WanDomain")
        self._WanVip = params.get("WanVip")
        self._WanPort = params.get("WanPort")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._PeriodEndTime = params.get("PeriodEndTime")
        self._Uin = params.get("Uin")
        self._TdsqlVersion = params.get("TdsqlVersion")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._UniqueVpcId = params.get("UniqueVpcId")
        self._UniqueSubnetId = params.get("UniqueSubnetId")
        self._OriginSerialId = params.get("OriginSerialId")
        self._NodeCount = params.get("NodeCount")
        self._IsTmp = params.get("IsTmp")
        self._ExclusterId = params.get("ExclusterId")
        self._Id = params.get("Id")
        self._Pid = params.get("Pid")
        self._Qps = params.get("Qps")
        self._Paymode = params.get("Paymode")
        self._Locker = params.get("Locker")
        self._StatusDesc = params.get("StatusDesc")
        self._WanStatus = params.get("WanStatus")
        self._IsAuditSupported = params.get("IsAuditSupported")
        self._Machine = params.get("Machine")
        self._IsEncryptSupported = params.get("IsEncryptSupported")
        self._Cpu = params.get("Cpu")
        self._Ipv6Flag = params.get("Ipv6Flag")
        self._Vipv6 = params.get("Vipv6")
        self._WanVipv6 = params.get("WanVipv6")
        self._WanPortIpv6 = params.get("WanPortIpv6")
        self._WanStatusIpv6 = params.get("WanStatusIpv6")
        self._DbEngine = params.get("DbEngine")
        self._DbVersion = params.get("DbVersion")
        self._DcnFlag = params.get("DcnFlag")
        self._DcnStatus = params.get("DcnStatus")
        self._DcnDstNum = params.get("DcnDstNum")
        self._InstanceType = params.get("InstanceType")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._DbVersionId = params.get("DbVersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBParamValue(AbstractModel):
    """TencentDB parameter information.

    """

    def __init__(self):
        r"""
        :param _Param: Parameter name
        :type Param: str
        :param _Value: Parameter value
        :type Value: str
        """
        self._Param = None
        self._Value = None

    @property
    def Param(self):
        """Parameter name
        :rtype: str
        """
        return self._Param

    @Param.setter
    def Param(self, Param):
        self._Param = Param

    @property
    def Value(self):
        """Parameter value
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Param = params.get("Param")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DCNReplicaConfig(AbstractModel):
    """DCN configuration

    """

    def __init__(self):
        r"""
        :param _RoReplicationMode: DCN running status. Valid values: `START` (running), `STOP` (pause)
Note: This field may return null, indicating that no valid values can be obtained.
        :type RoReplicationMode: str
        :param _DelayReplicationType: Delayed replication type. Valid values: `DEFAULT` (no delay), `DUE_TIME` (specified replication time)
Note: This field may return null, indicating that no valid values can be obtained.
        :type DelayReplicationType: str
        :param _DueTime: Specified time for delayed replication
Note: This field may return null, indicating that no valid values can be obtained.
        :type DueTime: str
        :param _ReplicationDelay: The number of seconds to delay the replication
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReplicationDelay: int
        """
        self._RoReplicationMode = None
        self._DelayReplicationType = None
        self._DueTime = None
        self._ReplicationDelay = None

    @property
    def RoReplicationMode(self):
        """DCN running status. Valid values: `START` (running), `STOP` (pause)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RoReplicationMode

    @RoReplicationMode.setter
    def RoReplicationMode(self, RoReplicationMode):
        self._RoReplicationMode = RoReplicationMode

    @property
    def DelayReplicationType(self):
        """Delayed replication type. Valid values: `DEFAULT` (no delay), `DUE_TIME` (specified replication time)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DelayReplicationType

    @DelayReplicationType.setter
    def DelayReplicationType(self, DelayReplicationType):
        self._DelayReplicationType = DelayReplicationType

    @property
    def DueTime(self):
        """Specified time for delayed replication
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DueTime

    @DueTime.setter
    def DueTime(self, DueTime):
        self._DueTime = DueTime

    @property
    def ReplicationDelay(self):
        """The number of seconds to delay the replication
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ReplicationDelay

    @ReplicationDelay.setter
    def ReplicationDelay(self, ReplicationDelay):
        self._ReplicationDelay = ReplicationDelay


    def _deserialize(self, params):
        self._RoReplicationMode = params.get("RoReplicationMode")
        self._DelayReplicationType = params.get("DelayReplicationType")
        self._DueTime = params.get("DueTime")
        self._ReplicationDelay = params.get("ReplicationDelay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DCNReplicaStatus(AbstractModel):
    """DCN status information

    """

    def __init__(self):
        r"""
        :param _Status: DCN running status. Valid values: `START` (running), `STOP` (pause).
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _Delay: The current delay, which takes the delay value of the replica instance.
        :type Delay: int
        """
        self._Status = None
        self._Delay = None

    @property
    def Status(self):
        """DCN running status. Valid values: `START` (running), `STOP` (pause).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Delay(self):
        """The current delay, which takes the delay value of the replica instance.
        :rtype: int
        """
        return self._Delay

    @Delay.setter
    def Delay(self, Delay):
        self._Delay = Delay


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Delay = params.get("Delay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Database(AbstractModel):
    """Database information

    """

    def __init__(self):
        r"""
        :param _DbName: Database name
        :type DbName: str
        """
        self._DbName = None

    @property
    def DbName(self):
        """Database name
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName


    def _deserialize(self, params):
        self._DbName = params.get("DbName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseFunction(AbstractModel):
    """Database function information

    """

    def __init__(self):
        r"""
        :param _Func: Function name
        :type Func: str
        """
        self._Func = None

    @property
    def Func(self):
        """Function name
        :rtype: str
        """
        return self._Func

    @Func.setter
    def Func(self, Func):
        self._Func = Func


    def _deserialize(self, params):
        self._Func = params.get("Func")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabasePrivilege(AbstractModel):
    """Database permission

    """

    def __init__(self):
        r"""
        :param _Privileges: Permission information
        :type Privileges: list of str
        :param _Database: Database name
        :type Database: str
        """
        self._Privileges = None
        self._Database = None

    @property
    def Privileges(self):
        """Permission information
        :rtype: list of str
        """
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges

    @property
    def Database(self):
        """Database name
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database


    def _deserialize(self, params):
        self._Privileges = params.get("Privileges")
        self._Database = params.get("Database")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseProcedure(AbstractModel):
    """Database stored procedure information

    """

    def __init__(self):
        r"""
        :param _Proc: Stored procedure name
        :type Proc: str
        """
        self._Proc = None

    @property
    def Proc(self):
        """Stored procedure name
        :rtype: str
        """
        return self._Proc

    @Proc.setter
    def Proc(self, Proc):
        self._Proc = Proc


    def _deserialize(self, params):
        self._Proc = params.get("Proc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseTable(AbstractModel):
    """Database table information

    """

    def __init__(self):
        r"""
        :param _Table: Table name
        :type Table: str
        """
        self._Table = None

    @property
    def Table(self):
        """Table name
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table


    def _deserialize(self, params):
        self._Table = params.get("Table")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseView(AbstractModel):
    """Database view information

    """

    def __init__(self):
        r"""
        :param _View: View name
        :type View: str
        """
        self._View = None

    @property
    def View(self):
        """View name
        :rtype: str
        """
        return self._View

    @View.setter
    def View(self, View):
        self._View = View


    def _deserialize(self, params):
        self._View = params.get("View")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DcnDetailItem(AbstractModel):
    """DCN details

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _Region: Region where the instance resides
        :type Region: str
        :param _Zone: Availability zone where the instance resides
        :type Zone: str
        :param _Vip: Instance IP address
        :type Vip: str
        :param _Vipv6: Instance IPv6 address
        :type Vipv6: str
        :param _Vport: Instance port
        :type Vport: int
        :param _Status: Instance status
        :type Status: int
        :param _StatusDesc: Instance status description
        :type StatusDesc: str
        :param _DcnFlag: DCN flag. Valid values: `1` (primary), `2` (disaster recovery)
        :type DcnFlag: int
        :param _DcnStatus: DCN status. Valid values: `0` (none), `1` (creating), `2` (syncing), `3` (disconnected)
        :type DcnStatus: int
        :param _Cpu: Number of CPU cores of the instance
        :type Cpu: int
        :param _Memory: Instance memory capacity in GB
        :type Memory: int
        :param _Storage: Instance storage capacity in GB
        :type Storage: int
        :param _PayMode: Billing mode
        :type PayMode: int
        :param _CreateTime: Creation time of the instance in the format of 2006-01-02 15:04:05
        :type CreateTime: str
        :param _PeriodEndTime: Expiration time of the instance in the format of 2006-01-02 15:04:05
        :type PeriodEndTime: str
        :param _InstanceType: Instance type. Valid values: `1` (dedicated primary instance), `2` (non-dedicated primary instance), `3` (non-dedicated disaster recovery instance), `4` (dedicated disaster recovery instance)
        :type InstanceType: int
        :param _ReplicaConfig: Configuration information of DCN replication. This field is null for a primary instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReplicaConfig: :class:`tencentcloud.mariadb.v20170312.models.DCNReplicaConfig`
        :param _ReplicaStatus: DCN replication status. This field is null for the primary instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReplicaStatus: :class:`tencentcloud.mariadb.v20170312.models.DCNReplicaStatus`
        :param _EncryptStatus: Whether KMS is enabled.
        :type EncryptStatus: int
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Region = None
        self._Zone = None
        self._Vip = None
        self._Vipv6 = None
        self._Vport = None
        self._Status = None
        self._StatusDesc = None
        self._DcnFlag = None
        self._DcnStatus = None
        self._Cpu = None
        self._Memory = None
        self._Storage = None
        self._PayMode = None
        self._CreateTime = None
        self._PeriodEndTime = None
        self._InstanceType = None
        self._ReplicaConfig = None
        self._ReplicaStatus = None
        self._EncryptStatus = None

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
        """Region where the instance resides
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        """Availability zone where the instance resides
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Vip(self):
        """Instance IP address
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vipv6(self):
        """Instance IPv6 address
        :rtype: str
        """
        return self._Vipv6

    @Vipv6.setter
    def Vipv6(self, Vipv6):
        self._Vipv6 = Vipv6

    @property
    def Vport(self):
        """Instance port
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Status(self):
        """Instance status
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        """Instance status description
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def DcnFlag(self):
        """DCN flag. Valid values: `1` (primary), `2` (disaster recovery)
        :rtype: int
        """
        return self._DcnFlag

    @DcnFlag.setter
    def DcnFlag(self, DcnFlag):
        self._DcnFlag = DcnFlag

    @property
    def DcnStatus(self):
        """DCN status. Valid values: `0` (none), `1` (creating), `2` (syncing), `3` (disconnected)
        :rtype: int
        """
        return self._DcnStatus

    @DcnStatus.setter
    def DcnStatus(self, DcnStatus):
        self._DcnStatus = DcnStatus

    @property
    def Cpu(self):
        """Number of CPU cores of the instance
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """Instance memory capacity in GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        """Instance storage capacity in GB
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def PayMode(self):
        """Billing mode
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def CreateTime(self):
        """Creation time of the instance in the format of 2006-01-02 15:04:05
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def PeriodEndTime(self):
        """Expiration time of the instance in the format of 2006-01-02 15:04:05
        :rtype: str
        """
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

    @property
    def InstanceType(self):
        """Instance type. Valid values: `1` (dedicated primary instance), `2` (non-dedicated primary instance), `3` (non-dedicated disaster recovery instance), `4` (dedicated disaster recovery instance)
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def ReplicaConfig(self):
        """Configuration information of DCN replication. This field is null for a primary instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DCNReplicaConfig`
        """
        return self._ReplicaConfig

    @ReplicaConfig.setter
    def ReplicaConfig(self, ReplicaConfig):
        self._ReplicaConfig = ReplicaConfig

    @property
    def ReplicaStatus(self):
        """DCN replication status. This field is null for the primary instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DCNReplicaStatus`
        """
        return self._ReplicaStatus

    @ReplicaStatus.setter
    def ReplicaStatus(self, ReplicaStatus):
        self._ReplicaStatus = ReplicaStatus

    @property
    def EncryptStatus(self):
        """Whether KMS is enabled.
        :rtype: int
        """
        return self._EncryptStatus

    @EncryptStatus.setter
    def EncryptStatus(self, EncryptStatus):
        self._EncryptStatus = EncryptStatus


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._Vip = params.get("Vip")
        self._Vipv6 = params.get("Vipv6")
        self._Vport = params.get("Vport")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._DcnFlag = params.get("DcnFlag")
        self._DcnStatus = params.get("DcnStatus")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._PayMode = params.get("PayMode")
        self._CreateTime = params.get("CreateTime")
        self._PeriodEndTime = params.get("PeriodEndTime")
        self._InstanceType = params.get("InstanceType")
        if params.get("ReplicaConfig") is not None:
            self._ReplicaConfig = DCNReplicaConfig()
            self._ReplicaConfig._deserialize(params.get("ReplicaConfig"))
        if params.get("ReplicaStatus") is not None:
            self._ReplicaStatus = DCNReplicaStatus()
            self._ReplicaStatus._deserialize(params.get("ReplicaStatus"))
        self._EncryptStatus = params.get("EncryptStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Deal(AbstractModel):
    """Order information

    """

    def __init__(self):
        r"""
        :param _DealName: Order number
        :type DealName: str
        :param _OwnerUin: Account
        :type OwnerUin: str
        :param _Count: Number of items
        :type Count: int
        :param _FlowId: ID of the associated process, which can be used to query the process execution status.
        :type FlowId: int
        :param _InstanceIds: The ID of the created instance, which is required only for the order that creates an instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceIds: list of str
        :param _PayMode: Payment mode. Valid values: 0 (postpaid), 1 (prepaid)
        :type PayMode: int
        """
        self._DealName = None
        self._OwnerUin = None
        self._Count = None
        self._FlowId = None
        self._InstanceIds = None
        self._PayMode = None

    @property
    def DealName(self):
        """Order number
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def OwnerUin(self):
        """Account
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def Count(self):
        """Number of items
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def FlowId(self):
        """ID of the associated process, which can be used to query the process execution status.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceIds(self):
        """The ID of the created instance, which is required only for the order that creates an instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def PayMode(self):
        """Payment mode. Valid values: 0 (postpaid), 1 (prepaid)
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._OwnerUin = params.get("OwnerUin")
        self._Count = params.get("Count")
        self._FlowId = params.get("FlowId")
        self._InstanceIds = params.get("InstanceIds")
        self._PayMode = params.get("PayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountRequest(AbstractModel):
    """DeleteAccount request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :type InstanceId: str
        :param _UserName: Username
        :type UserName: str
        :param _Host: Access host allowed for user
        :type Host: str
        """
        self._InstanceId = None
        self._UserName = None
        self._Host = None

    @property
    def InstanceId(self):
        """Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        """Username
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        """Access host allowed for user
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountResponse(AbstractModel):
    """DeleteAccount response structure.

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


class DescribeAccountPrivilegesRequest(AbstractModel):
    """DescribeAccountPrivileges request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the form of `tdsql-ow728lmc`, which can be obtained by querying the instance details through `DescribeDBInstances`.
        :type InstanceId: str
        :param _UserName: Login username.
        :type UserName: str
        :param _Host: Access host allowed for a user. An account is uniquely identified by username and host.
        :type Host: str
        :param _DbName: Database name. `\*` indicates that global permissions will be queried (i.e., `\*.\*`), in which case the `Type` and `Object ` parameters will be ignored.
        :type DbName: str
        :param _Type: Type. Valid values: table, view, proc, func, \*. If `DbName` is a specific database name and `Type` is `\*`, the permissions of the database will be queried (i.e., `db.\*`), in which case the `Object` parameter will be ignored.
        :type Type: str
        :param _Object: Type name. For example, if `Type` is `table`, `Object` indicates a specific table name; if both `DbName` and `Type` are specific names, it indicates a specific object name and cannot be `\*` or empty.
        :type Object: str
        :param _ColName: If `Type` is `table` and `ColName` is `\*`, the permissions of the table will be queried; if `ColName` is a specific field name, the permissions of the corresponding field will be queried.
        :type ColName: str
        """
        self._InstanceId = None
        self._UserName = None
        self._Host = None
        self._DbName = None
        self._Type = None
        self._Object = None
        self._ColName = None

    @property
    def InstanceId(self):
        """Instance ID in the form of `tdsql-ow728lmc`, which can be obtained by querying the instance details through `DescribeDBInstances`.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        """Login username.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        """Access host allowed for a user. An account is uniquely identified by username and host.
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def DbName(self):
        """Database name. `\*` indicates that global permissions will be queried (i.e., `\*.\*`), in which case the `Type` and `Object ` parameters will be ignored.
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Type(self):
        """Type. Valid values: table, view, proc, func, \*. If `DbName` is a specific database name and `Type` is `\*`, the permissions of the database will be queried (i.e., `db.\*`), in which case the `Object` parameter will be ignored.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Object(self):
        """Type name. For example, if `Type` is `table`, `Object` indicates a specific table name; if both `DbName` and `Type` are specific names, it indicates a specific object name and cannot be `\*` or empty.
        :rtype: str
        """
        return self._Object

    @Object.setter
    def Object(self, Object):
        self._Object = Object

    @property
    def ColName(self):
        """If `Type` is `table` and `ColName` is `\*`, the permissions of the table will be queried; if `ColName` is a specific field name, the permissions of the corresponding field will be queried.
        :rtype: str
        """
        return self._ColName

    @ColName.setter
    def ColName(self, ColName):
        self._ColName = ColName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        self._DbName = params.get("DbName")
        self._Type = params.get("Type")
        self._Object = params.get("Object")
        self._ColName = params.get("ColName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountPrivilegesResponse(AbstractModel):
    """DescribeAccountPrivileges response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Privileges: Permission list.
        :type Privileges: list of str
        :param _UserName: Database account username
        :type UserName: str
        :param _Host: Database account host
        :type Host: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._Privileges = None
        self._UserName = None
        self._Host = None
        self._RequestId = None

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
    def Privileges(self):
        """Permission list.
        :rtype: list of str
        """
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges

    @property
    def UserName(self):
        """Database account username
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        """Database account host
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

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
        self._InstanceId = params.get("InstanceId")
        self._Privileges = params.get("Privileges")
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        self._RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the form of `tdsql-ow728lmc`, which can be obtained by querying the instance details through `DescribeDBInstances`.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Instance ID in the form of `tdsql-ow728lmc`, which can be obtained by querying the instance details through `DescribeDBInstances`.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, which is passed through from the input parameters.
        :type InstanceId: str
        :param _Users: Instance user list.
        :type Users: list of DBAccount
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._Users = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """Instance ID, which is passed through from the input parameters.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Users(self):
        """Instance user list.
        :rtype: list of DBAccount
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

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
        self._InstanceId = params.get("InstanceId")
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = DBAccount()
                obj._deserialize(item)
                self._Users.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackupFilesRequest(AbstractModel):
    """DescribeBackupFiles request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Query by instance ID
        :type InstanceId: str
        :param _BackupType: Backup type. Valid values: `Data` (data backup), `Binlog` (Binlog backup), `Errlog` (error log), `Slowlog` (slow log).
        :type BackupType: str
        :param _StartTime: Query by start time
        :type StartTime: str
        :param _EndTime: Query by end time
        :type EndTime: str
        :param _Limit: Pagination parameter
        :type Limit: int
        :param _Offset: Pagination parameter
        :type Offset: int
        :param _OrderBy: Sorting dimension. Valid values: `Time`, `Size`.
        :type OrderBy: str
        :param _OrderType: Sorting order. Valid values: `DESC`, `ASC`.
        :type OrderType: str
        """
        self._InstanceId = None
        self._BackupType = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderType = None

    @property
    def InstanceId(self):
        """Query by instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupType(self):
        """Backup type. Valid values: `Data` (data backup), `Binlog` (Binlog backup), `Errlog` (error log), `Slowlog` (slow log).
        :rtype: str
        """
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def StartTime(self):
        """Query by start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Query by end time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        """Pagination parameter
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Pagination parameter
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        """Sorting dimension. Valid values: `Time`, `Size`.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderType(self):
        """Sorting order. Valid values: `DESC`, `ASC`.
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupType = params.get("BackupType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderType = params.get("OrderType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupFilesResponse(AbstractModel):
    """DescribeBackupFiles response structure.

    """

    def __init__(self):
        r"""
        :param _Files: List of backup files
        :type Files: list of InstanceBackupFileItem
        :param _TotalCount: Total number
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Files = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Files(self):
        """List of backup files
        :rtype: list of InstanceBackupFileItem
        """
        return self._Files

    @Files.setter
    def Files(self, Files):
        self._Files = Files

    @property
    def TotalCount(self):
        """Total number
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
        if params.get("Files") is not None:
            self._Files = []
            for item in params.get("Files"):
                obj = InstanceBackupFileItem()
                obj._deserialize(item)
                self._Files.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDBEncryptAttributesRequest(AbstractModel):
    """DescribeDBEncryptAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of `tdsql-ow728lmc`
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Instance ID in the format of `tdsql-ow728lmc`
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBEncryptAttributesResponse(AbstractModel):
    """DescribeDBEncryptAttributes response structure.

    """

    def __init__(self):
        r"""
        :param _EncryptStatus: Whether encryption is enabled. Valid values: `1` (enabled), `2` (disabled).
        :type EncryptStatus: int
        :param _CipherText: DEK key
        :type CipherText: str
        :param _ExpireDate: DEK key expiration date
        :type ExpireDate: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._EncryptStatus = None
        self._CipherText = None
        self._ExpireDate = None
        self._RequestId = None

    @property
    def EncryptStatus(self):
        """Whether encryption is enabled. Valid values: `1` (enabled), `2` (disabled).
        :rtype: int
        """
        return self._EncryptStatus

    @EncryptStatus.setter
    def EncryptStatus(self, EncryptStatus):
        self._EncryptStatus = EncryptStatus

    @property
    def CipherText(self):
        """DEK key
        :rtype: str
        """
        return self._CipherText

    @CipherText.setter
    def CipherText(self, CipherText):
        self._CipherText = CipherText

    @property
    def ExpireDate(self):
        """DEK key expiration date
        :rtype: str
        """
        return self._ExpireDate

    @ExpireDate.setter
    def ExpireDate(self, ExpireDate):
        self._ExpireDate = ExpireDate

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
        self._EncryptStatus = params.get("EncryptStatus")
        self._CipherText = params.get("CipherText")
        self._ExpireDate = params.get("ExpireDate")
        self._RequestId = params.get("RequestId")


class DescribeDBInstanceDetailRequest(AbstractModel):
    """DescribeDBInstanceDetail request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of `tdsql-ow728lmc`
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Instance ID in the format of `tdsql-ow728lmc`
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceDetailResponse(AbstractModel):
    """DescribeDBInstanceDetail response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _Status: Instance status
        :type Status: int
        :param _StatusDesc: Current status of the instance
        :type StatusDesc: str
        :param _Vip: Private IP address
        :type Vip: str
        :param _Vport: Private port
        :type Vport: int
        :param _IsTmp: Whether it is a temp instance. Valid values: `0` (no), non-zero value (yes).
        :type IsTmp: int
        :param _NodeCount: Number of nodes. Valid values: `2` (1 primary-1 replica), `3` (1 primary-2 replicas).
        :type NodeCount: int
        :param _Region: Instance region name, such as ap-shanghai.
        :type Region: str
        :param _Zone: Instance AZ name, such as ap-guangzhou-1.
        :type Zone: str
        :param _VpcId: VPC ID in string type
        :type VpcId: str
        :param _SubnetId: VPC subnet ID in string type
        :type SubnetId: str
        :param _WanStatus: Public network status. Valid values: `0` (not enabled), `1` (enabled), `2` (disabled), `3`: (enabling), `4` (disabling).
        :type WanStatus: int
        :param _WanDomain: Domain name for public network access, which can be resolved by the public network.
        :type WanDomain: str
        :param _WanVip: Public IP address, which can be accessed over the public network.
        :type WanVip: str
        :param _WanPort: Public network port
        :type WanPort: int
        :param _ProjectId: Project ID of the instance
        :type ProjectId: int
        :param _TdsqlVersion: TDSQL version information
        :type TdsqlVersion: str
        :param _Memory: Instance memory capacity in GB
        :type Memory: int
        :param _Storage: Instance storage capacity in GB
        :type Storage: int
        :param _MasterZone: Primary AZ, such as ap-shanghai-1.
        :type MasterZone: str
        :param _SlaveZones: List of replica AZs, such as ap-shanghai-2.
        :type SlaveZones: list of str
        :param _AutoRenewFlag: Auto-renewal flag. Valid values: `0` (no), `1` (yes).
        :type AutoRenewFlag: int
        :param _ExclusterId: Dedicated cluster ID, which is empty for a non-dedicated cluster instance.
        :type ExclusterId: str
        :param _PayMode: Billing mode. Valid values: `prepaid` (monthly subscription), `postpaid` (pay-as-you-go).
        :type PayMode: str
        :param _CreateTime: Creation time of the instance in the format of 2006-01-02 15:04:05
        :type CreateTime: str
        :param _IsAuditSupported: Whether the instance supports audit
        :type IsAuditSupported: bool
        :param _PeriodEndTime: Expiration time of the instance in the format of 2006-01-02 15:04:05
        :type PeriodEndTime: str
        :param _Machine: Model information
        :type Machine: str
        :param _StorageUsage: Storage space utilization
        :type StorageUsage: str
        :param _LogStorage: Size of log storage space in GB
        :type LogStorage: int
        :param _IsEncryptSupported: Whether data encryption is supported. Valid values: `1` (yes), `0`: (no).
        :type IsEncryptSupported: int
        :param _Vip6: Private network IPv6 address
Note: This field may return null, indicating that no valid values can be obtained.
        :type Vip6: str
        :param _Cpu: Number of CPU cores of an instance.
        :type Cpu: int
        :param _Pid: Product type ID
        :type Pid: int
        :param _Qps: Max QPS
        :type Qps: int
        :param _Ipv6Flag: Whether IPv6 is supported.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Ipv6Flag: int
        :param _WanVipv6: Public IPv6 address, which can be accessed over the public network
Note: This field may return null, indicating that no valid values can be obtained.
        :type WanVipv6: str
        :param _WanStatusIpv6: Public network status. Valid values: `0` (not enabled), `1` (enabled), `2` (disabled), `3`: (enabling), `4` (disabling).
Note: This field may return null, indicating that no valid values can be obtained.
        :type WanStatusIpv6: int
        :param _WanPortIpv6: Public network IPv6 port
Note: This field may return null, indicating that no valid values can be obtained.
        :type WanPortIpv6: int
        :param _DbEngine: Database engine
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbEngine: str
        :param _DbVersion: Database version
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbVersion: str
        :param _ResourceTags: Tag information
        :type ResourceTags: list of ResourceTag
        :param _DcnFlag: DCN type. Valid values: `0` (N/A), `1` (primary instance), `2` (disaster recovery read-only instance)
Note: This field may return null, indicating that no valid values can be obtained.
        :type DcnFlag: int
        :param _DcnStatus: DCN status. Valid values: `0` (N/A), `1` (creating), `2` (syncing), `3` (disconnected)
Note: This field may return null, indicating that no valid values can be obtained.
        :type DcnStatus: int
        :param _DcnDstNum: Number of disaster recovery read-only instances
Note: This field may return null, indicating that no valid values can be obtained.
        :type DcnDstNum: int
        :param _InstanceType: Instance type. Valid values: `1` (dedicated primary instance), `2` (non-dedicated primary instance), `3` (non-dedicated disaster recovery read-only instance), `4` (dedicated disaster recovery read-only instance)
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceType: int
        :param _NodesInfo: Instance node information
Note: This field may return null, indicating that no valid values can be obtained.
        :type NodesInfo: list of NodeInfo
        :param _IsMaxUserConnectionsSupported: Whether the instance supports setting the connection limit, which is not supported for kernel version 10.1.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsMaxUserConnectionsSupported: bool
        :param _DbVersionId: The displayed database version
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbVersionId: str
        :param _EncryptStatus: Encryption status. Valid values: `0` (disabled), `1` (enabled).
Note: This field may return null, indicating that no valid values can be obtained.
        :type EncryptStatus: int
        :param _ReplicaConfig: Configuration information of DCN
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReplicaConfig: :class:`tencentcloud.mariadb.v20170312.models.DCNReplicaConfig`
        :param _ReplicaStatus: Running status of DCN
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReplicaStatus: :class:`tencentcloud.mariadb.v20170312.models.DCNReplicaStatus`
        :param _ExclusterType: Type of dedicated cluster. Valid values: `0` (public cloud), `1` (finance cage), `2` (CDC cluster).
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExclusterType: int
        :param _RsAccessStrategy: Nearby VPC access
Note: This field may return null, indicating that no valid values can be obtained.
        :type RsAccessStrategy: int
        :param _ReservedNetResources: Unclaimed network resource
        :type ReservedNetResources: list of ReservedNetResource
        :param _IsPhysicalReplicationSupported: Whether physical replication is supported.
        :type IsPhysicalReplicationSupported: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Status = None
        self._StatusDesc = None
        self._Vip = None
        self._Vport = None
        self._IsTmp = None
        self._NodeCount = None
        self._Region = None
        self._Zone = None
        self._VpcId = None
        self._SubnetId = None
        self._WanStatus = None
        self._WanDomain = None
        self._WanVip = None
        self._WanPort = None
        self._ProjectId = None
        self._TdsqlVersion = None
        self._Memory = None
        self._Storage = None
        self._MasterZone = None
        self._SlaveZones = None
        self._AutoRenewFlag = None
        self._ExclusterId = None
        self._PayMode = None
        self._CreateTime = None
        self._IsAuditSupported = None
        self._PeriodEndTime = None
        self._Machine = None
        self._StorageUsage = None
        self._LogStorage = None
        self._IsEncryptSupported = None
        self._Vip6 = None
        self._Cpu = None
        self._Pid = None
        self._Qps = None
        self._Ipv6Flag = None
        self._WanVipv6 = None
        self._WanStatusIpv6 = None
        self._WanPortIpv6 = None
        self._DbEngine = None
        self._DbVersion = None
        self._ResourceTags = None
        self._DcnFlag = None
        self._DcnStatus = None
        self._DcnDstNum = None
        self._InstanceType = None
        self._NodesInfo = None
        self._IsMaxUserConnectionsSupported = None
        self._DbVersionId = None
        self._EncryptStatus = None
        self._ReplicaConfig = None
        self._ReplicaStatus = None
        self._ExclusterType = None
        self._RsAccessStrategy = None
        self._ReservedNetResources = None
        self._IsPhysicalReplicationSupported = None
        self._RequestId = None

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
    def Status(self):
        """Instance status
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        """Current status of the instance
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def Vip(self):
        """Private IP address
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """Private port
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def IsTmp(self):
        """Whether it is a temp instance. Valid values: `0` (no), non-zero value (yes).
        :rtype: int
        """
        return self._IsTmp

    @IsTmp.setter
    def IsTmp(self, IsTmp):
        self._IsTmp = IsTmp

    @property
    def NodeCount(self):
        """Number of nodes. Valid values: `2` (1 primary-1 replica), `3` (1 primary-2 replicas).
        :rtype: int
        """
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def Region(self):
        """Instance region name, such as ap-shanghai.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        """Instance AZ name, such as ap-guangzhou-1.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcId(self):
        """VPC ID in string type
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """VPC subnet ID in string type
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def WanStatus(self):
        """Public network status. Valid values: `0` (not enabled), `1` (enabled), `2` (disabled), `3`: (enabling), `4` (disabling).
        :rtype: int
        """
        return self._WanStatus

    @WanStatus.setter
    def WanStatus(self, WanStatus):
        self._WanStatus = WanStatus

    @property
    def WanDomain(self):
        """Domain name for public network access, which can be resolved by the public network.
        :rtype: str
        """
        return self._WanDomain

    @WanDomain.setter
    def WanDomain(self, WanDomain):
        self._WanDomain = WanDomain

    @property
    def WanVip(self):
        """Public IP address, which can be accessed over the public network.
        :rtype: str
        """
        return self._WanVip

    @WanVip.setter
    def WanVip(self, WanVip):
        self._WanVip = WanVip

    @property
    def WanPort(self):
        """Public network port
        :rtype: int
        """
        return self._WanPort

    @WanPort.setter
    def WanPort(self, WanPort):
        self._WanPort = WanPort

    @property
    def ProjectId(self):
        """Project ID of the instance
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TdsqlVersion(self):
        """TDSQL version information
        :rtype: str
        """
        return self._TdsqlVersion

    @TdsqlVersion.setter
    def TdsqlVersion(self, TdsqlVersion):
        self._TdsqlVersion = TdsqlVersion

    @property
    def Memory(self):
        """Instance memory capacity in GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        """Instance storage capacity in GB
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def MasterZone(self):
        """Primary AZ, such as ap-shanghai-1.
        :rtype: str
        """
        return self._MasterZone

    @MasterZone.setter
    def MasterZone(self, MasterZone):
        self._MasterZone = MasterZone

    @property
    def SlaveZones(self):
        """List of replica AZs, such as ap-shanghai-2.
        :rtype: list of str
        """
        return self._SlaveZones

    @SlaveZones.setter
    def SlaveZones(self, SlaveZones):
        self._SlaveZones = SlaveZones

    @property
    def AutoRenewFlag(self):
        """Auto-renewal flag. Valid values: `0` (no), `1` (yes).
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def ExclusterId(self):
        """Dedicated cluster ID, which is empty for a non-dedicated cluster instance.
        :rtype: str
        """
        return self._ExclusterId

    @ExclusterId.setter
    def ExclusterId(self, ExclusterId):
        self._ExclusterId = ExclusterId

    @property
    def PayMode(self):
        """Billing mode. Valid values: `prepaid` (monthly subscription), `postpaid` (pay-as-you-go).
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def CreateTime(self):
        """Creation time of the instance in the format of 2006-01-02 15:04:05
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def IsAuditSupported(self):
        """Whether the instance supports audit
        :rtype: bool
        """
        return self._IsAuditSupported

    @IsAuditSupported.setter
    def IsAuditSupported(self, IsAuditSupported):
        self._IsAuditSupported = IsAuditSupported

    @property
    def PeriodEndTime(self):
        """Expiration time of the instance in the format of 2006-01-02 15:04:05
        :rtype: str
        """
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

    @property
    def Machine(self):
        """Model information
        :rtype: str
        """
        return self._Machine

    @Machine.setter
    def Machine(self, Machine):
        self._Machine = Machine

    @property
    def StorageUsage(self):
        """Storage space utilization
        :rtype: str
        """
        return self._StorageUsage

    @StorageUsage.setter
    def StorageUsage(self, StorageUsage):
        self._StorageUsage = StorageUsage

    @property
    def LogStorage(self):
        """Size of log storage space in GB
        :rtype: int
        """
        return self._LogStorage

    @LogStorage.setter
    def LogStorage(self, LogStorage):
        self._LogStorage = LogStorage

    @property
    def IsEncryptSupported(self):
        """Whether data encryption is supported. Valid values: `1` (yes), `0`: (no).
        :rtype: int
        """
        return self._IsEncryptSupported

    @IsEncryptSupported.setter
    def IsEncryptSupported(self, IsEncryptSupported):
        self._IsEncryptSupported = IsEncryptSupported

    @property
    def Vip6(self):
        """Private network IPv6 address
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Vip6

    @Vip6.setter
    def Vip6(self, Vip6):
        self._Vip6 = Vip6

    @property
    def Cpu(self):
        """Number of CPU cores of an instance.
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Pid(self):
        """Product type ID
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def Qps(self):
        """Max QPS
        :rtype: int
        """
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def Ipv6Flag(self):
        """Whether IPv6 is supported.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Ipv6Flag

    @Ipv6Flag.setter
    def Ipv6Flag(self, Ipv6Flag):
        self._Ipv6Flag = Ipv6Flag

    @property
    def WanVipv6(self):
        """Public IPv6 address, which can be accessed over the public network
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._WanVipv6

    @WanVipv6.setter
    def WanVipv6(self, WanVipv6):
        self._WanVipv6 = WanVipv6

    @property
    def WanStatusIpv6(self):
        """Public network status. Valid values: `0` (not enabled), `1` (enabled), `2` (disabled), `3`: (enabling), `4` (disabling).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._WanStatusIpv6

    @WanStatusIpv6.setter
    def WanStatusIpv6(self, WanStatusIpv6):
        self._WanStatusIpv6 = WanStatusIpv6

    @property
    def WanPortIpv6(self):
        """Public network IPv6 port
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._WanPortIpv6

    @WanPortIpv6.setter
    def WanPortIpv6(self, WanPortIpv6):
        self._WanPortIpv6 = WanPortIpv6

    @property
    def DbEngine(self):
        """Database engine
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DbEngine

    @DbEngine.setter
    def DbEngine(self, DbEngine):
        self._DbEngine = DbEngine

    @property
    def DbVersion(self):
        """Database version
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DbVersion

    @DbVersion.setter
    def DbVersion(self, DbVersion):
        self._DbVersion = DbVersion

    @property
    def ResourceTags(self):
        """Tag information
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def DcnFlag(self):
        """DCN type. Valid values: `0` (N/A), `1` (primary instance), `2` (disaster recovery read-only instance)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DcnFlag

    @DcnFlag.setter
    def DcnFlag(self, DcnFlag):
        self._DcnFlag = DcnFlag

    @property
    def DcnStatus(self):
        """DCN status. Valid values: `0` (N/A), `1` (creating), `2` (syncing), `3` (disconnected)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DcnStatus

    @DcnStatus.setter
    def DcnStatus(self, DcnStatus):
        self._DcnStatus = DcnStatus

    @property
    def DcnDstNum(self):
        """Number of disaster recovery read-only instances
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DcnDstNum

    @DcnDstNum.setter
    def DcnDstNum(self, DcnDstNum):
        self._DcnDstNum = DcnDstNum

    @property
    def InstanceType(self):
        """Instance type. Valid values: `1` (dedicated primary instance), `2` (non-dedicated primary instance), `3` (non-dedicated disaster recovery read-only instance), `4` (dedicated disaster recovery read-only instance)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def NodesInfo(self):
        """Instance node information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of NodeInfo
        """
        return self._NodesInfo

    @NodesInfo.setter
    def NodesInfo(self, NodesInfo):
        self._NodesInfo = NodesInfo

    @property
    def IsMaxUserConnectionsSupported(self):
        """Whether the instance supports setting the connection limit, which is not supported for kernel version 10.1.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsMaxUserConnectionsSupported

    @IsMaxUserConnectionsSupported.setter
    def IsMaxUserConnectionsSupported(self, IsMaxUserConnectionsSupported):
        self._IsMaxUserConnectionsSupported = IsMaxUserConnectionsSupported

    @property
    def DbVersionId(self):
        """The displayed database version
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DbVersionId

    @DbVersionId.setter
    def DbVersionId(self, DbVersionId):
        self._DbVersionId = DbVersionId

    @property
    def EncryptStatus(self):
        """Encryption status. Valid values: `0` (disabled), `1` (enabled).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._EncryptStatus

    @EncryptStatus.setter
    def EncryptStatus(self, EncryptStatus):
        self._EncryptStatus = EncryptStatus

    @property
    def ReplicaConfig(self):
        """Configuration information of DCN
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DCNReplicaConfig`
        """
        return self._ReplicaConfig

    @ReplicaConfig.setter
    def ReplicaConfig(self, ReplicaConfig):
        self._ReplicaConfig = ReplicaConfig

    @property
    def ReplicaStatus(self):
        """Running status of DCN
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DCNReplicaStatus`
        """
        return self._ReplicaStatus

    @ReplicaStatus.setter
    def ReplicaStatus(self, ReplicaStatus):
        self._ReplicaStatus = ReplicaStatus

    @property
    def ExclusterType(self):
        """Type of dedicated cluster. Valid values: `0` (public cloud), `1` (finance cage), `2` (CDC cluster).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ExclusterType

    @ExclusterType.setter
    def ExclusterType(self, ExclusterType):
        self._ExclusterType = ExclusterType

    @property
    def RsAccessStrategy(self):
        """Nearby VPC access
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RsAccessStrategy

    @RsAccessStrategy.setter
    def RsAccessStrategy(self, RsAccessStrategy):
        self._RsAccessStrategy = RsAccessStrategy

    @property
    def ReservedNetResources(self):
        """Unclaimed network resource
        :rtype: list of ReservedNetResource
        """
        return self._ReservedNetResources

    @ReservedNetResources.setter
    def ReservedNetResources(self, ReservedNetResources):
        self._ReservedNetResources = ReservedNetResources

    @property
    def IsPhysicalReplicationSupported(self):
        """Whether physical replication is supported.
        :rtype: bool
        """
        return self._IsPhysicalReplicationSupported

    @IsPhysicalReplicationSupported.setter
    def IsPhysicalReplicationSupported(self, IsPhysicalReplicationSupported):
        self._IsPhysicalReplicationSupported = IsPhysicalReplicationSupported

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
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._IsTmp = params.get("IsTmp")
        self._NodeCount = params.get("NodeCount")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._WanStatus = params.get("WanStatus")
        self._WanDomain = params.get("WanDomain")
        self._WanVip = params.get("WanVip")
        self._WanPort = params.get("WanPort")
        self._ProjectId = params.get("ProjectId")
        self._TdsqlVersion = params.get("TdsqlVersion")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._MasterZone = params.get("MasterZone")
        self._SlaveZones = params.get("SlaveZones")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._ExclusterId = params.get("ExclusterId")
        self._PayMode = params.get("PayMode")
        self._CreateTime = params.get("CreateTime")
        self._IsAuditSupported = params.get("IsAuditSupported")
        self._PeriodEndTime = params.get("PeriodEndTime")
        self._Machine = params.get("Machine")
        self._StorageUsage = params.get("StorageUsage")
        self._LogStorage = params.get("LogStorage")
        self._IsEncryptSupported = params.get("IsEncryptSupported")
        self._Vip6 = params.get("Vip6")
        self._Cpu = params.get("Cpu")
        self._Pid = params.get("Pid")
        self._Qps = params.get("Qps")
        self._Ipv6Flag = params.get("Ipv6Flag")
        self._WanVipv6 = params.get("WanVipv6")
        self._WanStatusIpv6 = params.get("WanStatusIpv6")
        self._WanPortIpv6 = params.get("WanPortIpv6")
        self._DbEngine = params.get("DbEngine")
        self._DbVersion = params.get("DbVersion")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._DcnFlag = params.get("DcnFlag")
        self._DcnStatus = params.get("DcnStatus")
        self._DcnDstNum = params.get("DcnDstNum")
        self._InstanceType = params.get("InstanceType")
        if params.get("NodesInfo") is not None:
            self._NodesInfo = []
            for item in params.get("NodesInfo"):
                obj = NodeInfo()
                obj._deserialize(item)
                self._NodesInfo.append(obj)
        self._IsMaxUserConnectionsSupported = params.get("IsMaxUserConnectionsSupported")
        self._DbVersionId = params.get("DbVersionId")
        self._EncryptStatus = params.get("EncryptStatus")
        if params.get("ReplicaConfig") is not None:
            self._ReplicaConfig = DCNReplicaConfig()
            self._ReplicaConfig._deserialize(params.get("ReplicaConfig"))
        if params.get("ReplicaStatus") is not None:
            self._ReplicaStatus = DCNReplicaStatus()
            self._ReplicaStatus._deserialize(params.get("ReplicaStatus"))
        self._ExclusterType = params.get("ExclusterType")
        self._RsAccessStrategy = params.get("RsAccessStrategy")
        if params.get("ReservedNetResources") is not None:
            self._ReservedNetResources = []
            for item in params.get("ReservedNetResources"):
                obj = ReservedNetResource()
                obj._deserialize(item)
                self._ReservedNetResources.append(obj)
        self._IsPhysicalReplicationSupported = params.get("IsPhysicalReplicationSupported")
        self._RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Queries by instance ID or IDs. Instance ID is in the format of `tdsql-ow728lmc`. Up to 100 instances can be queried in one request.
        :type InstanceIds: list of str
        :param _SearchName: Search field name. Valid values: instancename (search by instance name), vip (search by private IP), all (search by instance ID, instance name, and private IP).
        :type SearchName: str
        :param _SearchKey: Search keyword. Fuzzy search is supported. Multiple keywords should be separated by line breaks (`\n`).
        :type SearchKey: str
        :param _ProjectIds: Queries by project ID
        :type ProjectIds: list of int
        :param _IsFilterVpc: Whether to search by VPC
        :type IsFilterVpc: bool
        :param _VpcId: VPC ID, which is valid when `IsFilterVpc` is 1
        :type VpcId: str
        :param _SubnetId: VPC subnet ID, which is valid when `IsFilterVpc` is 1
        :type SubnetId: str
        :param _OrderBy: Sort by field. Valid values: projectId, createtime, instancename
        :type OrderBy: str
        :param _OrderByType: Sorting order. Valid values: desc, asc
        :type OrderByType: str
        :param _Offset: Offset. Default value: 0
        :type Offset: int
        :param _Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _OriginSerialIds: Queries by `OriginSerialId`
        :type OriginSerialIds: list of str
        :param _IsFilterExcluster: Identifies whether to use the `ExclusterType` field. false: no, true: yes
        :type IsFilterExcluster: bool
        :param _ExclusterType: Instance cluster type. 1: non-dedicated cluster, 2: dedicated cluster, 0: all
        :type ExclusterType: int
        :param _ExclusterIds: Filters instances by dedicated cluster ID in the format of `dbdc-4ih6uct9`
        :type ExclusterIds: list of str
        :param _TagKeys: Tag key used in queries
        :type TagKeys: list of str
        :param _FilterInstanceType: Instance types used in filtering. Valid values: 1 (dedicated instance), 2 (primary instance), 3 (disaster recovery instance). Multiple values should be separated by commas.
        :type FilterInstanceType: str
        :param _Status: Use this filter to include instances in specific statuses
        :type Status: list of int
        :param _ExcludeStatus: Use this filter to exclude instances in specific statuses
        :type ExcludeStatus: list of int
        """
        self._InstanceIds = None
        self._SearchName = None
        self._SearchKey = None
        self._ProjectIds = None
        self._IsFilterVpc = None
        self._VpcId = None
        self._SubnetId = None
        self._OrderBy = None
        self._OrderByType = None
        self._Offset = None
        self._Limit = None
        self._OriginSerialIds = None
        self._IsFilterExcluster = None
        self._ExclusterType = None
        self._ExclusterIds = None
        self._TagKeys = None
        self._FilterInstanceType = None
        self._Status = None
        self._ExcludeStatus = None

    @property
    def InstanceIds(self):
        """Queries by instance ID or IDs. Instance ID is in the format of `tdsql-ow728lmc`. Up to 100 instances can be queried in one request.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def SearchName(self):
        """Search field name. Valid values: instancename (search by instance name), vip (search by private IP), all (search by instance ID, instance name, and private IP).
        :rtype: str
        """
        return self._SearchName

    @SearchName.setter
    def SearchName(self, SearchName):
        self._SearchName = SearchName

    @property
    def SearchKey(self):
        """Search keyword. Fuzzy search is supported. Multiple keywords should be separated by line breaks (`\n`).
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def ProjectIds(self):
        """Queries by project ID
        :rtype: list of int
        """
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def IsFilterVpc(self):
        """Whether to search by VPC
        :rtype: bool
        """
        return self._IsFilterVpc

    @IsFilterVpc.setter
    def IsFilterVpc(self, IsFilterVpc):
        self._IsFilterVpc = IsFilterVpc

    @property
    def VpcId(self):
        """VPC ID, which is valid when `IsFilterVpc` is 1
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """VPC subnet ID, which is valid when `IsFilterVpc` is 1
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def OrderBy(self):
        """Sort by field. Valid values: projectId, createtime, instancename
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        """Sorting order. Valid values: desc, asc
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Offset(self):
        """Offset. Default value: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

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
    def OriginSerialIds(self):
        """Queries by `OriginSerialId`
        :rtype: list of str
        """
        return self._OriginSerialIds

    @OriginSerialIds.setter
    def OriginSerialIds(self, OriginSerialIds):
        self._OriginSerialIds = OriginSerialIds

    @property
    def IsFilterExcluster(self):
        """Identifies whether to use the `ExclusterType` field. false: no, true: yes
        :rtype: bool
        """
        return self._IsFilterExcluster

    @IsFilterExcluster.setter
    def IsFilterExcluster(self, IsFilterExcluster):
        self._IsFilterExcluster = IsFilterExcluster

    @property
    def ExclusterType(self):
        """Instance cluster type. 1: non-dedicated cluster, 2: dedicated cluster, 0: all
        :rtype: int
        """
        return self._ExclusterType

    @ExclusterType.setter
    def ExclusterType(self, ExclusterType):
        self._ExclusterType = ExclusterType

    @property
    def ExclusterIds(self):
        """Filters instances by dedicated cluster ID in the format of `dbdc-4ih6uct9`
        :rtype: list of str
        """
        return self._ExclusterIds

    @ExclusterIds.setter
    def ExclusterIds(self, ExclusterIds):
        self._ExclusterIds = ExclusterIds

    @property
    def TagKeys(self):
        """Tag key used in queries
        :rtype: list of str
        """
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def FilterInstanceType(self):
        """Instance types used in filtering. Valid values: 1 (dedicated instance), 2 (primary instance), 3 (disaster recovery instance). Multiple values should be separated by commas.
        :rtype: str
        """
        return self._FilterInstanceType

    @FilterInstanceType.setter
    def FilterInstanceType(self, FilterInstanceType):
        self._FilterInstanceType = FilterInstanceType

    @property
    def Status(self):
        """Use this filter to include instances in specific statuses
        :rtype: list of int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ExcludeStatus(self):
        """Use this filter to exclude instances in specific statuses
        :rtype: list of int
        """
        return self._ExcludeStatus

    @ExcludeStatus.setter
    def ExcludeStatus(self, ExcludeStatus):
        self._ExcludeStatus = ExcludeStatus


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._SearchName = params.get("SearchName")
        self._SearchKey = params.get("SearchKey")
        self._ProjectIds = params.get("ProjectIds")
        self._IsFilterVpc = params.get("IsFilterVpc")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OriginSerialIds = params.get("OriginSerialIds")
        self._IsFilterExcluster = params.get("IsFilterExcluster")
        self._ExclusterType = params.get("ExclusterType")
        self._ExclusterIds = params.get("ExclusterIds")
        self._TagKeys = params.get("TagKeys")
        self._FilterInstanceType = params.get("FilterInstanceType")
        self._Status = params.get("Status")
        self._ExcludeStatus = params.get("ExcludeStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstancesResponse(AbstractModel):
    """DescribeDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible instances
        :type TotalCount: int
        :param _Instances: Instance details list
        :type Instances: list of DBInstance
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Instances = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of eligible instances
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Instances(self):
        """Instance details list
        :rtype: list of DBInstance
        """
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

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
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = DBInstance()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBLogFilesRequest(AbstractModel):
    """DescribeDBLogFiles request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of `tdsql-ow728lmc`.
        :type InstanceId: str
        :param _Type: Requested log type. Valid values: 1 (binlog), 2 (cold backup), 3 (errlog), 4 (slowlog).
        :type Type: int
        """
        self._InstanceId = None
        self._Type = None

    @property
    def InstanceId(self):
        """Instance ID in the format of `tdsql-ow728lmc`.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Type(self):
        """Requested log type. Valid values: 1 (binlog), 2 (cold backup), 3 (errlog), 4 (slowlog).
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBLogFilesResponse(AbstractModel):
    """DescribeDBLogFiles response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of `tdsql-ow728lmc`.
        :type InstanceId: str
        :param _Type: Requested log type. Valid values: 1 (binlog), 2 (cold backup), 3 (errlog), 4 (slowlog).
        :type Type: int
        :param _Total: Total number of requested logs
        :type Total: int
        :param _Files: Information such as `uri`, `length`, and `mtime` (modification time)
        :type Files: list of LogFileInfo
        :param _VpcPrefix: For an instance in a VPC, this prefix plus URI can be used as the download address
        :type VpcPrefix: str
        :param _NormalPrefix: For an instance in a common network, this prefix plus URI can be used as the download address
        :type NormalPrefix: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._Type = None
        self._Total = None
        self._Files = None
        self._VpcPrefix = None
        self._NormalPrefix = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """Instance ID in the format of `tdsql-ow728lmc`.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Type(self):
        """Requested log type. Valid values: 1 (binlog), 2 (cold backup), 3 (errlog), 4 (slowlog).
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Total(self):
        """Total number of requested logs
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Files(self):
        """Information such as `uri`, `length`, and `mtime` (modification time)
        :rtype: list of LogFileInfo
        """
        return self._Files

    @Files.setter
    def Files(self, Files):
        self._Files = Files

    @property
    def VpcPrefix(self):
        """For an instance in a VPC, this prefix plus URI can be used as the download address
        :rtype: str
        """
        return self._VpcPrefix

    @VpcPrefix.setter
    def VpcPrefix(self, VpcPrefix):
        self._VpcPrefix = VpcPrefix

    @property
    def NormalPrefix(self):
        """For an instance in a common network, this prefix plus URI can be used as the download address
        :rtype: str
        """
        return self._NormalPrefix

    @NormalPrefix.setter
    def NormalPrefix(self, NormalPrefix):
        self._NormalPrefix = NormalPrefix

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
        self._InstanceId = params.get("InstanceId")
        self._Type = params.get("Type")
        self._Total = params.get("Total")
        if params.get("Files") is not None:
            self._Files = []
            for item in params.get("Files"):
                obj = LogFileInfo()
                obj._deserialize(item)
                self._Files.append(obj)
        self._VpcPrefix = params.get("VpcPrefix")
        self._NormalPrefix = params.get("NormalPrefix")
        self._RequestId = params.get("RequestId")


class DescribeDBParametersRequest(AbstractModel):
    """DescribeDBParameters request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of `tdsql-ow728lmc`.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Instance ID in the format of `tdsql-ow728lmc`.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBParametersResponse(AbstractModel):
    """DescribeDBParameters response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of `tdsql-ow728lmc`.
        :type InstanceId: str
        :param _Params: Requests the current parameter values of the database
        :type Params: list of ParamDesc
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._Params = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """Instance ID in the format of `tdsql-ow728lmc`.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Params(self):
        """Requests the current parameter values of the database
        :rtype: list of ParamDesc
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params

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
        self._InstanceId = params.get("InstanceId")
        if params.get("Params") is not None:
            self._Params = []
            for item in params.get("Params"):
                obj = ParamDesc()
                obj._deserialize(item)
                self._Params.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBSecurityGroupsRequest(AbstractModel):
    """DescribeDBSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _Product: Database engine name. Valid value: `mariadb`.
        :type Product: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._Product = None
        self._InstanceId = None

    @property
    def Product(self):
        """Database engine name. Valid value: `mariadb`.
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceId(self):
        """Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSecurityGroupsResponse(AbstractModel):
    """DescribeDBSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param _Groups: Security group details
        :type Groups: list of SecurityGroup
        :param _VIP: Instance VIP
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type VIP: str
        :param _VPort: Instance port
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type VPort: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Groups = None
        self._VIP = None
        self._VPort = None
        self._RequestId = None

    @property
    def Groups(self):
        """Security group details
        :rtype: list of SecurityGroup
        """
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def VIP(self):
        """Instance VIP
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VIP

    @VIP.setter
    def VIP(self, VIP):
        self._VIP = VIP

    @property
    def VPort(self):
        """Instance port
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

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
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._VIP = params.get("VIP")
        self._VPort = params.get("VPort")
        self._RequestId = params.get("RequestId")


class DescribeDBSlowLogsRequest(AbstractModel):
    """DescribeDBSlowLogs request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of `tdsql-ow728lmc`.
        :type InstanceId: str
        :param _Offset: Data entry number starting from which to return results
        :type Offset: int
        :param _Limit: Number of results to be returned
        :type Limit: int
        :param _StartTime: Query start time in the format of 2016-07-23 14:55:20
        :type StartTime: str
        :param _EndTime: Query end time in the format of 2016-08-22 14:55:20
        :type EndTime: str
        :param _Db: Specific name of the database to be queried
        :type Db: str
        :param _OrderBy: Sorting metric. Valid values: query_time_sum, query_count
        :type OrderBy: str
        :param _OrderByType: Sorting order. Valid values: desc, asc
        :type OrderByType: str
        :param _Slave: Query slow queries from either the primary or the replica. Valid values: 0 (primary), 1 (replica)
        :type Slave: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._StartTime = None
        self._EndTime = None
        self._Db = None
        self._OrderBy = None
        self._OrderByType = None
        self._Slave = None

    @property
    def InstanceId(self):
        """Instance ID in the format of `tdsql-ow728lmc`.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        """Data entry number starting from which to return results
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of results to be returned
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def StartTime(self):
        """Query start time in the format of 2016-07-23 14:55:20
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Query end time in the format of 2016-08-22 14:55:20
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Db(self):
        """Specific name of the database to be queried
        :rtype: str
        """
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def OrderBy(self):
        """Sorting metric. Valid values: query_time_sum, query_count
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        """Sorting order. Valid values: desc, asc
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Slave(self):
        """Query slow queries from either the primary or the replica. Valid values: 0 (primary), 1 (replica)
        :rtype: int
        """
        return self._Slave

    @Slave.setter
    def Slave(self, Slave):
        self._Slave = Slave


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Db = params.get("Db")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._Slave = params.get("Slave")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSlowLogsResponse(AbstractModel):
    """DescribeDBSlowLogs response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Slow query log data
        :type Data: list of SlowLogData
        :param _LockTimeSum: Total statement lock time
        :type LockTimeSum: float
        :param _QueryCount: Total number of statement queries
        :type QueryCount: int
        :param _Total: Total number of results
        :type Total: int
        :param _QueryTimeSum: Total statement query time
        :type QueryTimeSum: float
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._LockTimeSum = None
        self._QueryCount = None
        self._Total = None
        self._QueryTimeSum = None
        self._RequestId = None

    @property
    def Data(self):
        """Slow query log data
        :rtype: list of SlowLogData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def LockTimeSum(self):
        """Total statement lock time
        :rtype: float
        """
        return self._LockTimeSum

    @LockTimeSum.setter
    def LockTimeSum(self, LockTimeSum):
        self._LockTimeSum = LockTimeSum

    @property
    def QueryCount(self):
        """Total number of statement queries
        :rtype: int
        """
        return self._QueryCount

    @QueryCount.setter
    def QueryCount(self, QueryCount):
        self._QueryCount = QueryCount

    @property
    def Total(self):
        """Total number of results
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def QueryTimeSum(self):
        """Total statement query time
        :rtype: float
        """
        return self._QueryTimeSum

    @QueryTimeSum.setter
    def QueryTimeSum(self, QueryTimeSum):
        self._QueryTimeSum = QueryTimeSum

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
            self._Data = []
            for item in params.get("Data"):
                obj = SlowLogData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._LockTimeSum = params.get("LockTimeSum")
        self._QueryCount = params.get("QueryCount")
        self._Total = params.get("Total")
        self._QueryTimeSum = params.get("QueryTimeSum")
        self._RequestId = params.get("RequestId")


class DescribeDBTmpInstancesRequest(AbstractModel):
    """DescribeDBTmpInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBTmpInstancesResponse(AbstractModel):
    """DescribeDBTmpInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TmpInstances: Temp instance
        :type TmpInstances: list of TmpInstance
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TmpInstances = None
        self._RequestId = None

    @property
    def TmpInstances(self):
        """Temp instance
        :rtype: list of TmpInstance
        """
        return self._TmpInstances

    @TmpInstances.setter
    def TmpInstances(self, TmpInstances):
        self._TmpInstances = TmpInstances

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
        if params.get("TmpInstances") is not None:
            self._TmpInstances = []
            for item in params.get("TmpInstances"):
                obj = TmpInstance()
                obj._deserialize(item)
                self._TmpInstances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDatabaseObjectsRequest(AbstractModel):
    """DescribeDatabaseObjects request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of `dcdbt-ow7t8lmc`.
        :type InstanceId: str
        :param _DbName: Database name, which can be obtained through the `DescribeDatabases` API.
        :type DbName: str
        """
        self._InstanceId = None
        self._DbName = None

    @property
    def InstanceId(self):
        """Instance ID in the format of `dcdbt-ow7t8lmc`.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbName(self):
        """Database name, which can be obtained through the `DescribeDatabases` API.
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DbName = params.get("DbName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabaseObjectsResponse(AbstractModel):
    """DescribeDatabaseObjects response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Passed through from input parameters.
        :type InstanceId: str
        :param _DbName: Database name.
        :type DbName: str
        :param _Tables: Table list.
        :type Tables: list of DatabaseTable
        :param _Views: View list.
        :type Views: list of DatabaseView
        :param _Procs: Stored procedure list.
        :type Procs: list of DatabaseProcedure
        :param _Funcs: Function list.
        :type Funcs: list of DatabaseFunction
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._DbName = None
        self._Tables = None
        self._Views = None
        self._Procs = None
        self._Funcs = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """Passed through from input parameters.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbName(self):
        """Database name.
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Tables(self):
        """Table list.
        :rtype: list of DatabaseTable
        """
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables

    @property
    def Views(self):
        """View list.
        :rtype: list of DatabaseView
        """
        return self._Views

    @Views.setter
    def Views(self, Views):
        self._Views = Views

    @property
    def Procs(self):
        """Stored procedure list.
        :rtype: list of DatabaseProcedure
        """
        return self._Procs

    @Procs.setter
    def Procs(self, Procs):
        self._Procs = Procs

    @property
    def Funcs(self):
        """Function list.
        :rtype: list of DatabaseFunction
        """
        return self._Funcs

    @Funcs.setter
    def Funcs(self, Funcs):
        self._Funcs = Funcs

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
        self._InstanceId = params.get("InstanceId")
        self._DbName = params.get("DbName")
        if params.get("Tables") is not None:
            self._Tables = []
            for item in params.get("Tables"):
                obj = DatabaseTable()
                obj._deserialize(item)
                self._Tables.append(obj)
        if params.get("Views") is not None:
            self._Views = []
            for item in params.get("Views"):
                obj = DatabaseView()
                obj._deserialize(item)
                self._Views.append(obj)
        if params.get("Procs") is not None:
            self._Procs = []
            for item in params.get("Procs"):
                obj = DatabaseProcedure()
                obj._deserialize(item)
                self._Procs.append(obj)
        if params.get("Funcs") is not None:
            self._Funcs = []
            for item in params.get("Funcs"):
                obj = DatabaseFunction()
                obj._deserialize(item)
                self._Funcs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDatabaseTableRequest(AbstractModel):
    """DescribeDatabaseTable request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of `dcdbt-ow7t8lmc`.
        :type InstanceId: str
        :param _DbName: Database name, which can be obtained through the `DescribeDatabases` API.
        :type DbName: str
        :param _Table: Table name, which can be obtained through the `DescribeDatabaseObjects` API.
        :type Table: str
        """
        self._InstanceId = None
        self._DbName = None
        self._Table = None

    @property
    def InstanceId(self):
        """Instance ID in the format of `dcdbt-ow7t8lmc`.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbName(self):
        """Database name, which can be obtained through the `DescribeDatabases` API.
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Table(self):
        """Table name, which can be obtained through the `DescribeDatabaseObjects` API.
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DbName = params.get("DbName")
        self._Table = params.get("Table")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabaseTableResponse(AbstractModel):
    """DescribeDatabaseTable response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance name.
        :type InstanceId: str
        :param _DbName: Database name.
        :type DbName: str
        :param _Table: Table name.
        :type Table: str
        :param _Cols: Column information.
        :type Cols: list of TableColumn
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._DbName = None
        self._Table = None
        self._Cols = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """Instance name.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbName(self):
        """Database name.
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Table(self):
        """Table name.
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Cols(self):
        """Column information.
        :rtype: list of TableColumn
        """
        return self._Cols

    @Cols.setter
    def Cols(self, Cols):
        self._Cols = Cols

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
        self._InstanceId = params.get("InstanceId")
        self._DbName = params.get("DbName")
        self._Table = params.get("Table")
        if params.get("Cols") is not None:
            self._Cols = []
            for item in params.get("Cols"):
                obj = TableColumn()
                obj._deserialize(item)
                self._Cols.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDatabasesRequest(AbstractModel):
    """DescribeDatabases request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of `dcdbt-ow7t8lmc`.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Instance ID in the format of `dcdbt-ow7t8lmc`.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabasesResponse(AbstractModel):
    """DescribeDatabases response structure.

    """

    def __init__(self):
        r"""
        :param _Databases: The database list of this instance.
        :type Databases: list of Database
        :param _InstanceId: Passed through from input parameters.
        :type InstanceId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Databases = None
        self._InstanceId = None
        self._RequestId = None

    @property
    def Databases(self):
        """The database list of this instance.
        :rtype: list of Database
        """
        return self._Databases

    @Databases.setter
    def Databases(self, Databases):
        self._Databases = Databases

    @property
    def InstanceId(self):
        """Passed through from input parameters.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        if params.get("Databases") is not None:
            self._Databases = []
            for item in params.get("Databases"):
                obj = Database()
                obj._deserialize(item)
                self._Databases.append(obj)
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class DescribeDcnDetailRequest(AbstractModel):
    """DescribeDcnDetail request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDcnDetailResponse(AbstractModel):
    """DescribeDcnDetail response structure.

    """

    def __init__(self):
        r"""
        :param _DcnDetails: DCN synchronization details
        :type DcnDetails: list of DcnDetailItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DcnDetails = None
        self._RequestId = None

    @property
    def DcnDetails(self):
        """DCN synchronization details
        :rtype: list of DcnDetailItem
        """
        return self._DcnDetails

    @DcnDetails.setter
    def DcnDetails(self, DcnDetails):
        self._DcnDetails = DcnDetails

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
        if params.get("DcnDetails") is not None:
            self._DcnDetails = []
            for item in params.get("DcnDetails"):
                obj = DcnDetailItem()
                obj._deserialize(item)
                self._DcnDetails.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFileDownloadUrlRequest(AbstractModel):
    """DescribeFileDownloadUrl request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _FilePath: Unsigned file path
        :type FilePath: str
        """
        self._InstanceId = None
        self._FilePath = None

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
    def FilePath(self):
        """Unsigned file path
        :rtype: str
        """
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._FilePath = params.get("FilePath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileDownloadUrlResponse(AbstractModel):
    """DescribeFileDownloadUrl response structure.

    """

    def __init__(self):
        r"""
        :param _PreSignedUrl: Signed download URL
        :type PreSignedUrl: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PreSignedUrl = None
        self._RequestId = None

    @property
    def PreSignedUrl(self):
        """Signed download URL
        :rtype: str
        """
        return self._PreSignedUrl

    @PreSignedUrl.setter
    def PreSignedUrl(self, PreSignedUrl):
        self._PreSignedUrl = PreSignedUrl

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
        self._PreSignedUrl = params.get("PreSignedUrl")
        self._RequestId = params.get("RequestId")


class DescribeInstanceNodeInfoRequest(AbstractModel):
    """DescribeInstanceNodeInfo request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, such as tdsql-6ltok4u9
        :type InstanceId: str
        :param _Limit: The maximum number of results returned at a time. By default, there is no upper limit to this value, that is, all results can be returned.
        :type Limit: int
        :param _Offset: Offset of the returned results. Default value: `0`.
        :type Offset: int
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        """Instance ID, such as tdsql-6ltok4u9
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        """The maximum number of results returned at a time. By default, there is no upper limit to this value, that is, all results can be returned.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset of the returned results. Default value: `0`.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceNodeInfoResponse(AbstractModel):
    """DescribeInstanceNodeInfo response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of nodes
        :type TotalCount: int
        :param _NodesInfo: Node information
        :type NodesInfo: list of NodeInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._NodesInfo = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of nodes
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def NodesInfo(self):
        """Node information
        :rtype: list of NodeInfo
        """
        return self._NodesInfo

    @NodesInfo.setter
    def NodesInfo(self, NodesInfo):
        self._NodesInfo = NodesInfo

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
        if params.get("NodesInfo") is not None:
            self._NodesInfo = []
            for item in params.get("NodesInfo"):
                obj = NodeInfo()
                obj._deserialize(item)
                self._NodesInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLogFileRetentionPeriodRequest(AbstractModel):
    """DescribeLogFileRetentionPeriod request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of `tdsql-ow728lmc`
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Instance ID in the format of `tdsql-ow728lmc`
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogFileRetentionPeriodResponse(AbstractModel):
    """DescribeLogFileRetentionPeriod response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of `tdsql-ow728lmc`
        :type InstanceId: str
        :param _Days: Backup log retention days
        :type Days: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._Days = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """Instance ID in the format of `tdsql-ow728lmc`
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Days(self):
        """Backup log retention days
        :rtype: int
        """
        return self._Days

    @Days.setter
    def Days(self, Days):
        self._Days = Days

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
        self._InstanceId = params.get("InstanceId")
        self._Days = params.get("Days")
        self._RequestId = params.get("RequestId")


class DescribeOrdersRequest(AbstractModel):
    """DescribeOrders request structure.

    """

    def __init__(self):
        r"""
        :param _DealNames: List of long order numbers to be queried, which are returned for the APIs for creating, renewing, or scaling instances.
        :type DealNames: list of str
        """
        self._DealNames = None

    @property
    def DealNames(self):
        """List of long order numbers to be queried, which are returned for the APIs for creating, renewing, or scaling instances.
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames


    def _deserialize(self, params):
        self._DealNames = params.get("DealNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrdersResponse(AbstractModel):
    """DescribeOrders response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Returned number of orders.
        :type TotalCount: int
        :param _Deals: Order information list.
        :type Deals: list of Deal
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Deals = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Returned number of orders.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Deals(self):
        """Order information list.
        :rtype: list of Deal
        """
        return self._Deals

    @Deals.setter
    def Deals(self, Deals):
        self._Deals = Deals

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
        if params.get("Deals") is not None:
            self._Deals = []
            for item in params.get("Deals"):
                obj = Deal()
                obj._deserialize(item)
                self._Deals.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePriceRequest(AbstractModel):
    """DescribePrice request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: AZ ID of the purchased instance.
        :type Zone: str
        :param _NodeCount: Number of instance nodes, which can be obtained 
 by querying the instance specification through the `DescribeDBInstanceSpecs` API.
        :type NodeCount: int
        :param _Memory: Memory size in GB, which can be obtained 
 by querying the instance specification through the `DescribeDBInstanceSpecs` API.
        :type Memory: int
        :param _Storage: Storage capacity in GB. The maximum and minimum storage space can be obtained 
 by querying instance specification through the `DescribeDBInstanceSpecs` API.
        :type Storage: int
        :param _Period: Purchase period in months
        :type Period: int
        :param _Count: The number of instances to be purchased. Only one instance is queried for price by default.
        :type Count: int
        :param _Paymode: Billing type. Valid values: `postpaid` (pay-as-you-go), `prepaid` (monthly subscription).
        :type Paymode: str
        :param _AmountUnit: Price unit. Valid values:   
`* pent` (cent), 
`* microPent` (microcent).
        :type AmountUnit: str
        """
        self._Zone = None
        self._NodeCount = None
        self._Memory = None
        self._Storage = None
        self._Period = None
        self._Count = None
        self._Paymode = None
        self._AmountUnit = None

    @property
    def Zone(self):
        """AZ ID of the purchased instance.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def NodeCount(self):
        """Number of instance nodes, which can be obtained 
 by querying the instance specification through the `DescribeDBInstanceSpecs` API.
        :rtype: int
        """
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def Memory(self):
        """Memory size in GB, which can be obtained 
 by querying the instance specification through the `DescribeDBInstanceSpecs` API.
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        """Storage capacity in GB. The maximum and minimum storage space can be obtained 
 by querying instance specification through the `DescribeDBInstanceSpecs` API.
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def Period(self):
        """Purchase period in months
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Count(self):
        """The number of instances to be purchased. Only one instance is queried for price by default.
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Paymode(self):
        """Billing type. Valid values: `postpaid` (pay-as-you-go), `prepaid` (monthly subscription).
        :rtype: str
        """
        return self._Paymode

    @Paymode.setter
    def Paymode(self, Paymode):
        self._Paymode = Paymode

    @property
    def AmountUnit(self):
        """Price unit. Valid values:   
`* pent` (cent), 
`* microPent` (microcent).
        :rtype: str
        """
        return self._AmountUnit

    @AmountUnit.setter
    def AmountUnit(self, AmountUnit):
        self._AmountUnit = AmountUnit


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._NodeCount = params.get("NodeCount")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._Period = params.get("Period")
        self._Count = params.get("Count")
        self._Paymode = params.get("Paymode")
        self._AmountUnit = params.get("AmountUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePriceResponse(AbstractModel):
    """DescribePrice response structure.

    """

    def __init__(self):
        r"""
        :param _OriginalPrice: Original price  
* Unit: Cent (default). If the request parameter contains `AmountUnit`, see `AmountUnit` description.
* Currency: CNY (Chinese site), USD (international site)
        :type OriginalPrice: int
        :param _Price: The actual price may be different from the original price due to discounts. 
* Unit: Cent (default). If the request parameter contains `AmountUnit`, see `AmountUnit` description.
* Currency: CNY (Chinese site), USD (international site)
        :type Price: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OriginalPrice = None
        self._Price = None
        self._RequestId = None

    @property
    def OriginalPrice(self):
        """Original price  
* Unit: Cent (default). If the request parameter contains `AmountUnit`, see `AmountUnit` description.
* Currency: CNY (Chinese site), USD (international site)
        :rtype: int
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def Price(self):
        """The actual price may be different from the original price due to discounts. 
* Unit: Cent (default). If the request parameter contains `AmountUnit`, see `AmountUnit` description.
* Currency: CNY (Chinese site), USD (international site)
        :rtype: int
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

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
        self._OriginalPrice = params.get("OriginalPrice")
        self._Price = params.get("Price")
        self._RequestId = params.get("RequestId")


class DescribeProjectSecurityGroupsRequest(AbstractModel):
    """DescribeProjectSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _Product: Database engine name. Valid value: `mariadb`.
        :type Product: str
        :param _ProjectId: Project ID
        :type ProjectId: int
        """
        self._Product = None
        self._ProjectId = None

    @property
    def Product(self):
        """Database engine name. Valid value: `mariadb`.
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def ProjectId(self):
        """Project ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectSecurityGroupsResponse(AbstractModel):
    """DescribeProjectSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param _Groups: Security group details
        :type Groups: list of SecurityGroup
        :param _Total: Total number of security groups.
        :type Total: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Groups = None
        self._Total = None
        self._RequestId = None

    @property
    def Groups(self):
        """Security group details
        :rtype: list of SecurityGroup
        """
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def Total(self):
        """Total number of security groups.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DestroyDBInstanceRequest(AbstractModel):
    """DestroyDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of “tdsqlshard-c1nl9rpv”. It is the same as the instance ID displayed in the TencentDB for MariaDB console.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Instance ID in the format of “tdsqlshard-c1nl9rpv”. It is the same as the instance ID displayed in the TencentDB for MariaDB console.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyDBInstanceResponse(AbstractModel):
    """DestroyDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, which is the same as the request parameter `InstanceId`.
        :type InstanceId: str
        :param _FlowId: Async task ID, which can be used in the [DescribeFlow](https://intl.cloud.tencent.com/document/product/557/56485?from_cn_redirect=1) API to query the async task result.
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._FlowId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """Instance ID, which is the same as the request parameter `InstanceId`.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FlowId(self):
        """Async task ID, which can be used in the [DescribeFlow](https://intl.cloud.tencent.com/document/product/557/56485?from_cn_redirect=1) API to query the async task result.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._InstanceId = params.get("InstanceId")
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class DestroyHourDBInstanceRequest(AbstractModel):
    """DestroyHourDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of tdsql-avw0207d. It is the same as the instance ID displayed in the TencentDB console.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Instance ID in the format of tdsql-avw0207d. It is the same as the instance ID displayed in the TencentDB console.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyHourDBInstanceResponse(AbstractModel):
    """DestroyHourDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task ID, which can be used in the [DescribeFlow](https://intl.cloud.tencent.com/document/product/237/16177?from_cn_redirect=1) API to query the async task result.
        :type FlowId: int
        :param _InstanceId: Instance ID, which is the same as the request parameter `InstanceId`.
        :type InstanceId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._InstanceId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Async task ID, which can be used in the [DescribeFlow](https://intl.cloud.tencent.com/document/product/237/16177?from_cn_redirect=1) API to query the async task result.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceId(self):
        """Instance ID, which is the same as the request parameter `InstanceId`.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._FlowId = params.get("FlowId")
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _Product: Database engine name. Valid value: `mariadb`.
        :type Product: str
        :param _SecurityGroupId: Security group ID
        :type SecurityGroupId: str
        :param _InstanceIds: Instance ID list, which is an array of one or more instance IDs.
        :type InstanceIds: list of str
        """
        self._Product = None
        self._SecurityGroupId = None
        self._InstanceIds = None

    @property
    def Product(self):
        """Database engine name. Valid value: `mariadb`.
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def SecurityGroupId(self):
        """Security group ID
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def InstanceIds(self):
        """Instance ID list, which is an array of one or more instance IDs.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateSecurityGroupsResponse(AbstractModel):
    """DisassociateSecurityGroups response structure.

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


class FunctionPrivilege(AbstractModel):
    """Function permission information

    """

    def __init__(self):
        r"""
        :param _Database: Database name
        :type Database: str
        :param _FunctionName: Function name
        :type FunctionName: str
        :param _Privileges: Permission information
        :type Privileges: list of str
        """
        self._Database = None
        self._FunctionName = None
        self._Privileges = None

    @property
    def Database(self):
        """Database name
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def FunctionName(self):
        """Function name
        :rtype: str
        """
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Privileges(self):
        """Permission information
        :rtype: list of str
        """
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._FunctionName = params.get("FunctionName")
        self._Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrantAccountPrivilegesRequest(AbstractModel):
    """GrantAccountPrivileges request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :type InstanceId: str
        :param _UserName: Login username.
        :type UserName: str
        :param _Host: Access host allowed for user. An account is uniquely identified by username and host.
        :type Host: str
        :param _DbName: Database name. `\*` indicates that global permissions will be set (i.e., `\*.\*`), in which case the `Type` and `Object ` parameters will be ignored. If `DbName` is not `\*`, the input parameter `Type` is required.
        :type DbName: str
        :param _Privileges: Global permission. Valid values: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`, `REFERENCES`, `INDEX`, `ALTER`, `CREATE TEMPORARY TABLES`, `LOCK TABLES`, `EXECUTE`, `CREATE VIEW`, `SHOW VIEW`, `CREATE ROUTINE`, `ALTER ROUTINE`, `EVENT`, `TRIGGER`, `SHOW DATABASES`, `REPLICATION CLIENT`, `REPLICATION SLAVE`. 
Database permission. Valid values: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`, `REFERENCES`, `INDEX`, `ALTER`, `CREATE TEMPORARY TABLES`, `LOCK TABLES`, `EXECUTE`, `CREATE VIEW`, `SHOW VIEW`, `CREATE ROUTINE`, `ALTER ROUTINE`, `EVENT`, `TRIGGER`. 
Table/View permission. Valid values: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`, `REFERENCES`, `INDEX`, `ALTER`, `CREATE VIEW`, `SHOW VIEW`, `TRIGGER`. 
Stored procedure/function permission. Valid values: `ALTER ROUTINE`, `EXECUTE`. 
Field permission. Valid values: `INSERT`, `REFERENCES`, `SELECT`, `UPDATE`.
        :type Privileges: list of str
        :param _Type: Type. Valid values: table, view, proc, func, \*. If `DbName` is a specific database name and `Type` is `\*`, the permissions of the database will be set (i.e., `db.\*`), in which case the `Object` parameter will be ignored
        :type Type: str
        :param _Object: Type name. For example, if `Type` is `table`, `Object` indicates a specific table name; if both `DbName` and `Type` are specific names, it indicates a specific object name and cannot be `\*` or empty
        :type Object: str
        :param _ColName: If `Type` is `table` and `ColName` is `\*`, the permissions will be granted to the table; if `ColName` is a specific field name, the permissions will be granted to the field
        :type ColName: str
        """
        self._InstanceId = None
        self._UserName = None
        self._Host = None
        self._DbName = None
        self._Privileges = None
        self._Type = None
        self._Object = None
        self._ColName = None

    @property
    def InstanceId(self):
        """Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        """Login username.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        """Access host allowed for user. An account is uniquely identified by username and host.
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def DbName(self):
        """Database name. `\*` indicates that global permissions will be set (i.e., `\*.\*`), in which case the `Type` and `Object ` parameters will be ignored. If `DbName` is not `\*`, the input parameter `Type` is required.
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Privileges(self):
        """Global permission. Valid values: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`, `REFERENCES`, `INDEX`, `ALTER`, `CREATE TEMPORARY TABLES`, `LOCK TABLES`, `EXECUTE`, `CREATE VIEW`, `SHOW VIEW`, `CREATE ROUTINE`, `ALTER ROUTINE`, `EVENT`, `TRIGGER`, `SHOW DATABASES`, `REPLICATION CLIENT`, `REPLICATION SLAVE`. 
Database permission. Valid values: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`, `REFERENCES`, `INDEX`, `ALTER`, `CREATE TEMPORARY TABLES`, `LOCK TABLES`, `EXECUTE`, `CREATE VIEW`, `SHOW VIEW`, `CREATE ROUTINE`, `ALTER ROUTINE`, `EVENT`, `TRIGGER`. 
Table/View permission. Valid values: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`, `REFERENCES`, `INDEX`, `ALTER`, `CREATE VIEW`, `SHOW VIEW`, `TRIGGER`. 
Stored procedure/function permission. Valid values: `ALTER ROUTINE`, `EXECUTE`. 
Field permission. Valid values: `INSERT`, `REFERENCES`, `SELECT`, `UPDATE`.
        :rtype: list of str
        """
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges

    @property
    def Type(self):
        """Type. Valid values: table, view, proc, func, \*. If `DbName` is a specific database name and `Type` is `\*`, the permissions of the database will be set (i.e., `db.\*`), in which case the `Object` parameter will be ignored
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Object(self):
        """Type name. For example, if `Type` is `table`, `Object` indicates a specific table name; if both `DbName` and `Type` are specific names, it indicates a specific object name and cannot be `\*` or empty
        :rtype: str
        """
        return self._Object

    @Object.setter
    def Object(self, Object):
        self._Object = Object

    @property
    def ColName(self):
        """If `Type` is `table` and `ColName` is `\*`, the permissions will be granted to the table; if `ColName` is a specific field name, the permissions will be granted to the field
        :rtype: str
        """
        return self._ColName

    @ColName.setter
    def ColName(self, ColName):
        self._ColName = ColName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        self._DbName = params.get("DbName")
        self._Privileges = params.get("Privileges")
        self._Type = params.get("Type")
        self._Object = params.get("Object")
        self._ColName = params.get("ColName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrantAccountPrivilegesResponse(AbstractModel):
    """GrantAccountPrivileges response structure.

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


class InstanceBackupFileItem(AbstractModel):
    """Backup file details of an instance

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _InstanceStatus: Instance status
        :type InstanceStatus: int
        :param _ShardId: Shard ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ShardId: str
        :param _FilePath: File path
        :type FilePath: str
        :param _FileName: File name
        :type FileName: str
        :param _FileSize: File size
        :type FileSize: int
        :param _BackupType: Backup type. Valid values: `Data` (data backup), `Binlog` (Binlog backup), `Errlog` (error log), `Slowlog` (slow log).
        :type BackupType: str
        :param _ManualBackup: Manual backup. Valid values: `0` (no), `1` (yes).
        :type ManualBackup: int
        :param _StartTime: Backup start time
        :type StartTime: str
        :param _EndTime: Backup end time
        :type EndTime: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceStatus = None
        self._ShardId = None
        self._FilePath = None
        self._FileName = None
        self._FileSize = None
        self._BackupType = None
        self._ManualBackup = None
        self._StartTime = None
        self._EndTime = None

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
    def InstanceStatus(self):
        """Instance status
        :rtype: int
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def ShardId(self):
        """Shard ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ShardId

    @ShardId.setter
    def ShardId(self, ShardId):
        self._ShardId = ShardId

    @property
    def FilePath(self):
        """File path
        :rtype: str
        """
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath

    @property
    def FileName(self):
        """File name
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        """File size
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def BackupType(self):
        """Backup type. Valid values: `Data` (data backup), `Binlog` (Binlog backup), `Errlog` (error log), `Slowlog` (slow log).
        :rtype: str
        """
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def ManualBackup(self):
        """Manual backup. Valid values: `0` (no), `1` (yes).
        :rtype: int
        """
        return self._ManualBackup

    @ManualBackup.setter
    def ManualBackup(self, ManualBackup):
        self._ManualBackup = ManualBackup

    @property
    def StartTime(self):
        """Backup start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Backup end time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceStatus = params.get("InstanceStatus")
        self._ShardId = params.get("ShardId")
        self._FilePath = params.get("FilePath")
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._BackupType = params.get("BackupType")
        self._ManualBackup = params.get("ManualBackup")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateDBInstanceRequest(AbstractModel):
    """IsolateDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID in the format of `tdsql-dasjkhd`. It is the same as the instance ID displayed on the TencentDB console. You can use the `DescribeDBInstances` API to query the ID, which is the value of the `InstanceId` output parameter.
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        """Instance ID in the format of `tdsql-dasjkhd`. It is the same as the instance ID displayed on the TencentDB console. You can use the `DescribeDBInstances` API to query the ID, which is the value of the `InstanceId` output parameter.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateDBInstanceResponse(AbstractModel):
    """IsolateDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _SuccessInstanceIds: IDs of isolated instances
        :type SuccessInstanceIds: list of str
        :param _FailedInstanceIds: IDs of instances failed to be isolated
        :type FailedInstanceIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SuccessInstanceIds = None
        self._FailedInstanceIds = None
        self._RequestId = None

    @property
    def SuccessInstanceIds(self):
        """IDs of isolated instances
        :rtype: list of str
        """
        return self._SuccessInstanceIds

    @SuccessInstanceIds.setter
    def SuccessInstanceIds(self, SuccessInstanceIds):
        self._SuccessInstanceIds = SuccessInstanceIds

    @property
    def FailedInstanceIds(self):
        """IDs of instances failed to be isolated
        :rtype: list of str
        """
        return self._FailedInstanceIds

    @FailedInstanceIds.setter
    def FailedInstanceIds(self, FailedInstanceIds):
        self._FailedInstanceIds = FailedInstanceIds

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
        self._SuccessInstanceIds = params.get("SuccessInstanceIds")
        self._FailedInstanceIds = params.get("FailedInstanceIds")
        self._RequestId = params.get("RequestId")


class IsolateDedicatedDBInstanceRequest(AbstractModel):
    """IsolateDedicatedDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of `tdsql-ow728lmc`
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Instance ID in the format of `tdsql-ow728lmc`
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateDedicatedDBInstanceResponse(AbstractModel):
    """IsolateDedicatedDBInstance response structure.

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


class KillSessionRequest(AbstractModel):
    """KillSession request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _SessionId: List of session IDs
        :type SessionId: list of int
        """
        self._InstanceId = None
        self._SessionId = None

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
    def SessionId(self):
        """List of session IDs
        :rtype: list of int
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KillSessionResponse(AbstractModel):
    """KillSession response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """Task ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class LogFileInfo(AbstractModel):
    """Pulled log information

    """

    def __init__(self):
        r"""
        :param _Mtime: Last modified time of log
        :type Mtime: int
        :param _Length: File length
        :type Length: int
        :param _Uri: Uniform resource identifier (URI) used during log download
        :type Uri: str
        :param _FileName: Filename
        :type FileName: str
        """
        self._Mtime = None
        self._Length = None
        self._Uri = None
        self._FileName = None

    @property
    def Mtime(self):
        """Last modified time of log
        :rtype: int
        """
        return self._Mtime

    @Mtime.setter
    def Mtime(self, Mtime):
        self._Mtime = Mtime

    @property
    def Length(self):
        """File length
        :rtype: int
        """
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def Uri(self):
        """Uniform resource identifier (URI) used during log download
        :rtype: str
        """
        return self._Uri

    @Uri.setter
    def Uri(self, Uri):
        self._Uri = Uri

    @property
    def FileName(self):
        """Filename
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName


    def _deserialize(self, params):
        self._Mtime = params.get("Mtime")
        self._Length = params.get("Length")
        self._Uri = params.get("Uri")
        self._FileName = params.get("FileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountDescriptionRequest(AbstractModel):
    """ModifyAccountDescription request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :type InstanceId: str
        :param _UserName: Login username.
        :type UserName: str
        :param _Host: Access host allowed for user. An account is uniquely identified by username and host.
        :type Host: str
        :param _Description: New account remarks, which can contain 0-256 characters.
        :type Description: str
        """
        self._InstanceId = None
        self._UserName = None
        self._Host = None
        self._Description = None

    @property
    def InstanceId(self):
        """Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        """Login username.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        """Access host allowed for user. An account is uniquely identified by username and host.
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Description(self):
        """New account remarks, which can contain 0-256 characters.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountDescriptionResponse(AbstractModel):
    """ModifyAccountDescription response structure.

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


class ModifyAccountPrivilegesRequest(AbstractModel):
    """ModifyAccountPrivileges request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of tdsql-c1nl9rpv. It is the same as the instance ID displayed in the TencentDB console.
        :type InstanceId: str
        :param _Accounts: Database account, including username and host address.
        :type Accounts: list of Account
        :param _GlobalPrivileges: Global permission. Valid values of `GlobalPrivileges`: `"SELECT"`, `"INSERT"`, `"UPDATE"`, `"DELETE"`, `"CREATE"`, `"PROCESS"`, `"DROP"`, `"REFERENCES"`, `"INDEX"`, `"ALTER"`, `"SHOW DATABASES"`, `"CREATE TEMPORARY TABLES"`, `"LOCK TABLES"`, `"EXECUTE"`, `"CREATE VIEW"`, `"SHOW VIEW"`, `"CREATE ROUTINE"`, `"ALTER ROUTINE"`, `"EVENT"`, `"TRIGGER"`.
Note: if the parameter is left empty, no change will be made to the granted global permissions. To clear the granted global permissions, set the parameter to an empty array.
        :type GlobalPrivileges: list of str
        :param _DatabasePrivileges: Database permission. Valid values of `Privileges`: `"SELECT"`, `"INSERT"`, `"UPDATE"`, `"DELETE"`, `"CREATE"`, `"DROP"`, `"REFERENCES"`, `"INDEX"`, `"ALTER"`, `"CREATE TEMPORARY TABLES"`, `"LOCK TABLES"`, `"EXECUTE"`, `"CREATE VIEW"`, `"SHOW VIEW"`, `"CREATE ROUTINE"`, `"ALTER ROUTINE"`, `"EVENT"`, `"TRIGGER"`.
Note: if the parameter is left empty, no change will be made to the granted database permissions. To clear the granted database permissions, set `Privileges` to an empty array.
        :type DatabasePrivileges: list of DatabasePrivilege
        :param _TablePrivileges: Database table permission. Valid values of `Privileges`: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`, `REFERENCES`, `INDEX`, `ALTER`, `CREATE VIEW`, `SHOW VIEW`, `TRIGGER`.
Note: if the parameter is not passed in, no change will be made to the granted table permissions. To clear the granted table permissions, set `Privileges` to an empty array.
        :type TablePrivileges: list of TablePrivilege
        :param _ColumnPrivileges: Column permission. Valid values of `Privileges`: `"SELECT"`, `"INSERT"`, `"UPDATE"`, `"REFERENCES"`.
Note: if the parameter is left empty, no change will be made to the granted column permissions. To clear the granted column permissions, set `Privileges` to an empty array.
        :type ColumnPrivileges: list of ColumnPrivilege
        :param _ViewPrivileges: Database view permission. Valid values of `Privileges`: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`, `REFERENCES`, `INDEX`, `ALTER`, `CREATE VIEW`, `SHOW VIEW`, `TRIGGER`.
Note: if the parameter is not passed in, no change will be made to the granted view permissions. To clear the granted view permissions, set `Privileges` to an empty array.
        :type ViewPrivileges: list of ViewPrivileges
        :param _FunctionPrivileges: Database function permissions. Valid values of `Privileges`: `ALTER ROUTINE`, `EXECUTE`.
Note: if the parameter is not passed in, no change will be made to the granted function permissions. To clear the granted function permissions, set `Privileges` to an empty array.
        :type FunctionPrivileges: list of FunctionPrivilege
        :param _ProcedurePrivileges: Database stored procedure permission. Valid values of `Privileges`: `ALTER ROUTINE`, `EXECUTE`.
Note: if the parameter is not passed in, no change will be made to the granted stored procedure permissions. To clear the granted stored procedure permissions, set `Privileges` to an empty array.
        :type ProcedurePrivileges: list of ProcedurePrivilege
        """
        self._InstanceId = None
        self._Accounts = None
        self._GlobalPrivileges = None
        self._DatabasePrivileges = None
        self._TablePrivileges = None
        self._ColumnPrivileges = None
        self._ViewPrivileges = None
        self._FunctionPrivileges = None
        self._ProcedurePrivileges = None

    @property
    def InstanceId(self):
        """Instance ID in the format of tdsql-c1nl9rpv. It is the same as the instance ID displayed in the TencentDB console.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Accounts(self):
        """Database account, including username and host address.
        :rtype: list of Account
        """
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts

    @property
    def GlobalPrivileges(self):
        """Global permission. Valid values of `GlobalPrivileges`: `"SELECT"`, `"INSERT"`, `"UPDATE"`, `"DELETE"`, `"CREATE"`, `"PROCESS"`, `"DROP"`, `"REFERENCES"`, `"INDEX"`, `"ALTER"`, `"SHOW DATABASES"`, `"CREATE TEMPORARY TABLES"`, `"LOCK TABLES"`, `"EXECUTE"`, `"CREATE VIEW"`, `"SHOW VIEW"`, `"CREATE ROUTINE"`, `"ALTER ROUTINE"`, `"EVENT"`, `"TRIGGER"`.
Note: if the parameter is left empty, no change will be made to the granted global permissions. To clear the granted global permissions, set the parameter to an empty array.
        :rtype: list of str
        """
        return self._GlobalPrivileges

    @GlobalPrivileges.setter
    def GlobalPrivileges(self, GlobalPrivileges):
        self._GlobalPrivileges = GlobalPrivileges

    @property
    def DatabasePrivileges(self):
        """Database permission. Valid values of `Privileges`: `"SELECT"`, `"INSERT"`, `"UPDATE"`, `"DELETE"`, `"CREATE"`, `"DROP"`, `"REFERENCES"`, `"INDEX"`, `"ALTER"`, `"CREATE TEMPORARY TABLES"`, `"LOCK TABLES"`, `"EXECUTE"`, `"CREATE VIEW"`, `"SHOW VIEW"`, `"CREATE ROUTINE"`, `"ALTER ROUTINE"`, `"EVENT"`, `"TRIGGER"`.
Note: if the parameter is left empty, no change will be made to the granted database permissions. To clear the granted database permissions, set `Privileges` to an empty array.
        :rtype: list of DatabasePrivilege
        """
        return self._DatabasePrivileges

    @DatabasePrivileges.setter
    def DatabasePrivileges(self, DatabasePrivileges):
        self._DatabasePrivileges = DatabasePrivileges

    @property
    def TablePrivileges(self):
        """Database table permission. Valid values of `Privileges`: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`, `REFERENCES`, `INDEX`, `ALTER`, `CREATE VIEW`, `SHOW VIEW`, `TRIGGER`.
Note: if the parameter is not passed in, no change will be made to the granted table permissions. To clear the granted table permissions, set `Privileges` to an empty array.
        :rtype: list of TablePrivilege
        """
        return self._TablePrivileges

    @TablePrivileges.setter
    def TablePrivileges(self, TablePrivileges):
        self._TablePrivileges = TablePrivileges

    @property
    def ColumnPrivileges(self):
        """Column permission. Valid values of `Privileges`: `"SELECT"`, `"INSERT"`, `"UPDATE"`, `"REFERENCES"`.
Note: if the parameter is left empty, no change will be made to the granted column permissions. To clear the granted column permissions, set `Privileges` to an empty array.
        :rtype: list of ColumnPrivilege
        """
        return self._ColumnPrivileges

    @ColumnPrivileges.setter
    def ColumnPrivileges(self, ColumnPrivileges):
        self._ColumnPrivileges = ColumnPrivileges

    @property
    def ViewPrivileges(self):
        """Database view permission. Valid values of `Privileges`: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`, `REFERENCES`, `INDEX`, `ALTER`, `CREATE VIEW`, `SHOW VIEW`, `TRIGGER`.
Note: if the parameter is not passed in, no change will be made to the granted view permissions. To clear the granted view permissions, set `Privileges` to an empty array.
        :rtype: list of ViewPrivileges
        """
        return self._ViewPrivileges

    @ViewPrivileges.setter
    def ViewPrivileges(self, ViewPrivileges):
        self._ViewPrivileges = ViewPrivileges

    @property
    def FunctionPrivileges(self):
        """Database function permissions. Valid values of `Privileges`: `ALTER ROUTINE`, `EXECUTE`.
Note: if the parameter is not passed in, no change will be made to the granted function permissions. To clear the granted function permissions, set `Privileges` to an empty array.
        :rtype: list of FunctionPrivilege
        """
        return self._FunctionPrivileges

    @FunctionPrivileges.setter
    def FunctionPrivileges(self, FunctionPrivileges):
        self._FunctionPrivileges = FunctionPrivileges

    @property
    def ProcedurePrivileges(self):
        """Database stored procedure permission. Valid values of `Privileges`: `ALTER ROUTINE`, `EXECUTE`.
Note: if the parameter is not passed in, no change will be made to the granted stored procedure permissions. To clear the granted stored procedure permissions, set `Privileges` to an empty array.
        :rtype: list of ProcedurePrivilege
        """
        return self._ProcedurePrivileges

    @ProcedurePrivileges.setter
    def ProcedurePrivileges(self, ProcedurePrivileges):
        self._ProcedurePrivileges = ProcedurePrivileges


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self._Accounts.append(obj)
        self._GlobalPrivileges = params.get("GlobalPrivileges")
        if params.get("DatabasePrivileges") is not None:
            self._DatabasePrivileges = []
            for item in params.get("DatabasePrivileges"):
                obj = DatabasePrivilege()
                obj._deserialize(item)
                self._DatabasePrivileges.append(obj)
        if params.get("TablePrivileges") is not None:
            self._TablePrivileges = []
            for item in params.get("TablePrivileges"):
                obj = TablePrivilege()
                obj._deserialize(item)
                self._TablePrivileges.append(obj)
        if params.get("ColumnPrivileges") is not None:
            self._ColumnPrivileges = []
            for item in params.get("ColumnPrivileges"):
                obj = ColumnPrivilege()
                obj._deserialize(item)
                self._ColumnPrivileges.append(obj)
        if params.get("ViewPrivileges") is not None:
            self._ViewPrivileges = []
            for item in params.get("ViewPrivileges"):
                obj = ViewPrivileges()
                obj._deserialize(item)
                self._ViewPrivileges.append(obj)
        if params.get("FunctionPrivileges") is not None:
            self._FunctionPrivileges = []
            for item in params.get("FunctionPrivileges"):
                obj = FunctionPrivilege()
                obj._deserialize(item)
                self._FunctionPrivileges.append(obj)
        if params.get("ProcedurePrivileges") is not None:
            self._ProcedurePrivileges = []
            for item in params.get("ProcedurePrivileges"):
                obj = ProcedurePrivilege()
                obj._deserialize(item)
                self._ProcedurePrivileges.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountPrivilegesResponse(AbstractModel):
    """ModifyAccountPrivileges response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task ID, which can be used in the [DescribeFlow](https://intl.cloud.tencent.com/document/product/237/16177?from_cn_redirect=1) API to query the async task result.
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Async task ID, which can be used in the [DescribeFlow](https://intl.cloud.tencent.com/document/product/237/16177?from_cn_redirect=1) API to query the async task result.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyDBEncryptAttributesRequest(AbstractModel):
    """ModifyDBEncryptAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of `tdsql-ow728lmc`
        :type InstanceId: str
        :param _EncryptEnabled: Whether to enable the data encryption (Once enabled, it can’t be disabled). Valid values: `1` (Yes), `0` (No. Default）
        :type EncryptEnabled: int
        """
        self._InstanceId = None
        self._EncryptEnabled = None

    @property
    def InstanceId(self):
        """Instance ID in the format of `tdsql-ow728lmc`
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EncryptEnabled(self):
        """Whether to enable the data encryption (Once enabled, it can’t be disabled). Valid values: `1` (Yes), `0` (No. Default）
        :rtype: int
        """
        return self._EncryptEnabled

    @EncryptEnabled.setter
    def EncryptEnabled(self, EncryptEnabled):
        self._EncryptEnabled = EncryptEnabled


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._EncryptEnabled = params.get("EncryptEnabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBEncryptAttributesResponse(AbstractModel):
    """ModifyDBEncryptAttributes response structure.

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


class ModifyDBInstancesProjectRequest(AbstractModel):
    """ModifyDBInstancesProject request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: List of IDs of instances to be modified. The ID is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :type InstanceIds: list of str
        :param _ProjectId: ID of the project to be assigned, which can be obtained through the `DescribeProjects` API.
        :type ProjectId: int
        """
        self._InstanceIds = None
        self._ProjectId = None

    @property
    def InstanceIds(self):
        """List of IDs of instances to be modified. The ID is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ProjectId(self):
        """ID of the project to be assigned, which can be obtained through the `DescribeProjects` API.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstancesProjectResponse(AbstractModel):
    """ModifyDBInstancesProject response structure.

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


class ModifyDBParametersRequest(AbstractModel):
    """ModifyDBParameters request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of `tdsql-ow728lmc`.
        :type InstanceId: str
        :param _Params: Parameter list. Each element is a combination of `Param` and `Value`.
        :type Params: list of DBParamValue
        """
        self._InstanceId = None
        self._Params = None

    @property
    def InstanceId(self):
        """Instance ID in the format of `tdsql-ow728lmc`.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Params(self):
        """Parameter list. Each element is a combination of `Param` and `Value`.
        :rtype: list of DBParamValue
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Params") is not None:
            self._Params = []
            for item in params.get("Params"):
                obj = DBParamValue()
                obj._deserialize(item)
                self._Params.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBParametersResponse(AbstractModel):
    """ModifyDBParameters response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of `tdsql-ow728lmc`.
        :type InstanceId: str
        :param _Result: Parameter modification result
        :type Result: list of ParamModifyResult
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._Result = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """Instance ID in the format of `tdsql-ow728lmc`.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Result(self):
        """Parameter modification result
        :rtype: list of ParamModifyResult
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._InstanceId = params.get("InstanceId")
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = ParamModifyResult()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyDBSyncModeRequest(AbstractModel):
    """ModifyDBSyncMode request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of the instance for which to modify the sync mode. The ID is in the format of `tdsql-ow728lmc`.
        :type InstanceId: str
        :param _SyncMode: Sync mode. Valid values: `0` (async), `1` (strong sync), `2` (downgradable strong sync).
        :type SyncMode: int
        """
        self._InstanceId = None
        self._SyncMode = None

    @property
    def InstanceId(self):
        """ID of the instance for which to modify the sync mode. The ID is in the format of `tdsql-ow728lmc`.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SyncMode(self):
        """Sync mode. Valid values: `0` (async), `1` (strong sync), `2` (downgradable strong sync).
        :rtype: int
        """
        return self._SyncMode

    @SyncMode.setter
    def SyncMode(self, SyncMode):
        self._SyncMode = SyncMode


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SyncMode = params.get("SyncMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBSyncModeResponse(AbstractModel):
    """ModifyDBSyncMode response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task ID. The task status can be queried through the `DescribeFlow` API.
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Async task ID. The task status can be queried through the `DescribeFlow` API.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyInstanceNetworkRequest(AbstractModel):
    """ModifyInstanceNetwork request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _VpcId: VpcId, ID of the desired VPC network.
        :type VpcId: str
        :param _SubnetId: SubnetId, subnet ID of the desired VPC network.
        :type SubnetId: str
        :param _Vip: The field is required to specify VIP.
        :type Vip: str
        :param _Vipv6: The field is required to specify VIPv6.
        :type Vipv6: str
        :param _VipReleaseDelay: VIP retention period in hours. Value range: 0-168. Default value: `24`. `0` indicates that the VIP will be released immediately, but there will be 1-minute delay.
        :type VipReleaseDelay: int
        """
        self._InstanceId = None
        self._VpcId = None
        self._SubnetId = None
        self._Vip = None
        self._Vipv6 = None
        self._VipReleaseDelay = None

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
    def VpcId(self):
        """VpcId, ID of the desired VPC network.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """SubnetId, subnet ID of the desired VPC network.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Vip(self):
        """The field is required to specify VIP.
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vipv6(self):
        """The field is required to specify VIPv6.
        :rtype: str
        """
        return self._Vipv6

    @Vipv6.setter
    def Vipv6(self, Vipv6):
        self._Vipv6 = Vipv6

    @property
    def VipReleaseDelay(self):
        """VIP retention period in hours. Value range: 0-168. Default value: `24`. `0` indicates that the VIP will be released immediately, but there will be 1-minute delay.
        :rtype: int
        """
        return self._VipReleaseDelay

    @VipReleaseDelay.setter
    def VipReleaseDelay(self, VipReleaseDelay):
        self._VipReleaseDelay = VipReleaseDelay


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Vip = params.get("Vip")
        self._Vipv6 = params.get("Vipv6")
        self._VipReleaseDelay = params.get("VipReleaseDelay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceNetworkResponse(AbstractModel):
    """ModifyInstanceNetwork response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task ID, which can be used to query the task status through `DescribeFlow` API.
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Async task ID, which can be used to query the task status through `DescribeFlow` API.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyInstanceVipRequest(AbstractModel):
    """ModifyInstanceVip request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Vip: Instance VIP
        :type Vip: str
        :param _Ipv6Flag: IPv6 flag
        :type Ipv6Flag: int
        :param _VipReleaseDelay: VIP retention period in hours. Value range: 0-168. Default value: `24`. `0` indicates that the VIP will be released immediately, but there will be 1-minute delay.
        :type VipReleaseDelay: int
        """
        self._InstanceId = None
        self._Vip = None
        self._Ipv6Flag = None
        self._VipReleaseDelay = None

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
    def Vip(self):
        """Instance VIP
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Ipv6Flag(self):
        """IPv6 flag
        :rtype: int
        """
        return self._Ipv6Flag

    @Ipv6Flag.setter
    def Ipv6Flag(self, Ipv6Flag):
        self._Ipv6Flag = Ipv6Flag

    @property
    def VipReleaseDelay(self):
        """VIP retention period in hours. Value range: 0-168. Default value: `24`. `0` indicates that the VIP will be released immediately, but there will be 1-minute delay.
        :rtype: int
        """
        return self._VipReleaseDelay

    @VipReleaseDelay.setter
    def VipReleaseDelay(self, VipReleaseDelay):
        self._VipReleaseDelay = VipReleaseDelay


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Vip = params.get("Vip")
        self._Ipv6Flag = params.get("Ipv6Flag")
        self._VipReleaseDelay = params.get("VipReleaseDelay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceVipResponse(AbstractModel):
    """ModifyInstanceVip response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task flow ID
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Async task flow ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyInstanceVportRequest(AbstractModel):
    """ModifyInstanceVport request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Vport: Instance Vport
        :type Vport: int
        """
        self._InstanceId = None
        self._Vport = None

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
    def Vport(self):
        """Instance Vport
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Vport = params.get("Vport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceVportResponse(AbstractModel):
    """ModifyInstanceVport response structure.

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


class ModifySyncTaskAttributeRequest(AbstractModel):
    """ModifySyncTaskAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _TaskIds: IDs of tasks for which to modify the attributes. The IDs can be obtained by the return value of the `DescribeSyncTasks` API. Up to 100 tasks can be operated at a time.
        :type TaskIds: list of str
        :param _TaskName: Task name. You can specify any name you like, but its length cannot exceed 100 characters.
        :type TaskName: str
        """
        self._TaskIds = None
        self._TaskName = None

    @property
    def TaskIds(self):
        """IDs of tasks for which to modify the attributes. The IDs can be obtained by the return value of the `DescribeSyncTasks` API. Up to 100 tasks can be operated at a time.
        :rtype: list of str
        """
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds

    @property
    def TaskName(self):
        """Task name. You can specify any name you like, but its length cannot exceed 100 characters.
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName


    def _deserialize(self, params):
        self._TaskIds = params.get("TaskIds")
        self._TaskName = params.get("TaskName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySyncTaskAttributeResponse(AbstractModel):
    """ModifySyncTaskAttribute response structure.

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


class NodeInfo(AbstractModel):
    """Instance node information

    """

    def __init__(self):
        r"""
        :param _NodeId: Node ID
        :type NodeId: str
        :param _Role: Node role. Valid values: `master`, `slave`
        :type Role: str
        """
        self._NodeId = None
        self._Role = None

    @property
    def NodeId(self):
        """Node ID
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def Role(self):
        """Node role. Valid values: `master`, `slave`
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._Role = params.get("Role")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamConstraint(AbstractModel):
    """Parameter constraint

    """

    def __init__(self):
        r"""
        :param _Type: Constraint type, such as `enum` and `section`.
        :type Type: str
        :param _Enum: List of valid values when constraint type is `enum`
        :type Enum: str
        :param _Range: Range when constraint type is `section`
Note: This field may return null, indicating that no valid values can be obtained.
        :type Range: :class:`tencentcloud.mariadb.v20170312.models.ConstraintRange`
        :param _String: List of valid values when constraint type is `string`
        :type String: str
        """
        self._Type = None
        self._Enum = None
        self._Range = None
        self._String = None

    @property
    def Type(self):
        """Constraint type, such as `enum` and `section`.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Enum(self):
        """List of valid values when constraint type is `enum`
        :rtype: str
        """
        return self._Enum

    @Enum.setter
    def Enum(self, Enum):
        self._Enum = Enum

    @property
    def Range(self):
        """Range when constraint type is `section`
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ConstraintRange`
        """
        return self._Range

    @Range.setter
    def Range(self, Range):
        self._Range = Range

    @property
    def String(self):
        """List of valid values when constraint type is `string`
        :rtype: str
        """
        return self._String

    @String.setter
    def String(self, String):
        self._String = String


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Enum = params.get("Enum")
        if params.get("Range") is not None:
            self._Range = ConstraintRange()
            self._Range._deserialize(params.get("Range"))
        self._String = params.get("String")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamDesc(AbstractModel):
    """Database parameter description

    """

    def __init__(self):
        r"""
        :param _Param: Parameter name
        :type Param: str
        :param _Value: Current parameter value
        :type Value: str
        :param _SetValue: Previously set value, which is the same as `value` after the parameter takes effect.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SetValue: str
        :param _Default: Default value
        :type Default: str
        :param _Constraint: Parameter constraint
        :type Constraint: :class:`tencentcloud.mariadb.v20170312.models.ParamConstraint`
        :param _HaveSetValue: Whether a value has been set. false: no, true: yes
        :type HaveSetValue: bool
        :param _NeedRestart: Whether restart is required. false: no;
true: yes.
        :type NeedRestart: bool
        """
        self._Param = None
        self._Value = None
        self._SetValue = None
        self._Default = None
        self._Constraint = None
        self._HaveSetValue = None
        self._NeedRestart = None

    @property
    def Param(self):
        """Parameter name
        :rtype: str
        """
        return self._Param

    @Param.setter
    def Param(self, Param):
        self._Param = Param

    @property
    def Value(self):
        """Current parameter value
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def SetValue(self):
        """Previously set value, which is the same as `value` after the parameter takes effect.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SetValue

    @SetValue.setter
    def SetValue(self, SetValue):
        self._SetValue = SetValue

    @property
    def Default(self):
        """Default value
        :rtype: str
        """
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def Constraint(self):
        """Parameter constraint
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ParamConstraint`
        """
        return self._Constraint

    @Constraint.setter
    def Constraint(self, Constraint):
        self._Constraint = Constraint

    @property
    def HaveSetValue(self):
        """Whether a value has been set. false: no, true: yes
        :rtype: bool
        """
        return self._HaveSetValue

    @HaveSetValue.setter
    def HaveSetValue(self, HaveSetValue):
        self._HaveSetValue = HaveSetValue

    @property
    def NeedRestart(self):
        """Whether restart is required. false: no;
true: yes.
        :rtype: bool
        """
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart


    def _deserialize(self, params):
        self._Param = params.get("Param")
        self._Value = params.get("Value")
        self._SetValue = params.get("SetValue")
        self._Default = params.get("Default")
        if params.get("Constraint") is not None:
            self._Constraint = ParamConstraint()
            self._Constraint._deserialize(params.get("Constraint"))
        self._HaveSetValue = params.get("HaveSetValue")
        self._NeedRestart = params.get("NeedRestart")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamModifyResult(AbstractModel):
    """Parameter modification result

    """

    def __init__(self):
        r"""
        :param _Param: Renames parameter
        :type Param: str
        :param _Code: Result of parameter modification. 0: success; -1: failure; -2: invalid parameter value.
        :type Code: int
        """
        self._Param = None
        self._Code = None

    @property
    def Param(self):
        """Renames parameter
        :rtype: str
        """
        return self._Param

    @Param.setter
    def Param(self, Param):
        self._Param = Param

    @property
    def Code(self):
        """Result of parameter modification. 0: success; -1: failure; -2: invalid parameter value.
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code


    def _deserialize(self, params):
        self._Param = params.get("Param")
        self._Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcedurePrivilege(AbstractModel):
    """Stored procedure permission information

    """

    def __init__(self):
        r"""
        :param _Database: Database name
        :type Database: str
        :param _Procedure: Stored procedure name
        :type Procedure: str
        :param _Privileges: Permission information
        :type Privileges: list of str
        """
        self._Database = None
        self._Procedure = None
        self._Privileges = None

    @property
    def Database(self):
        """Database name
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Procedure(self):
        """Stored procedure name
        :rtype: str
        """
        return self._Procedure

    @Procedure.setter
    def Procedure(self, Procedure):
        self._Procedure = Procedure

    @property
    def Privileges(self):
        """Permission information
        :rtype: list of str
        """
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Procedure = params.get("Procedure")
        self._Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReservedNetResource(AbstractModel):
    """Information of the reserved network resource

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC
        :type VpcId: str
        :param _SubnetId: Subnet
        :type SubnetId: str
        :param _Vip: Reserved private network IP under `VpcId` and `SubnetId`
        :type Vip: str
        :param _Vports: Port under `Vip`
        :type Vports: list of int
        :param _RecycleTime: Valid hours of VIP
        :type RecycleTime: str
        """
        self._VpcId = None
        self._SubnetId = None
        self._Vip = None
        self._Vports = None
        self._RecycleTime = None

    @property
    def VpcId(self):
        """VPC
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Subnet
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Vip(self):
        """Reserved private network IP under `VpcId` and `SubnetId`
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vports(self):
        """Port under `Vip`
        :rtype: list of int
        """
        return self._Vports

    @Vports.setter
    def Vports(self, Vports):
        self._Vports = Vports

    @property
    def RecycleTime(self):
        """Valid hours of VIP
        :rtype: str
        """
        return self._RecycleTime

    @RecycleTime.setter
    def RecycleTime(self, RecycleTime):
        self._RecycleTime = RecycleTime


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Vip = params.get("Vip")
        self._Vports = params.get("Vports")
        self._RecycleTime = params.get("RecycleTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAccountPasswordRequest(AbstractModel):
    """ResetAccountPassword request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :type InstanceId: str
        :param _UserName: Login username.
        :type UserName: str
        :param _Host: Access host allowed for user. An account is uniquely identified by username and host.
        :type Host: str
        :param _Password: New password, which can contain 6-32 letters, digits, and common symbols but not semicolons, single quotation marks, and double quotation marks.
        :type Password: str
        """
        self._InstanceId = None
        self._UserName = None
        self._Host = None
        self._Password = None

    @property
    def InstanceId(self):
        """Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        """Login username.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        """Access host allowed for user. An account is uniquely identified by username and host.
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Password(self):
        """New password, which can contain 6-32 letters, digits, and common symbols but not semicolons, single quotation marks, and double quotation marks.
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAccountPasswordResponse(AbstractModel):
    """ResetAccountPassword response structure.

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


class ResourceTag(AbstractModel):
    """Tag object, including tag key and tag value

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key
        :type TagKey: str
        :param _TagValue: Tag value
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """Tag key
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """Tag value
        :rtype: str
        """
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroup(AbstractModel):
    """Security group details

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _CreateTime: Creation time in the format of yyyy-mm-dd hh:mm:ss
        :type CreateTime: str
        :param _SecurityGroupId: Security group ID
        :type SecurityGroupId: str
        :param _SecurityGroupName: Security group name
        :type SecurityGroupName: str
        :param _SecurityGroupRemark: Security group remarks
        :type SecurityGroupRemark: str
        :param _Inbound: Inbound rule
        :type Inbound: list of SecurityGroupBound
        :param _Outbound: Outbound rule
        :type Outbound: list of SecurityGroupBound
        """
        self._ProjectId = None
        self._CreateTime = None
        self._SecurityGroupId = None
        self._SecurityGroupName = None
        self._SecurityGroupRemark = None
        self._Inbound = None
        self._Outbound = None

    @property
    def ProjectId(self):
        """Project ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CreateTime(self):
        """Creation time in the format of yyyy-mm-dd hh:mm:ss
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SecurityGroupId(self):
        """Security group ID
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupName(self):
        """Security group name
        :rtype: str
        """
        return self._SecurityGroupName

    @SecurityGroupName.setter
    def SecurityGroupName(self, SecurityGroupName):
        self._SecurityGroupName = SecurityGroupName

    @property
    def SecurityGroupRemark(self):
        """Security group remarks
        :rtype: str
        """
        return self._SecurityGroupRemark

    @SecurityGroupRemark.setter
    def SecurityGroupRemark(self, SecurityGroupRemark):
        self._SecurityGroupRemark = SecurityGroupRemark

    @property
    def Inbound(self):
        """Inbound rule
        :rtype: list of SecurityGroupBound
        """
        return self._Inbound

    @Inbound.setter
    def Inbound(self, Inbound):
        self._Inbound = Inbound

    @property
    def Outbound(self):
        """Outbound rule
        :rtype: list of SecurityGroupBound
        """
        return self._Outbound

    @Outbound.setter
    def Outbound(self, Outbound):
        self._Outbound = Outbound


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._CreateTime = params.get("CreateTime")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._SecurityGroupName = params.get("SecurityGroupName")
        self._SecurityGroupRemark = params.get("SecurityGroupRemark")
        if params.get("Inbound") is not None:
            self._Inbound = []
            for item in params.get("Inbound"):
                obj = SecurityGroupBound()
                obj._deserialize(item)
                self._Inbound.append(obj)
        if params.get("Outbound") is not None:
            self._Outbound = []
            for item in params.get("Outbound"):
                obj = SecurityGroupBound()
                obj._deserialize(item)
                self._Outbound.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupBound(AbstractModel):
    """Security group inbound/outbound rule

    """

    def __init__(self):
        r"""
        :param _Action: Policy, which can be `ACCEPT` or `DROP`
        :type Action: str
        :param _CidrIp: Source IP or source IP range, such as 192.168.0.0/16
        :type CidrIp: str
        :param _PortRange: Port
        :type PortRange: str
        :param _IpProtocol: Network protocol. UDP and TCP are supported.
        :type IpProtocol: str
        """
        self._Action = None
        self._CidrIp = None
        self._PortRange = None
        self._IpProtocol = None

    @property
    def Action(self):
        """Policy, which can be `ACCEPT` or `DROP`
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def CidrIp(self):
        """Source IP or source IP range, such as 192.168.0.0/16
        :rtype: str
        """
        return self._CidrIp

    @CidrIp.setter
    def CidrIp(self, CidrIp):
        self._CidrIp = CidrIp

    @property
    def PortRange(self):
        """Port
        :rtype: str
        """
        return self._PortRange

    @PortRange.setter
    def PortRange(self, PortRange):
        self._PortRange = PortRange

    @property
    def IpProtocol(self):
        """Network protocol. UDP and TCP are supported.
        :rtype: str
        """
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._CidrIp = params.get("CidrIp")
        self._PortRange = params.get("PortRange")
        self._IpProtocol = params.get("IpProtocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogData(AbstractModel):
    """Information of a slow query that has been logged

    """

    def __init__(self):
        r"""
        :param _CheckSum: Statement checksum for querying details
        :type CheckSum: str
        :param _Db: Database name
        :type Db: str
        :param _FingerPrint: Abstracted SQL statement
        :type FingerPrint: str
        :param _LockTimeAvg: Average lock time
        :type LockTimeAvg: str
        :param _LockTimeMax: Maximum lock time
        :type LockTimeMax: str
        :param _LockTimeMin: Minimum lock time
        :type LockTimeMin: str
        :param _LockTimeSum: Total lock time
        :type LockTimeSum: str
        :param _QueryCount: Number of queries
        :type QueryCount: str
        :param _QueryTimeAvg: Average query time
        :type QueryTimeAvg: str
        :param _QueryTimeMax: Maximum query time
        :type QueryTimeMax: str
        :param _QueryTimeMin: Minimum query time
        :type QueryTimeMin: str
        :param _QueryTimeSum: Total query time
        :type QueryTimeSum: str
        :param _RowsExaminedSum: Number of scanned rows
        :type RowsExaminedSum: str
        :param _RowsSentSum: Number of sent rows
        :type RowsSentSum: str
        :param _TsMax: Last execution time
        :type TsMax: str
        :param _TsMin: First execution time
        :type TsMin: str
        :param _User: Account
        :type User: str
        :param _ExampleSql: Sample SQL
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExampleSql: str
        :param _Host: Host address of account
        :type Host: str
        """
        self._CheckSum = None
        self._Db = None
        self._FingerPrint = None
        self._LockTimeAvg = None
        self._LockTimeMax = None
        self._LockTimeMin = None
        self._LockTimeSum = None
        self._QueryCount = None
        self._QueryTimeAvg = None
        self._QueryTimeMax = None
        self._QueryTimeMin = None
        self._QueryTimeSum = None
        self._RowsExaminedSum = None
        self._RowsSentSum = None
        self._TsMax = None
        self._TsMin = None
        self._User = None
        self._ExampleSql = None
        self._Host = None

    @property
    def CheckSum(self):
        """Statement checksum for querying details
        :rtype: str
        """
        return self._CheckSum

    @CheckSum.setter
    def CheckSum(self, CheckSum):
        self._CheckSum = CheckSum

    @property
    def Db(self):
        """Database name
        :rtype: str
        """
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def FingerPrint(self):
        """Abstracted SQL statement
        :rtype: str
        """
        return self._FingerPrint

    @FingerPrint.setter
    def FingerPrint(self, FingerPrint):
        self._FingerPrint = FingerPrint

    @property
    def LockTimeAvg(self):
        """Average lock time
        :rtype: str
        """
        return self._LockTimeAvg

    @LockTimeAvg.setter
    def LockTimeAvg(self, LockTimeAvg):
        self._LockTimeAvg = LockTimeAvg

    @property
    def LockTimeMax(self):
        """Maximum lock time
        :rtype: str
        """
        return self._LockTimeMax

    @LockTimeMax.setter
    def LockTimeMax(self, LockTimeMax):
        self._LockTimeMax = LockTimeMax

    @property
    def LockTimeMin(self):
        """Minimum lock time
        :rtype: str
        """
        return self._LockTimeMin

    @LockTimeMin.setter
    def LockTimeMin(self, LockTimeMin):
        self._LockTimeMin = LockTimeMin

    @property
    def LockTimeSum(self):
        """Total lock time
        :rtype: str
        """
        return self._LockTimeSum

    @LockTimeSum.setter
    def LockTimeSum(self, LockTimeSum):
        self._LockTimeSum = LockTimeSum

    @property
    def QueryCount(self):
        """Number of queries
        :rtype: str
        """
        return self._QueryCount

    @QueryCount.setter
    def QueryCount(self, QueryCount):
        self._QueryCount = QueryCount

    @property
    def QueryTimeAvg(self):
        """Average query time
        :rtype: str
        """
        return self._QueryTimeAvg

    @QueryTimeAvg.setter
    def QueryTimeAvg(self, QueryTimeAvg):
        self._QueryTimeAvg = QueryTimeAvg

    @property
    def QueryTimeMax(self):
        """Maximum query time
        :rtype: str
        """
        return self._QueryTimeMax

    @QueryTimeMax.setter
    def QueryTimeMax(self, QueryTimeMax):
        self._QueryTimeMax = QueryTimeMax

    @property
    def QueryTimeMin(self):
        """Minimum query time
        :rtype: str
        """
        return self._QueryTimeMin

    @QueryTimeMin.setter
    def QueryTimeMin(self, QueryTimeMin):
        self._QueryTimeMin = QueryTimeMin

    @property
    def QueryTimeSum(self):
        """Total query time
        :rtype: str
        """
        return self._QueryTimeSum

    @QueryTimeSum.setter
    def QueryTimeSum(self, QueryTimeSum):
        self._QueryTimeSum = QueryTimeSum

    @property
    def RowsExaminedSum(self):
        """Number of scanned rows
        :rtype: str
        """
        return self._RowsExaminedSum

    @RowsExaminedSum.setter
    def RowsExaminedSum(self, RowsExaminedSum):
        self._RowsExaminedSum = RowsExaminedSum

    @property
    def RowsSentSum(self):
        """Number of sent rows
        :rtype: str
        """
        return self._RowsSentSum

    @RowsSentSum.setter
    def RowsSentSum(self, RowsSentSum):
        self._RowsSentSum = RowsSentSum

    @property
    def TsMax(self):
        """Last execution time
        :rtype: str
        """
        return self._TsMax

    @TsMax.setter
    def TsMax(self, TsMax):
        self._TsMax = TsMax

    @property
    def TsMin(self):
        """First execution time
        :rtype: str
        """
        return self._TsMin

    @TsMin.setter
    def TsMin(self, TsMin):
        self._TsMin = TsMin

    @property
    def User(self):
        """Account
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def ExampleSql(self):
        """Sample SQL
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExampleSql

    @ExampleSql.setter
    def ExampleSql(self, ExampleSql):
        self._ExampleSql = ExampleSql

    @property
    def Host(self):
        """Host address of account
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host


    def _deserialize(self, params):
        self._CheckSum = params.get("CheckSum")
        self._Db = params.get("Db")
        self._FingerPrint = params.get("FingerPrint")
        self._LockTimeAvg = params.get("LockTimeAvg")
        self._LockTimeMax = params.get("LockTimeMax")
        self._LockTimeMin = params.get("LockTimeMin")
        self._LockTimeSum = params.get("LockTimeSum")
        self._QueryCount = params.get("QueryCount")
        self._QueryTimeAvg = params.get("QueryTimeAvg")
        self._QueryTimeMax = params.get("QueryTimeMax")
        self._QueryTimeMin = params.get("QueryTimeMin")
        self._QueryTimeSum = params.get("QueryTimeSum")
        self._RowsExaminedSum = params.get("RowsExaminedSum")
        self._RowsSentSum = params.get("RowsSentSum")
        self._TsMax = params.get("TsMax")
        self._TsMin = params.get("TsMin")
        self._User = params.get("User")
        self._ExampleSql = params.get("ExampleSql")
        self._Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableColumn(AbstractModel):
    """Database column information

    """

    def __init__(self):
        r"""
        :param _Col: Column name
        :type Col: str
        :param _Type: Column type
        :type Type: str
        """
        self._Col = None
        self._Type = None

    @property
    def Col(self):
        """Column name
        :rtype: str
        """
        return self._Col

    @Col.setter
    def Col(self, Col):
        self._Col = Col

    @property
    def Type(self):
        """Column type
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Col = params.get("Col")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TablePrivilege(AbstractModel):
    """Table permission

    """

    def __init__(self):
        r"""
        :param _Database: Database name
        :type Database: str
        :param _Table: Table name
        :type Table: str
        :param _Privileges: Permission information
        :type Privileges: list of str
        """
        self._Database = None
        self._Table = None
        self._Privileges = None

    @property
    def Database(self):
        """Database name
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        """Table name
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Privileges(self):
        """Permission information
        :rtype: list of str
        """
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Table = params.get("Table")
        self._Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateDedicatedDBInstanceRequest(AbstractModel):
    """TerminateDedicatedDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of `tdsql-ow728lmc`
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Instance ID in the format of `tdsql-ow728lmc`
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateDedicatedDBInstanceResponse(AbstractModel):
    """TerminateDedicatedDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task ID
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Async task ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class TmpInstance(AbstractModel):
    """Temp instance

    """

    def __init__(self):
        r"""
        :param _AppId: Application ID
Note: u200dThis field may returnu200d·nullu200d, indicating that no valid values can be obtained.
        :type AppId: int
        :param _CreateTime: Creation time
Note: u200dThis field may returnu200d·nullu200d, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _InstanceRemark: Instance remarks
Note: u200dThis field may returnu200d·nullu200d, indicating that no valid values can be obtained.
        :type InstanceRemark: str
        :param _TempType: Whether it is a temp instance. Valid values: `0` (non-temp instance), `1` (invalid temp instance), `2` (valid temp rollback instance).
Note: u200dThis field may returnu200d·nullu200d, indicating that no valid values can be obtained.
        :type TempType: int
        :param _Status: Instance status. Valid values: `0` (to be initialized), `1` (in process), `2` (running), `-1` (isolated), `-2` (eliminated).
Note: u200dThis field may returnu200d·nullu200d, indicating that no valid values can be obtained.
        :type Status: int
        :param _InstanceId: Instance ID in the format of `tdsql-ow728lmc`
Note: u200dThis field may returnu200d·nullu200d, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _Vip: Virtual instance IP
Note: u200dThis field may returnu200d·nullu200d, indicating that no valid values can be obtained.
        :type Vip: str
        :param _Vport: Virtual instance port
Note: u200dThis field may returnu200d·nullu200d, indicating that no valid values can be obtained.
        :type Vport: int
        :param _PeriodEndTime: Validity end time
Note: u200dThis field may returnu200d·nullu200d, indicating that no valid values can be obtained.
        :type PeriodEndTime: str
        :param _SrcInstanceId: Source instance ID in the format of `tdsql-ow728lmc`
Note: u200dThis field may returnu200d·nullu200d, indicating that no valid values can be obtained.
        :type SrcInstanceId: str
        :param _StatusDesc: Instance status description
Note: u200dThis field may returnu200d·nullu200d, indicating that no valid values can be obtained.
        :type StatusDesc: str
        :param _Region: Instance region
Note: u200dThis field may returnu200d·nullu200d, indicating that no valid values can be obtained.
        :type Region: str
        :param _Zone: AZ of the instance
Note: u200dThis field may returnu200d·nullu200d, indicating that no valid values can be obtained.
        :type Zone: str
        :param _Vipv6: Virtual IPv6 of the instance
Note: u200dThis field may returnu200d·nullu200d, indicating that no valid values can be obtained.
        :type Vipv6: str
        :param _Ipv6Flag: Instance IPv6 flag
Note: u200dThis field may returnu200d·nullu200d, indicating that no valid values can be obtained.
        :type Ipv6Flag: int
        """
        self._AppId = None
        self._CreateTime = None
        self._InstanceRemark = None
        self._TempType = None
        self._Status = None
        self._InstanceId = None
        self._Vip = None
        self._Vport = None
        self._PeriodEndTime = None
        self._SrcInstanceId = None
        self._StatusDesc = None
        self._Region = None
        self._Zone = None
        self._Vipv6 = None
        self._Ipv6Flag = None

    @property
    def AppId(self):
        """Application ID
Note: u200dThis field may returnu200d·nullu200d, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def CreateTime(self):
        """Creation time
Note: u200dThis field may returnu200d·nullu200d, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def InstanceRemark(self):
        """Instance remarks
Note: u200dThis field may returnu200d·nullu200d, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceRemark

    @InstanceRemark.setter
    def InstanceRemark(self, InstanceRemark):
        self._InstanceRemark = InstanceRemark

    @property
    def TempType(self):
        """Whether it is a temp instance. Valid values: `0` (non-temp instance), `1` (invalid temp instance), `2` (valid temp rollback instance).
Note: u200dThis field may returnu200d·nullu200d, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TempType

    @TempType.setter
    def TempType(self, TempType):
        self._TempType = TempType

    @property
    def Status(self):
        """Instance status. Valid values: `0` (to be initialized), `1` (in process), `2` (running), `-1` (isolated), `-2` (eliminated).
Note: u200dThis field may returnu200d·nullu200d, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InstanceId(self):
        """Instance ID in the format of `tdsql-ow728lmc`
Note: u200dThis field may returnu200d·nullu200d, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Vip(self):
        """Virtual instance IP
Note: u200dThis field may returnu200d·nullu200d, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """Virtual instance port
Note: u200dThis field may returnu200d·nullu200d, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def PeriodEndTime(self):
        """Validity end time
Note: u200dThis field may returnu200d·nullu200d, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

    @property
    def SrcInstanceId(self):
        """Source instance ID in the format of `tdsql-ow728lmc`
Note: u200dThis field may returnu200d·nullu200d, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SrcInstanceId

    @SrcInstanceId.setter
    def SrcInstanceId(self, SrcInstanceId):
        self._SrcInstanceId = SrcInstanceId

    @property
    def StatusDesc(self):
        """Instance status description
Note: u200dThis field may returnu200d·nullu200d, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def Region(self):
        """Instance region
Note: u200dThis field may returnu200d·nullu200d, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        """AZ of the instance
Note: u200dThis field may returnu200d·nullu200d, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Vipv6(self):
        """Virtual IPv6 of the instance
Note: u200dThis field may returnu200d·nullu200d, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Vipv6

    @Vipv6.setter
    def Vipv6(self, Vipv6):
        self._Vipv6 = Vipv6

    @property
    def Ipv6Flag(self):
        """Instance IPv6 flag
Note: u200dThis field may returnu200d·nullu200d, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Ipv6Flag

    @Ipv6Flag.setter
    def Ipv6Flag(self, Ipv6Flag):
        self._Ipv6Flag = Ipv6Flag


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._CreateTime = params.get("CreateTime")
        self._InstanceRemark = params.get("InstanceRemark")
        self._TempType = params.get("TempType")
        self._Status = params.get("Status")
        self._InstanceId = params.get("InstanceId")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._PeriodEndTime = params.get("PeriodEndTime")
        self._SrcInstanceId = params.get("SrcInstanceId")
        self._StatusDesc = params.get("StatusDesc")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._Vipv6 = params.get("Vipv6")
        self._Ipv6Flag = params.get("Ipv6Flag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDedicatedDBInstanceRequest(AbstractModel):
    """UpgradeDedicatedDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of the instance to be upgraded.  It is in the form of  `tdsql-ow728lmc`, which can be obtained by querying the instance details through the `DescribeDBInstances` API.
        :type InstanceId: str
        :param _Memory: Memory size in GB,  which can be obtained through the `DescribeFenceDBInstanceSpecs` API.
        :type Memory: int
        :param _Storage: Storage space size in GB.  You can obtain the disk space limits by querying instance specification through the `DescribeDBInstanceSpecs` API.
        :type Storage: int
        :param _SwitchAutoRetry: Whether to retry again when missing the switch time window. Valid values: `0` (no), `1` (yes).
        :type SwitchAutoRetry: int
        :param _SwitchStartTime: Switch start time
        :type SwitchStartTime: str
        :param _SwitchEndTime: Switch end time
        :type SwitchEndTime: str
        """
        self._InstanceId = None
        self._Memory = None
        self._Storage = None
        self._SwitchAutoRetry = None
        self._SwitchStartTime = None
        self._SwitchEndTime = None

    @property
    def InstanceId(self):
        """ID of the instance to be upgraded.  It is in the form of  `tdsql-ow728lmc`, which can be obtained by querying the instance details through the `DescribeDBInstances` API.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Memory(self):
        """Memory size in GB,  which can be obtained through the `DescribeFenceDBInstanceSpecs` API.
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        """Storage space size in GB.  You can obtain the disk space limits by querying instance specification through the `DescribeDBInstanceSpecs` API.
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def SwitchAutoRetry(self):
        """Whether to retry again when missing the switch time window. Valid values: `0` (no), `1` (yes).
        :rtype: int
        """
        return self._SwitchAutoRetry

    @SwitchAutoRetry.setter
    def SwitchAutoRetry(self, SwitchAutoRetry):
        self._SwitchAutoRetry = SwitchAutoRetry

    @property
    def SwitchStartTime(self):
        """Switch start time
        :rtype: str
        """
        return self._SwitchStartTime

    @SwitchStartTime.setter
    def SwitchStartTime(self, SwitchStartTime):
        self._SwitchStartTime = SwitchStartTime

    @property
    def SwitchEndTime(self):
        """Switch end time
        :rtype: str
        """
        return self._SwitchEndTime

    @SwitchEndTime.setter
    def SwitchEndTime(self, SwitchEndTime):
        self._SwitchEndTime = SwitchEndTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._SwitchAutoRetry = params.get("SwitchAutoRetry")
        self._SwitchStartTime = params.get("SwitchStartTime")
        self._SwitchEndTime = params.get("SwitchEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDedicatedDBInstanceResponse(AbstractModel):
    """UpgradeDedicatedDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task ID
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Async task ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ViewPrivileges(AbstractModel):
    """View permission information

    """

    def __init__(self):
        r"""
        :param _Database: Database name
        :type Database: str
        :param _View: View name
        :type View: str
        :param _Privileges: Permission information
        :type Privileges: list of str
        """
        self._Database = None
        self._View = None
        self._Privileges = None

    @property
    def Database(self):
        """Database name
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def View(self):
        """View name
        :rtype: str
        """
        return self._View

    @View.setter
    def View(self, View):
        self._View = View

    @property
    def Privileges(self):
        """Permission information
        :rtype: list of str
        """
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._View = params.get("View")
        self._Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        