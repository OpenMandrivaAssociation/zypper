%define beta %{nil}
%define scmrev %{nil}

Summary:	Command line package manager
Name:		zypper
Version:	1.14.50
%if "%{beta}" == ""
%if "%{scmrev}" == ""
Release:	1
Source0:	https://github.com/openSUSE/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%else
Release:	1.%{scmrev}.1
Source0:	%{name}-%{scmrev}.tar.xz
%endif
%else
%if "%{scmrev}" == ""
Release:	0.%{beta}.1
Source0:	%{name}-%{version}%{beta}.tar.bz2
%else
Release:	0.%{beta}.1.%{scmrev}.1
Source0:	%{name}-%{scmrev}.tar.xz
%endif
%endif
URL:		http://en.opensuse.org/Zypper
# Git at https://github.com/openSUSE/zypper
License:	GPLv2+ with special permission to link to OpenSSL
Group:		System/Configuration/Packaging
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	pkgconfig(libsolv)
BuildRequires:	pkgconfig(libzypp)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(augeas)
BuildRequires:	pkgconfig(rpm)
BuildRequires:	readline-devel
BuildRequires:	boost-devel
BuildRequires:	asciidoctor

%description
Zypper is a command line package manager, which makes use of libzypp,
providing functions like repository access, dependency solving,
package installation, etc.

YaST2 and RPM MetaData package repositories are supported.
Zypper repositories are similar to the ones used in YaST, which
also makes use of libzypp. Zypper can also handle repository
extensions like patches, patterns and products. 

%package needs-restarting
Summary:        needs-restarting compatibility with zypper
Group:          System/Configuration/Packaging
Requires:       zypper
Supplements:    zypper
BuildArch:      noarch

%description needs-restarting
Provides compatibility to DNF needs-restarting command using zypper

%prep
%if "%{scmrev}" == ""
%autosetup -p1 -n %{name}-%{version}%{beta}
%else
%autosetup -p1 -n %{name}
%endif
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

mv %buildroot%_docdir/packages/zypper %buildroot%_docdir/%name-%version
%find_lang %name

%files -f %name.lang
%{_sysconfdir}/bash_completion.d/zypper.sh
%config %{_sysconfdir}/logrotate.d/zypp-refresh.lr
%config %{_sysconfdir}/logrotate.d/zypper.lr
%config %{_sysconfdir}/zypp/zypper.conf
%config %{_sysconfdir}/zypp/apt-packagemap.d/*
%{_bindir}/apt
%{_bindir}/apt-get
%{_bindir}/aptitude
%{_bindir}/installation_sources
%{_bindir}/zypper
%{_sbindir}/zypp-refresh
%{_sbindir}/zypper-log
%doc %{_docdir}/%{name}-%{version}
%{_mandir}/man8/*
%{_datadir}/zypper

%files needs-restarting
%{_bindir}/needs-restarting
%{_mandir}/man1/needs-restarting.1*
