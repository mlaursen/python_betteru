

CREATE OR REPLACE VIEW INGREDIENT_VIEW AS
  SELECT I.ID,
         I.NAME INGREDIENT_NAME,
         B.NAME BRAND_NAME,
         C.NAME CATEGORY_NAME,
         DEFAULT_SERVING_SIZE,
         DEFAULT_SERVING_UNIT,
         ALT_SERVING_SIZE,
         ALT_SERVING_UNIT,
         CALORIES,
         FAT,
         CARBOHYDRATES,
         PROTEIN
  FROM INGREDIENTS_INGREDIENT I
  INNER JOIN INGREDIENTS_BRAND B ON (I.BRAND_ID = B.ID)
  INNER JOIN INGREDIENTS_CATEGORY C ON (I.CATEGORY_ID = C.ID)
  ORDER BY ID;

CREATE OR REPLACE VIEW MEALPARTS_VIEW AS
  SELECT ID, MEALID, AMOUNT, UNIT, INGREDIENT_NAME, BRAND_NAME, CATEGORY_NAME, CALORIES, FAT, CARBOHYDRATES, PROTEIN, SERVING_SIZE, SERVING_UNIT, DEFAULT_SERVING_SIZE, DEFAULT_SERVING_UNIT, 
         ALT_SERVING_SIZE, ALT_SERVING_UNIT, (CALORIES*RATIO) TOTAL_CALORIES, (FAT*RATIO) TOTAL_FAT, (CARBOHYDRATES*RATIO) TOTAL_CARBOHYDRATES, (PROTEIN*RATIO) TOTAL_PROTEIN
  FROM (SELECT ROWNUM ID, MEALID, MP.AMOUNT AMOUNT, MP.UNIT UNIT, INGREDIENT_NAME, BRAND_NAME, CATEGORY_NAME, CALORIES, FAT, CARBOHYDRATES, PROTEIN, DEFAULT_SERVING_SIZE, DEFAULT_SERVING_UNIT,
               ALT_SERVING_SIZE, ALT_SERVING_UNIT,
               CASE WHEN UNIT = 0 THEN (AMOUNT / DEFAULT_SERVING_SIZE)
                    ELSE (AMOUNT / ALT_SERVING_SIZE)
                    END AS RATIO,
               CASE WHEN UNIT = 0 THEN DEFAULT_SERVING_SIZE 
                    ELSE ALT_SERVING_SIZE
                    END AS SERVING_SIZE,
               CASE WHEN UNIT = 0 THEN DEFAULT_SERVING_UNIT
                    ELSE ALT_SERVING_UNIT
                    END AS SERVING_UNIT
        FROM MEALS_MEALPART MP
        JOIN INGREDIENT_VIEW IV
        ON MP.INGREDIENT_ID = IV.ID)
  ORDER BY ID;

CREATE OR REPLACE VIEW MEAL_VIEW AS
  SELECT ID, NAME, DESCRIPTION, TOTAL_CALORIES, TOTAL_FAT, TOTAL_CARBOHYDRATES, TOTAL_PROTEIN
  FROM (SELECT MEALID, SUM(TOTAL_CALORIES) TOTAL_CALORIES, SUM(TOTAL_FAT) TOTAL_FAT, SUM(TOTAL_CARBOHYDRATES) TOTAL_CARBOHYDRATES, SUM(TOTAL_PROTEIN) TOTAL_PROTEIN
        FROM MEALPARTS_VIEW
        GROUP BY MEALID) MPV
  JOIN MEALS_MEAL M
  ON M.ID = MPV.MEALID;


SELECT * FROM INGREDIENT_VIEW;
SELECT * FROM MEALPARTS_VIEW WHERE MEALID=2;
SELECT * FROM MEAL_VIEW;

SELECT * FROM MEALS_MEAL;

SELECT MEALID, NAME, DESCRIPTION, TOTAL_CALORIES, TOTAL_FAT, TOTAL_CARBOHYDRATES, TOTAL_PROTEIN
  FROM MEALPARTS_VIEW MPV
  JOIN MEALS_MEAL M
  ON M.ID = MPV.MEALID
  ORDER BY MEALID, NAME;

SELECT ID, NAME, DESCRIPTION, TOTAL_CALORIES, TOTAL_FAT, TOTAL_CARBOHYDRATES, TOTAL_PROTEIN
FROM (SELECT MEALID, SUM(TOTAL_CALORIES) TOTAL_CALORIES, SUM(TOTAL_FAT) TOTAL_FAT, SUM(TOTAL_CARBOHYDRATES) TOTAL_CARBOHYDRATES, SUM(TOTAL_PROTEIN) TOTAL_PROTEIN
      FROM MEALPARTS_VIEW
      GROUP BY MEALID) MPV
JOIN MEALS_MEAL M
ON M.ID = MPV.MEALID;