import xlsxwriter


class ProblemStatement():
    def read_excel(self):
        workbook = xlsxwriter.Workbook("otosheet.xlsx")
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'Header1')
        worksheet.write('B1', 'H1')
        worksheet.write('C1', 'H2')
        worksheet.write('D1', 'H3')
        worksheet.write('E1', 'H4')
        worksheet.write('F1', 'H5')
        worksheet.write('G1', 'H6')
        worksheet.write('H1', 'H7')
        worksheet.write('I1', 'H8')
        worksheet.write('J1', 'H9')
        worksheet.write('K1', 'H10')


        row = 1
        column = 0

        content = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

        for item in content :
            worksheet.write(row, column, item)
            
            row = row + 1

        return workbook.close()

    def write_excel(self):
        workbook = xlsxwriter.Workbook("otosheet.xlsx")
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'A1')
        worksheet.write('B1', 'A2')
        worksheet.write('C1', 'A3')
        worksheet.write('D1', 'A4')
        worksheet.write('E1', 'A5')
        worksheet.write('F1', 'A6')
        worksheet.write('G1', 'A7')
        worksheet.write('H1', 'A8')
        worksheet.write('I1', 'A9')
        worksheet.write('J1', 'A10')



        row = 1
        column = 0

        content = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        
        a_list = [item * 10 for item in content]
        for item in a_list :
            worksheet.write(row, column, item)      
            row = row + 1

        return workbook.close()


problem_statement = ProblemStatement()
problem_statement.read_excel() 
problem_statement.write_excel()



   
# def addone():
#     file = open("data/" + str(messager) + ".txt", "r")
#     dataint = f.readline()
#     dataint = int(dataint) + 1
#     file.close()
#     file = open("data/" + str(messager) + ".txt", "w")
#     file.write(str(dataint))
#     file.close()