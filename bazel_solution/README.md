## Bazel

Example about how create a listener and writer ROS node with CPP or with Python using bazel

To create this tutorial I cloned this: https://github.com/nicolov/ros-bazel \
Then I removed all unecessary parts in order to have the simplest possible project that create and run a rostopic listener and writer using only bazel

### Commands
Run these commands inside bazel_solution folder
* **bazel run //build:listener** to build the listener ros node
* **bazel run //src:listener** to build and run the listener ros node
* **bazel run //build:writer** to build the writer ros node
* **bazel run //src:writer** to build and run the writer ros node
