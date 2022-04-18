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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.antiddos.v20200309 import models


class AntiddosClient(AbstractClient):
    _apiVersion = '2020-03-09'
    _endpoint = 'antiddos.tencentcloudapi.com'
    _service = 'antiddos'


    def AssociateDDoSEipAddress(self, request):
        """This API is used to bind an EIP to an Anti-DDoS Advanced instance or a specified private IP of an ENI.

        :param request: Request instance for AssociateDDoSEipAddress.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.AssociateDDoSEipAddressRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.AssociateDDoSEipAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateDDoSEipAddress", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateDDoSEipAddressResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AssociateDDoSEipLoadBalancer(self, request):
        """This API is used to bind an Anti-DDoS EIP to the specified private IP of a CLB instance.

        :param request: Request instance for AssociateDDoSEipLoadBalancer.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.AssociateDDoSEipLoadBalancerRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.AssociateDDoSEipLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateDDoSEipLoadBalancer", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateDDoSEipLoadBalancerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateBlackWhiteIpList(self, request):
        """This API is used to add an Anti-DDoS IP blocklist/allowlist.

        :param request: Request instance for CreateBlackWhiteIpList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateBlackWhiteIpListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateBlackWhiteIpListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBlackWhiteIpList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateBlackWhiteIpListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateBoundIP(self, request):
        """This API is used to bind an IP to an Anti-DDoS Pro instance Both single IP instances and multi-IP instances are available. Note that you should wait until the current binding or unbinding completes before using this async API for new operations.

        :param request: Request instance for CreateBoundIP.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateBoundIPRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateBoundIPResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBoundIP", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateBoundIPResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCCPrecisionPolicy(self, request):
        """This API is used to create a CC precise protection policy.

        :param request: Request instance for CreateCCPrecisionPolicy.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateCCPrecisionPolicyRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateCCPrecisionPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCCPrecisionPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCCPrecisionPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCCReqLimitPolicy(self, request):
        """This API is used to create a CC frequency limit policy.

        :param request: Request instance for CreateCCReqLimitPolicy.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateCCReqLimitPolicyRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateCCReqLimitPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCCReqLimitPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCCReqLimitPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCcBlackWhiteIpList(self, request):
        """This API is used to create a layer 4 access control list to prevent CC attacks.

        :param request: Request instance for CreateCcBlackWhiteIpList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateCcBlackWhiteIpListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateCcBlackWhiteIpListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCcBlackWhiteIpList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCcBlackWhiteIpListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCcGeoIPBlockConfig(self, request):
        """This API is used to create a regional blocking configuration.

        :param request: Request instance for CreateCcGeoIPBlockConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateCcGeoIPBlockConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateCcGeoIPBlockConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCcGeoIPBlockConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCcGeoIPBlockConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDDoSAI(self, request):
        """This API is used to set Anti-DDoS AI protection switches.

        :param request: Request instance for CreateDDoSAI.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateDDoSAIRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateDDoSAIResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDDoSAI", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDDoSAIResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDDoSGeoIPBlockConfig(self, request):
        """This API is used to add an Anti-DDoS region blocking configuration.

        :param request: Request instance for CreateDDoSGeoIPBlockConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateDDoSGeoIPBlockConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateDDoSGeoIPBlockConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDDoSGeoIPBlockConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDDoSGeoIPBlockConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDDoSSpeedLimitConfig(self, request):
        """This API is used to add Anti-DDoS access rate limit configurations.

        :param request: Request instance for CreateDDoSSpeedLimitConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateDDoSSpeedLimitConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateDDoSSpeedLimitConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDDoSSpeedLimitConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDDoSSpeedLimitConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDefaultAlarmThreshold(self, request):
        """This API is used to set the default alarm threshold of an IP.

        :param request: Request instance for CreateDefaultAlarmThreshold.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateDefaultAlarmThresholdRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateDefaultAlarmThresholdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDefaultAlarmThreshold", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDefaultAlarmThresholdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateIPAlarmThresholdConfig(self, request):
        """This API is used to set the default alarm threshold of an IP.

        :param request: Request instance for CreateIPAlarmThresholdConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateIPAlarmThresholdConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateIPAlarmThresholdConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIPAlarmThresholdConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateIPAlarmThresholdConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateL7RuleCerts(self, request):
        """This API is used to configure certificates with layer-7 forwarding rules in a batch for SSL testing.

        :param request: Request instance for CreateL7RuleCerts.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateL7RuleCertsRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateL7RuleCertsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateL7RuleCerts", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateL7RuleCertsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePacketFilterConfig(self, request):
        """This API is used to add Anti-DDoS feature filtering rules.

        :param request: Request instance for CreatePacketFilterConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreatePacketFilterConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreatePacketFilterConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePacketFilterConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePacketFilterConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateProtocolBlockConfig(self, request):
        """This API is used to set Anti-DDoS protocol blocking configurations.

        :param request: Request instance for CreateProtocolBlockConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateProtocolBlockConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateProtocolBlockConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProtocolBlockConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateProtocolBlockConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSchedulingDomain(self, request):
        """This API is used to create a domain name for IP scheduling and switching.

        :param request: Request instance for CreateSchedulingDomain.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateSchedulingDomainRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateSchedulingDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSchedulingDomain", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSchedulingDomainResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateWaterPrintConfig(self, request):
        """This API is used to add Anti-DDoS watermark configurations.

        :param request: Request instance for CreateWaterPrintConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateWaterPrintConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateWaterPrintConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWaterPrintConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateWaterPrintConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateWaterPrintKey(self, request):
        """This API is used to add Anti-DDoS watermark keys.

        :param request: Request instance for CreateWaterPrintKey.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateWaterPrintKeyRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateWaterPrintKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWaterPrintKey", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateWaterPrintKeyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteBlackWhiteIpList(self, request):
        """This API is used to delete an Anti-DDoS IP blocklist/allowlist.

        :param request: Request instance for DeleteBlackWhiteIpList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DeleteBlackWhiteIpListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DeleteBlackWhiteIpListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBlackWhiteIpList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteBlackWhiteIpListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteCCLevelPolicy(self, request):
        """This API is used to delete a level-defining policy of CC attacks.

        :param request: Request instance for DeleteCCLevelPolicy.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DeleteCCLevelPolicyRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DeleteCCLevelPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCCLevelPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCCLevelPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteCCPrecisionPolicy(self, request):
        """This API is used to delete a CC precise protection policy.

        :param request: Request instance for DeleteCCPrecisionPolicy.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DeleteCCPrecisionPolicyRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DeleteCCPrecisionPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCCPrecisionPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCCPrecisionPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteCCThresholdPolicy(self, request):
        """This API is used to delete a CC cleansing threshold policy.

        :param request: Request instance for DeleteCCThresholdPolicy.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DeleteCCThresholdPolicyRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DeleteCCThresholdPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCCThresholdPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCCThresholdPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteCcBlackWhiteIpList(self, request):
        """This API is used to delete a layer-4 access control list.

        :param request: Request instance for DeleteCcBlackWhiteIpList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DeleteCcBlackWhiteIpListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DeleteCcBlackWhiteIpListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCcBlackWhiteIpList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCcBlackWhiteIpListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteCcGeoIPBlockConfig(self, request):
        """This API is used to delete a regional blocking configuration.

        :param request: Request instance for DeleteCcGeoIPBlockConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DeleteCcGeoIPBlockConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DeleteCcGeoIPBlockConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCcGeoIPBlockConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCcGeoIPBlockConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteDDoSGeoIPBlockConfig(self, request):
        """This API is used to delete Anti-DDoS region blocking configurations.

        :param request: Request instance for DeleteDDoSGeoIPBlockConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DeleteDDoSGeoIPBlockConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DeleteDDoSGeoIPBlockConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDDoSGeoIPBlockConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDDoSGeoIPBlockConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteDDoSSpeedLimitConfig(self, request):
        """This API is used to delete Anti-DDoS access rate limit configurations.

        :param request: Request instance for DeleteDDoSSpeedLimitConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DeleteDDoSSpeedLimitConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DeleteDDoSSpeedLimitConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDDoSSpeedLimitConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDDoSSpeedLimitConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeletePacketFilterConfig(self, request):
        """This API is used to delete Anti-DDoS feature filtering rules.

        :param request: Request instance for DeletePacketFilterConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DeletePacketFilterConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DeletePacketFilterConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePacketFilterConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePacketFilterConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteWaterPrintConfig(self, request):
        """This API is used to delete Anti-DDoS watermark configurations.

        :param request: Request instance for DeleteWaterPrintConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DeleteWaterPrintConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DeleteWaterPrintConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWaterPrintConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteWaterPrintConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteWaterPrintKey(self, request):
        """This API is used to delete Anti-DDoS watermark keys.

        :param request: Request instance for DeleteWaterPrintKey.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DeleteWaterPrintKeyRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DeleteWaterPrintKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWaterPrintKey", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteWaterPrintKeyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBasicDeviceStatus(self, request):
        """This API is used to querying the status of Anti-DDoS IP.

        :param request: Request instance for DescribeBasicDeviceStatus.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeBasicDeviceStatusRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeBasicDeviceStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBasicDeviceStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBasicDeviceStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBizTrend(self, request):
        """This API is used to get the traffic flow data collected in the specified period.

        :param request: Request instance for DescribeBizTrend.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeBizTrendRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeBizTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBizTrend", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBizTrendResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBlackWhiteIpList(self, request):
        """This API is used to get an Anti-DDoS IP blocklist/allowlist.

        :param request: Request instance for DescribeBlackWhiteIpList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeBlackWhiteIpListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeBlackWhiteIpListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBlackWhiteIpList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBlackWhiteIpListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCCLevelList(self, request):
        """This API is used to query the list of CC protection levels.

        :param request: Request instance for DescribeCCLevelList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeCCLevelListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeCCLevelListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCCLevelList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCCLevelListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCCLevelPolicy(self, request):
        """This API is used the query a level-defining policy of CC attacks

        :param request: Request instance for DescribeCCLevelPolicy.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeCCLevelPolicyRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeCCLevelPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCCLevelPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCCLevelPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCCThresholdList(self, request):
        """This API is used to query the list of CC cleansing thresholds.

        :param request: Request instance for DescribeCCThresholdList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeCCThresholdListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeCCThresholdListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCCThresholdList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCCThresholdListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCCTrend(self, request):
        """This API is used to get CC attack data, including total QPS peaks, attack QPS, total number of requests and number of attack requests.

        :param request: Request instance for DescribeCCTrend.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeCCTrendRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeCCTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCCTrend", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCCTrendResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDDoSTrend(self, request):
        """This API is used to get DDoS attack traffic bandwidth and attack packet rate.

        :param request: Request instance for DescribeDDoSTrend.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeDDoSTrendRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeDDoSTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSTrend", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSTrendResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDefaultAlarmThreshold(self, request):
        """This API is used to get the default alarm threshold of an IP.

        :param request: Request instance for DescribeDefaultAlarmThreshold.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeDefaultAlarmThresholdRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeDefaultAlarmThresholdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDefaultAlarmThreshold", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDefaultAlarmThresholdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeL7RulesBySSLCertId(self, request):
        """This API is used to query layer-7 rules matched with certificate IDs.

        :param request: Request instance for DescribeL7RulesBySSLCertId.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeL7RulesBySSLCertIdRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeL7RulesBySSLCertIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeL7RulesBySSLCertId", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeL7RulesBySSLCertIdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeListBGPIPInstances(self, request):
        """This API is used to get a list of Anti-DDoS Advanced instances.

        :param request: Request instance for DescribeListBGPIPInstances.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListBGPIPInstancesRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListBGPIPInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListBGPIPInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListBGPIPInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeListBlackWhiteIpList(self, request):
        """This API is used to get a list of Anti-DDoS IP blocklists/allowlists.

        :param request: Request instance for DescribeListBlackWhiteIpList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListBlackWhiteIpListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListBlackWhiteIpListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListBlackWhiteIpList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListBlackWhiteIpListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeListDDoSAI(self, request):
        """This API is used to get a list of Anti-DDoS AI protection switches.

        :param request: Request instance for DescribeListDDoSAI.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListDDoSAIRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListDDoSAIResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListDDoSAI", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListDDoSAIResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeListDDoSGeoIPBlockConfig(self, request):
        """This API is used to get a list of Anti-DDoS region blocking configurations.

        :param request: Request instance for DescribeListDDoSGeoIPBlockConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListDDoSGeoIPBlockConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListDDoSGeoIPBlockConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListDDoSGeoIPBlockConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListDDoSGeoIPBlockConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeListDDoSSpeedLimitConfig(self, request):
        """This API is used to get a list of Anti-DDoS access rate limit configurations.

        :param request: Request instance for DescribeListDDoSSpeedLimitConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListDDoSSpeedLimitConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListDDoSSpeedLimitConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListDDoSSpeedLimitConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListDDoSSpeedLimitConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeListIPAlarmConfig(self, request):
        """This API is used to get a list of IP alarm threshold configurations.

        :param request: Request instance for DescribeListIPAlarmConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListIPAlarmConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListIPAlarmConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListIPAlarmConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListIPAlarmConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeListListener(self, request):
        """This API is used to get a list of forwarding listeners.

        :param request: Request instance for DescribeListListener.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListListenerRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListListenerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListListener", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListListenerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeListPacketFilterConfig(self, request):
        """This API is used to get a list of Anti-DDoS feature filtering rules.

        :param request: Request instance for DescribeListPacketFilterConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListPacketFilterConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListPacketFilterConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListPacketFilterConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListPacketFilterConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeListProtectThresholdConfig(self, request):
        """This API is used to get a list of protection threshold configurations for AI protection switch, protection level, and CC threshold switch.

        :param request: Request instance for DescribeListProtectThresholdConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListProtectThresholdConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListProtectThresholdConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListProtectThresholdConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListProtectThresholdConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeListProtocolBlockConfig(self, request):
        """This API is used to get a list of Anti-DDoS protocol blocking configurations.

        :param request: Request instance for DescribeListProtocolBlockConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListProtocolBlockConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListProtocolBlockConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListProtocolBlockConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListProtocolBlockConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeListSchedulingDomain(self, request):
        """This API is used to get a list of intelligent scheduling domain names.

        :param request: Request instance for DescribeListSchedulingDomain.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListSchedulingDomainRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListSchedulingDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListSchedulingDomain", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListSchedulingDomainResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeListWaterPrintConfig(self, request):
        """This API is used to get a list of Anti-DDoS watermark configurations.

        :param request: Request instance for DescribeListWaterPrintConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListWaterPrintConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListWaterPrintConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListWaterPrintConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListWaterPrintConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisassociateDDoSEipAddress(self, request):
        """This API is used to unbind an Anti-DDoS EIP.

        :param request: Request instance for DisassociateDDoSEipAddress.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DisassociateDDoSEipAddressRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DisassociateDDoSEipAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateDDoSEipAddress", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisassociateDDoSEipAddressResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyCCPrecisionPolicy(self, request):
        """This API is used to modify a CC precise protection policy.

        :param request: Request instance for ModifyCCPrecisionPolicy.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.ModifyCCPrecisionPolicyRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.ModifyCCPrecisionPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCCPrecisionPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCCPrecisionPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyCcBlackWhiteIpList(self, request):
        """This API is used to modify a layer-4 access control list.

        :param request: Request instance for ModifyCcBlackWhiteIpList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.ModifyCcBlackWhiteIpListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.ModifyCcBlackWhiteIpListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCcBlackWhiteIpList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCcBlackWhiteIpListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDDoSGeoIPBlockConfig(self, request):
        """This API is used to modify Anti-DDoS region blocking configurations.

        :param request: Request instance for ModifyDDoSGeoIPBlockConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.ModifyDDoSGeoIPBlockConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.ModifyDDoSGeoIPBlockConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDDoSGeoIPBlockConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDDoSGeoIPBlockConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDDoSSpeedLimitConfig(self, request):
        """This API is used to modify Anti-DDoS access rate limit configurations.

        :param request: Request instance for ModifyDDoSSpeedLimitConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.ModifyDDoSSpeedLimitConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.ModifyDDoSSpeedLimitConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDDoSSpeedLimitConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDDoSSpeedLimitConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDomainUsrName(self, request):
        """This API is used to modify intelligent scheduling domain names.

        :param request: Request instance for ModifyDomainUsrName.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.ModifyDomainUsrNameRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.ModifyDomainUsrNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomainUsrName", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDomainUsrNameResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyNewDomainRules(self, request):
        """This API is used to modify layer-7 forwarding rules.

        :param request: Request instance for ModifyNewDomainRules.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.ModifyNewDomainRulesRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.ModifyNewDomainRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNewDomainRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNewDomainRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyPacketFilterConfig(self, request):
        """This API is used to modify Anti-DDoS feature filtering rules.

        :param request: Request instance for ModifyPacketFilterConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.ModifyPacketFilterConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.ModifyPacketFilterConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPacketFilterConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPacketFilterConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SwitchWaterPrintConfig(self, request):
        """This API is used to enable or disable Anti-DDoS watermark configurations.

        :param request: Request instance for SwitchWaterPrintConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.SwitchWaterPrintConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.SwitchWaterPrintConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchWaterPrintConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SwitchWaterPrintConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)