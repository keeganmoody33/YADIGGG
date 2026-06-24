# yadiggg: Sonic ID Capture and OLAF Matching Pipeline Makefile
# Date: Friday, June 5, 2026
# Status: Cross-Platform Build Automation V1.0

CC = gcc
CFLAGS = -O3 -Wall -Wextra -ffast-math -std=c99 -I.
TARGET = yadiggg_capture

# Detect operating system
UNAME_S := $(shell uname -s)
UNAME_M := $(shell uname -m)

# Conditional library and optimization flags based on Host Architecture
ifeq ($(UNAME_S), Darwin)
    # macOS Compilation (Emulated sandbox development mode)
    LIBS = -lsqlite3 -lm
    CFLAGS += -D__APPLE__
    printf_arch = Host OS: macOS ($(UNAME_M)) -> Compiling Emulated Sandbox
else
    # Embedded Yocto Linux or standard Linux PC Target
    LIBS = -lasound -lsqlite3 -lm -lpthread
    printf_arch = Host OS: Linux ($(UNAME_M)) -> Compiling Native ALSA Capture
    
    # Enable NEON Vectorization optimizations if compiling on ARM (Cortex-A53)
    ifneq ($(filter arm% aarch64, $(UNAME_M)),)
        CFLAGS += -march=armv8-a -mtune=cortex-a53 -mfpu=neon-fp-armv8 -mfloat-abi=hard
    endif
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
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS) $(LIBS)
	@echo "🎉 Compilation complete! Executable generated: ./$(TARGET)"

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS) $(TARGET)
	@echo "🧹 Clean complete. Directory cleared."

.PHONY: all clean info
