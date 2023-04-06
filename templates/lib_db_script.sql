create table books(book_id int Primary key, title varchar(255) unique, year int not null, in_stock int not null, author_id int not null, genre_id int not null, publisher_id int not null);
create table author(author_id int Primary key, name varchar(255), surname varchar(250) not null, popularity int);
create table publisher(publisher_id int Primary key, name varchar(255) not null);
create table genre(genre_id int Primary key, name varchar(255) not null);

alter table books add constraint fk_author_book FOREIGN KEY (author_id) references author(author_id);
alter table books add constraint fk_publisher_book FOREIGN KEY (publisher_id) references publisher(publisher_id);
alter table books add constraint fk_genre_book FOREIGN KEY (genre_id) references genre(genre_id);

-- insert values
insert into publisher(publisher_id, name) values(1, 'Harper&Colins'), 
                                                (2, 'Macmillan');
insert into genre(genre_id, name) values(1, 'fantasy'),
                                        (2, 'novel');
insert into author(author_id, name, surname, popularity) 
            values(1, 'John', 'Tolkien', 0),
                  (2, 'Jack', 'London', 0);
insert into books(book_id, title, year, in_stock, author_id, genre_id, publisher_id)
            values(1, 'Lord of the Rings: The Two Towers', 1957, 5, 1, 1, 1), 
                  (2, 'Martin Eden', 1905, 2, 2, 2, 2);