Emmet

단어 입력후 탭 -> 구문으로 변경

연산자 중첩 : >
다른레벨수준의 요소 중첩이 실행됨
Ex) h1 >h2>h3


Output

<h1>
	<h2>
		<h3></h3>
 	</h2>
</h1>

연산자 중첩 : +
같은레벨수준의 요소 중첩이 실행됨
 Ex) div+p+bq

Output

<div></div>
<p></p>
<blockquote></blockquote> 

연산자 중첩 : >,+ 중복사용시

Ex) div+div>p>span+em

Output

<div></div>
<div>
	<p><span></span><em.</em></p>
</div>

연산자 중첩 : ^ 사용시
직전 요소들 한단계 위에 실행됨

Ex) h1>h2>h3^h4

Output

<h1>
	<h2>
		<h3></h3>
	</h2>
	<h4></h4>
</h1>









^를 많이 사용하면 수만큼 위로 이동하여 실행됨
Ex) h1>h2>h3^^h4

Output

<h1>
	<h2>
		<h3></h3>
	</h2>
</h1>
<h4></h4>

곱셈 연산자 : *
*사용시 출력횟수 설정가능

Ex) h1>h2*5

Output 

<h1>
  <h2></h2>
  <h2></h2>
  <h2></h2>
  <h2></h2>
  <h2></h2>
</h1>

그룹 연산자 : ()

그룹 연산자는 중첩이 가능하며 *와 결합하여 사용이 가능하다.
Ex) (div>dl>(h1+h2)*5)

 Output

<div>
  <dl>
    <h1></h1>
    <h2></h2>
    <h1></h1>
    <h2></h2>
    <h1></h1>
    <h2></h2>
    <h1></h1>
    <h2></h2>
    <h1></h1>
    <h2></h2>
  </dl>
</div>

css에서 사용되는 ID와 Class

div#header+div #은  ID
Div.page+div .은 Class
Class는 중첩사용이 가능

Custom attribute (맞춤 속성)

Ex) h1 [title = “hello world” colspan=3]

Output

<h1 title = “hello world” colspan=“3”></h1>

Item numbering : $

요소뒤에 $를 추가하면 자동넘버링이 된다.
곱셈 연산자와 결합하여 사용하면 1~ 으로 자동으로 설정됨

Ex) ul>li#item$*5

Output

<ul>
  <li id="item1"></li>
  <li id="item2"></li>
  <li id="item3"></li>
  <li id="item4"></li>
  <li id="item5"></li>
</ul>

$를 연속으로 사용하면 연속한 개수만큼 단위생성

item$$$*5
ex) item001 ~item 005

넘버링 기준과 넘버링순서 변경

@사용

ul>li#item$@-*5

Output

<ul>
  <li id="item5"></li>
  <li id="item4"></li>
  <li id="item3"></li>
  <li id="item2"></li>
  <li id="item1"></li>
</ul>

기준숫자 설정하려면 

Ex) ul>li#item$@3*5

Output


<ul>
    <li class="item3"></li>
    <li class="item4"></li>
    <li class="item5"></li>
    <li class="item6"></li>
    <li class="item7"></li>
</ul>

요소에 텍스트 추가

Ex) a{Click me}

Output

<a href =“”>Click me</a>



emmet에서는 연산자 사이에 공백을 넣지 않는다.
공백은 정지기호 이기에 공백을 넣는다면 작동하지 않는다.


[emmet game](https://ahndohun.github.io/emmet-game/)
