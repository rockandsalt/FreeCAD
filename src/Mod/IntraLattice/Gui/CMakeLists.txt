
include_directories(
    ${CMAKE_SOURCE_DIR}/src
    ${CMAKE_CURRENT_BINARY_DIR}
    ${Boost_INCLUDE_DIRS}
    ${COIN3D_INCLUDE_DIRS}
    ${ZLIB_INCLUDE_DIR}
    ${PYTHON_INCLUDE_DIRS}
    ${XercesC_INCLUDE_DIRS}
)

set(IntraLatticeGui_LIBS
    IntraLattice
    FreeCADGui
)

if (BUILD_QT5)
    qt5_add_resources(IntraLattice_QRC_SRCS Resources/IntraLattice.qrc)
else()
    qt4_add_resources(IntraLattice_QRC_SRCS Resources/IntraLattice.qrc)
endif()

SET(IntraLatticeGui_SRCS
    ${IntraLattice_QRC_SRCS}
    AppIntraLatticeGui.cpp
    Command.cpp
    PreCompiled.cpp
    PreCompiled.h
    Workbench.cpp
    Workbench.h
)

add_library(IntraLatticeGui SHARED ${IntraLatticeGui_SRCS})
target_link_libraries(IntraLatticeGui ${IntraLatticeGui_LIBS})

fc_target_copy_resource(IntraLatticeGui 
    ${CMAKE_SOURCE_DIR}/src/Mod/IntraLattice
    ${CMAKE_BINARY_DIR}/Mod/IntraLattice
    InitGui.py)

SET_BIN_DIR(IntraLatticeGui IntraLatticeGui /Mod/IntraLattice)
SET_PYTHON_PREFIX_SUFFIX(IntraLatticeGui)
    
install(TARGETS IntraLatticeGui DESTINATION ${CMAKE_INSTALL_LIBDIR})
