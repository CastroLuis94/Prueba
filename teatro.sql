
CREATE TABLE teatro(
    idteatro INTEGER PRIMARY KEY,
    nombre  CHAR(50) ,
    año INTEGER
);

CREATE TABLE sala(
    idsala INTEGER PRIMARY KEY,
    nombre CHAR(50),
	capacidad INTEGER,
	microfo_amb BOOLEAN,
	maquina_humo BOOLEAN,
    idteatro INTEGER,
    FOREIGN KEY (idteatro) REFERENCES teatro(idteatro)
);

CREATE TABLE espectaculo(
    idespectaculo INTEGER PRIMARY KEY,
	nombre  TEXT,
	director CHAR(50),
	descripcion TEXT,
    meses_cartelera INTEGER,
    idteatro INTEGER,
    FOREIGN KEY (idteatro) REFERENCES teatro(idteatro)
);


CREATE TABLE cartelera(
    idcartelera INTEGER PRIMARY KEY,
    fecha date,
    idsala INTEGER,
    FOREIGN KEY (idsala) REFERENCES sala(idsala),
    idespectaculo INTEGER,
    FOREIGN KEY (idespectaculo) REFERENCES espectaculo(idespectaculo)
);

CREATE TABLE funcion(
    idfuncion INTEGER PRIMARY KEY,
    sucedio BOOLEAN,
    reservadas INTEGER,
    vendidas INTEGER,
    asistieron INTEGER,
    idsala INTEGER,
    FOREIGN KEY (idsala) REFERENCES sala(idsala),
    idespectaculo INTEGER,
    FOREIGN KEY (idespectaculo) REFERENCES espectaculo(idespectaculo)
    /* 
    -idsala
	-idespectaculo
    */
);


INSERT INTO teatro VALUES (1,"teatro1",1945);
INSERT INTO teatro VALUES (2,"teatro2",1994);


INSERT INTO sala VALUES (1,"sala1",450,FALSE,TRUE,1);
INSERT INTO sala VALUES (2,"sala2",150,TRUE,TRUE,1);


INSERT INTO espectaculo VALUES (1,"espectaculo1","director1","espectaculo de el teatro1",3,1);
INSERT INTO espectaculo VALUES (2,"espectaculo2","director2","espectaculo de el teatro1",6,1);
INSERT INTO espectaculo VALUES (3,"espectaculo3","director3","espectaculo de el teatro1",4,1);


INSERT INTO cartelera VALUES (1,"1999-01-01",1,1);
INSERT INTO cartelera VALUES (2,"1999-01-01",2,2);


INSERT INTO funcion VALUES (1,TRUE,150,200,175,1,1);
INSERT INTO funcion VALUES (2,TRUE,170,250,200,1,2);
INSERT INTO funcion VALUES (3,FALSE,150,200,175,2,1);
INSERT INTO funcion VALUES (4,TRUE,150,200,175,2,2);
INSERT INTO funcion VALUES (5,TRUE,250,200,175,2,3);

SELECT nombre,director,descripcion FROM espectaculo ORDER BY meses_cartelera DESC;
SELECT idsala,sum(asistieron) FROM funcion WHERE sucedio = TRUE GROUP BY idsala ; 
SELECT idespectaculo from funcion WHERE reservadas > vendidas AND sucedio = TRUE;

