
include_directories(
    ${Boost_INCLUDE_DIRS}
    ${OCC_INCLUDE_DIR}
    ${PYTHON_INCLUDE_DIRS}
    ${ZLIB_INCLUDE_DIR}
    ${XercesC_INCLUDE_DIRS}
)

set(IntraLattice_LIBS
    FreeCADApp
)

SET(IntraLattice_SRCS
    AppIntraLattice.cpp
    PreCompiled.cpp
    PreCompiled.h
)

add_library(IntraLattice SHARED ${IntraLattice_SRCS})
target_link_libraries(IntraLattice ${IntraLattice_LIBS})


fc_target_copy_resource(IntraLattice 
    ${CMAKE_SOURCE_DIR}/src/Mod/IntraLattice
    ${CMAKE_BINARY_DIR}/Mod/IntraLattice
    Init.py)

SET_BIN_DIR(IntraLattice IntraLattice /Mod/IntraLattice)
SET_PYTHON_PREFIX_SUFFIX(IntraLattice)

install(TARGETS IntraLattice DESTINATION ${CMAKE_INSTALL_LIBDIR})
