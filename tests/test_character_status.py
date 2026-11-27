
from CharacterManagement.Character import Character
from CharacterManagement.ProgressionManager import ProgressionManager
from UserInterface.CharacterStatus import CharacterStatus


class TestJob:
    name = "Test Job"

    def get_starting_abilities(self):
        return []


def test_character_status_display(capsys):
    character = Character("Aria", TestJob())
    manager = ProgressionManager()
    status = CharacterStatus()

    status.display(character, manager)

    output = capsys.readouterr().out

    assert "Aria" in output
    assert "Level: 1" in output
    assert "Health: 100/100" in output
    assert "Total Experience: 0" in output
    assert "Experience Remaining: 100" in output
    assert "Strength: 3" in output
