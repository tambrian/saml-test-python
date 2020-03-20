#!/usr/local/bin/python3

## AADTokenCredentials for multi-factor authentication
from msrestazure.azure_active_directory import AADTokenCredentials

## Required for Azure Data Lake Analytics job management
from azure.mgmt.datalake.analytics.job import DataLakeAnalyticsJobManagementClient
from azure.mgmt.datalake.analytics.job.models import JobInformation, JobState, USqlJobProperties

## Other required imports
import adal, uuid, time


client_cert_file = 'privatekey_clear.pem'

def authenticate_client_cert():

    authority_host_uri = 'https://login.microsoftonline.com'
    tenant = ''
    authority_uri = authority_host_uri + '/' + tenant
    resource_uri = 'https://management.core.windows.net/'
    client_id = ''
    client_cert = open(client_cert_file, 'rb').read()
    client_cert_thumbprint = ''

    context = adal.AuthenticationContext(authority_uri, api_version=None)

    mgmt_token = context.acquire_token_with_client_certificate(resource_uri, client_id, client_cert, client_cert_thumbprint)

    credentials = AADTokenCredentials(mgmt_token, client_id)
    
    print(credentials.__dict__)
    
    return credentials

if __name__ == '__main__':
    creds = authenticate_client_cert()

""" def authenticate_device_code():

    authority_host_uri = 'https://login.microsoftonline.com'
    tenant = ''
    authority_uri = authority_host_uri + '/' + tenant
    resource_uri = 'https://management.core.windows.net/'
    client_id = ''

    context = adal.AuthenticationContext(authority_uri, api_version=None)
    code = context.acquire_user_code(resource_uri, client_id)
    print(code['message'])
    mgmt_token = context.acquire_token_with_device_code(resource_uri, code, client_id)
    credentials = AADTokenCredentials(mgmt_token, client_id)

    return credentials


if __name__ == '__main__':
    creds = authenticate_device_code() """