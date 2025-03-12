#include <windows.h>
#include <winhttp.h>

#include "hook_macro.h"

#define WINHTTPGETIEPROXYCONFIGFORCURRENTUSER

FAKE(BOOL, WINAPI, WinHttpGetIEProxyConfigForCurrentUser, WINHTTP_CURRENT_USER_IE_PROXY_CONFIG *pProxyConfig)
{
    if (!pProxyConfig) {
        SetLastError(ERROR_INVALID_PARAMETER);
        return FALSE;
    }

    LPCWSTR proxy = L"http://localhost:8080";
    SIZE_T len = wcslen(proxy) + 1;
    pProxyConfig->lpszProxy = (LPWSTR)GlobalAlloc(GPTR, len * sizeof(WCHAR));
    wcscpy_s(pProxyConfig->lpszProxy, len, proxy);
    return TRUE;
}
