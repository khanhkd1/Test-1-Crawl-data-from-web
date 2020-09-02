# Test-1-Crawl-data-from-web

Project function: crawl data from: https://www.goodreads.com/author/list/4634532.Nguy_n_Nh_t_nh?page=1&per_page=30

Bài test này có sử dụng dự án mã nguồn mở Underthesea

Thông tin về Underthesea: https://github.com/undertheseanlp

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



Requirements:
- install python3.6 (use Conda)

  - Macos 10.15.6: Open terminal run
    - /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
    - brew install mysql-client
    - python3 -m pip install --upgrade setuptools
    - brew install mysql
    - pip install mysqlclient
    - sudo pip install -r requirements.txt

  - Ubuntu 20.04: Open terminal run
    - sudo apt-get install mysql-client
    - sudo apt install python3-testresources
    - pip3 install --upgrade pip setuptools
    - sudo apt-get install mysql-server
    - sudo apt-get install libmysqlclient-dev
    - sudo pip3 install -r requirements.txt
