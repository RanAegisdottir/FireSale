INSERT INTO myprofile_users (name, email, username, password, bio, rating) VALUES('Kristin', 'kristin@gmail.com', 'krissa', 'fire123', '', 0);
INSERT INTO myprofile_userimage (user_img, user) VALUES('image', 1)

INSERT INTO shop_item (name, description, sellerID, condition, available, price_idea) VALUES('PS5', 'flott PS5', 0, 1, true, 5000);
INSERT INTO shop_conditions (status) VALUES('new');
INSERT INTO shop_itemimage (img_url, item) VALUES('PS5', 1);
INSERT INTO shop_offers (buyer, item, amount, accepted) VALUES(1, 1, 5000, false);

INSERT INTO checkout_payments (userID, card_name, card_num, exdate, cvc, companyname, country, street, zip, city, phone) VALUES(1, 'Kristin', 5555, 01-01-2023, 123, '', 1, 'Reykjabygð 47', '600', 'Reykjavík', '1234567');
INSERT INTO checkout_order (offer_id, pay_id) VALUES(1, 1);
INSERT INTO checkout_review (text, rating, order) VALUES('great', 5, 1);
INSERT INTO checkout_stars (star_img, star_num, user) VALUES('Star', 5, 1);




INSERT INTO myprofile_users (name, email, username, password, bio, rating) VALUES('Ran', 'ran@gmail.com', 'Robbery', 'fire123', '', 0);
INSERT INTO myprofile_userimage (user_img, user) VALUES('image', 2)

INSERT INTO shop_item (name, description, sellerID, condition, available, price_idea) VALUES('Pink Table', 'Old table', 2, 2, true, 3000);
INSERT INTO shop_conditions (status) VALUES('old');
INSERT INTO shop_itemimage (img_url, item) VALUES('Table', 2);
INSERT INTO shop_offers (buyer, item, amount, accepted) VALUES(2, 2, 3500, false);

INSERT INTO checkout_country (country) VALUES('NZ');
INSERT INTO checkout_payments (userID, card_name, card_num, exdate, cvc, companyname, country, street, zip, city, phone) VALUES(2, 'Ran', 1111, 01-02-2024, 987, '', 2, 'Laugavegur 1', '400', 'Reykjavík', '9876543');
INSERT INTO checkout_order (offer_id, pay_id) VALUES(2, 2);
INSERT INTO checkout_review (text, rating, order) VALUES('bad', 1, 2);
INSERT INTO checkout_stars (star_img, star_num, user) VALUES('Star', 1, 2);




INSERT INTO myprofile_users (name, email, username, password, bio, rating) VALUES('Jon', 'jon@gmail.com', 'jhonny', 'fire123', '', 0);
INSERT INTO myprofile_userimage (user_img, user) VALUES('image', 3)

INSERT INTO shop_item (name, description, sellerID, condition, available, price_idea) VALUES('Sofa', 'New sofa', 3, 1, true, 7000);
INSERT INTO shop_conditions (status) VALUES('used');
INSERT INTO shop_itemimage (img_url, item) VALUES('sofa', 3);
INSERT INTO shop_offers (buyer, item, amount, accepted) VALUES(3, 3, 6000, false);

INSERT INTO checkout_country (country) VALUES('NZ');
INSERT INTO checkout_payments (userID, card_name, card_num, exdate, cvc, companyname, country, street, zip, city, phone) VALUES(3, 'Jon', 2222, 10-10-2024, 777, '', 1, 'draugavegur 1', '800', 'Reykjavík', '77777777');
INSERT INTO checkout_order (offer_id, pay_id) VALUES(3, 3);
INSERT INTO checkout_review (text, rating, order) VALUES('good', 3, 3);
INSERT INTO checkout_stars (star_img, star_num, user) VALUES('Star', 3, 3);