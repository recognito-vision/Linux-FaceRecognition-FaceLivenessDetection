cmake_minimum_required(VERSION 3.5)

project(facesdklite LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(OpenCV REQUIRED)


add_library(libengine_1 SHARED IMPORTED)
set_target_properties(libengine_1 PROPERTIES IMPORTED_LOCATION ${CMAKE_SOURCE_DIR}/../engine/libengine_1.so)

add_library(libengine_2 SHARED IMPORTED)
set_target_properties(libengine_2 PROPERTIES IMPORTED_LOCATION ${CMAKE_SOURCE_DIR}/../engine/libengine_2.so)

add_library(libengine_3 SHARED IMPORTED)
set_target_properties(libengine_3 PROPERTIES IMPORTED_LOCATION ${CMAKE_SOURCE_DIR}/../engine/libengine_3.so)

add_library(libengine SHARED IMPORTED)
set_target_properties(libengine PROPERTIES IMPORTED_LOCATION ${CMAKE_SOURCE_DIR}/../engine/libengine.so)

add_executable(facesdklite main.cpp
    )

target_include_directories(facesdklite
    PUBLIC ${PROJECT_SOURCE_DIR}
    PUBLIC ${OpenCV_INCLUDE_DIRS}
)


target_link_libraries(facesdklite
    ${OpenCV_LIBS}
    libengine_1
    libengine_2
    libengine_3
    libengine
)
