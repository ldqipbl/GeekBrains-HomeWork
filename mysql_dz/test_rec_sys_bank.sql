DELIMITER //

DROP PROCEDURE IF EXISTS mvp;
CREATE PROCEDURE mvp (value INT)
BEGIN
	IF value > (SELECT MAX(id) FROM users) THEN
		SELECT "count user" AS error, (SELECT MAX(id) FROM users) AS last_user_id;
	END IF;

	IF (SELECT invest_prod FROM count_client_get_products WHERE id = value) > 3 THEN
		SELECT value AS users, "investments > 3" AS recomend;
	ELSEIF (SELECT invest_prod FROM count_client_get_products WHERE id = value) = 0 THEN
		SELECT value AS users, "investments = 0" AS recomend;
	END IF;

        IF (SELECT card_prod FROM count_client_get_products WHERE id = value) > 3 THEN
                SELECT value AS users, "card > 3" AS recomend;
        ELSEIF (SELECT card_prod FROM count_client_get_products WHERE id = value) = 0 THEN
                SELECT value AS users, "card = 0" AS recomend;
        END IF;

        IF (SELECT credit_prod FROM count_client_get_products WHERE id = value) > 3 THEN
                SELECT value AS users, "credit > 3" AS recomend;
        ELSEIF (SELECT credit_prod FROM count_client_get_products WHERE id = value) = 0 THEN
                SELECT value AS users, "credit = 0" AS recomend;
        END IF;

        IF (SELECT insurance_prod FROM count_client_get_products WHERE id = value) > 3 THEN
                SELECT value AS users, "insurance > 3" AS recomend;
        ELSEIF (SELECT insurance_prod FROM count_client_get_products WHERE id = value) = 0 THEN
                SELECT value AS users, "insurance = 0" AS recomend;
        END IF;

END //

DELIMITER ;


call mvp(2);

