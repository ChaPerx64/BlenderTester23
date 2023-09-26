# BlenderTester23
## What is it?

This project is done as part of my test automation abilities check.

It is a tester app that can automatically test scripts put into `scenarios` subdirectory utilizing [Blender Python API](https://docs.blender.org/api/current/index.html#) and [Pytest](https://pytest.org/).

## How to run it?

To launch it, run the following:
```
pytest --x_resolution [value] --y_resolution [value] --blender_path [value] --output_path [value] 
```
where:
* `x_resolution`, `y_resolution` -- resolution of images rendered, in px, int
* `blender_path` -- path to blender executable (3.X series versions)
* `output_path` -- path to a directory, where you want to see the output

## How to install and use it
Prerequisites: Have Blender of version 3.3 or newer installed
1. Clone this repo.
1. Create local environment and install dependencies from `requirements.txt`
1. Put your scenarios in subdirectories of `scenarios` and name the main module `scenario.py`. Subdirectories' names will be used as scenario names and used in the output and logs.
    - Note: scenarios should only describe a scene (geometry, materials, environment, lighting etc.) and not contain render commands or settings like `bpy.ops.render.render()`. Any render setting might get overwritten.
1. Run the `pytest` command as [described above](#how-to-run-it)
1. Now check your `output_path`

## How does it work?

Basic scructure is this:
- All essential functions are located in `runner` directory
- Default CLI logging is configured in `pytest.ini`
- All session-scope fixtures are located in `conftest.py`
- The only test function `test_shapecreation` and `testwrapper` fixture it requires are located in `test_blender.py`
    - `testwrapper` is responsible for:
        - collecting the parameters needed to perform a Blender run
        - saving results of each test run
    - `testwrapper` is parametrized with parameters returned by `runner.finder.findscenarios` function, which looks for `.py` files in `scenarios` directory
    - `testwrapper` also requires these following fixtures:
        - `request` - Pytest built-it fixture
        - `sysinfo` - fixture that collects system info
            - System info is collected by `runner.sysinfo.get_sysinfo` utilizing `cpuinfo` and `platform` libraries.
        - `input_args` - fixture that parses arguments with which `pytest` was called
    - `test_shapecreation` asserts three following statements:
        - Blender subprocess return code is 0
        - Blender subprocess STDOUT is not empty
        - Blender subprocess STDOUT contains `Saved: ` string, indicating that the rendered image was, most likely, saved

## Jenkins pipeline

This project is supplied with `Jenkinsfile`, which contains pipeline description in Groovy language.

As long as your agent runs in an environment with blender installed and able to execute Blender renders headlessly, It should work.

For the purposes of testing this pipeline I created [JenkinsBlenderTester](https://github.com/ChaPerx64/JenkinsBlenderTester).