Summary:	gView is a GTK+ image browser and viewer
Summary(pl):	gView jest przeglądarką plików graficznych opartą na GTK+
Name:		gview
Version:	0.1.12
Release:	1
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Copyright:	GPL
Source0:	http://www.geocities.com/ResearchTriangle/Facility/1468/sg/%{name}-%{version}.tar.gz
Source1:	gview.desktop
BuildRequires:	gtk+-devel >= 1.1.9
BuildRequires:	glib-devel >= 1.1.9
BuildRequires:	imlib-devel >= 1.4.0
BuildRequires:	XFree86-devel
BuildRoot:   	/tmp/%{name}-%{version}-root

%define 	_prefix		/usr/X11R6

%description
gView is an image browser and viewer, using GTK+ and Imlib, 
that uses a style similar to that of ACDSee for Windows.

%description -l pl
gView jest przeglądarką obrazków wykorzystującą biblioteki GTK+ 
i Imlib, posiadającą interfejs zbliżony do ACDSee dla Windows.

%prep
%setup -q

%build
%configure 

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/applnk/Graphics/Viewers

make install-strip DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applnk/Graphics/Viewers

gzip -9nf README ChangeLog TODO NEWS AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,ChangeLog,TODO,NEWS,AUTHORS}.gz
%attr (755,root,root) %{_bindir}/gview

%{_datadir}/applnk/Graphics/Viewers/gview.desktop
