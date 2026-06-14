#!/bin/bash
# Create libwebp.so.6 symlink for dlib compatibility on Debian Trixie
ln -sf /usr/lib/x86_64-linux-gnu/libwebp.so.7 /usr/lib/x86_64-linux-gnu/libwebp.so.6 2>/dev/null || true
ln -sf /usr/lib/x86_64-linux-gnu/libpng16.so.16 /usr/lib/x86_64-linux-gnu/libpng16.so.16 2>/dev/null || true
ldconfig 2>/dev/null || true
