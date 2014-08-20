#!/usr/bin/python                                                                                                   
# -*- coding: utf8 -*-

# 
# @project: convert2utf8
# @author: roga@roga.tw
# the convert2utf8.res mapping file is based on "深藍UTF-8正體簡體轉換函數 1.0" http://tinyurl.com/3joxvnm
#
#

import sys
import os
import shutil
import ConfigParser

def convert_simplified_to_traditional(t_str, s_str, o_str):
    str = u""
    for i in range(0, len(o_str)) :
        if s_str.find(o_str[i]) != -1 :
            str += t_str[s_str.index(o_str[i])]
        else :
            str += o_str[i]
    return str

# start error message

MSG_AUTHOR = "convert2utf8, GPL v2, author: roga<roga@roga.tw>.\n"
MSG_WRONG_ARGC = "錯誤 - 使用方法： convert2utf8 [filename] {source file encoding}\n" + "預設來源編碼是 gbk , code page 詳見： http://docs.python.org/library/codecs.html#standard-encodings"
MSG_NOT_SUPPORT_ENCODING = "錯誤 - 無法正確解讀來源檔案，請指定正確的編碼。\n"
MSG_TEXT_FILE_NOT_FOUND = "錯誤 - 檔案找不到："
MSG_CONVERT_FINISH = "成功 - 轉換完成。\n"
MSG_RESOURCE_FILE_NOT_FOUND = "錯誤 - 簡繁字對映應檔找不到，請重新安裝本程式。\n"
# end of error message

# start parse parameters

print MSG_AUTHOR

argc = len(sys.argv)

if argc > 3 or argc == 1:
    exit(MSG_WRONG_ARGC);
elif argc == 3 :
    mode = sys.argv[2]
elif argc == 2 :
    mode = 'gbk'
else :
    exit(MSG_WRONG_ARGC)

# end of parse parameters.

dir_separator = os.path.sep
current_dir = os.getcwd()
current_file = sys.argv[1] 

if not os.path.isfile (current_file): 
    target_file = current_dir + dir_separator + current_file
else :
    target_file = current_file
    
# check file exists or not.
if not os.path.isfile (target_file): 
     exit(MSG_TEXT_FILE_NOT_FOUND + "%s" % target_file) 

config = ConfigParser.ConfigParser()

resource_file = '/usr/local/bin/convert2utf8.res';
if not os.path.isfile (resource_file): 
    exit(MSG_RESOURCE_FILE_NOT_FOUND)

config.readfp(open(resource_file))
t_str = config.get("mapping","traditional_str")
s_str = config.get("mapping","simplified_str" )

result_content = u''
original_content = u''

fp = open(target_file, 'r')
original_content = fp.read()
fp.close()

try:
    result_content = convert_simplified_to_traditional(t_str.decode('utf8'), s_str.decode('utf8'), original_content.decode(mode))
except:
    exit(MSG_NOT_SUPPORT_ENCODING)

if len(result_content) != 0 :
    # do backup
    shutil.copy2(target_file, target_file + '.bak')
    # write result to file.
    fp = open(target_file, 'w')
    fp.write(result_content.encode('utf8'))
    fp.close()
    exit(MSG_CONVERT_FINISH)