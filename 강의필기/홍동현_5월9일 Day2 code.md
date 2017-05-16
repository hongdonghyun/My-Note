#5/9일 Day2

##표만들기

<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>table</title>
</head>

<style>
html, body {
  font-size: 12px;
  color: #333;
}
table {
   border-collapse: collapse;
   text-align: center;
   border: 1px solid #ooo;
}

tr,th,td{
  border: 1px solid #999;
  padding: 4px 8px;
}
</style>
<body>

</body>
</html>


<table>
  <thead>
    <tr>
      <td colspan="9">포켓몬스터의 전설의 포켓몬</td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th colspan="1">지방</th>
      <th colspan="2">메인 전설의 포켓몬</th>
      <th colspan="6">그 외 전설의 포켓몬</th>
    </tr>
  </tbody>
  <tbody>
    <td colspan="1">관동지방</td>
    <td colspan="2">뮤츠</td>
    <td colspan="2">프리져</td>
    <td colspan="2">썬더</td>
    <td colspan="2">파이어</td>
  </tbody>
  <tbody>
    <td colspan="1">성도지방</td>
    <td colspan="1">칠색조</td>
    <td colspan="1">루기아</td>
    <td colspan="2">라이코</td>
    <td colspan="2">엔테이</td>
    <td colspan="2">스이쿤</td>
  </tbody>
  <tbody>
    <tr>
      <td rowspan="2">호연지방</td>
      <td>그란돈</td>
      <td>가이오가</td>
      <td colspan ="2">레지락</td>
      <td colspan ="2">레지아이스</td>
      <td colspan ="2" >레지스틸</td>
    </tr>
    <tr>
      <td colspan="2">레큐쟈</td>
      <td colspan="2">라티아스</td>
      <td colspan="2">라티오스</td>
      <td colspan="2">테오키스</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <td rowspan="2">칼로스지방</td>
      <td>a</td>
      <td>b</td>
      <td rowspan="2" colspan="6"></td>
    </tr>
<tr>
  <td colspan="2">c</td>
</tr>
<tr>
  <td rowspan="3">a</td>
  <td>a</td>
  <td>a</td>
  <td colspan="3">a</td>
  <td colspan="3">a</td>
</tr>
<tr>
  <td>a</td>
  <td>a</td>
  <td colspan="3">a</td>
  <td colspan="3">a</td>
</tr>
<tr>
  <td colspan="2">a</td>
  <td colspan="3"></td>
  <td colspan="3"></td>

</tr>
  </tbody>

</table>

##간단 회원가입창


<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  <form action="">
  <h3>회원가입</h3>
  <fieldset>
    <legend>기본정보</legend>
    <div>
      <label for ="username">ID</label>
      <input type="text" id ="username" placeholder="특수문자 제외, 4~16자">
    </div>
    <div>
      <label for="password"><b>비밀번호</label></b>
      <input type="password" id ="password" placeholder="비밀번호 입력">
    </div>
    <div>
      <label for="email">이메일</label>
      <input type="text" id="email">
    </div>
    <div>
      <label for="gender">
      <label for="gender">성별</label>
      <select name="gender" id="gender">
      <option value="m">남성</option>
      <option value="f">여성</option>
    </select>
  </label>
      </div>
  </fieldset>
  <fieldset>
    <legend>선택입력</legend>
    <div>
      <label for="age">나이</label>
      <input type="number" id="age" name="age" min ="1" max="150">
    </div>
    <div>
      <label for="address">주소</label>
      <input type="text" id="address" name="address">
    </div>
    <div>
    <label for="introduce">자기소개</label>
    <textarea name="introduce"
     id="introduce"
      cols="60"
      rows="4" placeholder="자기소개"></textarea>
  </div>
  </fieldset>
  <button type="submit">회원가입</button>
</form>

</body>
</html>

# form 요소

form은 클라이언트에서 서버로 데이터를 전송 할 때 사용되는 태그
method는 get, post가 사용되며
get은 URL에 데이터가 담겨서 전달되며 
post는 URL과 별도로 데이터가 전송된다.

get 예제
ex) 구글에서 마크다운 검색	
[마크다운]
(https://www.google.co.kr/search?q=google&oq=goo&aqs=chrome.0.69i59j69i60l3j69i57j69i60.2176j0j4&sourceid=chrome&ie=UTF-8#q=%EB%A7%88%ED%81%AC%EB%8B%A4%EC%9A%B4)

post 예제
ex)네이버 로그인	
[네이버 로그인](https://nid.naver.com/nidlogin.login)


#클래스와 아이디
##네이밍 규칙
* 첫글자는 알파벳으로 시작
* 대소문자 구분 (다른요소로 인식함)
* 두번째부터는 알파벳,숫자,-,_ 사용 가능

##클래스와 아이디의 차이
* id는 단 한번만 선언이 가능 오직 하나만 존재해야하기 때문
* class는 중복선언이 가능
* 네이밍시 명확히 구별할 수 있도록 선언하여야 한다.

#색상
색상표 링크 -> [색상표 링크](http://www.homejjang.com/03/color_name.php)

#CSS
마크업 언어가 실제 표시되는 방법을 기술하는 언어		
레이아웃과 스타일을 정의할때 사용

선언예시)```
selector {
	property: value;
	}```
**selector**: 선택자(규칙을 어디에 적용할지 결정)
**property**: 속성	
**value**: 값

# 외부 CSS사용

**<link rel = "stylesheet" href =  불러올 주소(상대경로)**

*link태그를 사용하여 외부CSS파일을 HTML문서에 연결*

# developer tools(개발자 도구)

- mac: cmd + alt + i
- linux: ctrl + shift+ i
- windows: F12

요소선택 단축키: cmd + shift + c

# CSS선택자
 *(Asterisk)기호를 사용
 ```
 ex) * {
 padding: 0;
 margin: 0;
 }	```
 *주로 페이지 내부요소를 초기화,기본값 설정시에 주로사용 모든요소를 탐색하기에 로딩시간이 길어짐 자주사용하지 않는것이 좋다.*	
 
 **#은 id .(dot)은 class**

##복합 선택자
포함관계를 가지는 태그들 사이(종속관계?)에서, 포함하는 요소는'부모 요소',포함되는 요소는'자식 요소'라고 한다.

같은 부모요소를 가지는 요소는 '형제관계'라고 하며 먼저 선언된 요소를 '형 요소'이후 선언되는 요소를'동생 요소'라고 한다.
**부모 요소 내부에서 보다 윗 줄에 쓰여진 것을 칭함** 

ex)	
**하위 선택자**	
```
section ul {	
	border: 1px solid black;	
	}
```

*하위 선택자는 부모요소에 포함된 '모든'하위 요소를 지정한다.*

**자식 선택자**	
```
section > ul {	
	border: 1px solid black;	
	}
```

*자식 선택자는 **'부모요소'**바로 아래 '자식요소**'만'**을 지정한다.*

**인접 형제 선택자**
```
h1 + u1 {	
	background: azure;	
	color: darkblue;	
	}```

선언된 조건을 충족하는 **'첫번째'동생 요소**만을 지정함	
```
h1 ~ ul {	
	background: azure;	
	color: darkblue;	
	}	```
	
선언된 조건을 충족하는 **'모든'동생 요소**를 지정함
