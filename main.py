import pythonping
import requests


# hostname: ip or domain


def check_ping(hostname):
  """
  핑 테스트 함수
  :param hostname:
  :return:
  """
  res = pythonping.ping(hostname, count=3, interval=1)  # verbose=True,

  for item in res:
    print(item)  # 개별 출력


def check_http(url):
  """
  http 테스트 함수
  :param url: 
  :return: 
  """
  response = requests.get(url)
  print(response.status_code)
  # print(response.text)


if __name__ == '__main__':
  ####################
  # ping
  # check_ping('127.0.0.1')
  # check_ping('blog.hacksper.com')

  ####################
  # http
  check_http('https://blog.hacksper.com')



