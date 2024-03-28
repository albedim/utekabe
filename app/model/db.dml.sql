USE judjen;

INSERT INTO plans VALUES (NULL, 'FREE', false, 0, false, '• Crea fino a 4 prodotti,• Personalizza il tuo account,• Analisi basica delle vendite');
INSERT INTO plans VALUES (NULL, 'Premium', true, 5.99, true, '• Vantaggi del piano FREE,• Crea illimitati prodotti,• Analisi avanzata delle vendite');

INSERT INTO types VALUES (NULL, 'Articolo');
INSERT INTO types VALUES (NULL, 'E-book');
INSERT INTO types VALUES (NULL, 'Guida');
INSERT INTO types VALUES (NULL, 'Ricetta');

INSERT INTO users (user_id, email, name, surname, bio, recovery_token, country_code, city, plan_id, paypal_email, image_path, password, library_name, created_on)
VALUES
    (21836382, 'giulia.bianchi@example.com', 'Giulia', 'Bianchi', 'Mi piace il cinema e amo viaggiare, vendo guide su come trovare alloggi', NULL, 'IT', 'Milano', 1, 'giulia.bianchi.paypal@example.com', 'files/images/users/default.png', '0cc175b9c0f1b6a831c399e269772661', 'giux34', '2024-03-14'),
    (30926236, 'luca.verde@example.com', 'Luca', 'Marini', 'tutorial su videogiochi e articoli sul gaming professionale', NULL, 'IT', 'Napoli', 1, 'luca.verde.paypal@example.com', 'files/images/users/default.png', '0cc175b9c0f1b6a831c399e269772661', 'Biblioteca di Luca', '2024-03-14'),
    (41759375, 'andrea.ferrari@example.com', 'Andrea', 'Brette', 'amante degli animali e scrivo articoli per aiutare le persone che hanno cani', NULL, 'IT', 'Torino', 1, 'andrea.ferrari.paypal@example.com', 'files/images/users/default.png', '0cc175b9c0f1b6a831c399e269772661', 'andre1', '2024-03-14'),
    (18592725, 'francesca.romano@example.com', 'Francesca', 'Romano', 'ciao a tutti', NULL, 'IT', 'Palermo', 1, 'francesca.romano.paypal@example.com', 'files/images/users/default.png', '0cc175b9c0f1b6a831c399e269772661', 'kekkalib', '2024-03-26'),
    (63642367, 'marco.galli@example.com', 'Mery', 'Foiuti', 'appassionato di fotografia e montagna, vendo guide su come fare foot', NULL, 'IT', 'Genova', 1, 'marco.galli.paypal@example.com', 'files/images/users/default.png', '0cc175b9c0f1b6a831c399e269772661', 'avco', '2024-03-01'),
    (71257544, 'chiara.moretti@example.com', 'Chiara', 'Moretti', 'Amante della letteratura e del teatro', NULL, 'IT', 'Bologna', 1, 'chiara.moretti.paypal@example.com', 'files/images/users/default.png', '0cc175b9c0f1b6a831c399e269772661', 'bichiara', '2024-03-4'),
    (81153633, 'paolo.rizzo@example.com', 'Paolo', 'Brescia', 'hey', NULL, 'IT', 'Verona', 1, 'paolo.rizzo.paypal@example.com', 'files/images/users/default.png', '0cc175b9c0f1b6a831c399e269772661', 'paolo09', '2024-03-26'),
    (93667438, 'elisa.barbieri@example.com', 'Elisa', 'Martini', 'ragazza che ama programmare, ti insegno con i miei ebook', NULL, 'IT', 'Catania', 1, 'elisa.barbieri.paypal@example.com', 'files/images/users/default.png', '0cc175b9c0f1b6a831c399e269772661', 'elischiatta', '2024-03-26'),
    (10513474, 'andrea.mancini@example.com', 'Marta', 'Mancini', 'Amo il cibo e mi piace cucinare, vendo ricette e guide', NULL, 'IT', 'Trieste', 1, 'andrea.mancini.paypal@example.com', 'files/images/users/default.png', '0cc175b9c0f1b6a831c399e269772661', 'bioumix', '2024-03-14'),
    (11234434, 'valentina.lombardi@example.com', 'Valentina', 'Borsi', 'hey', NULL, 'IT', 'Padova', 1, 'valentina.lombardi.paypal@example.com', 'files/images/users/default.png', '0cc175b9c0f1b6a831c399e269772661', 'vale04', '2024-03-26');


INSERT INTO reviews (user_id, content, created_on, stars)
VALUES
(21836382, 'Un servizio eccellente per creare la propria libreria digitale, ho pubblicato i miei ebook e le mie ricette senza problemi', NOW(), 5),
(30926236, 'mi piace l''idea di poter condividere la mia libreria tramite un semplice link.', NOW(), 4),
(41759375, 'Fantastico ho iniziato a pubblicare le mie guide di viaggio e sto già ricevendo i miei primi guadagni, scrivo per lavoro però quindi sono avvantaggiato xD', NOW(), 4),
(18592725, 'Sono rimasta impressionata dalla facilità con cui ho potuto pubblicare i miei ebooks.', NOW(), 5),
(63642367, 'Ho appena iniziato a utilizzare questo servizio per pubblicare le mie ricette e mi ha colpito la sua semplicità e versatilità', NOW(), 4),
(71257544, 'è un''ottima piattaforma per pubblicare i propri articoli e guadagnare dalla vendita dei prodotti digitali. Consiglio vivamente questo servizio a tutti gli aspiranti scrittori e creatori di contenuti.', NOW(), 5),
(81153633, 'Ho creato la mia libreria digitale e ho già ricevuto i primi acquisti dai miei amici e seguaci. È emozionante vedere il mio lavoro apprezzato ahahah', NOW(), 5),
(93667438, 'Il processo di pubblicazione dei miei ebook è stato semplice e intuitivo.', NOW(), 5),
(10513474, 'Mi sono appena iscritto a questo servizio e sto già gassaporando la semplicità di quest ultimo', NOW(), 4),
(11234434, 'ottimo modo per monetizzare i miei contenuti digitali.', NOW(), 4);




INSERT INTO plans VALUES (NULL, 'FREE', false, 0, false, '• Create up to 4 products,• Personalize your account,• Basic sales analytics');
INSERT INTO plans VALUES (NULL, 'Premium', true, 5.99, true, "• FREE plan's advantages","• Create how much products as you want","• Advanced sales analytics");

INSERT INTO types VALUES (NULL, 'Artcle');
INSERT INTO types VALUES (NULL, 'E-book');
INSERT INTO types VALUES (NULL, 'Guide');
INSERT INTO types VALUES (NULL, 'Recipe');

mysqldump -u bliddo -h bliddo.mysql.pythonanywhere-services.com --set-gtid-purged=OFF --no-tablespaces --column-statistics=0 'bliddo$default'  > db-backup.sql

INSERT INTO users (user_id, email, name, surname, bio, recovery_token, country_code, city, plan_id, paypal_email, image_path, password, library_name, created_on)
VALUES
    (21836382, 'giulia.broddi@example.com', 'Giulia', 'Broddi', 'I like cinema and love to travel, I sell guides on how to find accommodations', NULL, 'IT', 'Milan', 1, 'giulia.broddi@example.com', 'files/images/users/default.png', '0cc175b9c0f1b6a831c399e269772661', 'giux34', '2024-03-14'),
    (30926236, 'luke.mars@example.com', 'Luke', 'Mars', 'tutorial on video games and articles on professional gaming', NULL, 'UK', 'London', 1, 'luke.mars@example.com', 'files/images/users/default.png', '0cc175b9c0f1b6a831c399e269772661', 'Luke''s Library', '2024-03-14'),
    (41759375, 'andrew.bretty@example.com', 'Andrew', 'Bretty', 'animal lover and I write articles to help people who have dogs', NULL, 'UK', 'Glasgow', 1, 'andrew.bretty@example.com', 'files/images/users/default.png', '0cc175b9c0f1b6a831c399e269772661', 'andre1', '2024-03-14'),
    (18592725, 'juliette.romy@example.com', 'Juliette', 'Romy', 'hello everyone', NULL, 'US', 'New York', 1, 'juliette.romy@example.com', 'files/images/users/default.png', '0cc175b9c0f1b6a831c399e269772661', 'kekkalib', '2024-03-26'),
    (63642367, 'mary.king@example.com', 'Mary', 'King', 'passionate about photography and mountains, I sell guides on how to do foot', NULL, 'UK', 'Manchester', 1, 'mary.king@example.com', 'files/images/users/default.png', '0cc175b9c0f1b6a831c399e269772661', 'avco', '2024-03-01'),
    (71257544, 'carol.brownie@example.com', 'Carol', 'Brownie', 'Lover of literature and theater', NULL, 'UK', 'London', 1, 'carol.brownie@example.com', 'files/images/users/default.png', '0cc175b9c0f1b6a831c399e269772661', 'bichiara', '2024-03-04'),
    (81153633, 'paul.white@example.com', 'Paul', 'White', 'hey', NULL, 'US', 'New Jersey', 1, 'paul.white@example.com', 'files/images/users/default.png', '0cc175b9c0f1b6a831c399e269772661', 'paolo09', '2024-03-26'),
    (93667438, 'antonio.perrante@example.com', 'Antonio', 'Perrante', 'girl who loves programming, I teach you with my ebooks', NULL, 'ES', 'Valencia', 1, 'antonio.perrante@example.com', 'files/images/users/default.png', '0cc175b9c0f1b6a831c399e269772661', 'elischiatta', '2024-03-26'),
    (10513474, 'kathleen.davis@example.com', 'Kathleen', 'Davis', 'I love food and I like to cook, I sell recipes and guides', NULL, 'US', 'Los Angeles', 1, 'kathleen.davis@example.com', 'files/images/users/default.png', '0cc175b9c0f1b6a831c399e269772661', 'bioumix', '2024-03-14'),
    (11234434, 'angela.rodriguez@example.com', 'Angela', 'Rodriguez', 'hey', NULL, 'ES', 'Madrid', 1, 'angela.rodriguez@example.com', 'files/images/users/default.png', '0cc175b9c0f1b6a831c399e269772661', 'vale04', '2024-03-26');

INSERT INTO reviews (user_id, content, created_on, stars)
VALUES
(21836382, 'Excellent service to create your own digital library, I have published my ebooks and my recipes without problems', NOW(), 5),
(30926236, 'I like the idea of being able to share my library through a simple link.', NOW(), 4),
(41759375, 'Fantastic, I started publishing my travel guides and I am already receiving my first earnings, I write for work though so I am advantaged xD', NOW(), 4),
(18592725, 'I was impressed by how easy it was to publish my ebooks.', NOW(), 5),
(63642367, 'I have just started using this service to publish my recipes and I am impressed by its simplicity and versatility', NOW(), 4),
(71257544, 'it is a great platform to publish your articles and earn from the sale of digital products. I highly recommend this service to all aspiring writers and content creators.', NOW(), 5),
(81153633, 'I created my digital library and I have already received the first purchases from my friends and followers. It is exciting to see my work appreciated ahahah', NOW(), 5),
(93667438, 'The process of publishing my ebooks was simple and intuitive.', NOW(), 5),
(10513474, 'I have just signed up for this service and I am already enjoying the simplicity of it', NOW(), 4),
(11234434, 'great way to monetize my digital content.', NOW(), 4);