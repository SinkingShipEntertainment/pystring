
# --------------------------------------
# CMake definitions
cmake_minimum_required(VERSION 3.12)

project(pystring VERSION 1.1.3 LANGUAGES CXX C)

# We need to compile with -fPIC (Position Independent Code) so that
# other applications that will link against this one can load this one
# into their .so
# Only libraries that are compiled iwth fPIC can be included into other .so libraries.
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# --------------------------------------
# Build in-tree not allowed
if(${CMAKE_SOURCE_DIR} STREQUAL ${CMAKE_BINARY_DIR})
    message(FATAL_ERROR "In-source build not allowed.")
endif()

# --------------------------------------
# Compile and link library
set(SOURCES
    pystring.cpp
)

set(BUILD_INCLUDES
    ${CMAKE_CURRENT_SOURCE_DIR}
)

add_library(pystring STATIC ${SOURCES})

target_include_directories(pystring
    PUBLIC
        "$<BUILD_INTERFACE:${BUILD_INCLUDES}>"
        "$<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>"
)

set_target_properties(pystring PROPERTIES
    PUBLIC_HEADER ${CMAKE_CURRENT_SOURCE_DIR}/pystring.h
)

include(GNUInstallDirs)
install(TARGETS pystring
    EXPORT ${PROJECT_NAME}_EXPORTED_TARGETS
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/pystring
)
