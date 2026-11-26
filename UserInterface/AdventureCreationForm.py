class AdventureCreationForm:

    def display (self):
        print("\n================================")
        print("      CREATE AN ADVENTURE")
        print("================================")

        title = input ("Adventure title: ")
        description = input ("Adventure description: ")

        adventure_data = {
            "title": title,
            "description": description
        }

        return adventure_data