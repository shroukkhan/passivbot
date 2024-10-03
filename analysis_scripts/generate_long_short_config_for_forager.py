# write main method like ___main___ in python
import os


if __name__ == '__main__':
    directories = {'longs': r'C:\AgodaGit\passivbot\configs\live\longs',
                   'shorts': r'C:\AgodaGit\passivbot\configs\live\shorts'}
    ROOT_PATH = 'C:/AgodaGit/passivbot/'
    
    '''
    now 
    1. iterate through longs and shorts directories listing all files ending with .json , use glob
    2. for each file , get the name without extension
    3. append the name and the file path starting from configs/live/longs/ or configs/live/shorts/ to two separate list
    '''
    
    longs = []
    shorts = []
    for directory in directories:
        for file in os.listdir(directories[directory]):
            if file.endswith('.json'):
                file_name_without_extension = file.split('.')[0]
                _directory = directories[directory].replace('\\', '/').replace(ROOT_PATH,'')
                #line_to_append = f'{file_name_without_extension}: {_directory}/{file}'
                line_to_append = f'{file_name_without_extension}'
                if directory == 'longs':
                    longs.append(line_to_append)
                else:
                    shorts.append(line_to_append)


    # print longs as a string separated by new line
    print('\n'.join(longs))
    print('\n\n-----\n\n')
    print('\n'.join(shorts))
    

