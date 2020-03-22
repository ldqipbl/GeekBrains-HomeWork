DROP TABLE IF EXISTS card_2;                      --Карты(дебетовый, кредитные)
CREATE TABLE card_2(
        id SERIAL PRIMARY KEY,
        user_id BIGINT UNSIGNED,
        products_id BIGINT,
        ue INT,
        date_of_creation DATE,
        FOREIGN KEY (user_id) REFERENCES users(id));

INSERT INTO card VALUES
        (0, 2, 6, 20000, '2000-01-21'),
        (0, 2, 7, 100000, '2000-01-21'),
        (0, 3, 7, 100000, '2010-03-23'),
        (0, 3, 7, 100000, '2015-04-04'),
        (0, 3, 6, 20000, '2020-05-25');

