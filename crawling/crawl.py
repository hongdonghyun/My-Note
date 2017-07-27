# web_toon 패키지 내부의 NaverWebtooncrawler 클래스형 인스턴스를 생성 인스턴스에서 crawl_episode생성

# from web_toon import *
#
# naver_crawl = NaverWebtoonCrawler(697685, 'thu')  # 웹툰 아이디랑 요일
#
# for i in range(1, 20):
#     naver_crawl.crawl_episode(i)


import sys

from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QTextEdit, QGridLayout, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        title = QLabel('웹툰ID')
        author = QLabel('요일')
        review = QLabel('Review')


        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
