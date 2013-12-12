--------------------------------------------------------
--  File created - Tuesday-November-19-2013   
--------------------------------------------------------
REM INSERTING into BETTERU.MEALS_MEAL
set DEFINE off;
INSERT INTO BETTERU.MEALS_MEAL (id,name,DESCRIPTION) values (1,'300g Chicken Breast','300g chicken breast with random seasonings and veggies.');
INSERT INTO BETTERU.MEALS_MEAL (id,name,DESCRIPTION) values (2,'Protein shake w/ greek yogurt, milk, and oats','Isopure protein with 12 oz milk and 227g fat free greek yogurt in a blender');
INSERT INTO BETTERU.MEALS_MEAL (id,name,DESCRIPTION) values (3,'200g Chicken Breast','200g chicken breast with random seasonings and veggies.');
INSERT INTO BETTERU.MEALS_MEAL (id,name,DESCRIPTION) values (4,'Isopure Protein Shake with Milk and Greek Yogurt','Isopure protein with 12 oz milk, 40g oats and 227g fat free greek yogurt in a blender');
INSERT INTO BETTERU.MEALS_MEAL (ID,NAME,DESCRIPTION) values (5,'2 eggs','2 hard boiled eggs.');

exec RESET_SEQ('MEALS_MEAL');