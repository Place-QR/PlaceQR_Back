from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # gender 컬럼에 옵션으로 넣어 줄 클래스
    class GenderChoices(models.TextChoices):
        # 첫번째 값은 데이터베이스에 들어갈 value, 두번째 값은 관리자 페이지에 들어갈 label
        MALE = ("male", "Male") 
        FEMALE = ("female", "Female")
        
    # 성과 이름으로 분류하는 것은 서구적인 정보 입력 방식이기 때문에 관리자 페이지에서 보이지 않도록 설정한다. editable=False
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    
    # 이름 입력창
    name = models.CharField(max_length=150, default="")
    # 유저가 호스트일 경우
    is_host = models.BooleanField(null=True)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices)


