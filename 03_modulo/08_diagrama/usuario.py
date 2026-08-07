from foto import Foto, FotoPerfil
from typing import Union, List

class Usuario:
    def __init__(self, correo: str, contrasena: str) -> None:
        self.__correo = correo
        self.__contrasena = contrasena
        self.__album_fotos: List[Foto] = []
        self.__foto_perfil = FotoPerfil()
        self.__amigos: List['Usuario'] = [] # Cuando un proyecto crece, lo ideal es quitarle la responsabilidad de recursividad al Usuario.

    @property
    def correo(self) -> str:
        return self.__correo

    @property
    def album_fotos(self) -> List[Foto]:
        return self.__album_fotos

    @property
    def foto_perfil(self) -> Foto:
        return self.__foto_perfil

    @property
    def amigos(self) -> List['Usuario']:
        return self.__amigos

    def agregar_fotos_album(self, imagen: str, ancho: int, alto: int) -> None:
        nueva_foto = Foto(imagen, ancho, alto)
        self.__album_fotos.append(nueva_foto)

    def actualizar_foto_perfil(self, imagen: str, ancho: int, alto: int) -> None:
        self.__foto_perfil.imagen = imagen
        self.__foto_perfil.ancho = ancho
        self.__foto_perfil.alto = alto

    def agregar_amigo(self, amigo: 'Usuario') -> None:
        if amigo not in self.__amigos:
            self.__amigos.append(amigo)

    def reaccionar(self, foto: Union[Foto, FotoPerfil]) -> None:
        foto.reacciones += 1
