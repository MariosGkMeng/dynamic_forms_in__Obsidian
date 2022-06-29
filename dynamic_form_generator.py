from genericpath import exists
from turtle import fd
import numpy as np
import re
import os
import subprocess
for i in range(15): print("      ") 


class findOccurrences():
    def __init__(self, s, ch):
        y = [i for i, letter in enumerate(s) if letter == ch]
        # y = []
        # for i, letter in enumerate(s): 
        #     if letter == ch:
        #         y.append(i)
        self.y = y
    
    # def append(self, x):
    #     z = []
    


def read_table_obsidian(file1, varId):
    """Reads a table in Obsidian. The table itself is specified via 'varId'.
       Example:
       --------
       # Parameters  
    """

    table_start_prefix = '- |'
    found_table = False
    table_has_started = False
    Lines = file1.readlines()
    table = []
    i = -1
    for iLn, ln in enumerate(Lines):

        if not found_table:
            if varId in ln: found_table = True

        if not table_has_started:
            if found_table and table_start_prefix in ln:
                table_has_started = True
                iTbl = iLn

        if table_has_started and iLn > iTbl:

            if not '|' in ln: break

            row = ln.split('|')
            row = [item for item in row if len(item) > 0 and item!= '\n']
            for i in range(len(row)): row[i] = row[i].replace(' ', '')
            table.append(row)

    columns = Lines[iTbl-1].split('|')
    columns = [item for item in columns if len(item) > 0]
    for i in range(len(columns)): columns[i] = columns[i].replace(' ', '')
    return table, columns

def extract_parameters_md_file(Lines, par):

    # global value_val_i

    vars = []
    vals = []
    fams = []
    cpLines = []
    # value_val_i = 0
    # value_val_i = par['value_val_i']
    found_table = False
    sep = par['sep']
    pval = dict()
    pvar = dict()
    iRun = 0
    for iLn, ln in enumerate(Lines):
        par_family = ''
        cpLn = ln
        if par['curr_run_prefix'] in ln:
            # get run number
            iRun = ln.replace(par['curr_run_prefix'], '')
            iRun = iRun.replace(' ', '')
            iRun = iRun.replace('\n', '')

        if ln.startswith(par['line_inp']) and (not found_table):
            found_table = True
            if par['search_family']:
                # Get parameter family ========================================================
                
                for ii in range(2, 100):
                    cLine = Lines[iLn-ii]
                    if cLine.startswith('##'):
                        i0=cLine.find('(')+1
                        i1=cLine.find(')')
                        par_family = cLine[i0:i1].replace(' ', '')
                        break
                # ======================================================================================

        elif found_table:

            if not ln.startswith(sep): 
                # table ended
                found_table = False
            else:
                x = ln.split(sep)
                x = x[1:-1]
                Lx = len(x)
                for i in range(int(Lx/2)):
                    var_i = x[2*i]
                    val_i = x[2*i+1]
                    var_i = var_i.replace(' ', '')
                    if '[[' in var_i and ']]' in var_i:
                        i0=var_i.find('[[')+2
                        i1=var_i.find(']]')
                        var_i = var_i[i0:i1]

                    # Trim val_i back and forth ================================================================================================
                    if not val_i == ' '*len(val_i):
                        for i in range(6):
                            val_i = val_i.replace(' '*(i+1), ' ')
                        k0=0
                        while val_i[k0] == ' ': k0+=1
                        val_i = val_i[k0:]
                        k1=1
                        while val_i[-k1] == ' ': k1+=1

                        val_i = val_i[:-k1+1]
                    # ================================================================================================================================================================================================
                        # pval[val_i] = val_i
                        pvar[var_i] = val_i
                        if 'exec' in val_i:
                            entire_expr = val_i
                            val_i = val_i[:-1].replace('exec(', '')
                            val_i = val_i.replace('\*', "*")
                            val_i = val_i.replace('\==', "==")
                            
                            other_vars = np.unique(re.findall(par['words_pattern'], val_i, flags=re.IGNORECASE))
                            
                            for ii, ot in enumerate(other_vars):
                                other_vars[ii] = ot.replace(' ', '')

                            pp=pvar.keys()
                            lensV = []
                            for tmp in other_vars: lensV.append(len(tmp))

                            np.argsort(lensV)
                            tt = np.argsort(lensV)
                            val_i0 = val_i
                            
                            for vOther in other_vars[tt[-1::-1]]:
                                if not vOther in par['list_np']:
                                    if len(vOther)>0:
                                        vOther = vOther.replace('1-', '')
                                        vOtherB = vOther + ' ' # so that similar tags don't get confused
                                        if vOther in pp:
                                            val_i = val_i.replace(vOtherB, "pvar['" + vOther + "']")
                                        else:
                                            val_i = val_i.replace(vOtherB, "'" + vOther + "'")
                            val_i = val_i.replace("\'1\'", '1')
                            # try:
                            value_val_i = eval(val_i)
                            # except:
                                # raiseMsg = 'The expression: "' + val_i + '" could not be evaluated! Check the comments in the file:' + files['dynamic_form_lab']
                                # raise(raiseMsg)
                                # foundError = True
                                # errorLine = fd
                                # break

                            pvar[var_i] = value_val_i    
                            val_i = str(value_val_i)   
                            
                            cpLn = cpLn.replace(entire_expr, val_i)
                        vars.append(var_i)
                        vals.append(val_i)
                        fams.append(par_family)

        cpLines.append(cpLn)

    return vars, vals, fams, iRun, cpLines


# 👇🏼 USER PARAMETERS

par_case = 1 # 1: cover_letter_lab, 2: deleteme_lab

if par_case == 1:
    path0 = 'C:\\MARIOS\\WORK\\workTips'

    files = dict()
    files['dynamic_form_lab'] = path0 + '\\' + 'CoverLetterLab.md'
    files['field_source'] = 'tableJobs.md'
    files['table_source_name'] = '# Saved Positions'
    files['write_form'] = path0+ '\\' + 'CoverLetter.md'

    # 👇🏼👇🏼 columns from "files['table_source_name']" that are used as fields
    flds2change = ['#🔰/JobType', '#🔰/Topic', '#🔰/Country', '#🔰/Company']
    
elif par_case == 2:
    
    path0 = 'C:\\MARIOS\\WORK\\workTips'

    files = dict()
    files['dynamic_form_lab'] = path0 + '\\' + 'form_lab_deleteme1.md'
    files['field_source'] = 'table_deleteme1.md'
    files['table_source_name'] = '# Table'
    files['write_form'] = path0+ '\\' + 'form_deleteme1.md'

    # 👇🏼👇🏼 columns from "files['table_source_name']" that are used as fields
    flds2change = ['#🔰/Product_type', '#🔰/Country']
    #   ℹ --> can create this based on what is in "files['field_source']"
# 👆🏼👆🏼

# 👆🏼

par = dict()
par['list_np'] = ['abs', 'np']

fileFormLab = open(files['dynamic_form_lab'], encoding='utf8')#, 'r')
Lines = fileFormLab.readlines()


for ln in Lines:
    if '# FormID:' in ln:
        FormID = ln.replace('# FormID:', '')
        FormID = FormID.replace(' ','')
        FormID = FormID.replace('\n','')

file1 = open(path0+ '\\' + files['field_source'], encoding='utf8')

[table, columns] = read_table_obsidian(file1, files['table_source_name'])

for iTbl, row in enumerate(table):
    if row[0] == FormID:  break

# Get field values in FormID ==\==================================================\==================================================\==================================================    
fieldPrfx = dict()

# 👇🏼                                <search criteria>      <column index>    <field value>

for j, f in enumerate(flds2change): fieldPrfx[f]   = [[f],       np.NAN,             '']

# note: all elements of <search criteria> should be in the column name in order for the field to match
# 👆🏼

for key in fieldPrfx.keys():
    for ic, col in enumerate(columns):
        foundField = True
        for t in fieldPrfx[key][0]: 
            foundField = foundField and (t in col)

        if foundField: break
    fieldPrfx[key][1] = ic
    fieldPrfx[key][2] = table[iTbl][ic]
# \==================================================\==================================================\==================================================    




par['words_pattern'] = '[a-z,_,\/,#,🏁,⚠,💬,⚙,🗝,🔰,❓,🔅,🚧,🕊, 1-9, -]+' #'[a-z,_,#,🏁,💬,⚙,🗝,/,🔰,❓,💪,🚧,🕊, 1-9, -]+' 
par['line_inp'] = '| -'
par['curr_run_prefix'] = 'curr_run::' 
par['sep'] = "|"
par['search_family'] = False


# fileFormLab.close()
# fileFormLab = open(path0 + '\\' + 'CoverLetterLab.md', encoding='utf8')#, 'r')
# [table_pars, col_pars] = read_table_obsidian(fileFormLab, '# Parameters')

# for t in table_pars:
#     for fd in flds2change:
#         if fd in t:

for iLn, ln in enumerate(Lines):
    if '# Parameters' in ln: break

iLn0=iLn
keysSearch = fieldPrfx.keys()
for iLn, ln in enumerate(Lines[iLn0+1:]):
    for ik, key in enumerate(keysSearch):
        if key in ln:
            idxk = ln.find(key) + len(key)
            rest_of_line = ' | ' + fieldPrfx[key][2] + ' |\n'
            ln = ln[:idxk] + rest_of_line
            Lines[iLn+iLn0+1] = ln
            keysSearch = [item for item in keysSearch if item!=key]
            break

    if '# Main' in ln:
        break


for iLn, ln in enumerate(Lines):
    if '# Main' in ln: break


fileFormLab.close()
fileFormLab = open(files['dynamic_form_lab'], 'w', encoding='UTF-8') 
fileFormLab.writelines(Lines)
fileFormLab.close()

[vars, vals, fams, iRun, cpLines] = extract_parameters_md_file(Lines[:iLn-1], par)

mainBody0 = Lines[iLn+1:]
mainBody = ''
for ln in mainBody0:
    mainBody += ln


# Replace fields with their values \==================================================
n = 0
while ('#' in mainBody) and (n < 100):
    n += 1
    for i in range(len(vals)):
        if vals[i] != '':
            mainBody = mainBody.replace(vars[i], vals[i])
        else:
            mainBody = mainBody.replace(vars[i], '==' + vars[i].replace('#', '') + '==')
# \==================================================\==================================================


# Clean mainBody \==================================================

mainBody = mainBody.replace('..', '.')


# \==================================================\==================================================

# print(mainBody)    
file1.close()
file1 = open(files['write_form'], 'w', encoding='utf8')
file1.writelines(mainBody)
file1.close()
