class Adventure:

    def __init__ (self, title, description):
        self.title = title
        self.description = description
        self.scenes = []
        self.starting_scene = None

    def add_scene (self, scene):
        self.scenes.append (scene)

    def get_scenes (self):
        return self.scenes

    def set_starting_scene (self, scene):
        if scene not in self.scenes:
            raise ValueError ("Starting scene must belong to this adventure.")

        self.starting_scene = scene