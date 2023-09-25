
def pytest_addoption(parser):
    parser.addoption(
        "--blender_path",
        help="path to the executable file blender.exe"
    )
    parser.addoption(
        "--output_path",
        help="folder where test results will be saved."
    )
    parser.addoption(
        "--x_resolution",
        help="the width of the rendered image."
    )
    parser.addoption(
        "--y_resolution",
        help="the height of the rendered image."
    )
