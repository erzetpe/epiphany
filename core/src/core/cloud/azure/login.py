from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient


def get_credentials(client_id, client_secret, tenant_id):
    credentials = ServicePrincipalCredentials(
        client_id=client_id,
        secret=client_secret,
        tenant=tenant_id
    )
    return credentials


def get_client(client_id, client_secret, tenant_id, subscription_id):
    credentials = get_credentials(client_id, client_secret, tenant_id)
    client = ComputeManagementClient(credentials, subscription_id)
    return client


def run(args):
    print('Logging to Azure infrastructure.')
    return 0
