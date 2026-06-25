#!/data/data/com.termux/files/usr/bin/python3
# Redmi 13C Game Mode - For Helio G85
import os
import time

print("=== REDMI 13C GAME MODE ===")
print("Sun Tzu: 'Do not use a cannon to kill a mosquito. Use what fits.'")

def enable_13c_mode():
    print("\n[1] Killing background apps...")
    os.system("am kill-all") # This works on any Android

    print("[2] Clearing RAM cache...")
    os.system("sync; echo 3 > /proc/sys/vm/drop_caches") # Needs root

    print("[3] Setting MIUI to Performance mode...")
    os.system("settings put system speed_mode 1") # MIUI specific
    print("[4] Disabling animations...")
    os.system("settings put global window_animation_scale 0")
    os.system("settings put global transition_animation_scale 0")
    os.system("settings put global animator_duration_scale 0")

    print("\n✅ 13C GAME MODE ACTIVE")
    print("Expected: More stable 30-40 FPS. Don't expect 60.")
    print("13C Fund: 80% ACHIEVED")

if __name__ == "__main__":
    enable_13c_mode()
