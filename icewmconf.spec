Summary:	Very simple graphical configuration utility for IceWM
Summary(pl):	Bardzo proste graficzne narzêdzie do konfiguracji IceWM-a
Name:		icewmconf
Version:	2.1.0
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://sdboyd.dyndns.org/icewmconf/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
#Source2:	%{name}.png
#Source3:	%{name}_16x16.xpm
#Source4:	%{name}_32x32.xpm
URL:		http://sdboyd.dyndns.org/icewmconf/
Requires:	icewm
Requires:	tk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6/

%description
Very simple graphical configuration utility for icewm. Its a script.

%description -l pl
Bardzo proste graficzne narzêdzie konfiguracyjne dla IceWM-a. Jest to
w zasadzie prosty skrypt.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/Settings/IceWM}

install icewmconf-2.1.0 $RPM_BUILD_ROOT%{_bindir}/icewmconf
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Settings/IceWM

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changelog
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_applnkdir}/Settings/IceWM/*
