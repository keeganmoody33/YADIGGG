# yadiggg Sonic ID prototype build.

CC ?= gcc
CFLAGS ?= -O2
CFLAGS += -Wall -Wextra -std=c99
CPPFLAGS += -I.
LDFLAGS ?=
LDLIBS ?=
TARGET = yadiggg_capture
MOCK_CAPTURE ?= 0

# MOCK_CAPTURE exercises the synthetic-input path without claiming audio hardware support.
UNAME_S := $(shell uname -s)

ifeq ($(MOCK_CAPTURE),1)
    CPPFLAGS += -D__APPLE__
    LDLIBS += -lsqlite3 -lm
    printf_arch = synthetic-input prototype (no ALSA hardware)
else ifeq ($(UNAME_S), Darwin)
    CPPFLAGS += -D__APPLE__
    LDLIBS += -lsqlite3 -lm
    printf_arch = Darwin synthetic-input prototype
else
    LDLIBS += -lasound -lsqlite3 -lm -lpthread
    printf_arch = Linux ALSA prototype (compiler/target selected by CC)
endif

SRCS = olaf.c yadiggg_capture.c
OBJS = $(SRCS:.c=.o)

all: info $(TARGET)

info:
	@echo "=================================================="
	@echo "🛠️  yadiggg Build Automation System"
	@echo "📌  $(printf_arch)"
	@echo "=================================================="

$(TARGET): $(OBJS)
	$(CC) $(LDFLAGS) -o $@ $(OBJS) $(LDLIBS)
	@echo "Prototype executable generated: ./$@"

%.o: %.c
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS) $(TARGET)
	@echo "Clean complete."

.PHONY: all clean info
