from core.cloud.azure.login import get_resource_client


def create_resource_group(client_id, client_secret, tenant_id, subscription_id, resource_group_name, location):
    resource_client = get_resource_client(client_id, client_secret, tenant_id, subscription_id)
    resource_group_params = {'location': location}
    resource_client.resource_groups.create_or_update(resource_group_name, resource_group_params)


def get_resource_group(client_id, client_secret, tenant_id, subscription_id, resource_group_name):
    resource_client = get_resource_client(client_id, client_secret, tenant_id, subscription_id)
    resource_group = resource_client.resource_groups.get(resource_group_name)
    return resource_group
