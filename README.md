# Test-1-Crawl-data-from-web

Project function: crawl data from: https://www.goodreads.com/author/list/4634532.Nguy_n_Nh_t_nh?page=1&per_page=30

Refer to: https://viblo.asia/p/web-crawling-voi-thu-vien-beautifulsoup-1VgZvNGOZAw + internet

Form Data:
    data = [
    {
        Book ID,
        Title,
        Link,
        Author,
        Rate,
        Description,
        Review = [
        {
            User ID,
            User Name,
            Review Content,
            Rate,
            Date Post,
            Comment = [
            {
                User ID,
                User Name,
                Comment Content
            }
            ]
        }
        ]
    }
    ]

Node: sửa 'per_page' và 'page' của url (file main.py) để điều chỉnh số lượng sách muốn lấy thông tin

Requirements:
- install python3
- update pip
- install libraries from requirements.txt
  - Macos 10.15.6: Open terminal run
    - /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
    - brew install mysql-client
    - python3 -m pip install --upgrade setuptools
    - brew install mysql
    - pip3 install mysqlclient
    - brew install python
    - sudo pip3 install -r requirements.txt
    - pip install Flask-SQLAlchemy
    - pip install BeautifulSoup4 
  - Ubuntu 20.04: Open terminal run
    - sudo apt-get install mysql-client
    - sudo apt install python3-testresources
    - pip3 install --upgrade pip setuptools
    - sudo apt-get install mysql-server
    - sudo apt-get install libmysqlclient-dev
    - sudo pip3 install -r requirements.txt
