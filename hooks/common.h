#pragma once

#include <windows.h>
#include <wchar.h>

#include "hook_macro.h"

#undef LoadLibrary
HMODULE LoadLibrary(LPCSTR lpLibFileName)
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

#define SCHEME INTERNET_SCHEME_HTTP
#define HOST_NAME L"localhost"
#define HOST_NAME_LENGTH 9
#define PORT 8000

typedef BOOL(WINAPI *CrackUrl_ptr)(LPCWSTR, DWORD, DWORD, LPURL_COMPONENTSW);

BOOL CrackUrl_fake(CrackUrl_ptr crackUrl_real, LPCWSTR url, DWORD urlLength, DWORD flags, LPURL_COMPONENTSW urlComponents)
{
    if (urlComponents->dwHostNameLength <= HOST_NAME_LENGTH)
    {
        return FALSE;
    }

    if (!urlComponents->dwUrlPathLength)
    {
        return FALSE;
    }
    DWORD urlPathLength = urlComponents->dwUrlPathLength;

    if (crackUrl_real(url, urlLength, flags, urlComponents))
    {
        LPWSTR hostName;
        DWORD hostNameLength;

        if (urlComponents->dwHostNameLength == 14 && !wmemcmp(urlComponents->lpszHostName, L"api.doaxvv.com", 14))
        {
            hostName = L"/api";
            hostNameLength = 4;
        }
        else if (urlComponents->dwHostNameLength == 15 && !wmemcmp(urlComponents->lpszHostName, L"game.doaxvv.com", 15))
        {
            hostName = L"/game";
            hostNameLength = 5;
        }
        else if (urlComponents->dwHostNameLength == 16 && !wmemcmp(urlComponents->lpszHostName, L"api01.doaxvv.com", 16))
        {
            hostName = L"/api01";
            hostNameLength = 6;
        }
        else
        {
            return FALSE;
        }

        urlComponents->nScheme = INTERNET_SCHEME_HTTP;
        urlComponents->lpszHostName = HOST_NAME;
        urlComponents->dwHostNameLength = HOST_NAME_LENGTH;
        urlComponents->nPort = 8000;

        if (wmemmove_s(urlComponents->lpszUrlPath + hostNameLength, urlPathLength - hostNameLength, urlComponents->lpszUrlPath, urlComponents->dwUrlPathLength + 1))
        {
            return FALSE;
        }
        if (wmemcpy_s(urlComponents->lpszUrlPath, urlPathLength, hostName, hostNameLength))
        {
            return FALSE;
        }
        urlComponents->dwUrlPathLength += hostNameLength;

        return TRUE;
    }

    return FALSE;
}
