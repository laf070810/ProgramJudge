# This script is for judging programming homework.
# Usage: Put this script in the same dir as the homework and then run this script.

import subprocess
import os
import time
import zipfile
import shutil
from openpyxl import load_workbook


def check_once(executable, input, output):
    '''check the executable for one sample

    :param executable: String. the path of the executable
    :param input: String. sample input
    :param output: String. sample output
    :return: True or False
    '''
    ret = subprocess.run(
        executable,
        input=input,
        stdout=subprocess.PIPE,
        encoding='ascii')
    if (ret.stdout != output
            and ret.stdout[:-1] != output):  # 忽略末尾换行
        return False
    else:
        return True


def check(executable, inputs, outputs):
    '''check the executable for multiple samples

    :param executable: String. the path of the executable
    :param inputs: list of String. sample input
    :param outputs: list of String. sample Output
    :return: list of True and False
    '''
    return [check_once(executable, inputs[i], outputs[i]) for i in range(len(inputs))]


def get_samples():
    '''get samples for judging an executable

    :return: Tuple. (list of inputs, list of outputs)
    '''
    with open('sample.txt', "r") as inputs_file:
        inputs = inputs_file.readlines()  # 样例输入
    with open('ans.txt', "r") as outputs_file:
        outputs = outputs_file.readlines()  # 样例输出
    return inputs, outputs


def generate_samples():
    '''

    :return: Tuple. (list of inputs, list of outputs)
    '''

WORKBOOK_PATH = '新生c.xlsx'
wb = load_workbook(WORKBOOK_PATH)
ws = wb.active
cell_range = ws['A3':'B77']
names = [cell[0] for cell in cell_range]

files = os.listdir('.')
for file in files:
    if not os.path.isdir(file):
        if zipfile.is_zipfile(file) and file.split('.')[1] == 'zip':
            # ----------Extract the zip file----------
            with zipfile.ZipFile(file, 'r') as zf:
                for name in zf.namelist():
                    os.renames(zf.extract(name), name.encode('cp437').decode('gbk'))

            # ----------check for exercise 1----------
            dirname = file.split('.')[0]
            participant_name = dirname.split(' ')[0]
            inputs, outputs = get_samples()
            print('Judging ' + participant_name)
            begin_time = time.perf_counter()
            result = check('./' + dirname + '/1/1.exe', inputs, outputs)
            end_time = time.perf_counter()
            accuracy = result.count(True) / len(result)
            time_consumption = end_time - begin_time
            print('Successfully judged ' + participant_name)
            print('accuracy\ttime')
            print('{:.3f}'.format(accuracy) + '\t' + '{:.3f}'.format(time_consumption))
            for name in names:
                if name.value == participant_name:
                    ws.cell(row=name.row, column=name.col_idx + 1).value = accuracy
                    ws.cell(row=name.row, column=name.col_idx + 2).value = time_consumption
                    print('Successfully saved ' + participant_name + '\n')
                    break

            # ----------delete the extracted files----------
            shutil.rmtree(dirname)

wb.save(WORKBOOK_PATH)
wb.close()
