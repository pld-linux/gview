Summary:	gView is a GTK+ image browser and viewer
Summary(pl):	gView jest przegl±dark± plików graficznych opart± na GTK+
Name:		gview
Version:	0.1.8
Release:	1
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Copyright:	GPL
Source:		http://www.geocities.com/ResearchTriangle/Facility/1468/sg/%{name}-%{version}.tar.gz
BuildRequires:	gtk+-devel >= 1.1.9
BuildRequires:	glib-devel >= 1.1.9
BuildRequires:	imlib-devel >= 1.4.0
BuildRequires:	XFree86-devel
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
