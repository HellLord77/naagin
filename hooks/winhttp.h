#include <winhttp.h>

#include "utils.h"

#define WINHTTPCRACKURL

FAKE(BOOL, WINAPI, WinHttpCrackUrl, LPCWSTR pwszUrl, DWORD dwUrlLength, DWORD dwFlags, LPURL_COMPONENTS lpUrlComponents)
{
    return CrackUrl_fake(WinHttpCrackUrl_real, pwszUrl, dwUrlLength, dwFlags, lpUrlComponents);
}
