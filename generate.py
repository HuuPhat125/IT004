import os
import pandas as pd
import sqlite3

# Đường dẫn đến thư mục chứa các file Excel
data_folder = "C:\IT004\data"

# Kết nối tới database TRUONGHOC
# conn = sqlite3.connect('')
# with open(os.path.join(data_folder, f'{'write_pgd'}.sql'), 'w', encoding="utf-8") as f:
with open(os.path.join(data_folder, 'write_pgd.sql'), 'w', encoding="utf-8") as fi:
    fi.write("use truonghoc;\n")
    ten_pdg = ['Phòng GDĐT Cần Giờ',
                'Phòng GDĐT Nhà Bè',
                'Phòng GDĐT Bình Chánh',
                'Phòng GDĐT Hóc Môn',
                'Phòng GDĐT Củ Chi',
                'Phòng GDĐT quận 7',
                'Phòng GDĐT Bình Tân',
                'Phòng GDĐT quận 8',
                'Phòng GDĐT quận 6',
                'Phòng GDĐT quận 5',
                'Phòng GDĐT quận 4',
                'Phòng GDĐT quận 11',
                'Phòng GDĐT quận 10',
                'Phòng GDĐT quận 3',
                'Phòng GDĐT quận 2',
                'Phòng GDĐT Phú Nhuận',
                'Phòng GDĐT Tân Phú',
                'Phòng GDĐT Tân Bình',
                'Phòng GDĐT Bình Thạnh',
                'Phòng GDĐT Gò Vấp',
                'Phòng GDĐT quận 9',
                'Phòng GDĐT Thủ Đức',
                'Phòng GDĐT quận 12',
                'Phòng GDĐT quận 1',
                'null']
    ma_pgd =    ['CanGio',
                'NhaBe',
                'BinhChanh',
                'HocMon',
                'CuChi',
                'Quan7',
                'BinhTan',
                'Quan8',
                'Quan6',
                'Quan5',
                'Quan4',
                'Quan11',
                'Quan10',
                'Quan3',
                'Quan2',
                'PhuNhuan',
                'TanPhu',
                'TanBinh',
                'BinhThanh',
                'GoVap',
                'Quan9',
                'ThuDuc',
                'Quan12',
                'Quan1',
                'N/A']
    for i in range(25):
        if ten_pdg[i] != "null":
            fi.write("REPLACE INTO `PHONGGDDT` VALUE('{}', '{}', 'Sở Giáo dục và Đào tạo Hồ Chí Minh');\n".format(ma_pgd[i], ten_pdg[i]))
        else:
            fi.write("REPLACE INTO `PHONGGDDT` VALUE('{}', {}, 'Sở Giáo dục và Đào tạo Hồ Chí Minh');\n".format(ma_pgd[i], ten_pdg[i]))
            

# Lặp qua các file Excel trong thư mục
for file_name in os.listdir(data_folder):
    if file_name.endswith('.xlsx'):
        if file_name == 'datagdtx.xlsx':
            k = 0
        elif file_name == 'datamn.xlsx':
            k = 5
        elif file_name == 'datath.xlsx':
            k = 3
        elif file_name == 'datathcs.xlsx':
            k = 3
        elif file_name == 'datathpt.xlsx':
            k = 3

        # Đọc dữ liệu từ file Excel

        df = pd.read_excel(os.path.join(data_folder, file_name), skiprows = k)
 
        #thay thế các ô không có giá trị bằng giá trị null
        df.fillna("null", inplace=True)
        # Lấy tên bảng từ tên file Excel
        table_name = os.path.splitext(file_name)[0]

        # # Tạo câu lệnh INSERT và lưu vào file .sql tương ứng
        with open(os.path.join(data_folder, f'{table_name}.sql'), 'w', encoding="utf-8") as f:
            f.write("use truonghoc;\n")
            for row in df.itertuples(index = False):
                value = []
                j = 0
                if df.columns[j] == 'Mã trường':
                    value.append(row[j])
                    j = j + 1
                else:
                    value.append('null')
                if df.columns[j] == 'Tên trường':
                    value.append(row[j])
                    j = j +  1
                else:
                    value.append('null')
                if df.columns[j] == 'Sở GD&ĐT':
                    j = j + 1
                #     value.append(1)
                #     j = j + 1
                # else:
                #     value.append('null')
                if df.columns[j] == 'Phòng GD&ĐT':
                    for i in range(25):
                        if i == 24:
                            value.append('N/A')
                            j = j + 1
                        elif row[j] == ten_pdg[i]:
                            value.append(ma_pgd[i])
                            j = j + 1
                            break
                else:
                    value.append('null')
                if df.columns[j] == 'Địa chỉ':
                    value.append(row[j])
                    j = j + 1
                else:
                    value.append('null')
                if df.columns[j] == 'Loại hình':
                    if row[j] == 'Công lập':
                        value.append('CL')
                    elif row[j] == 'Tư thục':
                        value.append('TT')
                    elif row[j] == 'Dân lập':
                        value.append('DL')
                    else:
                        value.append('null')
                    j = j + 1
                else:
                    value.append('null')
                if df.columns[j] == 'Loại trường':
                    if row[j] == 'Trường phổ thông':
                        value.append('PT')
                    elif row[j] == 'TT GDTX':
                        value.append('GDTX')
                    elif row[j] == 'Dân tộc bán trú':
                        value.append('DTBT')
                    elif row[j] == 'Năng khiếu thể thao':
                        value.append('NKTT')
                    elif row[j] == 'TT GDNN - GDTX (Sát nhập theo TTLT số 39/2015)':
                        value.append('GDNN')
                    else:
                        value.append('null')
                    j = j + 1
                else:
                    value.append('null')
                if df.columns[j] == 'Cấp':
                    value.append(row[j])
                    j = j + 1
                else:
                    value.append('null')
                
                print(value)
                # columns = ', '.join(value)
                # values = ', '.join(['?' for c in row])
                insert_value = ""
                for i in value:
                    if i != 'null':
                        insert_value = insert_value + "'" + str(i) + "', "
                    elif i == 'null':
                        insert_value = insert_value  + str(i) + ", "
                insert_value = insert_value[:-2]
                insert_query = f"REPLACE INTO `truong`  VALUES ({insert_value})"
            #         # conn.execute(insert_query, row)
                f.write(f"{insert_query};\n")

# Đóng kết nối tới database
# conn.close()
