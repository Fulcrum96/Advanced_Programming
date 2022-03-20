#!/bin/bash 
echo "Agregar nuevo usuario al sistema."

read -p "Ingrese nombre de usuario: " username
if id -u $username >/dev/null 2>&1; then
    echo "El usuario ya existe."
    username=""
fi
echo $username

read -p "Ingrese nombre completo: " realname

read -sp "Ingrese la contraseña: " PASSWORD

read -p "Ingrese la ubicación del directorio HOME (ej: /home/$username: " homepath
echo $homepath

PS3="Seleccione el tipo de shell: "
shelloptions=("Shell (normal)" "Bash")
select chosenshell in "${shelloptions[@]}"; do
    case $chosenshell in
        "Shell (normal)")
            shelltype="/bin/sh" 
            break
            ;;
        "Bash")
            shelltype="/bin/bash"
            break
            ;;
        *)
            echo "Opción $REPLY no válida"
            ;;
    esac
done 
echo $shelltype

read -p "Ingrese el grupo al que pertenecerá el usuario: " group
if id -g $group >dev/null 2>&1; then
    echo "El grupo ya existe."
else
    groupadd $group
fi
echo $group

useradd -g $group -s $shelltype -d $homepath -m $username