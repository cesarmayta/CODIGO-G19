create table if not exists tbl_usuario(
    usuario_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    usuario_nombre VARCHAR(200) NOT NULL UNIQUE,
    usuario_password VARCHAR(200) NOT NULL
);

