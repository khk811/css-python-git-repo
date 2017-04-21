import socket
import sys


if __name__ == "__main__":
    #소켓 생성
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    except socket.error as e:
        print("Failed ")
        print("Reason: {}".format(str(e)))
        sys.exit();

    print("socket created")

    host = input("Enter host: ")
    port = input("Enter port: ")

    #소켓에 접속함.
    try:
        sock.connect((host, int(port)))
        print("socket connected")
        sock.shutdown(2)
        # 2번은 서버, 클라이언트 모두 종료하는 뜻.
        # write shutdown 1
        # read shutdown 0
    except socket.error as err:
        print("Failed")
        print("Reason: {}".format(str(err)))
        sys.exit();
