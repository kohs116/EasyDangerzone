# EasyDangerzone

<!-- ABOUT THE PROJECT -->
## π’ About The Project
μ¬μ©ν μ€νμμ€ νλ‘μ νΈ: [dangerzone](https://github.com/firstlookmedia/dangerzone)  
OS λ° μ¬λ¬ κ°μ§μ μμ‘΄μ±μ΄ λμ dangerzone νλ‘κ·Έλ¨μ μ½κ² μ¬μ©ν  μ μλλ‘ νμ₯ κ°λ°νμλ μ·¨μ§λ‘ κ³ μλ νλ‘μ νΈμλλ€.  

## π¬ μ€ν λμμ 
[μ€ν λμμ νμΈνκΈ°]( ./video)  

## π§ κΈ°λ₯ λͺ©λ‘
1. μΉμ νμΌμ μλ‘λ νλ©΄, μλ²μμ dangerzone μ κ±°μΉ λ°μ΄λ¬μ€ μλ μμ ν νμΌμ μ¬μ©μμκ² μ λ¬   
2. μ¬μ©μμκ² μ λ¬λ  λμλ Virustotal APIλ₯Ό κ±°μΉ κ²°κ³Όμ URLhausμ md5 ν΄μν€λ₯Ό λΉκ΅ν κ²°κ³Όλ₯Ό ν¨κ» μ μ μλ νμ΄μ§ μ μ   
3. Dashboardλ₯Ό ν΅ν΄ νμΌ λ³ν μΆμ΄ λ° μ¬μ©μ μΆμ΄ νμΈ κ°λ₯  
4. Feedback λ° λ¬Έμμ¬ν­μ Contactμμ μ μ‘ κ°λ₯  

νμ¬ μ§μ κ°λ₯ν νμΌ νμ λͺ©λ‘:  
* PDF(`.pdf`)
* WORD(`.docx`,`.doc`)
* EXCEL(`.xlsx`,`.xls`)
* PPT(`.pptx`,`.ppt`)
* ODF(`.odt`,`.ods`,`.odp`,`.ods`)
* JPEG(`.jpg`,`.jpeg`)
* GIF(`.gif`)
* PNG(`.png`)
* TIFF(`.tif`,`.tiff`)


<!-- GETTING STARTED -->
## π» Getting Started
for ubuntu 18.04 LTS:
```
#!/bin/bash

#echo 'ubuntu:korea123!!' | chpasswd
sudo -S sh -c 'echo "ubuntu:korea123!!" | chpasswd'

echo "deb https://packagecloud.io/firstlookmedia/code/ubuntu/ bionic main" | sudo tee -a /etc/apt/sources.list.d/firstlookmedia_code.list
curl -L https://packagecloud.io/firstlookmedia/code/gpgkey | sudo apt-key add -

sudo apt-get update
# sudo apt-get install -y ubuntu-desktop xrdp curl gnupg apt-transport-https dangerzone python3 python3-pip
sudo apt-get install -y curl gnupg apt-transport-https dangerzone python3 python3-pip

pip3 install django>=2.0
mkdir -p /tmp/dangerzone-pixel
mkdir -p /tmp/dangerzone-safe

sudo usermod -aG docker ubuntu
sudo chmod 666 /var/run/docker.sock
sudo systemctl daemon-reload
sudo systemctl start docker
sudo systemctl enable docker
/usr/bin/docker pull flmcode/dangerzone
```

for python3:
```
pip install -r requirements.txt
```

μ μκ΅¬μ¬ν­μ λͺ¨λ μ€μΉν λ€, manage.pyκ° μλ ν΄λλ‘ μ΄λν©λλ€.  

for customize:
```
my_settings.py

# λ°μ΄ν°λ² μ΄μ€μ μ λ³΄λ₯Ό μμ±ν©λλ€.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'λ°μ΄ν°λ² μ΄μ€ λͺ',
        'USER': 'μ μ μ΄λ¦',
        'PASSWORD':'ν¨μ€μλ',
        'HOST':'localhost',
        'PORT':'3306',
        'OPTIONS':{
            'init_command':'SET sql_mode="STRICT_TRANS_TABLES"'
        }
    }
}

```  
```
secrets.json

# κ°μ’ private keyλ€μ μμ±ν©λλ€.
{
  "API_KEY": "Virustotal API KEY",
  "SECRET_KEY" :"μ₯κ³  SECRET KEY",
  "WEBHOOK_KEY": "μ¬λ WEBHOOK KEY"
}
```


for Run program:
```
python3 manage.py runserver
or
python manage.py runserver
```

# π‘ UPDATE LIST
### ~11.27
* ubuntuμμ MySQL DB μ°λ  
* μλ¬ λ°μνλ λΆλΆ try~catchλ‘ μ²λ¦¬  

### ~10.19
* urlhash μ΄μ© md5 ν΄μν€λ‘ μμ±νμΌμΈμ§ νμΈ
* MySQL DB μ°λ
* ν΄λ κ΅¬μ‘° μ λ©΄ μμ  λ° MVC ν¨ν΄ 

### ~9.2
* νμΌ μλ‘λ μ, μ²«λ²μ§Έλ‘ 2page νμΌ, λλ²μ§Έλ‘ 1page νμΌμ μλ‘λ νλ©΄ μ²«λ²μ§Έ νμΌμ λλ²μ§Έ νμ΄μ§κ° κ°μ΄ mergeλμ λμ€λ μ€λ₯λ₯Ό λ°κ²¬ν¨ --> dangerzone-pixel λ΄λΆμ width, height, rgbλ₯Ό λ§€λ² λ³ν μ μ§μ°κ³  μλ‘ μλ°μ΄νΈνλλ‘ λ³κ²½  
* μ§μ λΆκ°λ₯ν νμ₯μλ₯Ό μλ‘λνμ¬ μ€ννλ©΄ λ΄λΆμμ μλ¬λ₯Ό λ°μμμΌ νμ΄μ§ μμ²΄μ μλ¬κ° λ³΄μ¬μ§λ μ€λ₯ --> νμ₯μμ λν μ‘°κ±΄μ κ±Έμ΄ μ§μ λΆκ°λ₯ν νμ₯μ νμΌμ μ ν μ λΆκ°λ₯νλ€λ alertλ₯Ό λμ°λλ‘ λ³κ²½

### ~9.10
* virustotal api json to table  
* link contact page to slack   
* modify handling file about dashboard   
