# - Top level CMake script for getting_started tutorials

#-----------------------------------------------------------------------
# Copyright (C) 2023 Guillaume Oliviero <oliviero@lp2ib.in2p3.fr>
#
#
# get_started/cpp_tutorial is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# get_started/cpp_tutorial is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with get_started/cpp_tutorial.  If not, see <http://www.gnu.org/licenses/>.
#-----------------------------------------------------------------------
message (STATUS "[info] Begin of 'CMakeLists.txt'.")

#-----------------------------------------------------------------------
# Enforce an out-of-source build.
#
if(${CMAKE_SOURCE_DIR} STREQUAL ${CMAKE_BINARY_DIR})
  message(STATUS "cpp_tutorial requires an out-of-source build.")
  message(STATUS "Please remove these files from ${CMAKE_BINARY_DIR} first:")
  message(STATUS "  CMakeCache.txt")
  message(STATUS "  CMakeFiles")
  message(STATUS "Once these files are removed, create a separate directory")
  message(STATUS "and run CMake from there, pointing it to:")
  message(STATUS "  ${CMAKE_SOURCE_DIR}")
  message(FATAL_ERROR "in-source build detected")
endif()

#-----------------------------------------------------------------------
# CMake/project requirements and configuration
#
cmake_minimum_required(VERSION 3.1 FATAL_ERROR)
project(cpp_tutorial VERSION 0.1.0)

# Includes



# Sources




# #-----------------------------------------------------------------------
# # Build the subdirectories as required
# #
# message(STATUS "[info] Adding subdirectory 'cpp_tutorial'...")
# add_subdirectory(cpp_tutorial)
