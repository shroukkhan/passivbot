import subprocess


def main():
    kwargs_list = [
        {'optimize_config_path': 'configs/optimize/scalp.hjson',
         'symbol': 'XTZUSDT'},
        {'optimize_config_path': 'configs/optimize/scalp.hjson',
         'symbol': 'ATOMUSDT'},
        {'optimize_config_path': 'configs/optimize/scalp.hjson',
         'symbol': 'XLMUSDT'},
    ]

    for kwargs in kwargs_list:
        formatted = f"python3 optimize.py {kwargs['optimize_config_path']}"
        for key in [k for k in kwargs if k != 'optimize_config_path']:
            formatted += f' --{key} {kwargs[key]}'
        print(formatted)
        subprocess.run([formatted], shell=True)


if __name__ == '__main__':
    main()