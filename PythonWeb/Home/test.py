# from Home.models import History, statusTracking
# from django.contrib.auth.models import User

# def transfer_data():
#     # Lấy tất cả người dùng từ bảng User
#     users = User.objects.all()
    
#     for user in users:
#         # Kiểm tra xem có bản ghi statusTracking nào có user_id tương ứng không
#         if not statusTracking.objects.filter(user_id=user.id).exists():
#             # Tạo bản ghi statusTracking mới nếu không tồn tại
#             statusTracking.objects.create(user_id=user.id)
    
#     return len(users)  # Trả về số lượng người dùng đã xử lý

# n = transfer_data()
# print(n)

# import sqlite3

# # Kết nối vào cơ sở dữ liệu SQLite
# conn = sqlite3.connect('/Users/admin/Desktop/python_training/django_project/PythonWeb/db.sqlite3')
# cursor = conn.cursor()

# # Lấy danh sách tất cả các người dùng từ bảng auth_user
# cursor.execute("DELETE FROM django_admin_log WHERE user_id IS 1")

# # Lưu thay đổi vào cơ sở dữ liệu
# conn.commit()

# # Đóng kết nối đến cơ sở dữ liệu SQLite
# conn.close()

