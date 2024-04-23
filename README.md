Đồ án 1 môn học cơ sở dữ liệu:

Xây dựng sơ đồ lược đồ CSDL TRUONGHOC (Trường học) gồm các lược đồ quan hệ, các khóa chính, các khóa ngoại.

Khi thực hiện câu lệnh 
```shell
mysql –u root –p < CreateSchema.sql
```
từ shell, có thể:
-	Tạo ra CSDL tên TRUONGHOC với tất cả các table kèm theo các ràng buộc PRIMARY KEY, FOREIGN KEY, NOT NULL đã xác định ở Câu 1.

File generate.py
-	Input: Đường dẫn đến folder Data chứa các file excel đã tải về.  
-	Output: các file có cùng tên trong Data, nhưng tên mở rộng là .sql: mỗi file .sql gồm các câu lệnh INSERT, khi chạy sẽ cho phép chuyển dữ liệu từ file excel vào table tương ứng trong database TRUONGHOC đã tạo ở Phần 1b.
