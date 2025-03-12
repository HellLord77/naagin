#include <windows.h>
#include <winhttp.h>

#include "hook_macro.h"

#define WINHTTPGETIEPROXYCONFIGFORCURRENTUSER

FAKE(BOOL, WINAPI, WinHttpGetIEProxyConfigForCurrentUser, WINHTTP_CURRENT_USER_IE_PROXY_CONFIG *pProxyConfig)
{
    if (!pProxyConfig)
    {
        SetLastError(ERROR_INVALID_PARAMETER);
        return FALSE;
    }

    LPCWSTR proxy = L"http://localhost:8080";
    SIZE_T len = wcslen(proxy) + 1;
    pProxyConfig->lpszProxy = (LPWSTR)GlobalAlloc(GMEM_FIXED, len * sizeof(WCHAR));
    if (!pProxyConfig->lpszProxy)
    {
        return FALSE;
    }

    wcscpy_s(pProxyConfig->lpszProxy, len, proxy);
    SetLastError(ERROR_SUCCESS);
    return TRUE;
}

#undef LoadLibrary
#define LoadLibrary(lpLibFileName) \
    ([]() -> HMODULE { \
        CHAR lpBuffer[MAX_PATH]; \
        if (!GetSystemDirectory(lpBuffer, MAX_PATH)) { \
            return NULL; \
        } \
        \
        CHAR lpLibFilePath[MAX_PATH]; \
        sprintf_s(lpLibFilePath, MAX_PATH, "%s\\%s", lpBuffer, lpLibFileName + 5); \
        return LoadLibraryA(lpLibFilePath); \
    })()
