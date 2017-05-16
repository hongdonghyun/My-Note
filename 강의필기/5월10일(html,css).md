# 5월10일

##줄 바꿈 설정

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<style media="screen">
  p.nowrap{
    white-space : nowrap;
    color: blue;
  }
  p.pre{
    white-space: pre;
    color: red;

  }
  p.pre-line{
    white-space: pre-line;
    color: green;
  }
  p.pre-wrap {
    white-space: pre-wrap;
    color: brown;
  }
</style>
<body>
<p class="nowrap">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
<p class="pre">Lorem ipsum dolor sit amet,
   consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
<p class="pre-line">Lorem ipsum dolor sit a
  met, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
<p class="pre-wrap">Lorem ipsum dolor sit
  amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>

</body>
</html>


## CSS배경 스타일

외부참조의 경우 url을 사용하는html기준으로 찾아서 넣어줘야 한다.(상대경로)
절대경로로 집어 넣어줘도된다.

내부참조로 불러오는 경우도 있다.

#배경 이미지 위치

background-position: x축 y축
양의값의 경우 x축 **우측** y축 **하단**

%의 경우 이미지 사이즈 기준으로 움직임

##이미지 내부참조 코드

<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<style media="screen">
  #background-image {
    height : 220px;
    border:1px solid:black;
    background-repeat: no-repeat;
    background-position:center right;
    background-image:url('image/aaaaaa.jpg')
  }
  }
</style>
<body>
  <div id="background-image">
    
  </div>

</body>
</html>

## 테두리

border-width : w x y z	
1개만 입력시 상하좌우 모두 변경	
4개는 상 우 하 좌 순서로 변경	
2개는 상하 좌우 변경	
border-top-width: x		
상단만 변경

###테두리 구성요소
- solid: 실선
- double: 이중선
- dotted: 점선
- dashed: 바느질선
- none: 없음

###속성 속기법
border: 모든변에 동일한 값만 적용
solid: 

## CSS박스 모델

## 마진겹침
<div style="margin-bottom:10px;">box1</div>
<div style="margin-top:30px;">box2</div>

두 블록요소 **마진이 겹치면 더하는것이 아니고 큰값이 적용** 가로는 해당없음			
겹치는 마진값을 준 경우 한쪽에 값을 몰아주거나 padding활용

##boxsizing

box-sizing: border-box
를 지정하면 요소에 설정한  width값에 맞추어 padding,border값을 제외한 width가 적용됨 

code)

<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<style>
  #box-sizing {
    width: 200px;
    height: 100px;
    background-color: black;

    border: 5px solid red;
    padding: 3px;
    box-sizing: border-box;
  }
</style>
<body>
  <div id="box-sizing"></div>

</body>
</html>

##테두리 합치기


<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<style>
  table {
    border-collapse: collapse;
  }
  td {
    border: 1px solid black;
    width: 30px;
    text-align: center;
  }
</style>
<body>
  <table>
    <tr>
      <tr>
        <td>A</td>
        <td>B</td>
        <td>C</td>
      </tr>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
  </table>

</body>
</html>

##테이블 셀 간격 띄우기


<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<style>
  table {
    border-spacing: 30px;
    
  }
  td {
    border: 1px solid black;
    width: 30px;
    text-align: center;
  }
</style>
<body>
  <table>
    <tr>
      <tr>
        <td>A</td>
        <td>B</td>
        <td>C</td>
      </tr>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
  </table>

</body>
</html>


