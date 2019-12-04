import backup.cloud.azure.create_snapshots as azure_create_snapshots
from core.helpers.data_loader import load_yaml_file

def init(sub_parser):
    sub_parser = sub_parser.add_parser('create', description='Create disk snapshots')
    sub_parser.add_argument('-f', '--file', help='File with environment configuration.')
    sub_parser.add_argument('--disks-snapshot', action="store_true", help='Should Epiphany perform disk snapshots.')
    sub_parser.set_defaults(func=run)


def run(args):

    if "file" in args and args.file:
        docs = load_yaml_file(args.file)

        for doc in docs:
            print(doc)

    else:
        print("Woooha...")
        exit(1)

    client = ""
    key = ""
    subscription_id = ""
    tenant_id = ""
    resource_group_name = ""

    if args.disks_snapshot:
        azure_create_snapshots.create_disks_snapshots(client_id=client, client_secret=key,
                                              tenant_id=tenant_id, subscription_id=subscription_id,
                                              resource_group_name=resource_group_name)
    else:
        print("Woooha...")
        exit(1)

    return 0
