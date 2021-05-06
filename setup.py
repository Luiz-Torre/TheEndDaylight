import cx_Freeze
executables = [cx_Freeze.Executable("main.py")]
cx_Freeze.setup(
    name="The End Daylight",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": [
                                "./images/.",
                                "./sounds/.",
                                "./PPlay/.",
                                "Computer_says_no.ttf"
                           ]}},
    executables=executables
)