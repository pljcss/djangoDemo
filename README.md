# djangoDemo
新建app
python manage.py startapp edu_users
python manage.py startapp edu_course
python manage.py startapp edu_organization
python manage.py startapp edu_operation

设计每个app的model

因为Image字段需要用到pillow所以需要安装该库
	pip install pillow

重载

设计数据库

迁移数据库
python manage.py makemigrations
python manage.py migrate
	
	出问题就删表、删migrations文件


安装xadmin

重新生成
python manage.py createsuperuser


验证码库
pip install  django-simple-captcha

生成验证码到数据库
	python manage.py makemigrations
	python manage.py migrate