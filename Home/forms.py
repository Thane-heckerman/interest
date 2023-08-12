from django import forms
import re
from django.contrib.auth.models import User

# Form đăng ký user
# tạo class thông tin của users
class RegistrationForms(forms.Form):
    username = forms.CharField(label='Tài khoản', max_length=50)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Nhập password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Nhập lại password', widget=forms.PasswordInput())

    # Hàm kiểm tra password 
    def PassCheck(self):
        # Trường hợp mật khẩu đã được nhập
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1: #test trường hợp không có and password1
                return password2 #test trường hợp return password1
        raise forms.ValidationError('mật khẩu không hợp lệ')
    
    # Hàm kiểm tra username có valid không
    def UsernameCheck(self):
        username = self.cleaned_data['username']
        if re.search(r'^\w+$',username):
            raise forms.ValidationError('usename có chứa ký tự đặc biệt')
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('tài khoản không tồn tại')
    
    # Hàm lưu user hợp lệ vào db
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'],password=self.cleaned_data['password1'],email = self.cleaned_data['email'])


    



