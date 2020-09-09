# 프로젝트 소개

'EasyDangerzone' 프로젝트는 악성코드 문서 파일을 안전한 파일로 변환하여 사용자에게 제공하는 것이 주된 목적이다.
Docker를 활용하여 네트워크가 단절된 컨테이너를 사용하여 문서 파일을 쪼개고 PDF 파일로 합친 다음 안전한 파일을 사용자에게 제공한다.
또한,  'EasyDangerzone' 프로젝트는 크게 "웹애플리케이션"과 "데스크탑S/W"로 구성되어 있다.
- 웹애플리케이션은 사용자가 브라우저를 이용하여  'EasyDangerzone' 사이트에 접속하고 문서 파일을 업로드하여 안전한 파일로 변환한다.
- 데스크탑 S/W는 브라우저에서 사이트 접속 없이 파일 업로드 기능을 사용하여 안전한 파일 변환이 가능하며, 추가적으로 좀 더 사용 편리성을 위해  컨텍스트 매뉴를 제공하여
설치 후 변환이 필요한 파일을 선택한 다음 오른쪽 마우스를 클릭하여 안전한 파일로 변환이 가능하다.

# 오픈소스 기반 문서형 악성코드 차단 프로그램

사용자의 환경에 의존적인 dangerzone 프로그램을 서버에서 실행시켜 웹을 통해 편리하게 이용할 수 있도록 구성  

## 실행 방법
* dangerzone까지 실행되는 데모 버전: [사이트 접속하기](http://ec2-13-209-68-171.ap-northeast-2.compute.amazonaws.com:5000/)
* web design 추가, dangerzone 실행 안됨: [사이트 접속하기](http://ec2-52-78-218-146.ap-northeast-2.compute.amazonaws.com:5000/)

실행방법 영상은 다음 링크의 동영상에서 확인하실 수 있습니다. 공유 드라이브를 사용하였기 때문에 허용된 사용자만 확인할 수 있습니다.   
* [실행화면 mp4](https://drive.google.com/drive/folders/1ku7cOMkbfjbLHsrQ8Lhv1KWfaGFCSlRL?usp=sharing)  확인하기

## 설치 방법
```
git clone https://lab.hanium.or.kr/20_hf262/main/setup-ec2-gui  
cd setup-ec2-gui   
chmod 777 setup-ec2-gui.sh  
./setup-ec2-gui.sh
```