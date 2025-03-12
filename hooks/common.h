#pragma once

#include <windows.h>

#include "hook_macro.h"

#undef LoadLibrary
inline HMODULE LoadLibrary(LPCSTR lpLibFileName)
{
    CHAR lpBuffer[MAX_PATH];
    if (!GetSystemDirectoryA(lpBuffer, MAX_PATH))
    {
        return NULL;
    }

    CHAR lpLibFilePath[MAX_PATH];
    sprintf_s(lpLibFilePath, MAX_PATH, "%s\\%s", lpBuffer, lpLibFileName + 5);
    return LoadLibraryA(lpLibFilePath);
}
