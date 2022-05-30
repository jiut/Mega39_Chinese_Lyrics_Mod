# """
# # 替换掉字符串value内竖线之后的的内容
# # """
import re

# src = '[{"fullline":"date","value":"2017数据"},{"fullline":"年收入","value":"3000|{"url":"http://www.abc.com/chart/income","x":"0","y":"456.172820"}"},{"fullline":"税款","value":"-"},{"fullline":"人数","value":"3419"},{"fullline":"部门","value":"27|{"url":"http://www.abc.com/department/list","x":"0","y":"155.852820"}"},{"fullline":"部门营收","value":"-"}]'

# #通过则表达式查找，如果有多个匹配，只能获取到最后一个
# matches = re.search('\|{.*?"}', src)
# while matches is not None:
#     src = src.replace(matches.group(0), '')
#     matches = re.search('\|{.*?"}', src)


def file_content_refullline(src_txt_file, map, target_txt_file):
    f1 = open(src_txt_file, 'rb')
    lines = f1.readlines()  # 整行读取
    for line in lines:
        r1 = line.strip()  # 去除原来每行后面的换行符，但有可能是\r或\r\n
        fullline = r1.strip().decode('utf-8')
        matches = re.search('pv_[0-9]{3}.lyric.[0-9]{3}=', fullline)
        if matches is None:
            matches = re.search('pv_[0-9]{3}.song_name=', fullline)
        if matches is not None:
            print(matches.group(0))
            f2 = open(map, 'rb')
            targetLines = f2.readlines()
            for targetLine in targetLines:
                r2 = targetLine.strip()
                target = r2.strip().decode('utf-8')
                lyrics = re.search(r'(?<='+matches.group(0)+').+', target)
                if lyrics is None:
                    continue
                else:
                    break
            if lyrics is not None:
                fullline = ("%s%s" %(matches.group(0),lyrics.group(0)))
            f2.close()
        newfile = open(target_txt_file, 'a', encoding='utf-8')
        fullline = (fullline+'\n')
        newfile.write(fullline)
        newfile.close()

file1 = './mdata_pv_db_old.txt'
file2 = './mdata_pv_db.txt'
file3 = './test3.txt'

file_content_refullline(file1, file2, file3)
