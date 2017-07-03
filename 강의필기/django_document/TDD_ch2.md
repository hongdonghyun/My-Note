#명령어

- assertEqual(a,b) : a == b
	- 같다면 True 반환
	
- assertNotEqual(a,b) : a != b
	- 같지 않다면 True 반환
	 
- assertTrue(x) : bool(x) is True
	- 값이 있다면 True 
 
- assertFalse(x) : bool(x) is False
	-  값이 없다면 True

- assertIs(a,b) : a is b
	- a 와 b가 같다면(같은 객체인지)
	
- assertIsNot(a,b) : a is not b
	- a 와 b가 같지 않다면(같은 객체가 아니라면)

- assertIsNone(x) : x is None
	- x가 None이라면 True반환

- assertInNotNone(x) : x is not None
	- x가 None이 아니라면 True반환

- assertIn(a,b) : a in b
- assertNotIn(a,b) : a not in b
- assertIsInstance(a,b) : isinstance(obj,cls)
	- a객체가 b의 타입이 같다면
- assertNotIsInstance(a,b) : 
	- a객체가 b의 타입과 같지 않다면
 