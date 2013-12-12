--------------------------------------------------------
--  File created - Wednesday-December-11-2013   
--------------------------------------------------------
REM INSERTING into BETTERU.INGREDIENTS_CATEGORY
SET DEFINE OFF;
Insert into BETTERU.INGREDIENTS_CATEGORY (ID,NAME) values (1,'Proteins');
Insert into BETTERU.INGREDIENTS_CATEGORY (ID,NAME) values (2,'Dairy');
Insert into BETTERU.INGREDIENTS_CATEGORY (ID,NAME) values (3,'Carbs');
Insert into BETTERU.INGREDIENTS_CATEGORY (ID,NAME) values (4,'Other');


exec RESET_SEQ('INGREDIENTS_CATEGORY');