cmake_minimum_required(VERSION 3.11)
project(delphi)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_CURRENT_SOURCE_DIR}/cmake")
set(Boost_NO_BOOST_CMAKE ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)
set(CMAKE_CXX_FLAGS
    "${CMAKE_CXX_FLAGS} -fvisibility=hidden -fvisibility-inlines-hidden")

find_package(Graphviz)

include_directories(${GRAPHVIZ_INCLUDE_DIRS})
# Add and link pybind11 modules
find_package(Boost COMPONENTS graph REQUIRED)
include_directories(lib)
include_directories(external)
include_directories(${Boost_INCLUDE_DIR})

find_package(range-v3 REQUIRED)
find_package(Eigen3 REQUIRED NO_MODULE)
find_package(fmt REQUIRED)
find_package(nlohmann_json REQUIRED)
find_package(pybind11 CONFIG REQUIRED)
message(STATUS "Found pybind11 v${pybind11_VERSION}: ${pybind11_INCLUDE_DIRS}")


find_package(Python3 REQUIRED)

set(PYBIND11_PYTHON_VERSION "${PYTHON_VERSION_MAJOR}.${PYTHON_VERSION_MINOR}")
set(PYBIND11_CPP_STANDARD -std=c++17)

file(GLOB SRC_FILES ${PROJECT_SOURCE_DIR}/lib/*.cpp)
find_package(SQLite3 REQUIRED)

add_library(Delphi
  lib/AnalysisGraph.hpp
  lib/construct_beta_pdfs.cpp
  lib/to_json.cpp
  lib/data.cpp
  lib/data.hpp
  lib/DiGraph.hpp
  lib/graphviz_interface.cpp
  lib/graphviz_interface.hpp
  lib/graphviz.cpp
  lib/kde.cpp
  lib/kde.hpp
  lib/random_variables.cpp
  lib/random_variables.hpp
  lib/rng.cpp
  lib/rng.hpp
  lib/train_model.cpp
  lib/tran_mat_cell.hpp
  lib/tran_mat_cell.cpp
  lib/utils.cpp
  lib/utils.hpp
  lib/Node.hpp
  lib/Edge.hpp
  lib/Indicator.hpp
  lib/Indicator.cpp
  lib/subgraphs.cpp
  lib/constructors.cpp
  lib/causemos_integration.cpp
  lib/sampling.cpp
  lib/inference.cpp
  lib/synthetic_data.cpp
  lib/graph_building.cpp
  lib/graph_modification.cpp
  lib/graph_utils.cpp
  lib/printing.cpp
  lib/indicator_manipulation.cpp
)

target_link_libraries(Delphi
                      PRIVATE ${Boost_LIBRARIES}
                              fmt::fmt
                              SQLite::SQLite3
                              nlohmann_json::nlohmann_json
                              Eigen3::Eigen
                              ${GRAPHVIZ_LIBS})
target_link_libraries(Delphi INTERFACE range-v3)

pybind11_add_module(DelphiPython MODULE lib/DelphiPython.cpp)
target_link_libraries(DelphiPython PRIVATE Delphi Eigen3::Eigen)
