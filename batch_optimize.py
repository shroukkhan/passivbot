import subprocess


def main():
    kwargs_list = [
        {'optimize_config_path': 'configs/optimize/vanilla.hjson',
         'symbol': 'ATOMUSDT'},
        {'optimize_config_path': 'configs/optimize/vanilla.hjson',
         'symbol': 'DASHUSDT'},
        {'optimize_config_path': 'configs/optimize/vanilla.hjson',
         'symbol': 'DYDXUSDT'},
        {'optimize_config_path': 'configs/optimize/vanilla.hjson',
         'symbol': 'LINKUSDT'},
        {'optimize_config_path': 'configs/optimize/vanilla.hjson',
         'symbol': 'MANAUSDT'},
        {'optimize_config_path': 'configs/optimize/vanilla.hjson',
         'symbol': 'MATICUSDT'},
        {'optimize_config_path': 'configs/optimize/vanilla.hjson',
         'symbol': 'XTZUSDT'},
    ]

    for kwargs in kwargs_list:
        formatted = f"python3 optimize.py {kwargs['optimize_config_path']}"
        for key in [k for k in kwargs if k != 'optimize_config_path']:
            formatted += f' --{key} {kwargs[key]}'
        print(formatted)
        subprocess.run([formatted], shell=True)


if __name__ == '__main__':
    main()