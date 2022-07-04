class Post:
    """
        게시글 클래스
        param id: 글번호
        param title: 글제목
        param content: 글내용
        param view_count: 조회수
    """
    def __init__(self, id, title, content, view_count):
        self.id = id
        self.title = title
        self.content = content
        self.view_count = view_count

    #게시물 수정
    def set_post(self, id, title, content, view_count):
        self.id = id
        self.title = title
        self.content = content
        self.view_count = view_count
    
    # 조회수 증가
    def add_view_count(self):
        self.view_count += 1


if __name__ == "__main__":
    post = Post(1, "테스트", "테스트입니다", 0)
    post.set_post(1, "테스트2", "테스트입니다2", 0)
    post.add_view_count()
    print(f"{post.id} / {post.title}/ {post.content} /{post.view_count}")