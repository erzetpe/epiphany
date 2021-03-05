# Changelog 0.10

## [0.10.0] YYYY-MM-DD

### Added

- [#1798](https://github.com/epiphany-platform/epiphany/issues/1798) - Additional alerts for Prometheus
- [#1355](https://github.com/epiphany-platform/epiphany/issues/1355) - Updating cloud based OS images - configuration required for Azure RHEL LVM images
- [#2081](https://github.com/epiphany-platform/epiphany/issues/2081) - Replace Skopeo with Crane

### Fixed

- [#1870](https://github.com/epiphany-platform/epiphany/issues/1870) - Do not install Filebeat when there is no Elasticsearch
- [#1881](https://github.com/epiphany-platform/epiphany/issues/1881) - epicli: wrong informations in help messages
- [#1959](https://github.com/epiphany-platform/epiphany/issues/1959) - Network traffic not allowed from load balancer's subnet to Kubernetes's subnet in AWS
- [#1991](https://github.com/epiphany-platform/epiphany/issues/1991) - When custom repo is used backup/recovery stops working
- [#1908](https://github.com/epiphany-platform/epiphany/issues/1908) - Research why Epiphany nodes hang when memory is overcommited
- [#1979](https://github.com/epiphany-platform/epiphany/issues/1979) - RabbitMQ fails on upgrade when 2 nodes are specified that are not clustered
- [#1984](https://github.com/epiphany-platform/epiphany/issues/1984) - RabbitMQ 3.7.10 fails on upgrade to 3.8.9: 'rabbitmqctl version' command not found
- [#1824](https://github.com/epiphany-platform/epiphany/issues/1824) - offline installation fails with error 'yum lockfile is held by another process' (Azure/RHEL)
- [#2069](https://github.com/epiphany-platform/epiphany/issues/2069) - [CentOS] epicli fails on task [repository : Create epirepo repository]
- [#2066](https://github.com/epiphany-platform/epiphany/issues/2066) - [CentOS] download-requirements.sh fails on extracting tar with backed up repos
- [#2067](https://github.com/epiphany-platform/epiphany/issues/2067) - [CentOS] epicli fails on task "repository : Wait for yum lock to be released" on CentOS Minimal
- [#1844](https://github.com/epiphany-platform/epiphany/issues/1844) - Default Password in Open Distro Elasticsearch, Filebeat, Kibana and Grafana
- [#1844](https://github.com/epiphany-platform/epiphany/issues/1844) - Default password in Open Distro for Elasticsearch, Filebeat, Kibana and Grafana

### Updated

- [#1953](https://github.com/epiphany-platform/epiphany/issues/1953) - Replace Pipenv with Poetry
- [#1862](https://github.com/epiphany-platform/epiphany/issues/1862) - Upgrade Ignite (2.9.1)
- [#1952](https://github.com/epiphany-platform/epiphany/issues/1952) - Upgrade ansible to 2.10.x
- [#1864](https://github.com/epiphany-platform/epiphany/issues/1864) - Upgrade Hashicorp Vault (1.6.1), Vault Helm Chart (0.9.0), Vault-k8s (0.7.0)
- [#2029](https://github.com/epiphany-platform/epiphany/issues/2029) - Remove old ARM references.
- [#1901](https://github.com/epiphany-platform/epiphany/issues/1901) - Make Epiphany upgrades selective (Kafka). Added new parameter for epicli (--upgrade-components)

### Breaking changes

### Known issues
