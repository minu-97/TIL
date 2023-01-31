# CSS
* HTML로는 웹 사이트의 내용을 구조화 CSS로는 웹 문서의 디자인을 구성
* 스타일을 사용하면 웹 문서의 내용과 상관없이 디자인만 바꿀 수 있다

## 스타일
* 브라우저 기본 스타일
  * 브라우저에서 기본으로 적용하는 스타일
  * 웹 문서에 아무 스타일도 적용하지 않고 HTML만 사용해도 기능에 따라 크기에 맞게 보여줌
  
* 인라인 스타일
  * 스타일 시트를 사용하지 않고 스타일을 적용할 대상에 직접 표시
  * 스타일을 적용하고 싶은 태그에 `style 속성`을 사용해 `style="속성 : 속성 값;"` 형태로 스타일 적용 
  * 예제
```html 
    <body>
        <h1  style="border: 1px red solid; text-align: center; font-style: italic; color:skyblue">인라인 스타일</h1>
    </body>
```
<body>
    <!--border는 속성요소의 테두리이며 속성요소가 차지하는만큼 표현된다  -->
    <!-- border weight, height 값을 주어 크기 조절이 가능하다 -->
    <!-- dotted, solid 등 보더 표현에 사용되는 선 스타일 있고 굵기 또한 설정 가능하다 -->
    <h1  style="border: 1px red solid; text-align: center; font-style: italic; color:skyblue">인라인 스타일</h1>
</body> 
  
  
* 내부 스타일
  * 웹 문서 안에서 사용할 스타일을 문서 안에 정리한 것
  * 모든 스타일 정보는 `<head>` 태그와 `</head>` 태그 안에서 정의
  * `<style>` 태그와 `</style>` 태그 사이에 작성
  * 예제
    ```html
        <style>
            /* 아래에 body에서 ul 아래 p태그 선택 */
            ul > li{
                 /*폰트 색상 변경*/
                color: skyblue;
                 /*글자 가운데 정렬*/
                text-align: center;
                 /*폰트 크기 40px*/
                font-size: 40px;
                 /*폰트 굵기 bold*/
                font-weight: bold;
            }
            /* id가 id_ex인 경우만 선택 */
            #id_ex{
                color: green;
            }
            /*class가 class_Ex인 경우만 선택 */
            .class_ex{
                color: orange;
            }


        </style>
    ``` 
```html

    <body>
        <ul>
            <p>내부 스타일 예제</p>
            <p id="id_ex">선택자 아이디 예제</p>
            <p class = "class_ex">선택자 클래스 예제</p>
        </ul>
    </body>
```
<html>
    <head>
        <style>
                ul > p{
                    color: skyblue;
                    text-align: center;
                    font-size: 40px;
                    font-weight: bold;
                }
                #id_ex{
                    color: green;
                }
                .class_ex{
                    color: orange;
                }
        </style>
    </head>
        <body>
            <ul>
                <p>내부 스타일 예제</p>
                <p id="id_ex">선택자 아이디 예제</p>
                <p class = "class_ex">선택자 클래스 예제</p>
            </ul>
        </body>
</html>

* 외부 스타일 시트
    * 여러 웹 문서에서 사용할 스타일을 별도 파일로 저장해 놓고 필요할
때마다 파일에서 가져와 사용
  * `<style>` 태그 없이 `<link>` 태그만 사용해 미리 만들어 놓은 외부 스타
일 시트 파일 연결
* **🔗 [예제](./source/2023_01_25_1.html)**
  * 🔗[결과](http://127.0.0.1:5501/source/2023_01_25_1.html)

## 참고
* 🔗[w3schools.com](https://www.w3schools.com/)
* 🔗[colorzilla.com](https://www.colorzilla.com/)
*  [DO it HTML + CSS + 자바스크립트 웹 표준의 정석](http://www.easyspub.co.kr/20_Menu/BookView/421/PUB) 출판사 이지퍼블리싱 저자 고경희


