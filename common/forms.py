from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.db.models import fields
from django import forms
from django.forms import widgets
from .models import *

class LoginForm(AuthenticationForm):
    username = UsernameField(
        label=False,
        widget=forms.TextInput(attrs={'autofocus': True, 'placeholder' : 'ID를 입력하세요', 'class' : 'login_input_id'}))
    password = forms.CharField(
        strip=False,
        label=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'placeholder' : '비밀번호를 입력하세요', 'class' : 'login_input_pwd'}),
    )



class RegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = '사용자 ID'
        self.fields['username'].help_text = '<ul><li>사용할 아이디 입력해주세요.</li><li>문자, 숫자, 특수문자 (@  .  | - _)  사용가능</li></ul>'
        self.fields['password1'].label = '비밀번호'
        self.fields['password1'].help_text = '<ul><li>비밀번호에 개인정보를 담지 마세요.</li><li>최소 8글자 이상되어야 합니다.</li><li>일반적으로 널리 사용되는 비밀번호는 사용할 수 없습니다.</li><li>숫자로만 이루어질 수 없습니다.</li></ul>'
        self.fields['password2'].label = '비밀번호 확인'
        self.fields['password2'].help_text = '<ul><li>위와 동일한 패스워드 입력</li></ul>'
        self.fields['name'].label = '이름'
        self.fields['name'].help_text = '<ul><li>이름을 입력해주세요.</li></ul>'
        self.fields['nickname'].label = '닉네임'
        self.fields['nickname'].help_text = '<ul><li>사용할 별명을 입력해주세요.</li></ul>'
        self.fields['email'].label = '이메일 주소'
        self.fields['content'].label = '소개글'

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'name', 'nickname', 'content', 'gender']
        widgets = {
            # 'username': forms.TextInput(attrs={'placeholder': '15자 이내로 입력 가능합니다.'}),
            # 'password1': ,
            # 'password2': ,
            # 'name': ,
            'gender': forms.RadioSelect(),
        }
