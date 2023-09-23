# BlenderTester23
## What is it?
This project is done as part of my test automation abilities check.

It is a tester app that can automatically test scripts utilizing Blender Python API.

It comes as a convenient CLI tool (utilizes [Typer](https://typer.tiangolo.com/)), that can test any scenarios put into `scenarios` subdirectory.

To launch it, simply run the following:
```
python tests_runner.py BLENDER_PATH OUTPUT_PATH X_RESOLUTION Y_RESOLUTION
```
where:
* BLENDER_PATH is path to blender executable (3.X series versions)
* OUTPUT_PATH -- path to a directory, where you want to see the output
* X_RESOLUTION, Y_RESOLUTION -- resolution of images rendered

There is also an optional argument `--create-dir (=False by default)` - when it is `True`, `tests_runner` creates a subdirectory `run_YYYY-MM-DD_hh-mm-ss` in your chosen `OUTPUT_PATH`, in case you want to run the same tests multiple times and not get the results overwritten.

## How to install and use it
Prerequisites: Have Blender of version 3.3 or newer installed
1. Clone this repo.
1. Create local environment and install dependencies from `requirements.txt`
1. Put your scenarios in subdirectories of `scenarios` and name the main module `scenario.py`. Subdirectories' names will be used as scenario names and used in the output and logs
1. Run `python tests_runner.py BLENDER_PATH OUTPUT_PATH X_RESOLUTION Y_RESOLUTION`
1. `tests_runner` will find all the scenarios and will test them, outputting an `image.png` of given resolution, `render.log` and some additional info in `report.json`
1. Now check your OUTPUT_PATH
