--------------------------------------------------------
--  File created - Tuesday-November-19-2013   
--------------------------------------------------------
REM INSERTING into MEALS_MEALPART
SET DEFINE OFF;
INSERT INTO MEALS_MEALPART (ID,MEALID,INGREDIENT_ID,AMOUNT,UNIT) VALUES (1,1,1,300,1);
INSERT INTO MEALS_MEALPART (ID,MEALID,INGREDIENT_ID,AMOUNT,UNIT) VALUES (2,2,6,2,0);
INSERT INTO MEALS_MEALPART (ID,MEALID,INGREDIENT_ID,AMOUNT,UNIT) VALUES (3,2,8,12,1);
INSERT INTO MEALS_MEALPART (ID,MEALID,INGREDIENT_ID,AMOUNT,UNIT) VALUES (4,2,4,227,0);
INSERT INTO MEALS_MEALPART (ID,MEALID,INGREDIENT_ID,AMOUNT,UNIT) VALUES (5,2,9,40,1);
INSERT INTO MEALS_MEALPART (ID,MEALID,INGREDIENT_ID,AMOUNT,UNIT) VALUES (6,3,1,200,1);
INSERT INTO MEALS_MEALPART (ID,MEALID,INGREDIENT_ID,AMOUNT,UNIT) VALUES (7,4,6,2,0);
INSERT INTO MEALS_MEALPART (ID,MEALID,INGREDIENT_ID,AMOUNT,UNIT) VALUES (8,4,8,12,1);
INSERT INTO MEALS_MEALPART (ID,MEALID,INGREDIENT_ID,AMOUNT,UNIT) VALUES (9,4,4,227,0);
INSERT INTO MEALS_MEALPART (ID,MEALID,INGREDIENT_ID,AMOUNT,UNIT) VALUES (10,5,3,2,0);

exec RESET_SEQ('MEALS_MEALPART');
