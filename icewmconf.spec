Summary:	Very simple graphical configuration utility for IceWM
Summary(pl):	Bardzo proste graficzne narzêdzie do konfiguracji IceWM-a
Name:		icewmconf
Version:	2.1.0
Release:	3
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://sdboyd.dyndns.org/icewmconf/%{name}-%{version}.tar.gz
# Source0-md5:	e5d599142116daa29f348e3eff52cc55
Source1:	%{name}.desktop
#Source2:	%{name}.png
#Source3:	%{name}_16x16.xpm
#Source4:	%{name}_32x32.xpm
URL:		http://sdboyd.dyndns.org/icewmconf/
Requires:	icewm
Requires:	tk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Very simple graphical configuration utility for icewm. Its a script.

%description -l pl
Bardzo proste graficzne narzêdzie konfiguracyjne dla IceWM-a. Jest to
w zasadzie prosty skrypt.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}}

install icewmconf-2.1.0 $RPM_BUILD_ROOT%{_bindir}/icewmconf
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changelog
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_desktopdir}/*
