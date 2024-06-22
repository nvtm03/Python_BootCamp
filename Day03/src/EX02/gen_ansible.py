import yaml

input_file = '../../materials/todo.yml'
output_file = 'deploy.yml'
with open(input_file, 'r') as fp:
    data = yaml.safe_load(fp)


deploy = [
    {
        'name': 'EX02',
        'hosts': 'all',
        'tasks': [
            {
                'name': f'Install {data["server"]["install_packages"]}',
                'ansible.builtin.apt': {
                    'pkg': data['server']['install_packages']
                }
            },
        ]
    }
]

for file in data['server']['exploit_files']:
    yaml_for_file = {
        'name': f'Copy {file}',
        'ansible.builtin.copy': {
            'src': f'../EX01/{file}',
            'dest': f'/etc/{file}'
        }
    }
    deploy[0]['tasks'].append(yaml_for_file)


for file in data['server']['exploit_files']:
    args = ''
    if file == 'consumer.py':
        args += ' -e'
        for bad_guy in data['bad_guys']:
            args += f' {bad_guy}'
    yaml_for_file = {
        'name': f'Run a script {file}',
        'ansible.builtin.script': {
            'cmd': f'python3 /etc/{file}{args}'
        }
    }
    deploy[0]['tasks'].append(yaml_for_file)


with open(output_file, 'w') as fp:
    yaml.safe_dump(deploy, fp, encoding='UTF-8', sort_keys=None)
