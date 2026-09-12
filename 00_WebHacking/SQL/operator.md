
-- 산술 연산자 : +, -, *, / 
-- 우선순위 : * = / > + = -
```SQL
select 5-1*2; -- 3
```

-- 비교 연산자 : >, <, >=, <=, =, !=, "!="는 "<>"로도 표현됨. 
```SQL
select * from table where colum1 > 180;
```

-- 논리 연산자 : AND, OR, NOT  
-- 우선순위 : NOT > AND > OR 
```SQL
select true AND false
select true OR false
select NOT true
```

-- 비트 연산자 : AND(&), OR(|), XOR(^) -> 이진수로 변환했을 때, 각 자릿수에 대하여 실행. 
-- XOR은 둘 중 하나가 1일 때만 1임  

-- IN연산자 : 일치하는 데이터  
-- LIKE연산자 : 어떤 단어가 포함된 문자열 검색  