INSERT INTO ACCOUNTS_ACCOUNT (ID,USERNAME,PASSWORD,BIRTHDAY,GENDER,UNITS,EMAIL,ACTIVE_SINCE) VALUES (0,'admin','abcd',TO_DATE('24-OCT-13','DD-MON-RR'),'m','imperial','mlaursen03@gmail.com',TO_DATE('24-OCT-13','DD-MON-RR'));
INSERT INTO ACCOUNTS_ACCOUNT (ID,USERNAME,PASSWORD,BIRTHDAY,GENDER,UNITS,EMAIL,ACTIVE_SINCE) VALUES (1,'mlaursen','324a3a227592408791417bde0ead3355261729a8cadb9bb0cdea5c95801df076ecf5803d65c7bebf7fa0c49ea4a1925c57cd3f366a5be57390d3d1245a52e597',TO_DATE('21-JAN-91','DD-MON-RR'),'m','imperial','mlaursen03@gmail.com',TO_DATE('27-OCT-13','DD-MON-RR'));

INSERT INTO ACCOUNTS_ACCOUNTSETTINGS (ID,ACCOUNT_ID,RECALCULATE_DAY_OF_WEEK,ACTIVITY_MULTIPLIER,HEIGHT,DATE_CHANGED) VALUES (0,0,1,'sedentary',72,TO_DATE('24-OCT-13','DD-MON-RR'));
INSERT INTO ACCOUNTS_ACCOUNTSETTINGS (ID,ACCOUNT_ID,RECALCULATE_DAY_OF_WEEK,ACTIVITY_MULTIPLIER,HEIGHT,DATE_CHANGED) VALUES (1,1,1,'sedentary',71,TO_DATE('27-OCT-13','DD-MON-RR'));

EXEC RESET_SEQ('ACCOUNTS_ACCOUNT');
EXEC RESET_SEQ('ACCOUNTS_ACCOUNTSETTINGS');