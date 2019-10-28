# python3.5写入excel示例
import xlsxwriter

workbook = xlsxwriter.Workbook('Py3读写excel.xlsx')
worksheet1 = workbook.add_worksheet("测试PY写入excel1")
worksheet2 = workbook.add_worksheet("测试PY写入excel2")
for i in range(100):
    worksheet1.write(i, 0, '陈健')
    worksheet2.write(i, 0, '陈健')
    # worksheet1
# worksheet.close()
workbook.close()
