import xlwt
import xlrd


class ExcelOperation:
    def read_excel(self):
        try:
            workbook = xlrd.open_workbook('/home/oto/Desktop/Project/django-projects/storefront/xlwt_save01.xlsx',on_demand=True)
            worksheet = workbook.sheet_by_index(0)
            read_data_list = list()
            for row in range(1, worksheet.nrows):
                h1 = int(worksheet.cell_value(row, 0)) if worksheet.cell_value(row, 0) else 0
                h2 = int(worksheet.cell_value(row, 1)) if worksheet.cell_value(row, 1) else 0
                read_data_row_list = [h1, h2]
                read_data_list.append(read_data_row_list)
            return read_data_list
        except Exception as e:
            print(e.__str__())
            pass

    def write_excel(self, input_data):
        try:

            worksheet = xlwt.Workbook()
            sheet = worksheet.add_sheet('data_multiple_by_ten')
            sheet.write(0, 0, 'Yo')
            sheet.write(0, 1, 'Howdy')
            i = 1
            for input_value in input_data:
                j = 0
                a1 = input_value[0] * 10 if len(input_value) > 0 else 0
                a2 = input_value[1] * 10 if len(input_value) > 1 else 0
                sheet.write(i, j, a1)
                sheet.write(i, j + 1, a2)
                print(a1, a2)
                i+=1
            worksheet.save("data_multiple_by_ten.xlsx")
        except Exception as e:
            print(e.__str__())
            pass


ops = ExcelOperation()
read_output = ops.read_excel()
ops.write_excel(read_output)