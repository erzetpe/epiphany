import core.cloud.azure.login as login
from datetime import datetime

from backup import logger


def create_disks_snapshots(client_id, client_secret, tenant_id, subscription_id, target_resource_group_name,
                           destination_resource_group_name, destination_location):
    compute_client = login.get_compute_client(client_id=client_id, client_secret=client_secret, tenant_id=tenant_id,
                                              subscription_id=subscription_id)
    disks = compute_client.disks.list_by_resource_group(resource_group_name=target_resource_group_name)
    timestamp = datetime.now()
    for disk in disks:
        snapshot_name = f"{disk.name}-snapshot-{timestamp:%Y%m%d-%H%M%S}"
        data = {
            # todo: Setup of location
            'location': disk.location,
            'creation_data': {
                'create_option': "Copy",
                'source_uri': disk.id
            }
        }
        status = compute_client.snapshots.create_or_update(destination_resource_group_name,
                                                           snapshot_name,
                                                           data)
        if status.result().provisioning_state == "Succeeded":
            logger.info(f"Created Azure Snapshot: {snapshot_name}.")
        else:
            logger.error(f"Something went terribly wrong. {status.result()}")
            exit(1)
