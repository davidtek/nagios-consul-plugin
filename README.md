## What is this?

This is a consul check integration plugin for nagios that makes easy to add nagios commands that queries health checks for a specific service in a consul cluster.

Returns 2 if there are any critical checks, 1 if there are no criticals but warnings. Returns 3 when node service found. Returns 0 on passing checks.


@note : although forked from nagios-consul-plugin, this fork contains different fonctionality entirely and can coexist with nagios-consul-plugin

## Example

Query the local consul agent for the service called redis
```
$ python check-consul-service-health.py redis
Passing: 1
> client-194:redis:service: "redis" check:_nomad-check-5b66dc56a4ddb90311cb544f84d299d0de76d0e8:passing

```

## Install dependencies with pip

```
pip install -r requirements.txt
```

## Usage

```
$ python check-consul-service-health.py -h
Usage: 
    check-consul-health.py SERVICE
        [--addr=ADDR]
        [--verbose]

Arguments:
    SERVICE service to check

Options:
    -h --help                  show this
    -v --verbose               verbose output
    --addr=ADDR                consul address [default: http://localhost:8500]
```

