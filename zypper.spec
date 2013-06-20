%define beta %{nil}
%define scmrev 20130619

Name: zypper
Version: 1.9.1
%if "%{beta}" == ""
%if "%{scmrev}" == ""
Release: 1
Source0: %{name}-%{version}.tar.bz2
%else
Release: 0.%{scmrev}.1
Source0: %{name}-%{scmrev}.tar.xz
%endif
%else
%if "%{scmrev}" == ""
Release: 0.%{beta}.1
Source0: %{name}-%{version}%{beta}.tar.bz2
%else
Release: 0.%{beta}.0.%{scmrev}.1
Source0: %{name}-%{scmrev}.tar.xz
%endif
%endif
Patch0: zypper-1.9.1-compile.patch
Summary: Command line package manager
URL: http://en.opensuse.org/Zypper
# Git at https://github.com/openSUSE/zypper
License: GPLv2+ with special permission to link to OpenSSL
Group: System/Configuration/Packaging
BuildRequires: cmake
BuildRequires: solv-devel zypp-devel

%description
Zypper is a command line package manager, which makes use of libzypp,
providing functions like repository access, dependency solving,
package installation, etc.

YaST2 and RPM MetaData package repositories are supported.
Zypper repositories are similar to the ones used in YaST, which
also makes use of libzypp. Zypper can also handle repository
extensions like patches, patterns and products. 

%prep
%if "%{scmrev}" == ""
%setup -q -n %{name}-%{version}%{beta}
%else
%setup -q -n %{name}
%endif
%apply_patches
%cmake

%build
cd build
%make

%install
cd build
%makeinstall_std
cd ..
mv %buildroot%_docdir/packages/zypper %buildroot%_docdir/%name-%version
%find_lang %name

%files -f %name.lang
%{_sysconfdir}/bash_completion.d/zypper.sh
%config %{_sysconfdir}/logrotate.d/zypp-refresh.lr
%config %{_sysconfdir}/logrotate.d/zypper.lr
%config %{_sysconfdir}/zypp/zypper.conf
%{_bindir}/aptitude
%{_bindir}/installation_sources
%{_bindir}/zypper
%{_sbindir}/zypp-refresh
%{_sbindir}/zypper-log
%doc %{_docdir}/%{name}-%{version}
%{_datadir}/man/man8/*
%{_datadir}/zypper
