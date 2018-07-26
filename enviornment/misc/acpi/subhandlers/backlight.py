#!/usr/bin/python2

import sys
import os

import argparse

BL_SYSFS_BASE="/sys/class/backlight/intel_backlight/"


def get_max_brightness():
    b = open(os.path.join(BL_SYSFS_BASE, "max_brightness")).read().strip()
    return int(b)


def get_current_brightness():
    b = open(os.path.join(BL_SYSFS_BASE, "actual_brightness")).read().strip()
    return int(b)


def get_new_brightness(max_bl, current_bl, diff_percent):
    # print("current_bl: %d" % current_bl)
    # print("max_bl: %d" % max_bl)
    # print("diff: %d" % diff_percent)
    diff_bl = max_bl * (diff_percent/100.0)
    # print("diff bl: %d" % diff_bl)
    new_bl = current_bl + diff_bl
    print("new bl: %d" % new_bl)
    if new_bl <= 0:
        return 1
    elif new_bl > max_bl:
        return max_bl
    else:
        return new_bl


def write_new_brightness(bl):
    b = open(os.path.join(BL_SYSFS_BASE, "brightness"), "w")
    b.write("%d" % bl)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-down", dest="down", type=int)
    parser.add_argument("-up", dest="up", type=int)
    args = parser.parse_args()

    new_bl = get_current_brightness()
    max_bl = get_max_brightness()

    if args.down:
        new_bl = get_new_brightness(max_bl, new_bl, args.down * -1)
    elif args.up:
        new_bl = get_new_brightness(max_bl, new_bl, args.up)

    write_new_brightness(new_bl)

if __name__ == "__main__":
    sys.exit(main())
