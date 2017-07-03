#Django

./manage.py migrate

적용하기

./manage.py makemigrations

적용한거 불러오기




```
from blog.models import Post
from django.contrib.auth.models import User
from django.utils import timezone

Post.objects.all()


pl =Post.objects.all()
#포스트 전체 출력
pl.query()
#쿼리 보기


user = User.objects.get(id=1)
#유저 지정

Post.objects.create(title="Test title",text = "Test Text",author=user)
#게시글 만들기



pl=Post.objects.filter(title__contains ='만들고')
#필터 적용

Post.objects.filter(published_date__lte=timezone.now())
#필터 적용

post = Post.objects.get(title='Test title')
# test title이라는 post객체 가져오기
post.publish()
#현재시간 적용
```
