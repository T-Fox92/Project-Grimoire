import json
from pathlib import Path
from datetime import datetime

from CharacterManagement.Character import Character
from CharacterManagement.JobDefinitions import PLAYABLE_JOBS
from CharacterManagement.RaceDefinitions import PLAYABLE_RACES
from AdventureManagement.TutorialAdventure import create_tutorial_adventure


class SaveGameManager:

    MAX_SAVE_SLOTS = 50
    SAVE_VERSION = 1

    def __init__ (self):
        self.save_directory = (Path (__file__).resolve().parent.parent / "saves")

    # ==========================================
    # CHARACTER SERIALIZATION
    # ==========================================

    def get_job_by_name (self, job_name):

        for job in PLAYABLE_JOBS:
            if job.name == job_name:
                return job

        return None

    def get_race_by_name (self, race_name):

        for race in PLAYABLE_RACES:
            if race.name == race_name:
                return race

        return None

    def get_ability_by_name (self, job, ability_name):

        for ability in job.get_starting_abilities():
            if ability.name == ability_name:
                return ability

        for ability in job.get_available_abilities ():
            if ability.name == ability_name:
                return ability

        for specialization in job.get_specialization ():
            for ability in specialization.get_abilities ():
                if ability.name == ability_name:
                    return ability

        return None

    def reconstruct_character (self, character_data):

        job = self.get_job_by_name (character_data ["job"])
        race = self.get_race_by_name (character_data ["race"])

        if job is None or race is None:
            raise ValueError ("Invalid race or job in save data.")

        character = Character (
            name = character_data ["name"],
            job = job,
            attributes = character_data ["attributes"].copy (),
            race = race
        )

        character.level = character_data ["level"]
        character.experience = character_data ["experience"]
        character.currentHealth = character_data ["current_health"]
        character.maxHealth = character_data ["max_health"]

        # Restore learned abilities
        character.learnedAbilities = []

        for ability_name in character_data ["learned_abilities"]:

            ability = self.get_ability_by_name (job, ability_name)

            if ability is None:
                raise ValueError (f"Unknown ability in save data: {ability_name}")

            character.learnedAbilities.append (ability)

        character.specializationAffinities = character_data ["specialization_affinities"].copy ()

        return character

    def serialize_character (self, character):

        character_data = character.get_details ()

        return character_data.copy ()

    # ==========================================
    # SAVE SLOT HELPERS
    # ==========================================

    def get_save_path (self, slot):

        if not isinstance (slot, int) or isinstance (slot, bool):
            raise ValueError ("Save slot must be an integer.")

        if slot < 1 or slot > self.MAX_SAVE_SLOTS:
            raise ValueError ("Invalid save slot.")

        return self.save_directory / f"save_{slot:02}.json"

    def get_available_slots (self):

        self.save_directory.mkdir (parents = True, exist_ok = True)

        slots = []

        for slot in range (1, self.MAX_SAVE_SLOTS + 1):

            save_path = self.get_save_path (slot)

            slots.append ({
                "slot": slot, 
                "occupied": save_path.is_file()
                })

        return slots


    # ==========================================
    # SAVE GAME
    # ==========================================

    def save_game (self, slot, character, adventure, current_scene, confirm_overwrite = False):

        save_path = self.get_save_path (slot)

        if save_path.exists() and not confirm_overwrite:
            return False

        self.save_directory.mkdir (parents = True, exist_ok = True)

        save_data = {
            "save_version": self.SAVE_VERSION,
            "slot": slot,
            "saved_at": datetime.now().isoformat(timespec="seconds"),
            "character": self.serialize_character(character),
            "adventure": {
                "title": adventure.title,
                "current_scene": current_scene.name
            }
        }

        temporary_path = save_path.with_suffix(".tmp")

        try:
            with temporary_path.open ("w", encoding = "utf-8") as save_file:
                json.dump (save_data, save_file, indent = 4)

            temporary_path.replace(save_path)

        finally:
            if temporary_path.exists ():
                temporary_path.unlink ()

        return True


    # ==========================================
    # LOAD GAME
    # ==========================================

    def load_game (self, slot):

        save_path = self.get_save_path (slot)

        if not save_path.is_file ():
            return None

        try:
            with save_path.open ("r", encoding = "utf-8") as save_file:
                save_data = json.load (save_file)

            if save_data.get ("save_version") != self.SAVE_VERSION:
                raise ValueError ("Unsupported save file version.")

            character = self.reconstruct_character (save_data ["character"])

            adventure, current_scene = self.reconstruct_adventure (save_data ["adventure"])

            return {
                "slot": save_data ["slot"],
                "saved_at": save_data ["saved_at"],
                "character": character,
                "adventure": adventure,
                "current_scene": current_scene
            }

        except (json.JSONDecodeError, KeyError, TypeError) as error:
            raise ValueError ("Save file is corrupted or invalid.") from error


    # ==========================================
    # DELETE SAVE
    # ==========================================

    def delete_save (self, slot, confirm = False):

        save_path = self.get_save_path (slot)

        if not save_path.is_file ():
            return False

        if not confirm:
            return False

        save_path.unlink ()

        return True

    # ==========================================
    # REBUILD ADVENTURE
    # ==========================================


    def reconstruct_adventure(self, adventure_data):

        # Rebuild the adventure from its original definition
        if adventure_data["title"] == "Tutorial":
            adventure = create_tutorial_adventure()
        else:
            raise ValueError(
                f"Unknown adventure: {adventure_data['title']}"
            )

        # Find the scene where the player last saved
        current_scene = None

        for scene in adventure.get_scenes():
            if scene.name == adventure_data["current_scene"]:
                current_scene = scene
                break

        if current_scene is None:
            raise ValueError(
                f"Unknown scene: {adventure_data['current_scene']}"
            )

        return adventure, current_scene
