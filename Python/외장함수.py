# sys 모듈

# 명령 행에서 인수 전달하기
# sys.argv
# python 명령어 뒤의 모든 것들이 공백을 기준으로 나뉘어서 sys.argv 리스트의 요소가 된다

# 강제로 스크립트 종료하기
# sys.exit

# 자신이 만든 모듈 불러와 사용하기 # append
# sys.path

# pickle 모듈 
# :객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈

# 데이터를 그대로 파일에 저장
# pickle.dump()

# 저장한 데이터를 불러오기
# pickle.load()

# OS 모듈
# : 환경변수나 디렉터리, 파일 등의 OS자원을 제어할 수 있게 해주는 모듈

# 내 시스템의 환경 변수값을 알고 싶을 때
# os.environ

# 디렉터리 위치 변경하기
# os.chdir

# 디렉터리 위치 돌려받기
# os.getcwd

# 시스템 명령어 호출하기
# os.system

# 실행한 시스템 명령어의 결과값 돌려받기
# os.popen

# shutil 모듈
# : 파일을 복사해 주는 모듈

shutil.copy('src.txt','dst.txt') # src라는 이름의 파일을 dst로 복사한다

# glob 모듈
# : 특정 디렉터리에 있는 파일 이름 모두를 알아야 할 때 사용

# 디렉터리에 있는 파일들을 리스트로 만들기
# glob(pathname)

# tempfile 모듈
# : 파일을 임시로 만들어서 사용할 때 유용

# 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 돌려준다
# tempfile.mktemp

# 임시 저장공간으로 사용할 파일 객체를 돌려준다 기본적으로 바이너리 쓰기 모드를 갖고 f.close가 호출되면 파일 객체는 자동으로 사라진다
# tempfile.TemporaryFile

# time 모듈

# 현재시간을 실수 형태로 돌려줌
# time.time

# 돌려준 실수 값을 사용해서 연도, 월, 일, 시 , 분, 초,...의 형태로 바꾸어 준다
# time.localtime

# time.localtime에 의해서 반환된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 돌려주는 함수
# time.asctime

# time.asctime(time.localtime(time.time())) 을 사용해 간편하게 표시. 항상 현재시간만을 돌려준다
# time.ctime

# 시간에 관계된 것을 세밀하게 표현하는 여러 가지 포맷 코드를 제공
# time.strtime 

# 일정한 시간 간격을 두고 루프를 실행할 수 있도록 함
# time.sleep

# calendar 모듈

# 그해의 전체 달력을 볼 수 있다
# calender.calendar(연도), calendar.prcal(연도)

# calendar.weekday(연도, 월, 일)함수는 그 날짜에 해당하는 요일 정보를 돌려준다. 월요일은 0 일요일은 6

# calendar.monthrange(연도, 월)함수는 입력받은 달의 1일이 무슨 요일인지와 그 달이 며칠까지 있는지를 튜플 형태로 돌려준다

# random 모듈

# random.random() : 0.0에서 1.0사이의 실수 중에서 난수 값을 돌려줌

# random.radint(1,10) : 1에서 10사이의 정수 중에서 난수값을 돌려줌

# random.shuffle : 리스트의 항목을 무작위로 섞고 싶을 때 사용

# webbrowser : 자신의 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈
# webbrowser.open("http://google.com")
# webbrowser.open_new("http://google.com") # 이미 웹 브라우저가 실행된 상태이더라도 새로운 창으로 해당 주소가 열리게 함





