cmake_minimum_required(VERSION 2.8.12)
project(cmake_wrapper)

include(conanbuildinfo.cmake)
conan_basic_setup()

add_compile_definitions(WIN32_LEAN_AND_MEAN) 
add_compile_definitions(NOMINMAX) 
add_subdirectory("source_subfolder")
