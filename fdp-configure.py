#!/usr/bin/env python3

import json
import os
import re
import sys

if __name__ == '__main__':

    _FLAG_ = sys.argv[1] if len(sys.argv) == 2 else None

    if _FLAG_ == '--help':

        print('Uso:')
        print('fdp-configure [flag] \n')
        print(
            '--global       : Salva o arquivo de configuração no HOME do usuário atual. Caso seja omitido o path atual será usado.'
        )
        sys.exit(0)

    _CONFIG_PATH_ = (
        os.path.join(os.getenv('HOME'), 'fdp.config.json')
        if len(sys.argv) == 2 and sys.argv[1] == '--global'
        else os.path.join(os.getcwd(), 'fdp.config.json')
    )

    data_config = {}

    if os.path.exists(_CONFIG_PATH_):

        with open(_CONFIG_PATH_, 'r') as f:
            data_config = json.load(f)

    else:

        data_config['projects'] = {}

    project_name = input('- Digite o nome do projeto: ')

    regex_pattern = r'^[a-z_-]+$'

    if not re.fullmatch(regex_pattern, project_name):
        print(
            'Erro: nome do projeto deve ter apenas letras minúsculas hífens e/ou underlines!',
            file=sys.stderr,
        )
        sys.exit(1)

    if project_name not in data_config['projects']:
        data_config['projects'][project_name] = {}

    while True:

        env = input('- Digite o ambiente do projeto [padrão: dev]: ')

        if len(env) == 0:
            env = 'dev'

        if not re.fullmatch(regex_pattern, project_name):
            print(
                'Erro: env do projeto deve ter apenas letras minúsculas hífens e/ou underlines!',
                file=sys.stderr,
            )
            sys.exit(1)

        if env not in data_config['projects'][project_name]:
            data_config['projects'][project_name][env] = {}

        data_config['projects'][project_name][env]['host'] = input(
            f'({env}) - HOST: '
        )
        data_config['projects'][project_name][env]['user'] = input(
            f'({env}) - USER: '
        )
        data_config['projects'][project_name][env]['pass'] = input(
            f'({env}) - PASS: '
        )
        data_config['projects'][project_name][env]['path'] = input(
            f'({env}) - PATH: '
        )

        opt = str(input('- Adicionar mais um ambiente? (s/N) ')).upper()

        if opt == '':
            opt = 'N'

        while opt not in ['N', 'S']:
            print('Digite S ou N!')
            opt = str(input('- Adicionar mais um ambiente? (s/N) ')).upper()

        if str(opt).upper() == 'N':
            break

    with open(_CONFIG_PATH_, 'w') as f:
        json.dump(data_config, f, indent=2)

    print('Configuração finalizada!')
