# filter_plugins/docker_filters.py


def create_docker_flags(flags):
    if flags:
        return "\n".join([create_docker_flag(item) for item in flags])
    return None


def create_docker_flag(item):
    if isinstance(item, dict):
        key = list(item.keys())[0]
        value = item[key]
        if isinstance(value, list):
            return "\n".join(['--{} "{}" \\'.format(key, val) for val in value])
        else:
            return '--{} "{}" \\'.format(key, value)
    elif isinstance(item, str):
        return "--{} \\".format(item)
    else:
        return ""


class FilterModule(object):
    def filters(self):
        return {
            "create_docker_flags": create_docker_flags,
        }
