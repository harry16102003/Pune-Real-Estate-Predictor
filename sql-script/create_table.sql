use pune_real_estate_db;

CREATE TABLE raw_house_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    area_type VARCHAR(255),
    availability VARCHAR(255),
    location VARCHAR(255),
    size VARCHAR(50),
    society VARCHAR(255),
    total_sqft VARCHAR(50), -- Stored as VARCHAR to handle ranges like '1133 - 1384'
    bath FLOAT,
    balcony FLOAT,
    price FLOAT
);

SELECT * FROM raw_house_data LIMIT 10;