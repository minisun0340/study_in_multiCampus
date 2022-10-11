from flask import Flask

#Flask인스턴스 생성
app = Flask(__name__)

#flask에서 Flask객체의 route메소드를 @기호와 함께 추가해서 요청 path를 설정
@app.route("/")
def hello():
    return "Hello Raspberry PI"


# 장고는 기본 포트 8000, 웹소켓 9001, 브로커 1883, 오라클 1521
#flask의 실행을 요청 - 기본port가 5000
#debug=True는 코드가 변경되면 서버를 restart하지 않아도 반영된다는 의미
app.run(host="0.0.0.0", debug=True) #아이피로 접속해도 된다