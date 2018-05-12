#!/bin/bash
# Default acpi script that takes an entry for all actions

case "$1" in
    button/lid)
    	logger 'ButtonLid pressed'
        case "$3" in
            close)
                logger 'ButtonLid closed'
                ;;
            open)
                logger 'ButtonLid open'
                ;;
            *)
                logger "ButtonLid action undefined: $2"
                ;;
        esac
	;;
    button/mute)
    	logger 'ButtonMute pressed'
	sudo -u hjz env XDG_RUNTIME_DIR=/run/user/1000 amixer -D pulse sset 'Master' toggle
	;;
    button/volumedown)
    	logger 'ButtonVolumedown pressed'
	sudo -u hjz env XDG_RUNTIME_DIR=/run/user/1000 amixer -D pulse sset 'Master' unmute
	sudo -u hjz env XDG_RUNTIME_DIR=/run/user/1000 amixer -D pulse sset 'Master' 4%-
	;;
    button/volumeup)
    	logger 'ButtonVolumeup pressed'
	sudo -u hjz env XDG_RUNTIME_DIR=/run/user/1000 amixer -D pulse sset 'Master' unmute
	sudo -u hjz env XDG_RUNTIME_DIR=/run/user/1000 amixer -D pulse sset 'Master' 4%+
	;;
    video/brightnessdown)
    	logger 'VideoBrightnessdown pressed'
	/etc/acpi/subhandlers/backlight.py -down 5
	;;
    video/brightnessup)
    	logger 'VideoBrightnessup pressed'
	/etc/acpi/subhandlers/backlight.py -up 5
	;;
    video/switchmode)
    	logger 'VideoSwitchmode pressed'
	;;
    button/wlan)
    	logger 'ButtonWlan pressed'
	;;
    button/power)
        case "$2" in
            PBTN|PWRF)
                logger 'PowerButton pressed'
                ;;
            *)
                logger "ACPI action undefined: $2"
                ;;
        esac
        ;;
    button/sleep)
        case "$2" in
            SLPB|SBTN)
                logger 'SleepButton pressed'
                ;;
            *)
                logger "ACPI action undefined: $2"
                ;;
        esac
        ;;
    ac_adapter)
        case "$2" in
            AC|ACAD|ADP0)
                case "$4" in
                    00000000)
                        logger 'AC unpluged'
                        ;;
                    00000001)
                        logger 'AC pluged'
                        ;;
                esac
                ;;
            *)
                logger "ACPI action undefined: $2"
                ;;
        esac
        ;;
    battery)
        case "$2" in
            BAT0)
                case "$4" in
                    00000000)
                        logger 'Battery online'
                        ;;
                    00000001)
                        logger 'Battery offline'
                        ;;
                esac
                ;;
            CPU0)
                ;;
            *)  logger "ACPI action undefined: $2" ;;
        esac
        ;;
    button/lid)
        case "$3" in
            close)
                logger 'LID closed'
                ;;
            open)
                logger 'LID opened'
                ;;
            *)
                logger "ACPI action undefined: $3"
                ;;
    esac
    ;;
    *)
        logger "ACPI group/action undefined: $1 / $2"
        ;;
esac

# vim:set ts=4 sw=4 ft=sh et:
