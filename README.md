[![Download](https://api.bintray.com/packages/helmesjo/public-conan/corrade%3Ahelmesjo/images/download.svg) ](https://bintray.com/helmesjo/public-conan/corrade%3Ahelmesjo/_latestVersion)
[![Build Status Travis](https://travis-ci.org/helmesjo/conan-corrade.svg?branch=stable%2F2018.10)](https://travis-ci.com/helmesjo/conan-corrade)
[![Build Status AppVeyor](https://ci.appveyor.com/api/projects/status/github/helmesjo/conan-corrade?branch=stable%2F2018.10&svg=true)](https://ci.appveyor.com/project/helmesjo/conan-corrade)

## Conan package recipe for [*corrade*](https://magnum.graphics/corrade)

Corrade is a multiplatform utility library written                     in C++11/C++14. It's used as a base for the Magnum                     graphics engine, among other things.

The packages generated with this **conanfile** can be found on [Bintray](https://bintray.com/helmesjo/public-conan/corrade%3Ahelmesjo).


## Issues

If you wish to report an issue or make a request for a Bincrafters package, please do so here:

[Bincrafters Community Issues](https://github.com/bincrafters/community/issues)


## For Users

### Basic setup

    $ conan install corrade/2018.10@helmesjo/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    corrade/2018.10@helmesjo/stable

    [generators]
    cmake

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.


## Build and package

The following command both runs all the steps of the conan file, and publishes the package to the local system cache.  This includes downloading dependencies from "build_requires" and "requires" , and then running the build() method.

    $ conan create . helmesjo/stable


### Available Options
| Option        | Default | Possible Values  |
| ------------- |:----------------- |:------------:|
| msvc2017_compatibility      | False |  [True, False] |
| build_deprecated      | False |  [True, False] |
| build_tests      | False |  [True, False] |
| with_pluginmanager      | False |  [True, False] |
| gcc47_compatibility      | False |  [True, False] |
| shared      | False |  [True, False] |
| fPIC      | True |  [True, False] |
| with_testsuite      | True |  [True, False] |
| msvc2015_compatibility      | False |  [True, False] |
| with_interconnect      | False |  [True, False] |


## Add Remote

    $ conan remote add helmesjo "https://api.bintray.com/conan/helmesjo/public-conan"


## Conan Recipe License

NOTE: The conan recipe license applies only to the files of this recipe, which can be used to build and package corrade.
It does *not* in any way apply or is related to the actual software being packaged.

[MIT](https://github.com/helmesjo/conan-corrade/blob/stable/2018.10/LICENSE.md)
