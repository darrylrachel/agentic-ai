# You're creating a notification system for a smart kettle.
# It should remind the user only when the kettle has finished boiling.
# Task:
#   * A varibale kettle_boiled = True
#   * if boiled, show: "Kettle done! Time to make chai!"

kettle_boiled = True

def tea_kettle():
    if kettle_boiled:
        print("Kettle done! Time to make chai!")
    else:
        print("Not ready!")

tea_kettle()