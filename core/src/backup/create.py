import backup.cloud.azure.snapshots as azure_snapshots
import backup.cloud.azure.resource_group as azure_resource_group
from core.helpers.data_loader import load_yaml_file
from core.helpers.doc_list_helpers import select_single
from core.cloud.azure.login import get_subscription_client


def init(sub_parser):
    sub_parser = sub_parser.add_parser('create', description='Create disk snapshots')
    sub_parser.add_argument('-f', '--file', help='File with environment configuration.')
    sub_parser.add_argument('--disks-snapshot', action="store_true", help='Should Epiphany perform disk snapshots.')
    sub_parser.set_defaults(func=run)


def get_azure_subscription_id(client_id, client_secret, tenant_id, subscription_name):
    subscription_client = get_subscription_client(client_id=client_id, client_secret=client_secret, tenant_id=tenant_id)
    subscriptions = subscription_client.subscriptions.list()

    filtered_subscription = list(filter(lambda x: x.display_name == subscription_name, subscriptions))

    if len(filtered_subscription) == 1:
        subscription_id = filtered_subscription[0].subscription_id
        return subscription_id
    else:
        print("Woooha... No subscription found.")
        exit(1)


def run_azure(cluster_config, backup_config):
    credentials = cluster_config["specification"]["cloud"]["credentials"]
    client_id = credentials["client_id"]
    client_secret = credentials["client_secret"]
    tenant_id = credentials["tenant_id"]
    subscription_name = cluster_config["specification"]["cloud"]["subscription_name"]

    subscription_id = get_azure_subscription_id(client_id, client_secret, tenant_id, subscription_name)

    target_resource_group_name = f"{cluster_config['specification']['prefix']}-{cluster_config['specification']['name']}-rg"
    target_resource_group = azure_resource_group.get_resource_group(client_id, client_secret, tenant_id,
                                                                    subscription_id, target_resource_group_name)

    destination_resource_group_name = backup_config["specification"]["destination_resource_group_name"]
    destination_resource_group_region = target_resource_group.location

    azure_resource_group.create_resource_group(client_id, client_secret, tenant_id, subscription_id,
                                               destination_resource_group_name, destination_resource_group_region)

    azure_snapshots.create_disks_snapshots(client_id=client_id, client_secret=client_secret,
                                           tenant_id=tenant_id, subscription_id=subscription_id,
                                           target_resource_group_name=target_resource_group_name,
                                           destination_resource_group_name=destination_resource_group_name,
                                           destination_location=destination_resource_group_region)


def run(args):
    if "file" in args and args.file:
        docs = load_yaml_file(args.file)
        cluster_config = select_single(docs, lambda x: x["kind"] == 'epiphany-cluster')
        docs = load_yaml_file(args.file)
        backup_config = select_single(docs, lambda x: x["kind"] == 'configuration/backup')

        if cluster_config["provider"] == "azure":

            if args.disks_snapshot:
                run_azure(cluster_config, backup_config)

            else:
                print("Woooha... No parameter?")
                exit(1)

        else:
            print("Woooha... Not implemented yet.")
            exit(1)

    else:
        print("Woooha...")
        exit(1)

    return 0
