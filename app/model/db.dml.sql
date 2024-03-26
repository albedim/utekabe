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
