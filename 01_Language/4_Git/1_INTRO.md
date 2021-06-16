# 01. INTRO

> - `git`은 DVCS(분산 버전 관리 시스템, Distribute Version Control System)으로, 
>   - 소스 코드의 버전 및 이력을 관리할 수 있다.



## 1. Basic

1. 기본 단축키
    - `Ctrl` + `c` : Cancel
    - `Ctrl` + `d` : Delete
    - `Ctrl` + `l` : cLear
    - `Ctrl` + `a` : 라인 맨 앞(A)으로 이동
    - `Ctrl` + `e` : 라인 맨 뒤(End)로 이동
    - `Ctrl` + `b` : 앞으로 커서 이동 (←)
    - `Ctrl` + `f` : 뒤로 커서 이동 (→)
    - `Ctrl` + `w` : 단어 단위로 삭제
    - `Ctrl` + `u` : 현재 입력 중인 라인 전체 삭제

    cf. manual 보기 👉 `$ man <command>`

    
    
2. Directory

    ```bash
    # 1. Print Working Directory 👉 현재 위치 확인
    $ pwd
    
    # 2. Change Directory 👉 이동
    $ cd # 홈 dir로 이동
    $ cd .. # 상위 dir로 이동
    $ cd - # 이전 dir로 이동(뒤로 가기)
    $ cd <dir> # 해당 dir로 이동
    
    # 3. MaKe DIRectory 👉 디렉토리 생성
    $ mkdir <dir_name>
    
    # 4. 폴더 삭제
    $ rm -rf <dir_name>
    
    # 5. 폴더 내 검색
    $ find . -name '*.txt'
    ```

    

3. Files

    ① 기본

    ```bash
    # 1. touch 👉 파일 생성
    $ touch <file>
    
    # 2. ReMove 👉 파일 삭제
    $ rm <file>
    $ rm -f <file> # 파일 강제 삭제
    
    # 3. MoVe 👉 파일 이동 (or 이름 변경)
    $ mv <file> <dir> # 파일을 해당 디렉토리로 이동
    $ mv <old> <new> # <old> 이름을 <new>로 변경
    
    # 4. CoPy 👉 파일 복사
    $ cp <old> <new> # <old>를 <new> 이름으로 복사
    
    # 5. 현재 위치에 있는 파일 확인
    $ ls
    $ ls -a # 숨긴 파일까지 보기
    $ ls -l # 상세 정보 같이 보기
    $ ls -t # 파일 생성 순으로 정렬해서 보기
    $ ls -alt # 옵션은 붙여서 사용 가능
    ```

    ② 파일 조작

    ```bash
    # 1. 입·출력
    $ echo 'hello' # print
    $ echo 'hello' > <file> # redirect(>) 👉 출력 값을 파일에 덮어쓰기
    $ echo 'world' >> <file> # append(>>) 👉 출력 값을 파일에 이어붙이기
    $ cat greetings.txt # 파일 내용 출력
    
    # 2. 출력 방식 설정
    $ head <file> # 상단 10줄만 출력
    $ tail <file> # 하단 10줄만 출력
    
    # 3. Word Count
    $ wc <file> # 줄, 단어, 바이트를 세서 출력
    
    # cf. 파이프 활용 가능
    $ head <file> | wc # 상단 10줄의 줄/단어/바이트 수 출력
    
    # 4. 파일 탐색
    $ less <file>
    # 페이지 이동(F, B) / 반 페이지 이동(U, D) / 검색 (/<pattern>)
    
    # 5. 파일 편집
    $ vim
    ```



## 2. Plus +

1. 정규식(Global Regular Expression and Print)

    ```bash
    $ grep <string> <file> # 해당 문자열을 파일에서 검색
    $ grep -i <string> <file> # 대소문자 구분없이 검색
    
    # [example]
    $ pip list | grep -i django
    ```

    

2. Process Status

    ```bash
    $ ps # 프로세스 보기
    $ ps aux | grep 'runserver'
    
    # 프로세스를 pid로 kill
    $ kill -<level> <pid>
    
    # 프로세스를 이름으로 kill
    $ kill -<level> -f <name>
    ```

    

3. etc.

    ```bash
     # 1. 프로그램 설치 위치(path) 출력
    $ which <program>
    
    # 2. URL과 상호작용
    $ curl <url>
    
    # 3. 새로 갱신되는 내용 확인하기
    $ ping google.com > google.log
    $ tail -f google.log
    ```

    
