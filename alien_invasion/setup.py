import cx_Freeze

executables = [cx_Freeze.Executable("alien_invasion.py")]

cx_Freeze.setup(
    name="Alien Invasion Clone",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["ship.bmp", "alien.bmp", "alien.py", 
                           "bullet.py", "button.py", "game_functions.py", "game_stats.py", 
                           "scoreboard.py", "settings.py", "ship.py"]}},
    executables = executables

    )