Summary:	Very simple graphical configuration utility for icewm
Summary(pl):	Bardzo proste graficzne narzêdzie do konfiguracji icewm'a
Name:		icewmconf
Version:	1.0.0
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	%{name}-%{version}.gz
#Source1:	%{name}.desktop
#Source2:	%{name}.png
#Source3:	%{name}_16x16.xpm
#Source4:	%{name}_32x32.xpm
Requires:	icewm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6/

%description
Very simple graphical configuration utility for icewm.

%description -l pl
Bardzo proste graficzne narzêdzie konfiguracyjne dla icewm. Jest to w
zasadzie prosty skrypt.

%setup

%build

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT%{_bindir} 

%{__install} %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
