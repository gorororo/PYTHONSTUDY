import os
import csv
from post import Post

# 메인프로그램
# 파일경로
#변수(객체) 선언
file_path="./data.csv"
post_list = [] #post 객체를 저장할 리스트
# print(os.path.exists(file_path))

#data.csv 파일이 있다면 
if os.path.exists(file_path):
    #게시글 로딩
    print("게시글 로딩중...")
    f = open(file_path, "r", encoding="utf8")
    reader = csv.reader(f)
    for data in reader:
        post = Post(int(data[0]),data[1],data[2], int(data[3]))
        post_list.append(post)

else:
    #파일생성
    f = open(file_path,"w", encoding="utf-8", newline="")
    f.close()


# 메뉴 출력하기
while True:

    print ('\n\n-ICT BLOG-')
    print('-메뉴를 선택해 주세요-')
    print('1.게시글 쓰기')
    print('2.게시글 목록')
    print('3.게시글 종료')

    try :
        choice = int(input('>>>'))
    except ValueError:
        print('숫자를 입력해 주세요')
    else :
        if choice == 1 :
            print('게시글 쓰기')
        elif choice == 2 :
            print('게시글 목록')
        elif choice == 3 :
            print('프로그램 종료')
            break