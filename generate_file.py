#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader
import yaml
import os
import glob

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def generate_files():
    yaml_file = yaml.load(open('values.yaml'))
    cur_env = Environment(loader=FileSystemLoader(THIS_DIR),
                         trim_blocks=True)

    promenade_files = glob.glob("template/*")
    if not os.path.exists('output'):
        os.makedirs('output')

    for f in promenade_files:
        new_name = f.replace("template", "output")
        with open(new_name, 'w') as cur_file:
            cur_file.write(cur_env.get_template(f).render(
        shapes=yaml_file['shapes'], general=yaml_file['general']))

if __name__ == '__main__':
    generate_files()
