-- 1. Product count and average price by category
SELECT
    category,
    COUNT(*) AS product_count,
    ROUND(AVG(price), 2) AS average_price
FROM products
GROUP BY category
ORDER BY average_price DESC;


-- 2. Top 5 rated products
SELECT
    title,
    category,
    rating_rate,
    rating_count
FROM products
ORDER BY rating_rate DESC, rating_count DESC
LIMIT 5;


-- 3. Products priced above the overall average
SELECT
    title,
    category,
    price
FROM products
WHERE price > (
    SELECT AVG(price)
    FROM products
)
ORDER BY price DESC;


-- 4. Highest-priced product in each category
SELECT
    p.title,
    p.category,
    p.price
FROM products p
WHERE p.price = (
    SELECT MAX(p2.price)
    FROM products p2
    WHERE p2.category = p.category
)
ORDER BY p.category;


-- 5. Average rating by category
SELECT
    category,
    COUNT(*) AS product_count,
    ROUND(AVG(rating_rate), 2) AS average_rating
FROM products
GROUP BY category
ORDER BY average_rating DESC;