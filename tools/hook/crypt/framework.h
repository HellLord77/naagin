#pragma once

#define WIN32_LEAN_AND_MEAN // Exclude rarely-used stuff from Windows headers
// Windows Header Files
#include <windows.h>
#include <wincrypt.h>

#include <detours/detours.h>

#pragma comment(lib, "crypt32.lib")
