cmake_minimum_required(VERSION 3.16)

project(csapptest)

if(CMAKE_SIZEOF_VOID_P EQUAL 8)
    enable_language(ASM_MASM)
    add_executable(csapptest main.cpp asm1.asm)
else()
    add_executable(csapptest main.cpp)
endif()