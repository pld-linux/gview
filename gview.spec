Summary:	gView is a GTK+ image browser and viewer
Summary(pl):	gView jest przegl±dark± plików graficznych opart± na GTK+
Name:		gview
Version:	0.1.7
Release:	1
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Copyright:	GPL
Source:		http://www.geocities.com/ResearchTriangle/Facility/1468/sg/%{name}-%{version}.tar.gz
BuildPrereq:	gtk+-devel >= 1.1.9
BuildPrereq:	glib-devel >= 1.1.9
BuildPrereq:	imlib-devel >= 1.4.0
BuildPrereq:	XFree86-devel
BuildRoot:   	/tmp/%{name}-%{version}-root

%define _prefix	/usr/X11R6

%description
gView is an image browser and viewer, using GTK+ and Imlib, 
that uses a style similar to that of ACDSee for Windows.

%description -l pl
gView jest przegl±dark± obrazków wykorzystuj±c± biblioteki GTK+ 
i Imlib, posiadaj±c± interfejs zbli¿ony do ACDSee dla Windows.

%prep
%setup -q

%build
LDFLAGS="-s" \
%configure 

make

%install
rm -rf $RPM_BUILD_ROOT

make install-strip DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README ChangeLog TODO NEWS AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,ChangeLog,TODO,NEWS,AUTHORS}.gz
%attr (755,root,root) %{_bindir}/gview

%changelog
* Fri Jun 25 1999 Piotr Czerwiñski <pius@pld.org.pl> 
  [0.1.7-1]
- initial rpm release.
