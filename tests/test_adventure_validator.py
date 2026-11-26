
from SubmissionValidation.AdventureValidator import AdventureValidator


def test_valid_adventure():
    validator = AdventureValidator()

    adventure_data = {
        "title": "The Lost Temple",
        "description": "Explore an ancient temple."
    }

    errors = validator.validate_adventure(adventure_data)

    assert errors == []


def test_missing_title():
    validator = AdventureValidator()

    adventure_data = {
        "title": "",
        "description": "Explore an ancient temple."
    }

    errors = validator.validate_adventure(adventure_data)

    assert "Adventure title is required." in errors


def test_missing_description():
    validator = AdventureValidator()

    adventure_data = {
        "title": "The Lost Temple",
        "description": ""
    }

    errors = validator.validate_adventure(adventure_data)

    assert "Adventure description is required." in errors
