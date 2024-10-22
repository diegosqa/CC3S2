class Usuario:
    def __init__(self, rol):
        self.rol = rol

class RBACSystem:
    permisos = {
        'administrador': ['ver', 'editar', 'eliminar'],
        'editor': ['ver', 'editar'],
        'lector': ['ver']
    }

    def puede_realizar(self, usuario, accion):
        return accion in self.permisos.get(usuario.rol, [])
