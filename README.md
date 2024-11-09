**Docker systemd service**
=========================

This role lets you configure a docker container and run it as a systemd service on **debian-based** distributions. This role is heavily sourced from [mhutter.docker-systemd-service](https://github.com/mhutter/ansible-docker-systemd-service), but aims at providing some of the missing features of said role.

**Requirements**
---------------

This roles assumes you have **docker** installed on the target host. You can use [ednz_cloud.install_docker](https://github.com/ednz_cloud/install_docker) to do so.

**Role Variables**
-----------------

### Service configuration

```yaml
docker_systemd_service_container_name: "My-Service"
```
The name that will be assigned to the container.

```yaml
docker_systemd_service_image: # by default, not defined
```
The image (and optionally tag) to use for the service.

```yaml
docker_systemd_service_start: true
```
Indicates whether the service should start after installation. Defaults to `true`.

```yaml
docker_systemd_service_systemd_unit_options: {}
```
Extra options to add to the `[Unit]` section of the systemd unit file. Map of strings.

```yaml
docker_systemd_service_systemd_service_options: {}
```
Extra options to add to the `[Service]` section of the systemd unit file. Map of strings.

```yaml
docker_systemd_service_name: "{{ docker_systemd_service_container_name }}_container"
```
The name of the systemd service to register.

### Container configuration

```yaml
docker_systemd_service_container_env: {}
```
A list of key/value pairs, that will be written to the environment file for the container.

```yaml
docker_systemd_service_container_pull_image: true
```
Whether or not the role should pull the image during its run, prior to starting the service.

```yaml
docker_systemd_service_container_pull_force_source: true
```
If `docker_systemd_service_container_pull_image: true`, whether the pull you be executed at every run. See [`docker_image.force_source`](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_image_module.html#parameter-force_source)

```yaml
docker_systemd_service_flags: []
```
This variable lets you pass whatever flags you need to the docker run command. It is a list, to which you can add multiple types of flags:

 - ```yaml
    - key: value
    # will pass the flag --key "value" to the container.
    Example:
      - network: host
 - ```yaml
    - simple_key
    # will pass the flag --simple_key to the container.
    Example:
      - privileged
 - ```yaml
    - key:
        - value1
        - value2
    # will pass the flags --key "value1" --key "value2" to the container.
    Example:
      - volume:
          - /path/on/host:/path/on/container
          - /var/run/docker.sock:/var/run/docker.sock:ro

**Dependencies**
---------------

None.

**Example Playbook**
-------------------

```yaml
# calling the role inside a playbook with either the default or group_vars/host_vars
- hosts: servers
  roles:
    - ednz_cloud.docker_systemd_service
```

**License**
----------

MIT / BSD

**Author Information**
---------------------

This role was created by Bertrand Lanson in 2023.
