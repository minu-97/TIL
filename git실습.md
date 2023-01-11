# 2023-01-11 학습내용

## git

* 분산 버전 관리 프로그램
* 백업, 복구, 협업을 위해 사용
* [Git 공식문서](https://git-scm.com/book/ko/v2)
### git의 구조
![git로컬저장소](https://git-scm.com/figures/18333fig0106-tn.png)
* Working Directory (= Working Tree) : 사용자의 일반적인 작업이 일어나는 곳
* Staging Area (= Index) : 커밋을 위한 파일 및 폴더가 추가되는 곳
* Working Directory → Staging Area → Repository 의 순서로 버전관리 수행합니다.
### git 초기 설정
> Git 설치 후 최초 한번 설정
  1. 누가 커밋을 했는지 확인하기위해 이름과 이메일을 설정
```bash
    $git config --global user.name"이름"
    $git config -- global user.email
```
  2. 작성자가 올바르게 설정되었는지 확인
``` bash
    $ git config --global --list
```

### git 기본 명령어

#### 1. git init

```bash
$ git init
 # 실행결과
 "Initialized empty Git repository in E:/proj/multi_AI/git/TIL/.git/"
```
* 작업 중인 위치를 git으로 관리한다는 명령어
* ```.git``` 이라는 숨긴 폴더 생성

#### 2. git status

``` $ git status ```
* working Directory와 staging area에 있는 파일의 현재 상태를 알려주는 명령어
* 상태
  1. `untraked` : gitdl 관리하지 않는 파일 
  2. `tracked`: git이 관리하는 파일
   * `Unmodified` : 최신상태
   * `Modified` : 수정되었지만 아직 staging Area에 반영되지 않은 상태
   * `staged` : staging Area에 올라간 상태
   *  
#### 3. git add
```bash
#특정 파일
$ git add a.txt

#특정 폴더
$ git add multi_Ai

#현재 디렉토리에 속한 파일/폴더 전부
$ git add .
```
* working Directory에 있는 파일 staginig Area로 올리는 명령어
* Untracked, Modified → Staged 로 상태를 변경합니다.

#### (4) git commit
```bash
$ git commit -m "상세하게 적기"
#예시
$ git commit -m "TIL_23_01_11"
# On branch master Your branch is up to date with 'origin/master' #
```
* staging Area에 올라온 파일의 변경 사항을 하나의 버전으로 저장하는 명령어
* 커밋은 `SHA-1` 알고리즘에 의해 반환된 고유의 해시 값 ID로 가짐
* `(root-commit)`은 해당 커밋이 최초의 커밋 일 때 만 표시해준다

#### (5) git log
```
$ git log
```
 * 커밋의 내역을 조회할 수 있는 명령어
 * 옵션
   * `--oneline` : 한줄로 요약
   * `--graph` : 브랜치와 머지 내역을 그래프로 보여줌
   * `-all` : 현재 브랜치를 포함한 모든 브랜치의 내역을 보여줌
   *  `--reverse` : 커밋 내역의 순서를 반대로 보여줌
   *  `-p` : 파일의 변경 내용도 같이 보여줌
   *  `-2` : 원하는 갯수 만큼의 내역을 보여줌

#### (6) git remote
* 로컬 저장소에 원격 저장소를 `등록, 조회, 삭제`를 하는 명령어
    1. 등록
        `git remote add <이름> <깃허브의 repositories 주소>`
    2. 조회
        `git remote -v`
    3. 삭제
        `git remote rm <이름>` 또는 `git remote remove <이름>`
#### (7) git push
* 로컬 저장소의 커밋을 원격 저장소에 업로드 하는 명령어
* `git push <저장소 이름> <브랜치 이름>`
* `-u` 옵션 사용하면, 두 번째 커밋부터 `저장소, 이름, 브랜치 이름`생략 가능
``` bash
$ git push origin master
# origin이라는 이름의 원격저장소의 master 브랜치에 push
$ git push -u origin master
# 이후 작성은 $ git push 만 작성해도 가능
```