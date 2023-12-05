docker_systemd_service
=========
> This repository is only a mirror. Development and testing is done on a private gitea server.

This role lets you configure a docker container and run it as a systemd service on **debian-based** distributions.

Requirements
------------

This roles assumes you have docker installed on the target host. You can use [ednxzu.install_docker](https://github.com/ednxzu/install_docker) to do so.

Role Variables
--------------
Available variables are listed below, along with default values. A sample file for the default values is available in `default/docker_systemd_service.yml.sample` in case you need it for any `group_vars` or `host_vars` configuration.

```yaml
docker_systemd_service_container_name: "My-Service" # by default, set to "My-Service"
```
The name that will be assigned to the container.

```yaml
docker_systemd_service_image: # by default, not defined
```
The image (and optionally tag) to use for the service.

```yaml
docker_systemd_service_container_env: {} # by default, set to {}
```
A list of key/value pairs, that will be written to the environment file for the container. the key NEEDS TO BE CAPTIALIZED, it will not be done automatically. Example: `MY_ENV_VAR: foobar`.

```yaml
docker_systemd_service_container_pull_image: true # by default, set to true
```
Whether or not the role should pull the image during its run.

```yaml
docker_systemd_service_container_pull_force_source: true # by default, set to true
```
If `docker_systemd_service_container_pull_image: true`, whether the pull you be executed at every run. See [`docker_image.force_source`](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_image_module.html#parameter-force_source)

```yaml
docker_systemd_service_container_labels: [] # by default, set to []
```
A list of labels to add to the container. These should be strings of the form `some.label=value`.

```yaml
docker_systemd_service_container_cmd: [] # by default, set to []
```
A list of container run command to apply.

```yaml
docker_systemd_service_container_host_network: false  # by default, set to false
```
Whether the container should use the `network_mode: host`.

```yaml
docker_systemd_service_container_network: ""  # by default, set to ""
```
If `docker_systemd_service_container_host_network: false`, you can define the network to use for the container.

```yaml
docker_systemd_service_container_user: ""  # by default, set to ""
```
Define a user to use within the container. See [user settings](https://docs.docker.com/engine/reference/run/#user)

```yaml
docker_systemd_service_container_hostname: ""  # by default, set to ""
```
The hostname to apply to the container.

```yaml
docker_systemd_service_container_links: []  # by default, set to []
```
A list of `--links` arguments.

```yaml
docker_systemd_service_container_ports: []  # by default, set to []
```
A list of ports to expose. Example: `<host_port>:<container_port>`

```yaml
docker_systemd_service_container_hosts: []  # by default, set to []
```
A list of `--add-host` arguments.

```yaml
docker_systemd_service_container_volumes: []  # by default, set to []
```
A list of volumes and their mount points. Example: `/path/on/host:/path/in/container`

```yaml
docker_systemd_service_container_cap_add: []  # by default, set to []
```
A list of capabilities to add to the container. Example: `SYS_ADMIN`.

```yaml
docker_systemd_service_container_cap_drop: []  # by default, set to []
```
A list of capabilities to remove from the container.

```yaml
docker_systemd_service_container_devices: []  # by default, set to []
```
A list of devices to add to the container.

```yaml
docker_systemd_service_container_privileged: false  # by default, set to false
```
Whether to run the container in privileged mode. See [runtime privilege](https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities)

```yaml
docker_systemd_service_container_args: ""  # by default, set to ""
```
Arbitrary list of arguments to the `docker run` command as a string.

```yaml
docker_systemd_service_name: "{{ docker_systemd_service_container_name }}_container"  # by default, set to "{{ docker_systemd_service_container_name }}_container"
```
The name of the systemd service to register.

```yaml
docker_systemd_service_systemd_options: []  # by default, set to []
```
Extra options to include in systemd service file.

```yaml
docker_systemd_service_enabled: true  # by default, set to true
```
Whether the service should be enabled during the role's run.

```yaml
docker_systemd_service_masked: false  # by default, set to false
```
Whether the service should be marked as masked.

```yaml
docker_systemd_service_state: started  # by default, set to started
```
The state the service should be put in. Valid options are: `reloaded`, `restarted`, `started`, `stopped`, and `absent`. Realistically, you probably want to use `started` or `stopped`. `absent` can be used to remove the service and all associated files from the host.

```yaml
docker_systemd_service_restart: true  # by default, set to true
```
Whether the role should restart the service if changes are made to any of the files (when service is already runing).

Dependencies
------------

None.

Example Playbook
----------------

```yaml
# calling the role inside a playbook with either the default or group_vars/host_vars
- hosts: servers
  roles:
    - ednxzu.docker_systemd_service
```

License
-------

MIT / BSD

Author Information
------------------

This role was created by Bertrand Lanson in 2023.
