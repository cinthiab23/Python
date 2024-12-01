import os


# Main function
def main():
    try:
        # create main directory
        os.mkdir('MyFiles')
        print("Directory 'MyFiles created.")

        # Create subdirectories inside MyFiles
        os.mkdir('MyFiles/Docs')
        print("Subdirectory 'Docs' created inside 'MyFiles'. ")

        os.mkdir('MyFiles/Images')
        print("Subdirectory 'Images' created inside 'MyFiles'. ")

        os.mkdir('MyFiles/Videos')
        print("Subdirectory'Videos' created inside 'MyFiles'. ")

    except FileExistsError:
        print("Error: A directory with the same name already exists.")


main()
