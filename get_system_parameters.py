#!/usr/bin/env python
# coding: utf8


import sys
import platform
import os
import math


def get_python_version():
    """
    Get information about Python version

    :return:
    """

    """A string containing the version number of the Python interpreter plus additional information on the build 
    number and compiler used. This string is displayed when the interactive interpreter is started. Do not extract 
    version information out of it, rather, use version_info and the functions provided by the platform module."""
    version = sys.version

    """A tuple containing the five components of the version number: major, minor, micro, releaselevel, and serial. 
    All values except releaselevel are integers; the release level is 'alpha', 'beta', 'candidate', or 'final'. The 
    version_info value corresponding to the Python version 2.0 is (2, 0, 0, 'final', 0). The components can also be 
    accessed by name, so sys.version_info[0] is equivalent to sys.version_info.major and so on."""
    version_info = sys.version_info

    return version, version_info


def get_platform_info():
    """


    :return:
    """

    """Returns a tuple (bits, linkage) which contain information about the bit architecture and the linkage format 
    used for the executable. Both values are returned as strings."""
    architecture = platform.architecture()

    """Returns the machine type, e.g. 'i386'. An empty string is returned if the value cannot be determined."""
    machine = platform.machine()

    """Returns a single string identifying the underlying platform with as much useful information as possible."""
    platformv = platform.platform()

    """Returns a string identifying the Python implementation SCM branch."""
    python_branch = platform.python_branch()

    """Returns the Python version as tuple (major, minor, patchlevel) of strings."""
    python_version_tuple = platform.python_version_tuple()

    """Get Mac OS version information and return it as tuple (release, versioninfo, machine) with versioninfo being a 
    tuple (version, dev_stage, non_release_version). """
    mac_ver = platform.mac_ver()

    return architecture, machine, platformv, python_branch, python_version_tuple, mac_ver


def get_system_info_py3():
    """
    Get some information about system

    :return:
    """

    """An integer giving the maximum value a variable of type Py_ssize_t can take. It’s usually 2**31 - 1 on a 32-bit 
    platform and 2**63 - 1 on a 64-bit platform. """
    maxsize = sys.maxsize

    intsize = math.log2(maxsize+1)

    return maxsize


def get_sysconf():
    sysconf_names = os.sysconf_names

    sc_phys_pages = os.sysconf('SC_PHYS_PAGES')
    sc_pagesize = os.sysconf('SC_PAGESIZE')

    return sysconf_names, sc_phys_pages, sc_pagesize


def get_ram_size_gb_unix():
    sysconf_names, sc_phys_pages, sc_pagesize = get_sysconf()

    total_ram_bytes = sc_phys_pages * sc_pagesize
    factor_bytes_in_gbytes = 1024 * 1024 * 1024
    total_ram_gbytes = total_ram_bytes / factor_bytes_in_gbytes

    return total_ram_gbytes


def get_maxsize_py3():
    """

    :return:
    """

    """An integer giving the maximum value a variable of type Py_ssize_t can take. It’s usually 2**31 - 1 on a 32-bit 
    platform and 2**63 - 1 on a 64-bit platform. """
    maxsize = sys.maxsize

    return maxsize


def print_python_version():
    print('*** Python Version ***')
    version, version_info = get_python_version()
    print('Version: {0}\nVersion Info: {1}'.format(version, version_info))
    print('\n')

    return True


def print_platform_info():
    print('\n*** Platform Information ***')
    architecture, machine, platformv, python_branch, python_version_tuple, mac_ver = get_platform_info()
    print('Architecture: {0}'.format(architecture))
    print('Platfrom: {0}'.format(platformv))
    print('Machine: {0}'.format(machine))
    print('Python Branch: {0}'.format(python_branch))
    print('Python version tuple: {0}'.format(python_version_tuple))
    print('Mac Ver: {0}'.format(mac_ver))
    print('\n')

    return True


def print_system_info():
    print('\n*** System Information ***')
    maxsize = get_system_info_py3()
    print('Maximum Value of Integer (dec): {0}'.format(maxsize))
    print('Maximum Value of Integer (bin): {0:b}'.format(maxsize))
    print('\n')

    return True


def print_sysconf():
    print('*** Sysconfig ***')
    sysconf_names, sc_phys_pages, sc_pagesize = get_sysconf()
    print('Sysconf Names:')
    for name in sysconf_names:
        print('{0}'.format(name))

    print('SC_PHYS_PAGES = {0}'.format(sc_phys_pages))
    print('SC_PAGESIZE = {0}'.format(sc_pagesize))
    print('\n')

    return True


def print_ram_size_gb():
    print('*** RAM Size ***')
    ram_size_gb = get_ram_size_gb_unix()
    print('RAM Size in gagabyte(s) = {0}'.format(ram_size_gb))
    print('\n')

    return True


if __name__ == '__main__':
    print_python_version()
    print_platform_info()
    print_system_info()
    print_sysconf()
    print_ram_size_gb()