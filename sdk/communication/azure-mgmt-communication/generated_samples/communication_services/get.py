# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.communication import CommunicationServiceManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-communication
# USAGE
    python get.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = CommunicationServiceManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="11112222-3333-4444-5555-666677778888",
    )

    response = client.communication_services.get(
        resource_group_name="MyResourceGroup",
        communication_service_name="MyCommunicationResource",
    )
    print(response)


# x-ms-original-file: specification/communication/resource-manager/Microsoft.Communication/preview/2023-04-01-preview/examples/communicationServices/get.json
if __name__ == "__main__":
    main()
