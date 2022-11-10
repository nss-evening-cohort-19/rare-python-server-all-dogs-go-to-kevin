CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);

CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);


CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
);

CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);

CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);

CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

INSERT INTO Categories ('label') VALUES ('News');
INSERT INTO Tags ('label') VALUES ('JavaScript');
INSERT INTO Reactions ('label', 'image_url') VALUES ('happy', 'https://pngtree.com/so/happy');

INSERT INTO `Posts` VALUES (Null, 1, 5, "A Title", 1999-10-10, "Image URL", "Content", 1);
INSERT INTO `Posts` VALUES (Null, 1, 5, "Beans", 1999-10-10, "Image URL", "A lot of them", 1);
INSERT INTO `Posts` VALUES (Null, 1, 5, "Crumb", 1999-10-10, "Image URL", "All over the floor", 1);
INSERT INTO `Posts` VALUES (Null, 1, 5, "Banana", 1999-10-10, "Image URL", "Every morning", 1);
INSERT INTO `Posts` VALUES(Null, 55, 5, "Wake Up", 1999-10-10, "Image URL", "This craigs post", 1);

INSERT INTO `Comments` VALUES (Null, 18, 1, "Its a title alright");
INSERT INTO `Comments` VALUES (Null, 1, 2, "The best title");
INSERT INTO `Comments` VALUES (Null, 2, 3, "Always thinkin about em");
INSERT INTO `Comments` VALUES (Null, 2, 4, "Eating them in a theatre");

INSERT INTO `Subscriptions` VALUES (Null, 1, 55, 1999/01/01);

INSERT INTO `Users` VALUES (55, "Craig", "Imad", "Scrum47", "I love beans", "crumble@imad.com", "Password420", NULL, 2022, 1)

INSERT INTO `PostTags` VALUES (1, 17, 2)

SELECT
  c.id,
  c.post_id,
  c.author_id,
  c.content,
  p.id
FROM Comments c
JOIN Posts p
  ON c.post_id = p.id
WHERE p.id = 3

INSERT INTO `Reactions` VALUES (NULL, "A Label", "https://tinyurl.com/4zrpet4x");
INSERT INTO `Reactions` VALUES (NULL, "Another Label", "https://tinyurl.com/3vb8mex4");
INSERT INTO `Reactions` VALUES (NULL, "Another One", "https://tinyurl.com/yc494r5k");
