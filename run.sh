#!/bin/sh

set -e

verbose="false"

is_verbose() {
	if [ "${verbose}" = "true" ]
	then
		return 0
	else
		return 1
	fi
}

while getopts ":hv" opt
do
	case "${opt}" in
		"v")
			if [ "${verbose}" = "false" ]
			then
				verbose="true"
			else
				verbose="false"
			fi
		;;
		"h")
			echo "Usage of the ${0##*/}:
 -h: Show help, this helpful text.
"
		;;
		\?)
			echo "${0}: unknown option -${OPTARG}"
		;;
	esac
done

shift $((OPTIND - 1))

for par in "${@}"
do
	if [ -d "${par}" ]
	then
	 	is_verbose && echo "running for ${par}"
	 	docker run --rm -it --mount type=bind,src="$(realpath ${par})",dst="/mnt/${par##*/}" -w "/mnt/${par##*/}" "osrf/ros:humble-desktop"
		sudo chown -R "$(id -u)":"$(id -g)" "${par}"
	else
		echo "skipping, given parameter \"${par}\" is not a directory."
	fi
done
