#!/data/data/com.termux/files/usr/bin/python3
# ROG 3 Game Mode Activator - For ASUS ROG Phone 3
import os
import time

print("=== ROG 3 GAME MODE ACTIVATOR ===")
print("Sun Tzu: 'Speed is the essence of war. FPS is the essence of gaming.'")

def enable_game_mode():
    print("\n[1] Killing background apps...")
    os.system("am kill-all")
    time.sleep(1)

    print("[2] Setting CPU governor to performance...")
    os.system("echo performance > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor")

    print("[3] Clearing RAM cache...")
    os.system("sync; echo 3 > /proc/sys/vm/drop_caches")

    print("[4] Disabling thermal throttling...")
    os.system("setprop debug.thermal.throttling 0")

    print("\n✅ GAME MODE ACTIVE - ROG 3 UNLEASHED")
    print("ROG 3 Fund: 95% ACHIEVED")

if __name__ == "__main__":
    enable_game_mode()

