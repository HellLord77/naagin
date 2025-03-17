#include <wininet.h>

#include "common.h"

#define INTERNETCRACKURLW

FAKE(BOOL, WINAPI, InternetCrackUrlW, LPCWSTR lpszUrl, DWORD dwUrlLength, DWORD dwFlags, LPURL_COMPONENTSW lpUrlComponents)
{
    return CrackUrl_fake(InternetCrackUrlW_real, lpszUrl, dwUrlLength, dwFlags, lpUrlComponents);
}
