@echo off

::���·�����Ҫ�������Ƶ����Ƶ��ʽ�������г���һЩ��Ҫ����Ƶ��ʽ
set Ext=*.str

@REM md output

echo ��ʼ��Ƶת��

::���·����������ʽ���������Ϊmp4�������и���
for %%a in (%Ext%) do (
	echo ����ת����%%a
    D:\Files\Programs\DatabaseConverter\DatabaseConverter.exe "%%a"
)

echo ת�����

pause