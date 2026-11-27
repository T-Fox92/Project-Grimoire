class Scene:

    def __init__ (self, name, description):
        self.name = name
        self.description = description
        self.connections = []
        self.enemies = []

    def add_connection (self, scene):
        self.connections.append (scene)

    def add_enemy (self, enemy):
        self.enemies.append (enemy)

    