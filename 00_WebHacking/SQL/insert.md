CREATE DATABASE database;

CREATE TABLE table(
    colum1 int, 
    colum2 char, 
    colum3 char
)


-- 데어터 삽입
INSERT INTO table (colum1, colum2, colum3) VALUES (123, "hello", "bye");

-- 데이터 조회
SELECT colum1, colum2, colum3 FROM table;

-- 조건 붙여서 보기
SELECT colum1, colum2, colum3 FROM table WHERE colum1 = 123;

-- 일부만 보기
SELECT colum1, colum2 FROM table

-- 값 변겅(대부분 조건문 붙여서 함)(이하 명령 2개는 조건문이 없을 시, 전부 변경이므로, 주의!!)
-- UPDATE table SET colum1 = 1234, colum2 = "hmm...", colum3 = "yes!!";
-- 조건 붙어서 변경
UPDATE table SET colum1 = 1234, colum2 = "hmm...", colum3 = "yes!!" WHERE colum1 = 123;

-- 일부만 변경
UPDATE table SET colum2 = "haha", colum3 = "Owl" WHERE colum1 = 1234;

-- 데이터 삭제  
DELETE table WHERE colum1 = 1234;
