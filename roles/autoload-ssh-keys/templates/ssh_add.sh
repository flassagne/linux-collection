{# -*- mode: jinja-shell -*- #}
#! /bin/bash

ssh-add 
{%- for keys in ssh_keys %}
 -q ~/.ssh/{{ keys }}
{%- endfor %}
