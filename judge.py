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
        encoding='gbk')
    if (ret.stdout.replace('\r\n', '\n').strip('\n') != output
            and ret.stdout.replace('\r\n', '\n').strip('\n') + '\n' != output):  # 忽略末尾换行
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


def get_samples(n):
    '''get samples for judging an executable

    :param n: Integer. exercise number
    :return: Tuple. (list of inputs, list of outputs)
    '''
    with open('input_' + str(n) + '.txt', "r") as inputs_file:
        inputs = []

        row_num = inputs_file.readline()
        while row_num != '' and row_num != None:
            input = ""
            for i in range(int(row_num)):
                input += inputs_file.readline()
            inputs.append(input)

            row_num = inputs_file.readline()

    with open('output_' + str(n) + '.txt', "r") as outputs_file:
        outputs = []

        row_num = outputs_file.readline()
        while row_num != '' and row_num != None:
            output = ""
            for i in range(int(row_num)):
                output += outputs_file.readline()
            outputs.append(output)

            row_num = outputs_file.readline()

    return inputs, outputs


WORKBOOK_PATH = '新生c.xlsx'
wb = load_workbook(WORKBOOK_PATH)
ws = wb.active
cell_range = ws['A3':'A77']
names = [cell[0] for cell in cell_range]

files = os.listdir('.')
for file in files:
    if not os.path.isdir(file):
        if zipfile.is_zipfile(file) and file.split('.')[1] == 'zip':
            # ----------Extract the zip file----------
            with zipfile.ZipFile(file, 'r') as zf:
                for name in zf.namelist():
                    if not os.path.exists(name.encode('cp437').decode('gbk')):
                        os.renames(zf.extract(name), name.encode('cp437').decode('gbk'))

            # ----------check for exercises----------
            dirname = file.split('.')[0]
            participant_name = dirname.split(' ')[0]
            for i in range(3, 4):
                inputs, outputs = get_samples(i)
                print('Judging ' + participant_name + ' for exercise ' + str(i))
                begin_time = time.perf_counter()
                result = check('./' + dirname + '/' + str(i) + '/' + str(i) + '.exe', inputs, outputs)
                end_time = time.perf_counter()
                accuracy = result.count(True) / len(result)
                time_consumption = end_time - begin_time
                print('Successfully judged ' + participant_name + ' for exercise ' + str(i))
                print('accuracy\ttime')
                print('{:.3f}'.format(accuracy) + '\t' + '{:.3f}'.format(time_consumption))
                for name in names:
                    if name.value == participant_name:
                        ws.cell(row=name.row, column=name.col_idx + 3 * (i - 1) + 1).value = accuracy
                        ws.cell(row=name.row, column=name.col_idx + 3 * (i - 1) + 2).value = time_consumption
                        wb.save(WORKBOOK_PATH)
                        print('Successfully saved ' + participant_name + ' for exercise ' + str(i) + '\n')
                        break

            # ----------delete the extracted files and move the judged one to "Judged" dir----------
            shutil.rmtree(dirname)
            if not os.path.exists('Judged'):
                os.mkdir('Judged')
            shutil.move(file, 'Judged')

wb.close()
