#!/usr/bin/bash
echo; echo; echo


# -----------------------------------------------------------------------
# call as:
# curl https://raw.githubusercontent.com/LowellInstruments/liu/master/settings/installer_liu.sh
# -----------------------------------------------------------------------


printf '> CURL installer for Lowell Instruments Utils library\n'
printf '> Cloning repository liu'
git clone https://github.com/lowellinstruments/liu.git
rv=$?
if [ "$rv" -ne 0 ]; then
    printf 'error cloning liu github repository'
    exit 1
fi


printf '> Installing liu'
cd liu && pip install . -v
rv=$?
if [ "$rv" -ne 0 ]; then
    printf 'error installing liu'
    exit 1
fi
