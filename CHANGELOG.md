## v0.2.0 (2024-11-09)

### Feat

- enable customization of unit options in systemd file

## v0.1.0 (2024-11-09)

### Feat

- only allow starting and managing running services.
- **core**: change namespace
- **sample**: added sample file in defaults/
- **template**: do not print new lines if value of flag is None
- **cicd**: add publish job
- **cicd**: add unit testing jobs
- **tests**: added custom tests for both vagrant and docker
- **tests**: add testing for the default values on both docker and vagrant
- **readme**: update documentation on variables
- **template**: move flag formatting to filter_plugin
- **template**: test the type of data against list to enable passing integers or strings or lists
- **template**: add support for simple string flags
- **readme**: credits mhutter for original material
- **template**: add support for passing all docker run arguments
- **readme**: add requirements for docker being installed
- **ci**: add linting job
- **readme**: added description for all variables
- **molecule**: add default and default_vagrant tests
- make everything mostly work
- simple copy from mhutter role

### Fix

- typo in install.yml file
- handlers running in unpredictable ways
- change test scenario names in CICD
- wrong link in readme
- linting
