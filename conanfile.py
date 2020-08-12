#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os

def sort_libs(correct_order, libs, lib_suffix='', reverse_result=False):
    # Add suffix for correct string matching
    correct_order[:] = [s.__add__(lib_suffix) for s in correct_order]

    result = []
    for expectedLib in correct_order:
        for lib in libs:
            if expectedLib == lib:
                result.append(lib)

    if reverse_result:
        # Linking happens in reversed order
        result.reverse()

    return result

class LibnameConan(ConanFile):
    name = "magnum"
    version = "2020.06"
    description =   "Magnum — Lightweight and modular C++11/C++14 \
                    graphics middleware for games and data visualization"
    # topics can get used for searches, GitHub topics, Bintray tags etc. Add here keywords about the library
    topics = ("conan", "corrade", "graphics", "rendering", "3d", "2d", "opengl")
    url = "https://github.com/helmesjo/conan-magnum"
    homepage = "https://magnum.graphics"
    author = "helmesjo <helmesjo@gmail.com>"
    license = "MIT"  # Indicates license type of the packaged library; please use SPDX Identifiers https://spdx.org/licenses/
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    short_paths = True  # Some folders go out of the 260 chars path length scope (windows)

    # Options may need to change depending on the packaged library.
    settings = "os", "arch", "compiler", "build_type"
    options = {
        "shared": [True, False], 
        "fPIC": [True, False],
        "build_deprecated": [True, False],
        "build_multithreaded": [True, False],
        "build_plugins_static": [True, False],
        "target_gl": [True, False],
        "target_gles": [True, False],
        "with_anyaudioimporter": [True, False],
        "with_anyimageconverter": [True, False],
        "with_anyimageimporter": [True, False],
        "with_anysceneimporter": [True, False],
        "with_audio": [True, False],
        "with_debugtools": [True, False],
        "with_distancefieldconverter": [True, False],
        "with_eglcontext": [True, False],
        "with_fontconverter": [True, False],
        "with_glfwapplication": [True, False],
        "with_glxapplication": [True, False],
        "with_glxcontext": [True, False],
        "with_gl_info": [True, False],
        "with_imageconverter": [True, False],
        "with_magnumfont": [True, False],
        "with_magnumfontconverter": [True, False],
        "with_meshtools": [True, False],
        "with_objimporter": [True, False],
        "with_opengltester": [True, False],
        "with_primitives": [True, False],
        "with_scenegraph": [True, False],
        "with_sdl2application": [True, False],
        "with_shaders": [True, False],
        "with_text": [True, False],
        "with_tgaimageconverter": [True, False],
        "with_tgaimporter": [True, False],
        "with_vk": [True, False],
        "with_wavaudioimporter": [True, False],
        "with_windowlesseglapplication": [True, False],
        "with_windowlessglxapplication": [True, False],
        "with_xeglapplication": [True, False],
    }
    default_options = {
        "shared": False, 
        "fPIC": True,
        "build_deprecated": False,
        "build_multithreaded": True,
        "build_plugins_static": False,
        "target_gl": True,
        "target_gles": False,
        "with_anyaudioimporter": False,
        "with_anyimageconverter": False,
        "with_anyimageimporter": False,
        "with_anysceneimporter": False,
        "with_audio": False,
        "with_debugtools": True,
        "with_distancefieldconverter": False,
        "with_eglcontext": False,
        "with_fontconverter": False,
        "with_glfwapplication": False,
        "with_glxapplication": False,
        "with_glxcontext": False,
        "with_gl_info": False,
        "with_imageconverter": False,
        "with_magnumfont": False,
        "with_magnumfontconverter": False,
        "with_meshtools": True,
        "with_objimporter": False,
        "with_opengltester": False,
        "with_primitives": True,
        "with_scenegraph": True,
        "with_sdl2application": True,
        "with_shaders": True,
        "with_text": True,
        "with_tgaimageconverter": False,
        "with_tgaimporter": False,
        "with_vk": False,
        "with_wavaudioimporter": False,
        "with_windowlesseglapplication": False,
        "with_windowlessglxapplication": False,
        "with_xeglapplication": False,
    }

    # Custom attributes for Bincrafters recipe conventions
    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    requires = (
        "corrade/2020.06@helmesjo/stable"
    )

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        # To fix issue with resource management, see here:
        # https://github.com/mosra/magnum/issues/304#issuecomment-451768389
        if self.options.shared:
            self.options['corrade'].shared = True

    def requirements(self):
        if self.options.with_sdl2application:
            self.requires("sdl2/2.0.9@bincrafters/stable")
            # Custom options
            self.options["sdl2"].sdl2main = True
            if self.settings.os == "Linux":
                self.options["sdl2"].x11 = True

        if self.options.with_glfwapplication:
            self.requires("glfw/3.3.2@bincrafters/stable")

    def source(self):
        source_url = "https://github.com/mosra/magnum"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version

        # Rename to "source_subfolder" is a convention to simplify later steps
        os.rename(extracted_dir, self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)

        def add_cmake_option(option, value):
            var_name = "{}".format(option).upper()
            value_str = "{}".format(value)
            var_value = "ON" if value_str == 'True' else "OFF" if value_str == 'False' else value_str 
            cmake.definitions[var_name] = var_value
            print("{0}={1}".format(var_name, var_value))

        for option, value in self.options.items():
            add_cmake_option(option, value)

        add_cmake_option("BUILD_STATIC", not self.options.shared)
        add_cmake_option("BUILD_STATIC_PIC", not self.options.shared and self.options.get_safe("fPIC") == True)

        # Magnum uses suffix on the resulting 'lib'-folder when running cmake.install()
        # Set it explicitly to empty, else Magnum might set it implicitly (eg. to "64")
        add_cmake_option("LIB_SUFFIX", "")

        if self.settings.os == "Windows":
            cmake.definitions["-DNOMINMAX"] = "1"
            #cmake.cpp_defines.append("NOMINMAX") # Windows macros cause issues

        cmake.configure(build_folder=self._build_subfolder)

        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        cmake = self._configure_cmake()
        cmake.install()

        # This didn't work correctly in combination with generator 'cmake_find_package', and don't wanna spend time on it now.
        # Will use the conan-generated find-script instead (which works).
        
        #share_cmake = os.path.join(self.package_folder, "share", "cmake", "Magnum")
        #self.copy("MagnumConfig.cmake", src=share_cmake, dst=os.path.join(self.package_folder, "lib", "cmake", "Magnum"))
        #self.copy("FindMagnum.cmake", src=share_cmake, dst=os.path.join(self.package_folder, "lib", "cmake", "Magnum"))
        #tools.rmdir(os.path.join(self.package_folder, "share"))

    def package_info(self):
        #self.cpp_info.names["cmake_find_package"] = "Magnum"
        #self.cpp_info.names["cmake_find_package_multi"] = "Magnum"

        #self.cpp_info.includedirs.append("include")
        #self.cpp_info.builddirs.append(os.path.join("lib", "cmake", "Magnum"))
        #self.cpp_info.build_modules.append(os.path.join("lib", "cmake", "Magnum", "FindMagnum.cmake"))
        #self.cpp_info.build_modules.append(os.path.join("lib", "cmake", "Magnum", "MagnumConfig.cmake"))

        # See dependency order here: https://doc.magnum.graphics/magnum/custom-buildsystems.html
        allLibs = [
            #1
            "Magnum",
            "MagnumAnimation",
            "MagnumMath",
            #2
            "MagnumAudio",
            "MagnumGL",
            "MagnumSceneGraph",
            "MagnumTrade",
            "MagnumVk",
            #3
            "MagnumMeshTools",
            "MagnumPrimitives",
            "MagnumShaders",
            "MagnumTextureTools",
            "MagnumGlfwApplication",
            "MagnumXEglApplication",
            "MagnumWindowlessEglApplication",
            "MagnumGlxApplication" ,
            "MagnumWindowlessGlxApplication",
            "MagnumSdl2Application",
            "MagnumWindowlessSdl2Application",
            #4
            "MagnumDebugTools",
            "MagnumOpenGLTester",
            "MagnumText",
        ]
        
        # Sort all built libs according to above, and reverse result for correct link order
        suffix = '-d' if self.settings.build_type == "Debug" else ''
        builtLibs = tools.collect_libs(self)
        print("Found libs: ", builtLibs)
        self.cpp_info.libs = sort_libs(correct_order=allLibs, libs=builtLibs, lib_suffix=suffix, reverse_result=True)
        print("Link order: ", self.cpp_info.libs)

        if self.settings.os == "Windows":
            if self.settings.compiler == "Visual Studio":
                if not self.options.shared:
                    self.cpp_info.libs.append("OpenGL32.lib")
            else:
                self.cpp_info.libs.append("opengl32")
        else:
            if self.settings.os == "Macos":
                self.cpp_info.exelinkflags.append("-framework OpenGL")
            elif not self.options.shared:
                self.cpp_info.libs.append("GL")

        if self.options.shared:
            if self.settings.os == "Windows":
                self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))
            if self.settings.os == "Linux":
                self.env_info.LD_LIBRARY_PATH.append(os.path.join(self.package_folder, "lib"))
            if self.settings.os == "Macos":
                self.env_info.DYLD_LIBRARY_PATH.append(os.path.join(self.package_folder, "lib"))