cmake_minimum_required(VERSION 3.10)
project(TudorPianoAI)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Include directories for your project
include_directories(include)
include_directories(3rd-party/midifile/include)

# Find source files
file(GLOB SOURCES "src/*.cpp", "3rd-party/midifile/src/*.cpp")

# Add the executable based on the source files
add_executable(${PROJECT_NAME} ${SOURCES})

# Link against the external library
# Assuming the library is a static library named libmidifile.a
target_link_libraries(${PROJECT_NAME} "${CMAKE_SOURCE_DIR}/3rd-party/midifile/lib/libmidifile.a")
