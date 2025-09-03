#!/usr/bin/env python3

import os
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

    print(_CONFIG_PATH_)
