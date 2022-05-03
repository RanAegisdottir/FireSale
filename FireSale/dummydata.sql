INSERT INTO myprofile_users (name, email, username, password, bio, rating) VALUES('Kristin', 'kristin@gmail.com', 'krissa', 'fire123', '', 0);
INSERT INTO myprofile_userimage (user_img, user) VALUES('image', 1)

INSERT INTO shop_item (name, description, sellerID, condition, available) VALUES('PS5', 'flott PS5', 0, 1, true);
INSERT INTO shop_conditions (status) VALUES('new');
INSERT INTO shop_itemimage (img_url, item) VALUES('PS5', 1);
INSERT INTO shop_offers (buyer, item, amount, accepted) VALUES(1, 1, 5000, false);

INSERT INTO checkout_payments (userID, card_name, card_num, exdate, cvc, companyname, country, street, zip, city, phone) VALUES(1, 'Kristin', 5555, 01-01-2023, 123, '', 1, 'Reykjabygð 47', '600', 'Reykjavík', '1234567');
INSERT INTO checkout_order (offer_id, pay_id) VALUES(1, 1);
INSERT INTO checkout_review (text, rating, order) VALUES('great', 5, 1);
INSERT INTO checkout_stars (star_img, star_num, user) VALUES('Star', 5, 1);

