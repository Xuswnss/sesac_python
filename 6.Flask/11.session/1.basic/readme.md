# cookie
- 무언갈 저장했다가 가져나가는 공간.
- rfc에 정의 되어 있음.
- HTTP state management Mechanism
- 쿠키 발행 주체는 서버이다
- Client Side = 사용자 환경 웹브라우저
- Session -> 서버사이드, 발행자: 서버
- flask에서 라이브러리를 사용할 경우
- session key와 session value를 담아서 준다.
- session key는 인코딩해서 보여준다.
- base24와 전자서명으로 나뉨
- encoding != encryption(= 암호화)
- JSON.parse(atob('encoding된 문장')) -> 복호화
- 서버를 끄면 세션 정보가 원래 사라져야함.


- session에 DB를 연동해서 서버가 DB에 저장 세션의 파일, 서버가 파일에 저장
- 기본 값 메모리의 저장

#### curl 127.0.0.1:5000/set-session/xuswns --cookie-jar