create table Car
(
    id      serial primary key,
    model   varchar(255),
    year    int,
    details text
);

insert into Car (model, year, details)
values ('BMW E36', 1996, 'coupe'),
       ('Ford Focus MK3', 2011, 'hatchback'),
       ('Audi A8', 2018, 'kombi');