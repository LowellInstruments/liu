#!/usr/bin/bash
echo; echo; echo


# -----------------------------------------------------------------------
# this script automatically installs lowell-mat without its dependencies
# call as:
# curl https://raw.githubusercontent.com/LowellInstruments/lowell-mat/v4/settings/installer_lowell_mat.sh
# -----------------------------------------------------------------------


printf '> CURL installer for Lowell Instruments MAT library\n'
printf '> Cloning repository lowell-mat'
git clone https://github.com/lowellinstruments/lowell-mat.git -b v4
rv=$?
if [ "$rv" -ne 0 ]; then
    printf 'error cloning lowell-mat github repository'
    exit 1
fi


printf '> Installing lowell-mat in empty-dependencies mode'
cd lowell-mat && export MY_IGNORE_REQUIREMENTS_TXT=1 && pip install . -v
