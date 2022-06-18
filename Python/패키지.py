# 패키지는 도트를 사용하여 파이썬 모듈을 계층적(디렉터리 구조)으로 관리할 수 있게 해준다
# 예를 들어 모듈 이름이 A.B인 경우에는 A는 패키지 이름이 되고 B는 A 패키지의 B모듈이 된다.

# 패키지 생성 방법
# touch game/__init__.py
# touch game/sound/__init__.py
# touch game/sound/echo.py
# touch game/graphic/__init__.py
# touch game/graphic/render.py

# __init__.py는 일단 비워둔다

# echo.py
def echo_test():
  print("echo")

# render.py  
def render_test():
  print("render")

# set PYTHONPATH=경로

# 패키지 안의 함수 실행하기
>>> import game.sound.echo
>>> game.sound.echo.echo_test()

>>> from game.sound import echo
>>> echo.echo_test()

>>> from game.sound.echo import echo_test
>>> echo_test()

# 다음과 같이 사용하는 것은 불가능하다.
>>> import game
>>> game.sound.echo.echo_test()

>>> import game.sound.echo.echo_test

# __init__.py의 용도
>>> from game.sound import *
>>> echo.echo_test()
# 위와 같은 경우에 __init__.py 파일이 없다면 패키지로 인식되지 않는다.

# __init__.py
__all__ = ['echo']
# 위 문장이 뜻하는 것은 sound 디렉터리에서 *기호를 사용하여 import 할 경우 이곳에 정의된 echo 모듈만 import된다는 의미이다.

# relative 패키지
# graphic 디렉터리의 render.py 모듈이 sound 디렉터리의 echo.py모듈을 사용하고 싶다면?
# render.py
>>> from game.sound.echo import echo_test
# 또는
>>> from ...sound.echo import echo_test



