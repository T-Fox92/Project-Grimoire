class AdventureValidator:

    def validate_adventure (self, adventure_data):
        errors = []

        if not adventure_data ["title"].strip():
            errors.append ("Adventure title is required.")


        if not adventure_data ["description"].strip():
            errors.append ("Adventure description is required.")

        return errors