create or replace procedure sp_listar_regioness(regiones out SYS_REFCURSOR)
is
begin
    open regiones for select * from region;
end;

create or replace procedure sp_listar_permisos(permisos out SYS_REFCURSOR)
is
begin
    open permisos for select * from permiso;
end;

create or replace procedure sp_agregar_tasador(
    v_nombre varchar2,
    v_apellido varchar2,
    v_telefono integer,
    v_correo varchar2,
    v_contrasena varchar2,
    v_permiso varchar2,
    v_region varchar2,
    v_salida out number
)
is
begin
    insert into usuario(nombre, apellido, telefono, correo, contrasena,  permiso_rol, region_nombre)
    values(v_nombre, v_apellido, v_telefono, v_correo, v_contrasena, v_region, v_permiso);
    commit;
    v_salida:=1;

    exception

    when others then
        v_salida:=0;
end;

create or replace procedure sp_listar_usuario(usuario out SYS_REFCURSOR)
is
begin
    open usuario for select * from usuario;
end;

