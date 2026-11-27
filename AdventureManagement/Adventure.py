class Adventure:

    def __init__ (self, title, description):
        self.title = title
        self.description = description
        self.scenes = []

    def add_scene (self, scene):
        self.scenes.append (scene)

    def get_scenes (self):
        return self.scenes

    