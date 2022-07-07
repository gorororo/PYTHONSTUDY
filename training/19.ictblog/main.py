import os
import csv
from turtle import update
from post import Post

#  함수선언부
def write_post():
    print('\n-게시글 쓰기-')
    title = input('제목을 입력해주세요\n>>>')
    content = input('내용을 입력해주세요\n>>>')

# 글번호
# post_list에 요소가 있는지 검사 ver1
    # if len(post_list) == 0:
    #     id = 1
    # else : 
    #     id = post_list[-1].id +1

# post_list에 요소가 있는지 검사 ver2
    if not post_list:
        id = 1
    else :
        id = post_list[-1].id +1


    post = Post(id, title, content, 0)
    post_list.append(post)
    print("# 게시글이 등록 되었습니다.")
    print(post.id, post.title)

# 게시글 목록 확인
def list_post():
    print("\n- 게시글 목록 -")
    id_list= []

    for post in post_list:
        print('번호 :',post.id)
        print('제목 :', post.title)
        print('조회수 :', post.view_count)
        print()
        id_list.append(post.id)
    
    while True :
        print("Q) 글번호를 선택해주세요(메뉴로 돌아가려면 -1을 입력해주세요)")
        try :
            id = int(input('글번호 >>>'))
            if id in id_list :
                detail_post(id)
            elif id == -1 :
                break
            else :
                print('없는 글 번호 입니다.')
        except ValueError:
            print('숫자를 입력해주세요')


# 상세 페이지 처리
def detail_post(id):
    print('\n-게시글 상세-')
    
    for post in post_list:
        if post.id == id:
            #조회수 1증가
            post.add_view_count()
            print('번호 :',post.id)
            print('제목 :', post.title)
            print('본문 : ',post.content)
            print('조회수 :', post.view_count)
            target_post = post
#상세페이지 수정 삭제 처리    
    while True:
        print('Q)수정 : 1 삭제 : 2 (전단계 메뉴로 돌아가려면 -1 입력)')
        try:
            choice = int(input('>>>'))
            if choice == 1:
                update_post(target_post)
                break
            elif choice == 2 : 
                delete_post(target_post)
                break
            elif choice == -1:
                break
            else : 
                print('숫자를 잘못 입력 하셨습니다.')
        except ValueError:
            print('숫자를 입력하세요')

# 게시글 수정 함수
def update_post(target_post):
    print('\n- 게시글 수정 -')
    title = input('제목을 입력해주세요 \n>>>')
    content = input('본문을 입력해주세요 \n>>>')
    target_post.set_post(target_post.id, title,content ,target_post.view_count)
    print('#게시글이 수정 되었습니다.')

# 게시글 삭제
def delete_post(target_post):
    post_list.remove(target_post)
    print('\n- 게시물이 삭제 되었습니다.-')

# 게시글 저장
def save():
    f = open(file_path, "w", encoding='utf-8',newline="")
    writer = csv.writer(f)
    for post in post_list:
        row = [post.id,post.title, post.content, post.view_count]
        writer.writerow(row)
    f.close()
    print('# 저장이 완료 되었습니다.')
    print('# 프로그램 종료')



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
# 예외 처리
    try :
        choice = int(input('>>>'))
    except ValueError:
        print('숫자를 입력해 주세요')
    else :
        if choice == 1 :
            write_post()
        elif choice == 2 :
            list_post()
        elif choice == 3 :
            save()
            break
        

