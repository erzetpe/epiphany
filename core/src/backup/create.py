import backup.cloud.azure.create_snapshots as azure_create_snapshots
from core.helpers.data_loader import load_yaml_file
from core.helpers.doc_list_helpers import select_single


def init(sub_parser):
    sub_parser = sub_parser.add_parser('create', description='Create disk snapshots')
    sub_parser.add_argument('-f', '--file', help='File with environment configuration.')
    sub_parser.add_argument('--disks-snapshot', action="store_true", help='Should Epiphany perform disk snapshots.')
    sub_parser.set_defaults(func=run)


def run_azure(cluster_config):
    credentials = cluster_config["specification"]["cloud"]["credentials"]
    client_id = credentials["client_id"]
    client_secret = credentials["client_secret"]
    subscription_id = cluster_config["specification"]["cloud"]["subscription_name"]
    tenant_id = credentials["tenant_id"]
    resource_group_name = f"{cluster_config['specification']['prefix']}-{cluster_config['specification']['name']}-rg"

    azure_create_snapshots.create_disks_snapshots(client_id=client_id, client_secret=client_secret,
                                                  tenant_id=tenant_id, subscription_id=subscription_id,
                                                  resource_group_name=resource_group_name)


def run(args):

    if "file" in args and args.file:
        docs = load_yaml_file(args.file)
        cluster_config = select_single(docs, lambda x: x["kind"] == 'epiphany-cluster')

        if cluster_config["provider"] == "azure":

            if args.disks_snapshot:
                run_azure(cluster_config)

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
